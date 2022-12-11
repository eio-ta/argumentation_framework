import sys
sys.path.append('./files/')

from algo import *
from class_af import *



## FONCTIONS UTILITAIRES  #########################################################

def read_file(filename):
    with open(filename) as f:
        contents = f.read()
        res = contents.split("\n")
        if(res[-1] == ""):
            return res[:-1]
        return res



##   MAIN   #######################################################################

def main(argv):
    if(len(argv) > 1):
        data = read_file(argv[-1])
        af = ArgF()
        if(af.add_from_list(data)):
            good_af = af.is_good() 
            if(good_af[0]):
                af.print_argf()
            else:
                print(good_af[1])
                return
        else:
            print("Erreur : Mauvaise écriture du fichier")
            return
            
    # TODO :
    # si len(argv == 1) --> option -h MESSAGE D'AIDE
    # si len(argv) == 0) --> pas d'option MESSAGE D'AIDE

    
    

if __name__ == "__main__":
   main(sys.argv[1:])