create view artist_list as
select artists.name as artists, albums.name as albums, songs.track, songs.title from songs
inner join albums on songs.album = albums._id
inner join artists on albums.artist = artists._id
order by artists.name, albums.name, songs.track

drop view artist_list

create view album_list as select name from albums order by name collate nocase;

sqlite> select albums, track, title from artist_list where albums = 'Forbidden';
Forbidden|1|The Illusion of Power
Forbidden|2|Get a Grip
Forbidden|3|Can't Get Close Enough
Forbidden|4|Shaking Off the Chains
Forbidden|5|I Won't Cry for You
Forbidden|6|Guilty as Hell
Forbidden|7|Sick and Tired
Forbidden|8|Rusty Angels
Forbidden|9|Forbidden
Forbidden|10|Kiss of Death

select artists.name, songs.title from songs
inner join albums on songs.album = albums._id
inner join artists on albums.artist = artists._id
where artists.name = 'Deep Purple';

select songs.title from songs
inner join albums on songs.album = albums._id
inner join artists on albums.artist = artists._id
where artists.name = "Aerosmith"
order by artists.name collate nocase asc;

select count(songs.title) from songs
inner join albums on songs.album = albums._id
inner join artists on albums.artist = artists._id
where artists.name = "Aerosmith"
order by artists.name collate nocase asc;

select distinct(songs.title) from songs
inner join albums on songs.album = albums._id
inner join artists on albums.artist = artists._id
where artists.name = "Aerosmith"
order by artists.name collate nocase asc

select count(distinct(songs.title)) from songs
inner join albums on songs.album = albums._id
inner join artists on albums.artist = artists._id
where artists.name = "Aerosmith"
order by artists.name collate nocase asc;

select count(distinct(songs.title)), count(distinct(artists.name)), count(distinct(albums.name)) from songs
inner join albums on songs.album = albums._id
inner join artists on albums.artist = artists._id
where artists.name = "Aerosmith"
order by artists.name collate nocase asc;
