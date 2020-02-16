import time
import sys
from colorama import Back, Fore, Style

def printWinnerMessage(winner='', comment='', prefix=''):
  if winner=='' or comment=='':
    print(f"{Fore.WHITE} Something went wrong, please contact @itomtomfood")
    sys.exit()

  delay=2
  print(f"{Fore.BLUE}The {prefix}Winner is...")
  time.sleep(delay)
  print(f"{Back.BLUE}{Fore.WHITE}=> {winner} <=")
  print(f"  tagging: {comment}{Style.RESET_ALL}\n")
  time.sleep(delay)