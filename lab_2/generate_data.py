import names
import datetime
import random
from random_word import RandomWords
import requests
from random import seed
from random import randint
from essential_generators import DocumentGenerator
NUM_OF_GAMES = 250
NUM_OF_CREATORS = 50
NUM_OF_USERS = 250
NUM_OF_LANGUAGES =50
NUM_OF_TAGS =10

arrays = []

def remove_enter(str):
    result=''
    for i in str:
        if(i!='\n'):
            if(i==','):
                result+='.'
            else:
                result+=i
    return result

def generate_users(file):
    print("Start generating Users")
    file.write("\n\n*****************************model Users*****************************\n")
    file.write("firstName,lastName,username,dateOfBithday\n")
    for i in range(250):
        start_date = datetime.date(1960, 1, 1)
        end_date = datetime.date(2001, 12, 31)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        first_name=names.get_first_name()
        last_name=names.get_last_name()
        file.write(first_name+","+last_name+","+first_name+last_name+","+str(random_date)+"\n")
    print("End generating Users")

def generate_languages(file):
    print("Start generating Languages")
    file.write("\n\n*****************************model Languages*****************************\n")
    file.write("name\n")
    file.write("Mandarin Chinese\n")
    file.write("Spanish\n")
    file.write("English\n")
    file.write("Hindi (Sanskritised Hindustani)[9]\n")
    file.write("Bengali\n")
    file.write("Portuguese\n")
    file.write("Russian\n")
    file.write("Japanese\n")
    file.write("Western Punjabi[10]\n")
    file.write("Marathi\n")
    file.write("Telugu\n")
    file.write("Wu Chinese\n")
    file.write("Turkish\n")
    file.write("Korean\n")
    file.write("French\n")
    file.write("German\n")
    file.write("Vietnamese\n")
    file.write("Tamil\n")
    file.write("Yue Chinese\n")
    file.write("Urdu (Persianised Hindustani)[9]\n")
    file.write("Javanese\n")
    file.write("Italian\n")
    file.write("Egyptian Arabic\n")
    file.write("Gujarati\n")
    file.write("Iranian Persian\n")
    file.write("Bhojpuri\n")
    file.write("Min Nan Chinese\n")
    file.write("Hakka Chinese\n")
    file.write("Jin Chinese\n")
    file.write("Hausa\n")
    file.write("Kannada\n")
    file.write("Indonesian (Indonesian Malay)\n")
    file.write("Polish\n")
    file.write("Yoruba\n")
    file.write("Xiang Chinese\n")
    file.write("Malayalam\n")
    file.write("Odia\n")
    file.write("Maithili\n")
    file.write("Burmese\n")
    file.write("Eastern Punjabi[10]\n")
    file.write("Sunda\n")
    file.write("Sudanese Arabic\n")
    file.write("Algerian Arabic\n")
    file.write("Moroccan Arabic\n")
    file.write("Ukrainian\n")
    file.write("Igbo\n")
    file.write("Northern Uzbek\n")
    file.write("Sindhi\n")
    file.write("North Levantine Arabic\n")
    file.write("Romanian\n")
    print("End generating Languages")

def generate_tags(file):
    print("Start generating Tags")
    file.write("\n\n*****************************model Tags*****************************\n")
    file.write("name\n")
    file.write("Action\n")
    file.write("Adventure\n")
    file.write("Fighting\n")
    file.write("Platform\n")
    file.write("Puzzle\n")
    file.write("Racing\n")
    file.write("Role-playing\n")
    file.write("Shooter\n")
    file.write("Simulation\n")
    file.write("Sports\n")
    file.write("Strategy\n")
    print("End generating Tags")

def generate_creators(file):
    print("Start generating Creators")
    file.write("\n\n*****************************model Creators*****************************\n")
    file.write("name\n")
    seed(1)
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    words_list = response.content.splitlines()
    for i in range(50):
        file.write(str(words_list[randint(0, len(words_list))])[2:-1]+" "+str(words_list[randint(0, len(words_list))])[2:-1]+","+str(randint(1,30))+"\n")
    print("End generating Creators")

def generate_games(file):
    print("Start generating Games")
    file.write("\n\n*****************************model Games*****************************\n")
    file.write("name,description,price,systemRequirements,creatorID\n")
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    gen = DocumentGenerator()
    for i in range(NUM_OF_GAMES):
        game_name = ""
        num_of_word_in_name_game = randint(1,3)
        for j in range(num_of_word_in_name_game):
            game_name += gen.word()
        game_name =remove_enter(game_name)
        game_description =gen.sentence()
        game_description = remove_enter(game_description)
        game_system_requirements = gen.word()
        game_system_requirements = remove_enter(game_system_requirements)
        game_price = round(random.uniform(5.5,1000.5),2)
        creator_id =randint(1,NUM_OF_CREATORS)
        file.write(str(game_name)+","+str(game_description)+","+str(game_price)+","+str(game_system_requirements)+","+str(creator_id)+"\n")
    print("End generating Games")

def generate_games_users(file):
    print("Start generating Games_Users")
    file.write("\n\n*****************************model Games_Users*****************************\n")
    file.write("gameID,userID,date\n")
    for i in range(2):
        for j in range(NUM_OF_GAMES):
            start_date = datetime.date(2005, 1, 1)
            end_date = datetime.date(2020, 5, 1)
            time_between_dates = end_date - start_date
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            payment = round(random.uniform(5.5,1000.5),2)
            found = False
            game_id =0
            user_id =0
            while(not found):
                game_id = randint(1,NUM_OF_GAMES)
                user_id =randint(1, NUM_OF_USERS)
                found = True
                for i in arrays:
                    if(game_id == i[0] and user_id == i[1]):
                        game_id = randint(1,NUM_OF_GAMES)
                        user_id =randint(1, NUM_OF_USERS)
                        found =False
                        break
            arrays.append([game_id, user_id])
            file.write(str(game_id)+","+str(user_id)+","+str(random_date)+","+str(payment)+"\n")
    print("End generating Games_Users")

def generate_games_languages(file):
    print("Start generating Games_Languages")
    file.write("\n\n*****************************model Games_Languages*****************************\n")
    file.write("gameID,languageID\n")
    for j in range(NUM_OF_GAMES):
        file.write(str(randint(1,NUM_OF_GAMES))+","+str(randint(1, NUM_OF_LANGUAGES))+"\n")
    print("End generating Game_Languages")

def generate_games_tags(file):
    print("Start generating Games_Tags")
    file.write("\n\n*****************************model Games_Tags*****************************\n")
    file.write("gameID,tagsID\n")
    for j in range(NUM_OF_GAMES):
        file.write(str(randint(1,NUM_OF_GAMES))+","+str(randint(1, NUM_OF_TAGS))+"\n")
    print("End generating Games_Tags")

def generate_statuses(file):
    print("Start generating Statuses")
    file.write("\n\n*****************************model Statuses*****************************\n")
    file.write("gameID,userID,status\n")
    for j in arrays:
        file.write(str(j[0])+","+str(j[1])+","+str(randint(1,100))+"\n")
    print("End generating Statuses")

def generate_comments(file):
    print("Start generating Comments")
    file.write("\n\n*****************************model Comments*****************************\n")
    file.write("gameID,userID,comment\n")
    gen = DocumentGenerator()
    for j in arrays:
        comments = gen.sentence()
        comments = remove_enter(comments)
        file.write(str(j[0])+","+str(j[1])+","+str(comments)+"\n")
    print("End generating Comments")


        
if __name__ == "__main__":
    file = open("db.csv", "w+",encoding='utf8')
    generate_users(file)
    num=250
    generate_languages(file)
    num+=50
    generate_tags(file)
    num+=10
    generate_creators(file)
    generate_games(file)
    generate_games_users(file)
    generate_games_languages(file)
    generate_games_tags(file)
    generate_statuses(file)
    generate_comments(file)
    num+=NUM_OF_CREATORS
    num+=NUM_OF_GAMES
    print(num)
    file.close()
    
