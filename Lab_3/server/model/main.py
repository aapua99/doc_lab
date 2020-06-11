from base import *
from models import *
from datetime import date

session = Session()

def skip_space_between_model(file):
    next(file)
    next(file)
    next(file)

if __name__ == "__main__":
    file = open("db.csv", "r",encoding='utf8')
    next(file)
    skip_space_between_model(file)
    session = Session()
    id=0
    for line in file:
        
        if(line[0]=='\n'):
            break
        id+=1
        user_data = line.split(',')
        user = Users(id,user_data[0], user_data[1],user_data[2],date.fromisoformat(user_data[3][:-1]))
        session.add(user)
    session.commit()
    skip_space_between_model(file)
    id=0
    for line in file:
        if(line[0]=='\n'):
            break
        id+=1
        language = Languages(id,line[:-1])
        session.add(language)
    session.commit()
    skip_space_between_model(file)
    id = 0
    for line in file:
        if(line[0]=='\n'):
            break
        id += 1
        tag = Tags(id, line[:-1])
        session.add(tag)
    session.commit()
    skip_space_between_model(file)
    id = 0
    for line in file:
        if(line[0]=='\n'):
            break
        id += 1
        creator_data = line.split(',')
        creator = Creators(id, creator_data[0], int(creator_data[1]))
        session.add(creator)
    session.commit()
    skip_space_between_model(file)
    id =0
    for line in file:
        if(line[0]=='\n'):
            break
        id+=1
        game_data = line.split(',')
        game = Games(id,game_data[0], game_data[1], float(game_data[2]), game_data[3], int(game_data[4]))
        session.add(game)
    session.commit()
    skip_space_between_model(file)
    id =0
    games=[]
    users=[]
    for line in file:
        if(line[0]=='\n'):
            break
        id+=1
        game_user = line.split(',')
        game_id = int(game_user[0])
        user_id = int(game_user[1])
        games.append(game_user[0])
        users.append(game_user[1])
        statement = games_users_association.insert().values(id=id, gameID=game_id, userID=user_id, date=date.fromisoformat(game_user[2]), payment = float(game_user[3]))
        session.execute(statement)
        session.commit()
    skip_space_between_model(file)
    id =0
    for line in file:
        if(line[0]=='\n'):
            break
        id+=1
        game_language = line.split(',')
        game_id = int(game_language[0])
        language_id = int(game_language[1])
        statement = games_languages_association.insert().values(id=id, gameID=game_id, languageID=language_id)
        session.execute(statement)
        session.commit()
    skip_space_between_model(file)
    id =0
    for line in file:
        if(line[0]=='\n'):
            break
        id+=1
        game_tag = line.split(',')
        game_id = int(game_tag[0])
        tag_id = int(game_tag[1])
        statement = games_tags_association.insert().values(id=id, gameID=game_id, tagID=tag_id)
        session.execute(statement)
        session.commit()
    skip_space_between_model(file)
    id =0
    for line in file:
        if(line[0]=='\n'):
            break
        id+=1
        status_data = line.split(',')
        status =Statuses(id, int(games[id-1]), int(users[id-1]), int(status_data[2]))
        session.add(status)
    session.commit()
    skip_space_between_model(file)
    id =0
    for line in file:
        if(line[0]=='\n'):
            break
        id+=1
        comment_data = line.split(',')
        comment =Comments(id, int(games[id-1]), int(users[id-1]), comment_data[2])
        session.add(comment)
    session.commit()
    

# tag = Tags()
# tag.name = "hsdasad"
# tag.id = 1
# print(tag)

session.commit()
session.close()