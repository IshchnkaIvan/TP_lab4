USE enrolle_db;

SELECT * FROM enrolle
WHERE CT_rating > 225;

ALTER TABLE Enrolle
ADD university_id INT UNSIGNED;

alter table Enrolle
add FOREIGN KEY (university_id) REFERENCES university(id);

select count(*)
from Enrolle
where passing_score>250;