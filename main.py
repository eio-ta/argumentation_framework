import sys
from class_af import *



## FONCTIONS UTILITAIRES  #########################################################

def print_ans(list):
    if(list == [[]]):
        print("[]")
    elif(list == []):
        print("NO")
    else:
        str = ""
        for i in range(len(list)):
            str += "["
            if(len(list[i]) != 0):
                for j in range(len(list[i])-1):
                    str += list[i][j] + ","
                str += list[i][len(list[i])-1]
            str += "]"
            if((i+1) < len(list)):
                str += " "    
        print(str)


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
                grounded = af.grounded()
                completed = af.completed()
                preferred = af.preferred(completed)
                stable = af.stable(preferred)

                print_ans(grounded)
                print_ans(completed)
                print_ans(preferred)
                print_ans(stable)




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