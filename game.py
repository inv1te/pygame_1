from typing import final
import models, settings, exceptions

def start():
    print(
        '| WELCOME TO THE GAME |\n' +\
            "To start game enter '/play '\n" + 
            "To check the scores enter '/show scores'\n" +
            "To see the existing comands enter '/help'\n" +
            "To exit from the game enter '/exit'\n"    
    )
    choose = input()
    if choose == '/play':
        try:
            play()
        except exceptions.GameOver:
            raise exceptions.GameOver()
        except KeyboardInterrupt:
            pass
        finally:
            print('Good Bye!')
    elif choose == '/show scores':
        with open('scores.txt', 'r') as file:
            data = file.read()
            print(data)
    elif choose == '/help':
        print(
            "'/play' - to start the game \n" +
            "'/show scores' - to check the scores \n" +
            "'/help' - to check the existing comands \n" +
            "'/exit' - to leave the game"
        )
    elif choose == '/exit':
        raise KeyboardInterrupt

def play ():
    player = models.Player(input('Введите имя игрока: \n'))
    print('Players name: ' + player.name)
    
    level = 1
    enemy = models.Enemy(level)
    
    
    while True:
        try:
            player.attack(enemy_obj = enemy)
            player.defence(enemy_obj = enemy)
            
        except exceptions.EnemyDown:
            player.score += 5
            enemy = models.Enemy(enemy.level + 1)
            print('[+] You killed the enemy! [+]\n' +\
                    f'[?] Remains lives: {player.lives} [?]\n' 
                    f'[?] Current enemy level: {enemy.level} [?]\n'  
                    f'[?] Your total score: {player.score} [?]' 
                  )
def main():
    start()

if __name__ == '__main__':
    main()
    
    