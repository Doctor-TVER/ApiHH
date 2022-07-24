from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///orm.sqlite', echo=False)

Base = declarative_base()

vacancyskill = Table('vacancyskill', Base.metadata,
                     Column('id', Integer, primary_key=True),
                     Column('vacancy_id', Integer, ForeignKey('vacancy.id')),
                     Column('skill_id', Integer, ForeignKey('skill.id'))
                     )


class Skill(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(Integer, nullable=True)

    # note = Column(String, nullable=True)

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f'{self.id}) {self.name}: {self.number}'


class Vacancy(Base):
    __tablename__ = 'vacancy'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    region_id = Column(Integer, ForeignKey('region.id'))

    def __init__(self, name, region_id):
        self.name = name
        self.region_id = region_id


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)


session = Session()


session.add_all([Region('Москва', 0), Region('Питер', 78)])

# Скилы
# session.add_all([Skill('python'), Skill('java')])

session.commit()

# Создадим вакансии в разных регионах
regions = session.query(Region).all()

for region in regions:
    new_vacancy = Vacancy('python developer', region.id)
    session.add(new_vacancy)

session.commit()

moscow = session.query(Region).filter(Region.name == 'Москва').first()
print(moscow)

vacancies = session.query(Vacancy).filter(Vacancy.region_id == moscow.id).all()

print(len(vacancies))
print(vacancies[0].region_id)