#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#
 
import random 
from ps9pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ Constructs a new AI player object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak 
        self.lookahead = lookahead 

    def __repr__(self):
        """ Returns a string that represents the AI player object
        """
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """ Determines the column(s) that yield the max score
        """
        max_score = []
        
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_score += [i]
        if self.tiebreak == 'RANDOM':
            choices = [0,1]
            if random.choice(choices) == 0 :
                return max_score[0]
            else:
                return max_score[-1]
        elif self.tiebreak == 'LEFT':
            return max_score[0]
        elif self.tiebreak == 'RIGHT':
            return max_score[-1]
    
    def scores_for(self, b):
        """ Determines the scores for each of the cols in the board object 
        """
        scores = [0] * len(range(b.width))
        
        for i in range(b.width):
            if b.can_add_to(i) == False:
                scores[i] = -1
            elif b.is_win_for(self.checker):
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[i] = 0 
            elif self.lookahead == 0:
                scores[i] = 50 
            else:
                b.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opponent_score = opponent.scores_for(b)
                
                if 100 in opponent_score: 
                    scores[i] = 0 
                elif 50 in opponent_score:
                    scores[i] = 50
                elif 0 in opponent_score:
                    scores[i] = 100 
                    
                b.remove_checker(i)
        return scores

    def next_move(self, b): 
        """ Determines the AI player object's optimal next move
        """
        scores = self.scores_for(b)
        return self.max_score_column(scores)
                

                
                
                
                
                
                
        

        