# Information about the database
The default database type is SQLiteInitally, the database is located at [baseball.db](/database/baseball.db). This value is set in the [config.py](/config.py) in the 'SQLALCHEMY_DATABASE_URI' variable. 

If you wish to use MySQL, change the value of 'SQLALCHEMY_DATABASE_URI' in the [config.py](/config.py) file to:
```
mysql://[username]:[password]@[host]:[port]/[database_name]
```

* Change the items in the brackets to your value

Initially, this is a sqlite database and it is tested and working. This can be set to another database type, however there may need to be additional packages installed. Further, if there is a cloud database (either local or otherwise), then this must be live and connection ready before the app starts

Table information are in the following sections
* [Statcast](#statcast)

## Statcast
### General Info
This is where all the pitch-by-pitch data is located. The columns are located below. Please see this site: https://baseballsavant.mlb.com/csv-docs for information on the specific columns. The names are the same, except for 'id'.

### Table Information
| Column Name | Column Type | Other Information (If any) |
|:-----------:|:-----------:|:--------------------------:|
| id          | Integer     | Primary Key for statcast data |
| game_date   | String      |                            |
| pitch_type  | Date        |                            |
| release_speed | Float     |                            |
| release_pos_x | Float     |                            |
| release_pos_y | Float     |                            |
| release_pos_z | Float     |                            |
| batter      | String      |                            |
| pitcher     | String      |                            |
| events      | String      |                            |
| description | String      |                            |
| zone        | Text        |                            |
| des         | String      |                            |
| game_type   | String      |                            |
| stand       | String      |                            |
| p_throws    | String      |                            |
| home_team   | String      |                            |
| away_team   | String      |                            |
| type        | String      |                            | 
| hit_location | String     |                            | 
| bb_type     | String      |                            | 
| balls       | Integer     |                            | 
| strikes     | Integer     |                            | 
| pfx_x       | Float       |                            | 
| pfx_z       | Float       |                            | 
| plate_x     | Float       |                            | 
| plate_z     | Float       |                            | 
| on_3b       | String      |                            | 
| on_2b       | String      |                            | 
| on_1b       | Integer     |                            | 
| outs_when_up | String     |                            | 
| inning      | String      |                            | 
| inning_topbot | String    |                            | 
| hc_x        | Float       |                            | 
| hc_y        | Float       |                            | 
| vx0         | Float       |                            | 
| vy0         | Float       |                            | 
| vz0         | Float       |                            | 
| ax          | Float       |                            | 
| ay          | Float       |                            | 
| az          | Float       |                            | 
| sz_top      | Float       |                            | 
| sz_bot      | Float       |                            | 
| hit_distance_sc | Float   |                            | 
| launch_speed | Integer    |                            | 
| launch_angle | Float      |                            | 
| effective_speed | Integer |                            | 
| release_spin_rate | Integer |                          | 
| spin_axis   | Integer     |                            | 
| release_extension | String |                           | 
| game_pk     | Float       |                            | 
| fielder_2   | String      |                            | 
| fielder_3   | String      |                            | 
| fielder_4   | String      |                            | 
| fielder_5   | String      |                            | 
| fielder_6   | String      |                            | 
| fielder_7   | String      |                            | 
| fielder_8   | String      |                            | 
| fielder_9   | String      |                            | 
| estimated_ba_using_speedangle | Float |                | 
| estimated_woba_using_speedangle | Floatng |            | 
| woba_value  | Integer     |                            | 
| woba_denom  | Float       |                            | 
| babip_value | Integer     |                            | 
| iso_value   | Integer     |                            | 
| launch_speed_angle | Integer |                         | 
| at_bat_number | Integer   |                            | 
| pitch_number | String     |                            | 
| pitch_name  | Integer     |                            | 
| home_score  | Integer     |                            | 
| away_score  | Integer     |                            | 
| bat_score  | Integer      |                            | 
| fld_score  | Integer      |                            | 
| post_away_score | Integer |                            | 
| post_home_score | Integer |                            | 
| post_bat_score | Integer  |                            | 
| post_fld_score | Integer  |                            | 
| if_fielding_alignm | String |                          | 
| of_fielding_alignm | String |                          | 
| delta_run_exp | Float     |                            | 
| delta_home_win_exp | Float |                           |