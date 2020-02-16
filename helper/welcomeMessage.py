import time
from colorama import Fore, Style

def printWelcomeMessage():
  delay=2
  print(f"""\
    {Fore.GREEN}

  `-::::-`    ``     `       .-::-.`   
`/+:.```./o.`/o/     :+:   /o:.``.:+/. 
/+          :o:       .o: ++`       /o`
o/          /o///////: +/ o:.+/////:.o`
-o/`     .: `+/`     -+o. -+-      `++ 
 `:++//++/.   -:    `::`   `:-     ::` 
     `                                 
  `:/+++:.     .`    ``      ://+++-`   
`oy/-``.-+s- -so.    /yy:  .so-.` .:ss. 
+y.       ` `yo ``..`.-sy.`yo   `.`  oy`
s/          .y:.+////++sy-.y::oo+ooo:-y.
:y+`     `:. oy.      .sy. oy-      -yo 
 .+so/+oso/`  :o:    .o/`   -+-    `+:  
     ````                                                                        
  `.-:::-.     `-::-:-.     `://-      
`:/.` ``.//.  -/-`   .:/-  -/-:/-      
//   `````:/`-+`       -+-`+.//`   `
/:   -/+/:::`-+`       .+-`+-//.  ./-:/   
`/-    -//.  `:/.     .//  -+::::::-//`
 `--     .::   .://:///-    `-:////:-  

    script by @itomtomfood
""")
  time.sleep(delay)
  print(f"Starting the giveaway for Cha Cha Roll @chacharolluk\n{Style.RESET_ALL}")
  time.sleep(delay)