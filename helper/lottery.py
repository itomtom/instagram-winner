import time
import random
from colorama import Fore, Style

def shuffleAndPick(entries=[], exclude=''):
  delay=1
  animation = "|/-\\"
  randomNumber=random.randint(1,100)
  entries = removeFromEntries(entries, exclude)

  print(f"{Fore.RED}Shuffle for {randomNumber} times")
  time.sleep(delay)
  for i in range(randomNumber):
    time.sleep(0.1)
    print(f"Shuffling {animation[i % len(animation)]}", end="\r")
    random.shuffle(entries)
  print(f"Finished Shuffling\n{Style.RESET_ALL}")
  winner = entries[random.randint(0,len(entries)-1)].split('|')
  return winner[0], winner[1]

def removeFromEntries(entries, exclude):
  if exclude=='':
    return entries
  delay=1
  print(f"{Fore.RED}Removing {exclude} from entries for next winner{Style.RESET_ALL}")
  time.sleep(delay)
  return [entry for entry in entries if entry.split('|')[0] not in [exclude]]
