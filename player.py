from board import Board

class Player:
    def __init__(self, checker):
        """Constructs the player object
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker 
        self.num_moves = 0 
    
    def __repr__(self):
        """Returns a string representing the player object
        """
        return 'Player' + ' ' + str(self.checker)
    
    def opponent_checker(self):
        """Returns a string a one-character string representing the checker 
           of the Player object’s opponent
        """
        if self.checker == 'O':
            return 'X'
        if self.checker == 'X':
            return 'O'
    
    def next_move(self, b):
        """Returns the column where the player wants to make the next move
        """
        col = int(input('Enter a column: '))
        
        while True:
            if b.can_add_to(col):
                self.num_moves += 1 
                break 
            print('Try again!')
            col = int(input('Enter a column: '))
        return col 


    
    
    
    
    
    
    
        
       
          
            
        
        
        
        
        
