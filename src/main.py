#  ██╗  ██╗███████╗
#  ██║ ██╔╝██╔════╝
#  █████╔╝ ███████╗
#  ██╔═██╗ ╚════██║
#  ██║  ██╗███████║
#  ╚═╝  ╚═╝╚══════╝
from board import board

# Default Board Settings
ROWS = 10
COLS = 10
COLORS = ['RED', 'YELLOW', 'ORANGE', 'GREEN', 'BLUE']

def main():
    """
    Application entry point containing the main game loop.
    """
    b = board(ROWS, COLS)
    b.generate_random_board(COLORS)
    print(b)

if __name__ == '__main__':
    main()