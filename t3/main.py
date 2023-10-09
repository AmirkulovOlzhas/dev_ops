import sys
import random
import hmac
from tabulate import tabulate

class Game():
    args = sys.argv
    args.remove('main.py')

    Log = []
           
    user_move = ''
    pc_move = 0

    def set_user_move(self):
        print('Aviable moves:')
        for i in range(len(self.args)):
            print(f'{i+1} - {self.args[i]}')
        print('0 - exit\n? - help')
        self.user_move = input('Enter your move: ')
        try: 
            self.user_move = int(self.user_move)
            if int(self.user_move) > len(self.args) or int(self.user_move) < 0:
                print('Out of range')
                self.set_user_move()
            
        except ValueError:
            if self.user_move != '?':
                print("Enter a number or '?'")
                self.set_user_move()

    
    def get_user_move(self):
        return self.user_move


    def set_pc_move(self, hm):
        self.pc_move = random.randint(1, len(self.args))
        hm.set_pc_move(self.pc_move)


    def get_pc_move(self):
        return self.pc_move


    def check_args(self):
        if len(self.args) < 3:
            print('Not enough arguments')
            return True
        else:
            if len(self.args)%2 == 0:
                print('The number of arguments must be odd')
                return True
            else:
                # HMAC
                return False
            

class Table_Gen(Game):
    def __init__(self) -> None:
        super().__init__()
        self.Log = Game.Log
        self.table = self.create_table()
    
    
    def info_table(self):
        print(tabulate(self.table, headers=self.args, showindex=self.args, tablefmt='fancy_grid'))
        print(tabulate(self.Log, headers=['User', 'PC', 'Result'], tablefmt='fancy_grid'))

    def create_table(self):
        half = int((len(self.args)-1)/2)
        List = []
        for i in range(len(self.args)):
            L = []
            if i<half:
                range_value = range(i+1, i+1+half)
                result_1 = 'Win'
                result_2 = 'Lose'
            else:
                range_value = range(i-half, i)
                result_1 = 'Lose'
                result_2 = 'Win'
            for j in range(len(self.args)):
                if j in range_value:
                    L.append(result_1)
                elif j == i:
                    L.append('Draw')
                else:
                    L.append(result_2)
            List.append(L)
        return List
                
                


    


class game_rules(Game):
    def __init__(self, Game) -> None:
        super().__init__()
        self.args = Game.args
        self.user_move = Game.user_move
        self.pc_move = Game.pc_move
        self.half = (len(self.args)-1)/2
    
    
    def check_winner(self):
        if self.user_move == self.pc_move:
            return 'Draw!'
        if self.user_move>self.pc_move:
            if self.user_move-self.pc_move > self.half:
                return 'You win!'
        if self.user_move<self.pc_move:
            if self.pc_move-self.user_move < self.half:
                return 'You win!'
        return 'You lose!'


class HM_key(Game):
    hmac_key = None
    move = ''

    def set_pc_move(self, pc_move):
        self.pc_move = pc_move
        self.move = Game.args[self.pc_move-1].encode('utf-8')
        self.key = self.gen_random_key()
        self.hmac_key = self.gen_hmac()


    def gen_random_key(self):
        x = str(hex(random.getrandbits(256)))
        return x[2:]
    

    def get_key(self):
        return self.key
    

    def gen_hmac(self):
        x = hmac.new(bytes(self.key, 'utf-8'), self.move, digestmod='sha256').hexdigest()
        print(f'HMAC: {x}')
        return x
    

    def get_hmac(self):
        return self.hmac_key

    



def main():
    game = Game()
    table = Table_Gen()
    
    hm = HM_key()


    if game.check_args():
        sys.exit(0)

    
    while True:
        game.set_pc_move(hm)
        game.set_user_move()
        if game.get_user_move() == 0:
            break
        else:
            if game.get_user_move() == '?':
                table.info_table()
                continue
            print(f'Your move: {game.args[game.get_user_move()-1]}')
            print(f'Computer move: {game.args[game.get_pc_move()-1]}')
            check = game_rules(Game=game)
            result = check.check_winner()
            print(result)
            print(f'HMAC key: {hm.get_key()}')
            game.Log.append([game.args[game.get_user_move()-1], game.args[game.get_pc_move()-1], result])

            input_value = input('Play again? y/n/?: ')
            if input_value == '?':
                table.info_table()
                continue
            if input_value != 'y':
                break


if __name__ == '__main__':
    main()