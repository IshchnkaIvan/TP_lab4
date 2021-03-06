USE enrolle_db;

SELECT * FROM enrolle
WHERE CT_rating > 225;

ALTER TABLE enrolle
ADD university_id INT 
FOREIGN KEY (university) REFERENCES university(id);

select count(*)
from Enrolle
where passing_score>250;