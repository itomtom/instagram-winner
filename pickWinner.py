from helper.welcomeMessage import printWelcomeMessage
from helper.entries import getEntries
from helper.lottery import shuffleAndPick
from helper.winnerMessage import printWinnerMessage
from colorama import init, Fore, Back, Style 
init()
me = '@itomtomfood'

printWelcomeMessage()
entries = getEntries()
winner, comment = shuffleAndPick(entries)
printWinnerMessage(winner, comment, 'first is ')
winner, comment = shuffleAndPick(entries, winner)
printWinnerMessage(winner, comment, 'second is ')
