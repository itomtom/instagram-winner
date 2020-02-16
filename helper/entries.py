import csv
import re
import os
import time
import sys
from colorama import Fore, Style

def getEntries(me='@itomtomfood'):
  entries = set()
  with open(os.path.join(os.getcwd(), 'comments.csv')) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    printEntries(me)
    for row in csv_reader:
      user = f"@{row[2]}"
      comment = re.search(r"@[\w\.\_]+", row[1].strip())
      if not validEntry(row[3]) or user == me or not comment or user == comment.group():
        continue
      entries.add(user + "|" + comment.group())
  csv_file.close()
  return list(entries)

def validEntry(tagId):
  return tagId.isdigit()

def printEntries(me='@itomtomfood'):
  delay=3
  print(f"{Fore.YELLOW}Removing invalid comments", end="\r")
  time.sleep(delay)
  sys.stdout.write("\033[K")
  print(f"Removing comments made by myself {me}", end="\r")
  time.sleep(delay)
  sys.stdout.write("\033[K")
  print("Removing comments not tagging anyone", end="\r")
  time.sleep(delay)
  sys.stdout.write("\033[K")
  print(f"Building final list of entries\n{Style.RESET_ALL}")
  time.sleep(delay)