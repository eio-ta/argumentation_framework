import sys
from class_af import *

import os
width = os.get_terminal_size().columns




## FONCTIONS UTILITAIRES  ##########################################################################


# Affiche correctement les sémantiques
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


# Affiche correctement les booléens
def print_bol(b):
    if(b == True):
        print("YES")
    else:
        print("NO")


# Vérifie si l'argument e est acceptée crédulement ou sceptiquement ou non
def contains_all(e, list, b, af):
    res = af.give_sem(list, b)
    if(e in res):
        return True
    else:
        return False


# Lis le contenu d'un fichier
def read_file(filename):
    with open(filename) as f:
        contents = f.read()
        res = contents.split("\n")
        if(res[-1] == ""):
            return res[:-1]
        return res


# Affiche le message d'aide
def print_help():
    print()
    print("Commandes de l'utilisateur".center(width))
    print()
    print()

    print("\033[1m" + "DESCRIPTION" + "\033[0m")

    print("On appelle \"Argumentation Framework\" (AF) un graphe <A,R> avec les arguments A et les attaques R. Le programme ci-présent donne les différentes extensions et sémantiques.")
    print()

    print("Cette version accepte les options qui doivent être précédées d'un tiret et doit être suivies par un argument.")
    print()
    print()

    print("\033[1m" + "EXEMPLE" + "\033[0m")
    print("Pour afficher le graphe complet du fichier \"test.txt\" :")
    print("\033[1m  python3 program.py -p SE-CO -f test.txt \033[0m")
    print()
    print("Pour voir si l'argument \"a\" est acceptée crédulement pour le graphe stable du fichier \"test.txt\" :")
    print("\033[1m  python3 program.py -p DC-CO -f test.txt -a a \033[0m")
    print()
    print()

    print("\033[1m" + "INTRODUCTION AUX OPTIONS POSSIBLES" + "\033[0m")
    print("\033[1m  a  \033[0m Cible un argument précis [un argument obligatoire]")
    print()
    print("\033[1m  f  \033[0m Cible un fichier précis décrivant un AR. [un argument obligatoire]")
    print()
    print("\033[1m  h  \033[0m Affiche ce message d'aide. [sans argument]")
    print()
    print("\033[1m  p  \033[0m Précise le code de l'action que veut l'utilisateur. [un argument obligatoire]")
    print()
    print("Les options \"p\" et \"f\" sont obligatoires.")
    print()
    print()

    print("\033[1m" + "LISTE DES CODES POSSIBLES" + "\033[0m")
    print("\033[1m  PR-AF  \033[0m Affiche le graphe.")
    print()
    print("\033[1m  SE-GR  \033[0m Donne la sémantique fondée.")
    print()
    print("\033[1m  SE-CO  \033[0m Donne la sémantique complète.")
    print()
    print("\033[1m  SE-PR  \033[0m Donne la sémantique préférée.")
    print()
    print("\033[1m  SE-ST  \033[0m Donne la sémantique stable.")
    print()
    print("\033[1m  SE-ALL  \033[0m Donne toutes les sémantiques.")
    print()
    print("\033[1m  DC-CO  \033[0m (Sans argument) Donne tous les arguments crédulement acceptés. (Avec un argument) Vérifie si l'argument est crédulement accepté. [Pour la sémantique complète].")
    print()
    print("\033[1m  DS-CO  \033[0m (Sans argument) Donne tous les arguments sceptiquement acceptés. (Avec un argument) Vérifie si l'argument est sceptiquement accepté. [Pour la sémantique complète].")
    print()
    print("\033[1m  DC-ST  \033[0m (Sans argument) Donne tous les arguments crédulement acceptés. (Avec un argument) Vérifie si l'argument est crédulement accepté. [Pour la sémantique stable].")
    print()
    print("\033[1m  DS-ST  \033[0m (Sans argument) Donne tous les arguments sceptiquement acceptés. (Avec un argument) Vérifie si l'argument est sceptiquement accepté. [Pour la sémantique stable].")
    print()


# Répond à la demande de l'utilisateur
def good_code(code, arg, af):
    gr = af.grounded()
    co = af.completed()
    pr = af.preferred(co)
    st = af.stable(pr)

    match code:
        case "PR-AF":
            af.print_argf()
            return
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
            if(arg != ""):
                print_bol(contains_all(arg, co, True, af))
            else:
                print_ans(af.give_sem(co, True))
            return
        case "DC-CO":
            if(arg != ""):
                print_bol(contains_all(arg, co, False, af))
            else:
                print_ans(af.give_sem(co, False))
            return
        case "DS-ST":
            if(arg != ""):
                print_bol(contains_all(arg, st, True, af))
            else:
                print_ans(af.give_sem(st, True))
            return
        case "DC-ST":
            if(arg != ""):
                print_bol(contains_all(arg, st, False, af))
            else:
                print_ans(af.give_sem(st, False))
            return
        case _ :
            print_help()
            return




##   MAIN   ########################################################################################

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