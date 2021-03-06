create database if not exists Enrolle_db;
use Enrolle_db;
create table if not exists Enrolle
(
	id 				int 		unsigned auto_increment,
    surname 		varchar(30) NOT NULL,
    `name` 			varchar(20)	NOT NULL,
    middle_name 	varchar(20),
    gender 			varchar(1),
    nationality 	varchar(30),
    birthdate 		date,
    home_address 	varchar(256),
    CT_rating 		smallint 	unsigned NOT NULL,
    passing_score 	smallint 	unsigned NOT NULL,
    primary key (id)
);


create table if not exists University
(
	id 				int 		unsigned auto_increment,
    university_name		varchar(80) NOT NULL,
    university_description		varchar(200),
    primary key (id)
);
truncate table University;
insert into University (university_name)
	values("BSU");


truncate table Enrolle;
insert into Enrolle (surname, `name`, middle_name, gender, nationality, birthdate, home_address, CT_rating, passing_score)
	values("Belevich","Mikhail","Andreevich","M","belarussian",
			01/24/2002,"246000,Belarus,Gomel,International street,15,7",382,364),
            ("Ishchenko","Ivan","Sergeevich","M","belarussian",
			18/03/2002,"246000,Belarus,Gomel,Portovaya street,51",364,364),
            ("Korolko","Olga","Yurievna","F","belarussian",
			23/10/2001,"246000,Belarus,Pinsk,Krasnoflotskaya 8,2",350,328);
            
select count(*)
from Enrolle 
where passing_score>250;

select sum(CT_rating)
from Enrolle
where gender="M";

select max(CT_rating),min(CT_rating)
from Enrolle;

select Enrolle.*,University.*
from Enrolle
inner join University
on Enrolle.university_id=University.id
where University.id=3;          

