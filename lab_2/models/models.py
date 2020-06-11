from base import Base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship

class Comments(Base):
    __tablename__ = "Comments"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('Users.id'))
    gameID = Column(Integer ,ForeignKey('Games.id'))
    comment = Column(String(255))

    def __init__(self, id, gameID, userID, comment):
        self.id = id
        self.userID = userID
        self.gameID = gameID
        self.comment = comment

games_tags_association = Table('Games_Tags', Base.metadata,
    Column('id',Integer,primary_key=True),
    Column('gameID', Integer, ForeignKey('Games.id')),
    Column('tagID', Integer, ForeignKey('Tags.id'))
)

class Games(Base):
    __tablename__ = 'Games'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Float)
    systemRequirements = Column(String(255))
    creatorID = Column(Integer ,ForeignKey('Creators.id'))
    creator = relationship('Creators')
    comments = relationship('Comments')
    tags = relationship("Tags", secondary=games_tags_association)

    def __init__(self, id, name, description, price, systemRequirements,creatorID):
        self.id = id
        self.name =name
        self.description = description
        self.price = price
        self.systemRequirements = systemRequirements
        self.creatorID =creatorID



class Tags(Base):
    __tablename__ = 'Tags'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    games = relationship("Games", secondary=games_tags_association)

    def __init__(self, id, name):
        self.id = id
        self.name = name



class Languages(Base):
    __tablename__ = 'Languages'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, id, name):
        self.id=id
        self.name = name

games_languages_association = Table('Game_Languages', Base.metadata,
    Column('id',Integer,primary_key=True),
    Column('gameID', Integer, ForeignKey('Games.id')),
    Column('languageID', Integer, ForeignKey('Languages.id'))
)

class Creators(Base):
    __tablename__ = 'Creators'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    games = relationship("Games")
    percentage_of_profit = Column(Integer)

    def __init__(self, id, name, percentage_of_profit):
        self.id =id
        self.name = name
        self.percentage_of_profit = percentage_of_profit

class Statuses(Base):
    __tablename__ = "Statuses"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('Users.id'))
    gameID = Column(Integer ,ForeignKey('Games.id'))
    status = Column(Integer)
    game = relationship('Games')

    def __init__(self, id, gameID, userID, status):
        self.id = id
        self.userID = userID
        self.gameID = gameID
        self.status = status

games_users_association = Table('Games_Users', Base.metadata,
    Column('id',Integer,primary_key=True),
    Column('gameID', Integer, ForeignKey('Games.id')),
    Column('userID', Integer, ForeignKey('Users.id')),
    Column('date',Date),
    Column('payment',Float)
)
class Users(Base):
    __tablename__ = 'Users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    firstName = Column(String(255))
    lastName = Column(String(255))
    username = Column(String(255))
    dateOfBithday = Column(Date)
    statuses = relationship("Statuses")
    games = relationship("Games", secondary=games_users_association)
    comments = relationship('Comments')

    def __init__(self, id, firstName, lastName, username, dateOfBithday):
        self.id =id
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.dateOfBithday = dateOfBithday
