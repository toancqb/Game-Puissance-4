###############################
## Author: TRAN Quang Toan   ##
## Project Game Puissance 4  ##
## Version 1                 ##
## 10 Feb 2020               ##
###############################

from termcolor import colored, cprint

TITLE = '\n                             \n     [---PUISSANCE 4---]     \n                             '
COLORED_TITLE = colored(TITLE, 'red', 'on_white', attrs=['bold'])
TX = 6
TY = 7

INF = 10000000000000
NEG_INF = -10000000000000

CT = colored('|', 'cyan','on_white')
BT = colored('=', 'cyan','on_white')
BLK = ' '
BLK2= '   '
PLAYER_COLORED = [colored('-O-', 'red','on_yellow', attrs=['bold'])
	, colored('-X-', 'red','on_blue', attrs=['bold'])]
# PLAYER = (0, 1)
WARN_NUMBER = colored("0 -> 6 Seulement, Si vous plait!", 'red', 'on_white', attrs=['bold'])
WARN_NUMBER_MENU = colored("1 -> 5 Seulement, Si vous plait!", 'red', 'on_white', attrs=['bold'])
WARN_NUMBER_TURN = colored("0 -> 1 Seulement, Si vous plait!", 'red', 'on_white', attrs=['bold'])
WARN_TYPE = colored("Integer Seulement, Si vous plait! type again!", 'red', 'on_white', attrs=['bold'])
WARN_ILLEGALMOVE = colored("Out of Range, Please try again!", 'red', 'on_white', attrs=['bold'])

COLORDED_OPT = colored("\n                             \n1. 2 Players                 \n2. vs Computer(StupidAI)     \n3. vs Computer(NormalAI)     \n4. vs Computer(MinimaxAI)    \n5. AI vs AI                  \n                             \n"
	, 'red', 'on_white', attrs=['bold'])
TIE = colored("It's a tie", 'red', 'on_white', attrs=["bold"])
CHOOSE_TURN = colored("\n Do you want to play first? \n Press 1 for YES \n Press 0 for NO\n", 'white', 'on_red', attrs=["bold"])
TIME_PENALTY = 10 ## Pour que AI choisi le mouvement Gagne des que possible
