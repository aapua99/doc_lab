from model.models import DB
db=DB()

class Controller:
    def create_game(self, game):
        string = game.decode("utf-8")      
        game_arr = string.split("&")
        game_param = []
        for i in game_arr:
            game_param.append(i.split("=")[1])
        db.add_game_to_db(game_param)

    def get_game(self, start_str, number_str):
        start =int(start_str)
        number =int(number_str)
        if(number<=0):
            return False
        if(start<0):
            return False
        response = db.get_game_from_db(start, number)
        return response

    def update_game(self,game):
        if(game == None):
            return False
        print(game)
        string = game.decode("utf-8")
        game_arr = string.split("&")
        game_param = []
        for i in game_arr:
            game_param.append(i.split("=")[1])
        return db.update_game_in_db(game_param)

    def delete_game(self,game):
        if(game == None):
            return False
        print(game)
        string = game.decode("utf-8")
        game_arr = string.split("&")
        game_param = []
        for i in game_arr:
            game_param.append(i.split("=")[1])
        return db.delete_game_from_db(game_param)