import requests, time, sys, os, base64, json
from icecream import ic
from multiprocessing.pool import ThreadPool
logo = (""" \033[1;92m____  _   _ _                     _
|  _ \| | | | |__   ___  _ __ ___ | |__   ___ _ __
| |_) | |_| | '_ \ / _ \| '_ ` _ \| '_ \ / _ \ '__|
|  __/|  _  | |_) | (_) | | | | | | |_) |  __/ |
|_|   |_| |_|_.__/ \___/|_| |_| |_|_.__/ \___|_|
 by aknown version 0.3""")
if sys.platform == "linux" or sys.platform == "linux2":
    clr = "clear"
elif sys.platform == "win32" or sys.platform == "cygwin" or sys.platform == "msys":
    clr = "cls"
session = requests.Session()
if sys.version_info[0] != 3:
    os.system('clear')
    print(logo)
    print(65 * '\033[1;92m=')
    print('''\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 fb.py\n''')
    print(65 * '\033[1;92m═')
    sys.exit()
line = ("\033[1;92m╔═"+57*"\033[1;92m═")     
line2 = ("\033[1;92m║"+58*"\033[1;92m═")
LIMIT = 0
LIMIT1 = 0
ERROR = 0
SLEEP = 0
RUN = True
TARGET = ''
debug = False
debugError = False
try:
     from function import to09, to639, toplus63, pick
except ImportError:
     print("Need to update before starts...")
     sys.exit(1)

def bomb_process(api):
     pass

# mainporcesore
def bomber(jsonApi):
    global LIMIT, RUN, LIMIT1, ERROR, SLEEP
    while bool(RUN) == True:
        if bomb_process(api=jsonApi):
            sys.stdout.write(u"\033[1000D\033[1;92mSuccess: \033[1;97m{} \033[1;92mError: \033[1;91m{} \033[1;92m".format(
                str(LIMIT), str(ERROR)))
            sys.stdout.flush()

            if int(LIMIT) >= int(LIMIT1):
                RUN = False
        else:
            sys.stdout.write(u"\033[1000D\033[1;92mSuccess: \033[1;97m{} \033[1;92mError: \033[1;91m{} \033[1;92m".format(
                str(LIMIT), str(ERROR)))
            sys.stdout.flush()
        time.sleep(int(SLEEP))
# home


def home():
    global LIMIT1, SLEEP, TARGET
    os.system(clr)
    print(logo)
    print(line)
    print("\033[1;92m║ \033[1;94m—> \033[1;92mInput Target Number ex.09222222222")
    TARGET = pick()
    print("\033[1;92m║ \033[1;94m—> \033[1;92mLIMIT")
    LIMIT1 = pick()
    print("\033[1;92m║ \033[1;94m—> \033[1;92mSleep")
    SLEEP = pick()
    res = requests.get('')
    api = json.loads(res.text)
    
    p = ThreadPool(int(len(api['ph'])))
    # run the multiprocess
    p.map(bomber, [])
    # if bomber is finish its going here
    print("\r\r"+line)
    print("Done.")


# if run main it going to home
if __name__ == "__main__":
    home()