import sys
sys.path.append('./files/')

from class_af import *



## FONCTIONS UTILITAIRES  #########################################################

def read_file(filename):
    with open(filename) as f:
        contents = f.read()
        res = contents.split("\n")
        if(res[-1] == ""):
            return res[:-1]
        return res
    
def print_help():
    # print("Commandes de l'utilisateur")
    # print("DESCRIPTION   ")




    print("Commande sous la forme: \"COMMANDE -p [CODE] -f [NOM_FICHIER]\n")

    print("Informations sur les arguments :")
    print("\"-p\" : pour spécifier le code de la commande")
    print("\"-f\" : pour spécifier le nom du fichier")
    
    # print("\"-esperance\" : pour afficher l'espérance de T")
    # print("\"-mesureX\" : pour afficher la mesure invariante de la loi X_n (*)")
    # print("\"-mesureY\" : pour afficher la mesure invariante de la loi Y_n (**)")

    # print("\"-h\" pour afficher ce message d'aide\n")

    # print("(*) et (**) sont deux lois qui sont expliquées dans le README.md.")






##   MAIN   #######################################################################

def main(argv):
    if(len(argv) > 1):
        data = read_file(argv[-1])
        af = ArgF()
        if(af.add_from_list(data)):
            good_af = af.is_good() 
            if(good_af[0]):
                af.print_argf()
                print(af.grounded())
                print(af.completed())




            else:
                print(good_af[1])
                return
        else:
            print("Erreur : Mauvaise écriture du fichier")
            return
    else:
        print_help()
        return

    
    
if __name__ == "__main__":
   main(sys.argv[1:])