import sqlalchemy
from sqlalchemy import Column, Table, MetaData, ForeignKey, PrimaryKeyConstraint
from sqlalchemy import Integer, String, DateTime, SmallInteger, func
from sqlalchemy.orm import relationship, sessionmaker,Session
import pymysql
from sqlalchemy.sql import Engine
from init import Base


class ORMConnector:
    engine: Engine = None
    session: Session = None
    metadata:MetaData = None

    class University(Base):
        __tablename__ = "university"
        id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
        university_name = Column(String(80))
        university_description = Column(String(200))

        def __repr__(self):
            return "('%s','%s','%s')" % (self.id, self.university_name, self.university_description)

        def __init__(self, id, name, description):
            self.id = id
            self.university_name = name
            self.university_description = description

    class Enrolle(Base):
        __tablename__ = "enrolle"
        id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
        surname = Column(String(30))
        name = Column(String(20))
        middle_name = Column(String(20))
        gender = Column(String(1))
        nationality = Column(String(30))
        birthdate = Column(DateTime)
        home_address = Column(String(256))
        CT_rating = Column(SmallInteger)
        passing_score = Column(SmallInteger)
        university_id = Column(Integer, ForeignKey("university.id"))

        def __repr__(self):
            return "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                self.id, self.surname, self.name, self.middle_name, self.gender, self.nationality, self.birthdate,
                self.home_address, self.CT_rating, self.passing_score, self.university_id)

        def __init__(self, surname, name, middle_name, gender, nationality, birthdate, home_address, CT_rating,
                     passing_score, university_id):
            self.name = name
            self.middle_name = middle_name
            self.gender = gender
            self.surname = surname
            self.nationality = nationality
            self.birthdate = birthdate
            self.home_address = home_address
            self.CT_rating = CT_rating
            self.passing_score = passing_score
            self.university_id = university_id

    def __init__(self):
        self.engine = sqlalchemy.create_engine("mysql+pymysql://root:757020Key@localhost/enrolle_db", echo=None)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.metadata = sqlalchemy.MetaData(bind=self.engine)
        self.metadata.create_all(bind=self.engine)
        self.session.add_all((self.Enrolle('Belevich', 'Mikhail', 'Andreevich', 'M', 'belarussian', '0000-00-00',
                                           '246000,Belarus,Gomel,International street,15,7', 382, 364, None),
                              self.Enrolle('Ishchenko', 'Ivan', 'Sergeevich', 'M', 'belarussian', '0000-00-00',
                                           '246000,Belarus,Gomel,Portovaya street,51', 364, 364, None),
                              self.Enrolle('Korolko', 'Olga', 'Yurievna', 'F', 'belarussian', '0000-00-00',
                                           '246000,Belarus,Pinsk,Krasnoflotskaya 8,2', 350, 328, None)))

    def count_query(self) -> int:
        view = self.session.query(func.count()).filter(self.Enrolle.passing_score > 250).scalar()
        return view

    def sum_query(self) -> int:
        view = int(self.session.query(func.sum(self.Enrolle.CT_rating)).filter(self.Enrolle.gender == "M").scalar())
        return view

    def min_max_query(self) -> tuple[int, int]:
        view = self.session.query(func.max(self.Enrolle.CT_rating), func.min(self.Enrolle.CT_rating)).all()
        for min_val, max_val in view:
            return min_val, max_val

    def join_query(self) -> list[Enrolle]:
        view = self.session.query(self.Enrolle, self.University).join(self.University,
                                                                      self.Enrolle.university_id == self.University.id).filter(
            self.University.id == 3).all()
        return view

    def select_query(self) -> list[Enrolle]:
        view = self.session.query(self.Enrolle).filter(self.Enrolle.passing_score > 225).all()
        return view
