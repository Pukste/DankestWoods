drop database if exists gamebase;
create database gamebase;
use gamebase;

drop table if exists location;
drop table if exists player;
drop table if exists item;
drop table if exists event;

create table location(
locationid int not null,
nimi varchar(100),
description varchar(1024),
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

create table events(
eventsid int not null,
value int,
primary key (eventsid)
);

insert into location values
(1, "Woods", "You look around and there's naught but an ocean of trees to be seen.", 4, 5, 2, 6),
(2, "Tower", "There's a tall wooden tower. Judging by the rickety sound it might be best to not climb it.", null, null, 1, 3),
(3, "Tavern", "A homely tavern built next to a giant boulder. How delightful.", null, null, null, 2),
(4, "Shaman's Hut", "A crooked crummy wooden hut with patches of hay covering holes in the roof in big blotches. The surroundings have a strange almost odorless fragrance floating around, due to a warm draft coming from deeper in the forest it is uncertain whether the scent is coming from inside the hut or from further ahead.", null, 1, null, null),
(5, "Hill", "It's a wide field on a hill full of grass and flowers, it's the only area around with no tall trees on it. A castle can be seen in the distance.", 1, null, null, null),
(6, "Woods 2", "The tall trees continue endlessly. There are peculiarly shaped plants growing alongside surfaced tree roots.", null, 7, null, 1),
(7, "River", "It's a wide river, it doesn't look like you will be able to swim across it.", 6, null, null, null),
(8, "Village", "Lots of small houses. It's a village, not exactly brimming with life, but it's something.", 7, null, null, 9),
(9, "Marketplace", "A few stalls can be seen from the distance neatly lined up. Walking forward a peculiar sweet scent of grass and other plant life is in the air, there must be a ", null, null, 8, null),
(10, "Castle", "It's a large castle, made of stone as castles tend to be.", 8, null, null, null);

insert into player values
(1, 1);

insert into item values
(1, "The Sword of All Things Right", 2, null),
(2, "The Sword of All Things Left", null, null),
(3, "Suspicious Herbs", 6, null),
(4, "Wooden Tap", 3, null),
(5, "Magic Mushroom", 9, null),
(6, "Empty Vial", null, 1),
(7, "Vial of Water", null, null),
(8, "Banana", 5, null),
(9, "Endless Memory", null, null);
