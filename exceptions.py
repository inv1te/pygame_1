from telnetlib import GA
import models

def save_score_to_txt(score):
    def exception_decorator(func):
        print('Got score!')
        with open('scores.txt', 'w') as file:
            file.write(str(score))
        return func
    return exception_decorator
    

class GameOver(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None    
    def __str__(self):
        obj_player = self.message
        obj_players_score = models.Score(obj_player.name, obj_player.score)
        if self.message:
            obj_players_score.score_appending()
            return 'Game is over! \nYour total score: ' + obj_player.score 
        else:
            return 'Gameover has been raised'

def main():
    #p1 = models.Player('Danil')
    #p1.score = 15
    #raise GameOver(p1)
    pass
if __name__ == "__main__":
    main()

class EnemyDown(Exception):
    pass


