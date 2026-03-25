class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    def __init__(self, height, width): 
        """ Contructor for board objects 
        """
        self.height = height 
        self.width = width 
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string
        
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        for col in range(2*self.width + 1):
            s += '-' 
        s += '\n' 
        
        for i in range(self.width):
            if i > 9:
                i -= 10
            s += ' ' + str(i) 
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        row = 0 
        for row in range(self.height):
            if self.slots[row][col] == ' ':
                row += 1 
            if row + 1 > self.height:
                row -= 1
        while self.slots[row][col] != ' ':
            row -= 1
        
        self.slots[row][col] = checker
     
    def reset(self):
        """ resets the board; removes all pieces
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] != ' ':
                    self.slots[row][col] = ' '
                
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
                
    def can_add_to(self, col):
        """returns True is there is an empting slot in the col, False if otherwise 
        """
        if col < 0 or col >= self.width:
            return False 
        else: 
            for row in range(self.height):
                if self.slots[row][col] == ' ':
                    return True
        return False
    
    def is_full(self):
        """returns True if the board is full, False if otherwise
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] == ' ':
                    return False
        return True 
    
    def remove_checker(self, col):
        """removes the top checker of the col from the board
        """
        row = 0 
        assert(col >= 0 and col < self.width)
        
        row = 0 
        for r in range(self.height):
            if self.slots[row][col] == ' ':
                row += 1 
            if row + 1 > self.height:
                row -= 1
        self.slots[row][col] = ' '
    
    def is_win_for(self, checker):
        """returns True if there are 4 consecutive checkers vertically, 
           horizintally, or diagonally on the board. False if otherwise.
        """
        if self.is_vertical_win(checker) == True or self.is_horizontal_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True or self.is_up_diagonal_win(checker):
            return True 
        else:
            return False 
    
    def is_vertical_win(self, checker):
        """Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True 
        return False
    
        
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False
    
    def is_down_diagonal_win(self, checker):
        """Checks for a diagonal win that goes down for the specified checker. 
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """Checks for a diagonal win that goes up for the specified checker. 
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False
    
    
    
        
    


        
        
        
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
