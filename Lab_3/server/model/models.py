from model.base import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship
import json

session = Session()

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
    
    def __init__(self, name, description, price, systemRequirements,creatorID):
        self.name =name
        self.description = description
        self.price = price
        self.systemRequirements = systemRequirements
        self.creatorID =creatorID

    def get_json(self):
        map_object = {
            "id" : self.id,
            "name" : self.name,
            "description" : self.description,
            "price" : self.price,
            "systemRequirements" : self.systemRequirements,
            "creatorID" : self.creatorID
        }

        json_str = json.dumps(map_object)
        return json_str



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

class DB:
    def add_game_to_db(self, game):
        game_object = Games(game[0], game[1], float(game[2]), game[3], int(game[4]))
        session.add(game_object)
        session.commit()
        print("Added game")
    
    def get_game_from_db(self, start, count):
        response = []
        for i in range(start, start+count):
            game_object = session.query(Games).get(i)
            if(game_object == None):
                return response
            game_json_str = game_object.get_json()
            response.append(game_json_str)
        return response

    def update_game_in_db(self, game):
        game_object = session.query(Games).get(int(game[0]))
        if(game_object == None):
            return False
        game_object.name = game[1]
        game_object.description = game[2]
        game_object.price = float(game[3])
        game_object.systemRequirements = game[4]
        game_object.creatorID = int(game[5])
        session.add(game_object)
        session.commit()
        return True

    def delete_game_from_db(self, game):
        game_object = session.query(Games).get(int(game[0]))
        if(game_object == None):
            return False
        session.delete(game_object)
        session.commit()
        return True
        
        
        




