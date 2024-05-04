from functools import partial
import numpy as np
import matplotlib.pyplot as plt
import statsapi
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import plotly.express as px
import json
import plotly.graph_objects as go

import pandas as pd
import plotly.offline as offline


PITCH_LIMIT = 5
TIME_STEP = 0.01
PITCH_OFFSET = [
    125,  # y
    -200,  # x
    0,  # z
]

color_map = {
    # "Fastball": "blue",
    # "Curveball": "green",
    # "Slider": "red",
    # "Sinker": "orange",
    True: "Red"
}
# Initialize legend entries list
legend_entries = {}


def get_pitch_data(output_data: bool = False):
    """Retrieves pitch data

    :param output_data: Toggle for outputting pitch data, defaults to True
    :type output_data: bool, optional
    :return: Pitch Data
    :rtype: list
    """
    pitches_data = []

    game_data = statsapi.get("game", params={"gamePk": 746967})
    all_plays = game_data["liveData"]["plays"]["allPlays"]

    if output_data:
        with open("game.json", "w") as f:
            json.dump(all_plays, f, indent=4)

    for play in all_plays:
        for event in play["playEvents"]:
            if "pitchData" in event:
                coords = event["pitchData"]["coordinates"]
                initial_position = np.array(
                    [
                        coords["x0"] + PITCH_OFFSET[0],
                        coords["y0"] + PITCH_OFFSET[1],
                        coords["z0"] + PITCH_OFFSET[2],
                    ]
                )
                initial_velocity = np.array(
                    [coords["vX0"], coords["vY0"], coords["vZ0"]]
                )
                initial_acceleration = np.array(
                    [coords["aX"], coords["aY"], coords["aZ"]]
                )
                total_time = event["pitchData"]["plateTime"]
                pitch_type = event["details"]["type"]["description"]
                strike = event["details"]["isStrike"]
                pitches_data.append(
                    {
                        "initial_position": initial_position,
                        "initial_velocity": initial_velocity,
                        "initial_acceleration": initial_acceleration,
                        "plateTime": total_time,
                        "pitchType": pitch_type,
                        "strike": strike,
                    }
                )

            if len(pitches_data) > PITCH_LIMIT:
                break
        if len(pitches_data) > PITCH_LIMIT:
            break

    return pitches_data


def update_position_velocity(
    position: float, velocity: float, acceleration: float, dt: float
):
    """Function to update position and velocity using Euler's method"""
    new_velocity = velocity + acceleration * dt
    new_position = position + velocity * dt
    return new_position, new_velocity


def simulation(pitches_data: list):
    """Creates dataset of simulated pitch movement

    :param pitches_data: Pitch Data
    :type pitches_data: list

    :return: All Positons and velocities
    :rtype: tuple(list, list)
    """
    # Initialize lists to store trajectory data for each pitch
    all_positions = []
    all_velocities = []
    for pitch_data in pitches_data:
        total_time = pitch_data["plateTime"]
        initial_position = pitch_data["initial_position"]
        initial_velocity = pitch_data["initial_velocity"]
        initial_acceleration = pitch_data["initial_acceleration"]

        # Initialize lists to store trajectory data for current pitch
        positions = [initial_position]
        velocities = [initial_velocity]

        # Simulate the motion
        current_position = initial_position
        current_velocity = initial_velocity
        current_acceleration = initial_acceleration
        time = 0.0

        while time < total_time:
            # Update position and velocity
            current_position, current_velocity = update_position_velocity(
                current_position, current_velocity, current_acceleration, TIME_STEP
            )

            # Store updated position and velocity
            positions.append(current_position)
            velocities.append(current_velocity)

            # Increment time
            time += TIME_STEP

        # Convert lists to arrays for easier manipulation and store for plotting
        all_positions.append(np.array(positions))
        all_velocities.append(np.array(velocities))

    return all_positions, all_velocities


def generate_chart(all_positions: list, pitches_data: list):
    """Generates Pitch Visualization

    :param all_positions: Pitch Positions
    :type all_positions: list
    :param pitches_data: Pitches data
    :type pitches_data: list
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Define the rectangle vertices
    rect_vertices = np.array(
        [
            [-1, 0, 1.5799978960203],
            [1, 0, 1.5799978960203],
            [1, 0, 3.221186159159],
            [-1, 0, 3.221186159159],
        ]
    )

    # Define the rectangle face
    rect_faces = [
        [rect_vertices[0], rect_vertices[1], rect_vertices[2], rect_vertices[3]]
    ]

    # Create the Poly3DCollection object for the rectangle
    rectangle = Poly3DCollection(rect_faces, edgecolor="lightgray", lw=3, zorder=0.1)

    max_length = max(len(sublist) for sublist in all_positions)
    _ani = FuncAnimation(
        fig,
        update_plot,
        frames=max_length,
        interval=5,
        repeat=False,
        fargs=(ax, all_positions, pitches_data, rectangle),
    )

    plt.show()


def update_plot(frame, ax, all_positions, pitches_data, rectangle):
    """Updates trhe frame"""
    ax.clear()
    ax.set_xlim3d(-5, 5)
    ax.set_ylim3d(0, 70)
    ax.set_zlim3d(0, 7)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("X")
    ax.set_title("Live Baseball Pitch Trajectories")
    for i, position in enumerate(all_positions):
        strike = pitches_data[i]["strike"]
        color = color_map.get(strike, "black")
        ax.plot(
            position[:frame, 0], position[:frame, 1], position[:frame, 2], color=color
        )

    # ax.set_box_aspect([1,1,1])  # x, y, and z axes have the same scale
    ax.set_aspect("equal")

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.zaxis.set_visible(False)

    # Add the rectangle to the plot
    ax.add_collection3d(rectangle)

    # Create custom legend
    # for pitch_type, color in legend_entries.items():
    #     ax.plot([], [], color=color, label=pitch_type)


def _transform_coordinate(
    coord: pd.Series, center: float, scale: float, sign: float
) -> pd.Series:
    return sign * ((coord - center) * scale + center)


def transform_coordinates(
    coords: pd.DataFrame, scale: float, x_center: float = 125, y_center: float = 199
) -> pd.DataFrame:
    x_transform = partial(_transform_coordinate, center=x_center, scale=scale, sign=+1)
    y_transform = partial(_transform_coordinate, center=y_center, scale=scale, sign=-1)
    return coords.assign(x=coords.x.apply(x_transform), y=coords.y.apply(y_transform))


def get_stadium_scatter(team: str = "generic"):
    STADIUM_SCALE = 2.495 * 2 / 2.33
    stadiums = transform_coordinates(
        pd.read_csv("stadiums.csv", index_col=0), scale=STADIUM_SCALE
    )

    stadiums = stadiums.loc[stadiums["team"] == team]

    traces = []
    for segment in stadiums["segment"].unique():
        traces.append(
            go.Scatter3d(
                x=stadiums.loc[stadiums["segment"] == segment, "x"],
                y=stadiums.loc[stadiums["segment"] == segment, "y"],
                z=[0] * len(stadiums.loc[stadiums["segment"] == segment, "x"]),
                name=segment,
                # marker=None
                mode="lines",
            )
        )

    return traces


def generate_plotly_chart(all_positions):
    fig = go.Figure()
    for position in all_positions:
        df = pd.DataFrame(position, columns=["x", "y", "z"])

        fig.add_trace(go.Scatter3d(x=df["x"], y=df["y"], z=df["z"], mode="lines"))

    fig.add_traces(get_stadium_scatter("cardinals"))

    fig.update_layout(
        scene=dict(
            aspectmode="data",
        ),
    )

    offline.plot(fig, filename="plotly_chart.html", auto_open=False)


def main():
    pitches_data = get_pitch_data(True)
    all_positions, _all_velocities = simulation(pitches_data)

    # generate_chart(
    #     all_positions,
    #     pitches_data
    # )

    generate_plotly_chart(all_positions)


if __name__ == "__main__":
    main()
