use enrolle_db;

select * from enrolle
where CT_rating > 225;

alter table Enrolle
add university_id int unsigned;

alter table Enrolle
add FOREIGN KEY (university_id) REFERENCES university(id);

select enrolle.id, enrolle.surname, enrolle.`name`, enrolle.middle_name, enrolle.birthdate, university.university_name
from enrolle 
left join university ON enrolle.university_id = university.id;

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