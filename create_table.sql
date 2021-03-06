create database if not exists Enrolle_db;

create table if not exists Enrolle
(
	id int unsigned auto_increment,
    surname varchar(30),
    `name` varchar(20),
    middle_name varchar(20),
    gender varchar(1),
    nationality varchar(30),
    birthdate date,
    home_address varchar(256),
    CT_rating smallint unsigned,
    passing_score smallint unsigned,
    primary key id
);

insert into Enrolle 
	values("Belevich","Mikhail","Andreevich","M","belarussian",
			2002/01/24,"246000,Belarus,Gomel,International street,15,7",382,364),
            ("Ishchenko","Ivan","Sergeevich","M","belarussian",
			2002/03/18,"246000,Belarus,Gomel,Portovaya street,51",364,364)