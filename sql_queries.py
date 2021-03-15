# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = """
CREATE TABLE IF NOT EXISTS songplays (
song_id varchar primary key not null,
start_time timestamp,
user_id varchar,
user_agent text
);
"""

user_table_create = """
CREATE TABLE IF NOT EXISTS users (
user_id varchar primary key not null,
first_name varchar,
last_name varchar,
gender varchar,
level varchar
);
"""

song_table_create = """
CREATE TABLE IF NOT EXISTS songs (
    song_id varchar primary key not null,
    title text,
    artist_id varchar,
    year integer,
    duration float8
);
"""

artist_table_create = """
CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar primary key not null,
    name varchar,
    location varchar,
    latitude float,
    longitude float
);
"""

time_table_create = """
CREATE TABLE IF NOT EXISTS time (
    start_time timestamp not null,
    hour varchar,
    day integer,
    week integer,
    month integer,
    year integer,
    weekday varchar
);
"""

# INSERT RECORDS

songplay_table_insert = """
insert into songplays (song_id, start_time, user_id, user_agent) 
VALUES (%s)
"""

user_table_insert = """
insert into users (user_id, first_name, last_name, gender, level) 
VALUES (%s, %s, %s, %s, %s) on conflict do nothing 
"""

song_table_insert = """
INSERT INTO songs (song_id, title, artist_id, year, duration) 
VALUES (%s, %s, %s, %s, %s) on conflict do nothing 
"""

artist_table_insert = """
INSERT INTO artists (artist_id, name, location, latitude, longitude) 
VALUES (%s, %s, %s, %s, %s) on conflict do nothing 
"""

time_table_insert = """
insert into time (start_time, hour, day, week, month, year, weekday) 
VALUES (%s, %s, %s, %s, %s, %s, %s) on conflict do nothing 
"""

# FIND SONGS

song_select = """
select s.song_id, s.artist_id, a.name from songs as s 
join artists as a on (a.artist_id = s.artist_id) 
where s.title=%s and a.name=%s and s.duration=%s
"""

# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
