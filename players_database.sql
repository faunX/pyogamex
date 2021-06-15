use ogamex;

drop table planets_player;

CREATE TABLE planets_player (
	player_name	  varchar(255),
    galaxy_number INT,
    system_number INT,
    position_number INT,
    moon BOOLEAN DEFAULT FALSE,
    primary key (player_name, galaxy_number, system_number, position_number)
);

insert into planets_player(player_name, galaxy_number, system_number, position_number, moon)
values	('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('Wonderland', 1, 10, 2,true), ('Jace Beleren',1,10,9,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		('The Shadow', 1, 5, 4,true), ('Luzifer',1,5,13,true),
		