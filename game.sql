drop database if exists game;
create database game;
use game;

drop table if exists location;
drop table if exists player;
drop table if exists item;
drop table if exists event;

create table location(
locationid int not null,
description varchar(512),
primary key (locationid)
north int null,
south int null,
west int null,
east int null,
);

create table player(
playerid int,
locationid int,
primary key(playerid),
foreign key (locationid) references location(locationid)
);

create table item(
itemid int not null,
name varchar(256) not null,
locationid int,
playerid int,
primary key (itemid),
foreign key (playerid) references player(playerid),
foreign key (locationid) references location(locationid)
);

create table event(
eventid int not null,
value int,
primary key (eventid)
);

insert into location values (1, "Woods",
"You look around and there's nothing besides an ocean of trees to be seen.",
 4, 5, 2, 6),
insert into location values (2, "Tower",
"You look around and there's nothing besides an ocean of trees to be seen.",
null, null, 1, 3)

