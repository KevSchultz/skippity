#  ██╗  ██╗███████╗
#  ██║ ██╔╝██╔════╝
#  █████╔╝ ███████╗
#  ██╔═██╗ ╚════██║
#  ██║  ██╗███████║
#  ╚═╝  ╚═╝╚══════╝
import random
import pprint

class board:
    """
    Data Structure representing the game state of the skippity board. 

    The default game has five different colored skippers: red, yellow, orange, green, and blue.
    However, the current implementation can use arbitrary colors.  
    """
    def __init__(self, rows, cols):
        """
        Initialize a new instance of the board.

        Args:
            rows (int): number of rows
            cols (int): number of columns
        
        Returns:
            None
        """
        self.rows = rows
        self.cols = cols
        self.state = [["" for c in range(cols)] for r in range(rows)]
    
    def generate_random_board(self, colors):
        """
        Fills a random configuration of approximately an equaly amount of each color skipper.

        Args:
            None
        
        Returns:
            None
        """
        n = self.rows * self.cols
        skippers_per_color = n // len(colors)

        skippers = []

        # Add each color
        for color in colors:
            skippers.extend([color] * skippers_per_color)
        
        # Mix up the skippers. 
        random.shuffle(skippers)

        # Fill the board
        for r in range(self.rows):
            for c in range(self.cols):
                self.state[r][c] = skippers.pop()
    
    def __str__(self):
        return pprint.pformat(self.state)

