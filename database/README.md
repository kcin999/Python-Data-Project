# Information about the database
The default database type is SQLite. Initally, the databases are located at [baseball.db](/instance/baseball.db) and [robinhood.db](/instance/robinhood.db). This value is set in the [config.py](/config.py) in the 'SQLALCHEMY_DATABASE_URI' variable. 

If you wish to use MySQL, change the value of 'SQLALCHEMY_DATABASE_URI' in the [config.py](/config.py) file to:
```
mysql://[username]:[password]@[host]:[port]/[database_name]
```

* Change the items in the brackets to your value

Initially, this is a sqlite database and it is tested and working. This can be set to another database type, however there may need to be additional packages installed. Further, if there is a cloud database (either local or otherwise), then this must be live and connection ready before the app starts

Table information are in the following sections
* [baseball](#baseball)
* [Robinhood] (#robinhood)

## Baseball
### General Info
The baseball database is all of the baseball related data being leveraged within this program. Currently there are two tables, with their corresponding information below.
* [Pitches](#table-information-pitches)
* [Players](#table-information-players)

### Table Information: pitches
This is where all the pitch-by-pitch data is located. The columns are located below. Please see this site: https://baseballsavant.mlb.com/csv-docs for information on the specific columns. The names are the same, except for 'id'.

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

### Table Information: players
This is where all of the data is stored for players. Data is downloaded from here: https://raw.githubusercontent.com/chadwickbureau/register/master/data/people.csv. More info can be found here: https://github.com/chadwickbureau/register.

| Column Name | Column Type | Column Description |
|:-----------:|:-----------:|:------------------:|
| id          | Integer     | Primary Key for the table |
| key_retro   | String(10)  | Retrosheets Player ID |
| key_bbref   | String(10)  | Baseball Reference Player ID |
| key_fangraphs | String(10) | Fangraphs Player ID |
| key_mlbam   | String(10)  | MLBAM / Statcast Player ID |
| mlb_played_first | String(4) | Year of their first game |
| mlb_played_last | String(4) | Year of their last game|
| name_last   | String(20)  | Player's last name |
| name_first  | String(20)  | Player's first name |
| name_given  | String(60)  | Player's given name |
| name_suffix | String(20)  | Player's suffix |
| name_nick   | String(55)  | Nick name of the player, if any |
| birth_date  | Date        | Player's birthday |
| death_date  | Date        | Player's deathday |

## Robinhood
The robinhood data is used to keep track of stock information, such as stock prices over time, and things in one's portfolio.
* [Stocks](#table-information-stocks)
* [OwnedStock](#table-information-ownedstock)

### Table Information: Stocks
This table is the main key that keeps track of stock tickers and their associated companies.

| Column Name | Column Type | Column Description |
|:-----------:|:-----------:|:------------------:|
| stock_ticker | String(5)  | Stock Ticker, primary_key |
| company_name | String(50) | Company Name |
| created_datetime | DateTime | Date the stock was added to the database |
| updated_datetime |  DateTime | Last time the record was updated in the database |

Relationships:
* One to Many `stocks[stock_ticker]` to `ownedstock[ticker]`

### Table Information: OwnedStock
Overtime stock information tracking

| Column Name | Column Type | Column Description |
|:-----------:|:-----------:|:------------------:|
| id | Integer | Primary Key Column; autoincrement |
| ticker | String(5) | Stock Ticker; Foreign Key with `Stocks` |
| created_datetime | DateTime | Datetime the record was created |
| price | Numeric(8, 4) | Curremt Price per share|
| quantity | Numeric(16, 8) | Current Quantity owned|
| average_buy_price | Numeric(8, 4) | Average amount the quantity owned was purchased for |
| equity | Numeric(8, 4) | How much amount in dollars is owned|
| percent_change | Numeric(5, 2) | Percent Change since purchase |
| intraday_percent_change | Numeric(5, 2) | Percent Change within current day |
| equity_change | Numeric(8, 4) | How much equity has changed since purchase ($) |
| pe_ratio | Numeric(12, 8) | Price-to-earnings ratio |
| percentage | Numeric(5, 2) | Percentage of portfolio |