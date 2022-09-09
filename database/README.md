# Information about the database
Initally, the database is located at [baseball.db](/database/baseball.db). This value is set in the [config.py](/config.py) in the 'SQLALCHEMY_DATABASE_URI' variable. 


Initially, this is a sqlite database and it is tested and working. This can be set to another database type, however there may need to be additional packages installed. Further, if there is a cloud database (either local or otherwise), then this must be live and connection ready before the app starts

Table information are in the following sections
* [Statcast](#statcast)

## Statcast
### General Info
This is where all the pitch-by-pitch data is located. The columns are located below. Please see this site: https://baseballsavant.mlb.com/csv-docs for information on the specific columns. The names are the same, except for 'id'.

### Columns
* id
    * Type: 'Integer'
    * Primary Key for statcast data
* game_date
    * Type: 'String'
* pitch_type
    * Type: 'Date'
* release_speed
    * Type: 'Float'
* release_pos_x
    * Type: 'Float'
* release_pos_y
    * Type: 'Float'
* release_pos_z
    * Type: 'Float'
* batter
    * Type: 'String'
* pitcher
    * Type: 'String'
* events
    * Type: 'String'
* description
    * Type: 'String'
* zone
    * Type: 'Text'
* des
    * Type: 'String'
* game_type
    * Type: 'String'
* stand
    * Type: 'String'
* p_throws
    * Type: 'String'
* home_team
    * Type: 'String'
* away_team
    * Type: 'String'
* type
    * Type: 'String'
* hit_location
    * Type: 'String'
* bb_type
    * Type: 'String'
* balls
    * Type: 'Integer'
* strikes
    * Type: 'Integer'
* pfx_x
    * Type: 'Float'
* pfx_z
    * Type: 'Float'
* plate_x
    * Type: 'Float'
* plate_z
    * Type: 'Float'
* on_3b
    * Type: 'String'
* on_2b
    * Type: 'String'
* on_1b
    * Type: 'Integer'
* outs_when_up
    * Type: 'String'
* inning
    * Type: 'String'
* inning_topbot
    * Type: 'String'
* hc_x
    * Type: 'Float'
* hc_y
    * Type: 'Float'
* vx0
    * Type: 'Float'
* vy0
    * Type: 'Float'
* vz0
    * Type: 'Float'
* ax
    * Type: 'Float'
* ay
    * Type: 'Float'
* az
    * Type: 'Float'
* sz_top
    * Type: 'Float'
* sz_bot
    * Type: 'Float'
* hit_distance_sc
    * Type: 'Float'
* launch_speed
    * Type: 'Integer'
* launch_angle
    * Type: 'Float'
* effective_speed
    * Type: 'Integer'
* release_spin_rate
    * Type: 'Integer'
* spin_axis
    * Type: 'Integer'
* release_extension
    * Type: 'String'
* game_pk
    * Type: 'Float'
* fielder_2
    * Type: 'String'
* fielder_3
    * Type: 'String'
* fielder_4
    * Type: 'String'
* fielder_5
    * Type: 'String'
* fielder_6
    * Type: 'String'
* fielder_7
    * Type: 'String'
* fielder_8
    * Type: 'String'
* fielder_9
    * Type: 'String'
* estimated_ba_using
    * Type: 'Float_speedangle'
* estimated_woba_usi
    * Type: 'Floatng_speedangle'
* woba_value
    * Type: 'Integer'
* woba_denom
    * Type: 'Float'
* babip_value
    * Type: 'Integer'
* iso_value
    * Type: 'Integer'
* launch_speed_angle
    * Type: 'Integer'
* at_bat_number
    * Type: 'Integer'
* pitch_number
    * Type: 'String'
* pitch_name
    * Type: 'Integer'
* home_score
    * Type: 'Integer'
* away_score
    * Type: 'Integer'
* bat_score
    * Type: 'Integer'
* fld_score
    * Type: 'Integer'
* post_away_score
    * Type: 'Integer'
* post_home_score
    * Type: 'Integer'
* post_bat_score
    * Type: 'Integer'
* post_fld_score
    * Type: 'Integer'
* if_fielding_alignm
    * Type: 'Stringent'
* of_fielding_alignm
    * Type: 'Stringent'
* delta_run_exp
    * Type: 'Float'
* delta_home_win_exp
    * Type: 'Float'