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

def print_bol(b):
    if(b == True):
        print("YES")
    else:
        print("NO")


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

    print("\"-h\" : pour afficher ce message d'aide")
    
    # print("\"-esperance\" : pour afficher l'espérance de T")
    # print("\"-mesureX\" : pour afficher la mesure invariante de la loi X_n (*)")
    # print("\"-mesureY\" : pour afficher la mesure invariante de la loi Y_n (**)")

    # print("\"-h\" pour afficher ce message d'aide\n")

    # print("(*) et (**) sont deux lois qui sont expliquées dans le README.md.")


def good_code(code, arg, af):
    gr = af.grounded()
    co = af.completed()
    pr = af.preferred(co)
    st = af.stable(pr)
    tmp = True

    match code:
        case "SE-GR":
            print_ans(gr)
            return
        case "SE-CO":
            print_ans(co)
            return
        case "SE-PR":
            print_ans(pr)
            return
        case "SE-ST":
            print_ans(st)
            return
        case "SE-ALL":
            print("Grounted : ", end = '')
            print_ans(gr)
            print("Completed : ", end = '')
            print_ans(co)
            print("Preferred : ", end = '')
            print_ans(pr)
            print("Stable : ", end = '')
            print_ans(st)
            return
        case "DS-CO":
            if(co == [[]]):
                print("NO")
            elif(co == []):
                print("NO")
            else:
                for i in range(len(co)):
                    if(arg in co[i]):
                        tmp = False
                print_bol(tmp)
            return
        case "DC-CO":
            if(co == [[]]):
                print("NO")
            elif(co == []):
                print("NO")
            else:
                tmp = False
                for i in range(len(co)):
                    if(arg in co[i]):
                        tmp = True
                print_bol(tmp)
            return
        case "DS-ST":
            if(st == [[]]):
                print("NO")
            elif(st == []):
                print("NO")
            else:
                for i in range(len(st)):
                    if(arg not in st[i]):
                        tmp = False
                print_bol(tmp)
            return
        case "DC-ST":
            if(st == [[]]):
                print("NO")
            elif(st == []):
                print("NO")
            else:
                tmp = False
                for i in range(len(st)):
                    if(arg in st[i]):
                        tmp = True
                print_bol(tmp)
            return
        case _ :
            print_help()
            return





##   MAIN   #######################################################################

def main(argv):
    if(len(argv) >= 1):
        code = ""
        filename = ""
        arg = ""

        for i in range(0, len(argv)):
            if(argv[i] == "-h"):
                print_help()
                return
            elif(argv[i] == "-p"):
                code = argv[i+1]
            elif(argv[i] == "-f"):
                filename = argv[i+1]
            elif(argv[i] == "-a"):
                arg = argv[i+1]
        
        if(code == "" or filename == ""):
            print_help()
            return
        else:
            data = read_file(filename)
            af = ArgF()
            if(af.add_from_list(data)):
                good_af = af.is_good() 
                if(good_af[0]):
                    good_code(code, arg, af)
                else:
                    print(good_af[1])
            else:
                print("Erreur : Mauvaise écriture du fichier")
            return
    else:
        print_help()
        return

    
    
if __name__ == "__main__":
   main(sys.argv[1:])