import os


def clear_screen():
    os.system("cls" if os.name =="nt" else "clear")

class Player:
    def __init__(self):
        self.name = ""
        self.sympol = ""
        
    def choose_name(self):
            while True:
                name = input("Enter your name : ")
                if name.isalpha():
                    self.name = name
                    break
                print("make sure you enter letters only.")
        
        
    def choose_sympol(self):
            while True:
                sympol = input(f"{self.name} enter the sympol you want to play with : ")
                if sympol.isalpha() and len(sympol)==1 :
                    self.sympol = sympol.upper()
                    break
                print("make sure you enter a single chat only : ")
                
        
class Menu:
    def validate_intput(self):
        while True:
            choice = input("enter your choice (1 or 2) : ")
            if choice  == "1" or choice  == "2":
                break
            print(" make sure you enter valid option") 
        return choice
    
    def display_main_menu(self):

        print("""
              ============================
              | 1. start game             |
              | 2. exit game              |
              ============================
              """)
        return self.validate_intput()

      
        
    def display_end_menu(self):
        print("""
              ============================
              | 1. restart game           |
              | 2. exit game              |
              ============================
              """)
        return self.validate_intput()
       

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]
        
    def diplay_board(self):
        for i in range(0,9,3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-"*5)
 
                
    def update_board(self , choice , sympol):
        if self.is_valid_move(choice):
            self.board[choice-1] = sympol
            return True
        return False
            
        

         
    def is_valid_move(self , choice):
         if choice > 9 or choice<1:
             print("enter a valid number")
             return False
         else:
            return self.board[choice-1].isdigit()
        
        
        
    def reset_board(self):
        self.board = [str(i) for i in range(1,10)]
        
        
            

             
class Game:
    def __init__(self):
        self.menu =Menu()        
        self.board=Board()
        self.players=[Player() , Player()]
        self.CurrentPlayer=0
        
    def start_game(self):
        choice =  self.menu.display_main_menu()
        if choice=="1":
            self.setup_player()
            self.play_game()
        else:
            self.quit_game()

        
    def setup_player(self):
        for number,player in enumerate(self.players , start=1):
            print(f" palyer {number} enter your data")
            player.choose_name()
            player.choose_sympol()
        clear_screen()
    
    
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
               choice =  self.menu.display_end_menu()
               if choice =="1":
                   self.restart_game()
               else:
                   self.quit_game()
                   #break
            
            
         
        
    def restart_game(self):
        self.board.reset_board()
        self.CurrentPlayer = 0
        self.play_game()
            
    def play_turn(self):
        player = self.players[self.CurrentPlayer]
        clear_screen()
        self.board.diplay_board()
        print(f"{player.name} turn  ({ player.sympol })")
        try:
            while True:
                cell_choice = int(input("choose a cell (1-9)"))
                if self.board.update_board(cell_choice , player.sympol):
                    break
                else:
                    print("invalid move")
        except ValueError:
            print("enter a number from 1 - 9 ")
            
        self.switch_player()
            
            
        
    def switch_player(self):
        self.CurrentPlayer  = 1 -self.CurrentPlayer
        
    
    def check_win(self):
        winning_combinations = [[0,1,2] , [3,4,5] , [6,7,8] , [0,3,6] , [1,4,7] , [2,6,8] , [0,4,8] , [2,4,6]]
        for combo in winning_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]] :
                clear_screen()
                print(f"{self.players[1 - self.CurrentPlayer].name} won")
                print(f"{self.players[self.CurrentPlayer].name} Lose")
                self.board.diplay_board()
                return True
            
        return False
    
    
                                                                                                                                                                                                                       
    def check_draw(self):
        sympol1 = self.players[0].sympol
        sympol2 = self.players[1].sympol
        if self.board.board.count(sympol1)  + self.board.board.count(sympol2) == 9:
            print("draw")
            return True
    
    def quit_game(self):
            clear_screen()
            print("thank you for playing")
            exit()        
        
        
        
        

game = Game()
game.start_game()
    
        
        
         
         
             
        
         
    