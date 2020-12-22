try:
    import os
    import sys
    import time

    #system imports

    from  Shell import *
except ImportError as e:
    print("Error importing, " + str(e))


def main():
    print("""
  _____          ____    _____ 
 |  __ \        / __ \  / ____|
 | |__) |_   _ | |  | || (___  
 |  ___/| | | || |  | | \___ \ 
 | |    | |_| || |__| | ____) |
 |_|     \__, | \____/ |_____/ 
          __/ |                
         |___/                 
    """)
    shell()


if __name__ == "__main__":
    main()