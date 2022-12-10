import sys
sys.path.append('./files/')

from utils import *
from algo import *
from class_af import *



##   MAIN   #######################################################################

# Fonction MAIN
def main(argv):
    for i in range(0, len(argv)):
        print(argv[i])

if __name__ == "__main__":
   main(sys.argv[1:])