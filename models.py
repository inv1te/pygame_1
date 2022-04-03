from random import randint
import exceptions
import settings
from datetime import datetime, date, time

class Score:
    player_name = ''
    player_score = ''
    player_record_date = datetime.now()
    all_scores = []
    def score_appending(self):
        with open('scores.txt', 'r') as file:
            for i in file.read().splitlines():
                self.all_scores.append(i)
        new_score = (self.player_name + ' | ' +\
                        str(self.player_score) + ' | ' +\
                        str(self.player_record_date)
                    )
        self.all_scores.append(new_score)
        with open('scores.txt', 'w') as file:
            file.write("Player's name | Player's score | Date")
            for i in self.all_scores:
                file.write(i + '\n')
    
    def __init__(self, name, score) -> None:
        self.player_name = name
        self.player_score = score
        
class Enemy:
    level = 0
    lives = 0
    
    @staticmethod
    def select_attack():
        return randint(1, 3)
    
    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise exceptions.EnemyDown

    def __init__(self, level):
        self.level = level
        self.lives = level    
        
class Player:
    name = ''
    lives = settings.PLAYERS_LIVES
    score = 0
    allowed_atacks = 0
    
    @staticmethod
    def fight(attack,defence):
        print('! Fighting !\n' +\
                f'Your attack: {attack}\n' +\
                f'Enemy attack: {defence}'
            )
        if attack == 1:
            if defence == 1:
                return 0
            elif defence == 2:
                return 1
            elif defence == 3:
                return -1
        elif attack == 2:
            if defence == 1:
                return -1
            elif defence == 2:
                return 0
            elif defence == 3:
                return 1
        elif attack == 3:
            if defence == 1:
                return 1
            elif defence == 2:
                return -1
            elif defence == 3:
                return 0
    
    def decrease_lives(self):
        self.lives -= 1
        print('Remains lives: ' + str(self.lives))
        if self.lives <= 0:
            raise exceptions.GameOver(self)
    
    def attack(self, enemy_obj):
        players_attack = int(input('Выберите атаку: \n1 - Волшебник \n2 - Воин \n3 - Разбойник.\n'))
        if players_attack == 1 or players_attack == 2 or players_attack == 3:
            pass
        else:
            raise ValueError('Enter Correct Value')
        enemy_attack = enemy_obj.select_attack()
        fight_result = self.fight(players_attack, enemy_attack)
        if fight_result == 1:
            enemy_obj.decrease_lives()
            print("You attacked successfully!\n"+ \
                    "Enemie's remains lives: " + str(enemy_obj.lives)
                )
        elif fight_result == 0:
            print("It's a draw!")
        elif fight_result == -1:
            print("You missed!")
    
    def defence(self, enemy_obj):
        players_defence = int(input('Выберите защиту: \n1, 2 или 3.\n'))        
        if players_defence == 1 or players_defence == 2 or players_defence == 3:
            pass
        else:
            raise ValueError('Enter Correct Value')
        enemy_attack = enemy_obj.select_attack()
        fight_result = self.fight(enemy_attack, players_defence )
        if fight_result == 1:
            print("Enemy hit you!")
            self.decrease_lives()
        elif fight_result == 0:
            print("You blocked the damage!")
            pass
        elif fight_result == -1:
            print("You blocked the damage!")
        
        
    def __init__(self, name):
        self.name = name 
    
    def __str__(self):
        return 'Name: ' + self.name +\
            '\nLives: ' + str(self.lives)    
    
e1 = Enemy(5)
##print(e1.decrease_lives())
##print(e1.lives)
##print('-----------------')

##print(p1.fight(1,1))
#p1 = Player('Danil')
#p1.score = 15
#data_obj = Score(p1.name, p1.score)
#print(data_obj.score_appending())

