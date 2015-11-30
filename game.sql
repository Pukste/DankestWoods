drop database if exists pelisqlkanta;
create database pelisqlkanta;
use pelisqlkanta;

drop table if exists location;
drop table if exists player;
drop table if exists item;
drop table if exists event;

create table location(
locationid int not null,
description varchar(512),
north int null,
south int null,
west int null,
east int null,
primary key (locationid)
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

