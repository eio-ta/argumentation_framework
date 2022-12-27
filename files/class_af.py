import itertools



##  Définition de la classe AF  ####################################################################


# Classe AF "Argumentation Framework"
class ArgF:

    # Construteur de l'objet
    def __init__(self):
        self.args = []
        self.attacks = []


    # Ajoute un argument
    def add_args(self, a):
        self.args.append(a)


    # Ajoute une attaque entre deux arguments
    def add_attacks(self, a, b):
        self.attacks.append([a, b])


    # Affiche les attributs de l'objet
    def print_argf(self):
        print("Arguments : ", end = ' ')
        print(self.args)
        print("Attacks : ", end = ' ')
        print(self.attacks)


    # Retourne True si l'objet est correctement construit
    # Retourne False et son message d'erreur sinon
    def is_good(self):
        for a in self.args:
            if(self.args.count(a) != 1):
                return False, "Erreur : argument en double"
            if(a == "args" or a == "att"):
                return False, "Erreur : mauvais nom d'argument"
        for a, b in self.attacks:
            if(a not in self.args or b not in self.args):
                return False, "Erreur : argument non dans la liste"
        return True, ""


    # Ajoute à l'objet ses attributs en fonction d'une liste
    def add_from_list(self, data):
        for d in data:
            if(d[len(d)-1] != '.'):
                return False
            else:
                if(d[0:4] == "arg(" and d[-2:] == ")."):
                    self.add_args(d[4:-2])
                elif(d[0:4] == "att(" and d[-2:] == ")."):
                    name = d[4:-2].split(',')
                    self.add_attacks(name[0], name[1])
                else:
                    return False
        return True


    # Retourne True si l'argument e n'attaque personne dans une liste
    # Retourne False sinon
    def is_weak(self, e, list):
        for a, b in list:
            if(a == e):
                return False
        return True
    

    # Retourne True si l'argument e n'est pas attaqué dans une liste
    # Retourne False sinon
    def is_well(self, e, list):
        for a, b in list:
            if(b == e):
                return False
        return True


    # Retourne True si la liste d'arguments est conflict-free
    # Retourne False sinon
    def is_cf(self, list):
        for a, b in self.attacks:
            if(a in list and b in list):
                return True
        return False
    

    # Retourne tous les arguments non attaqués
    def get_valide(self):
        valide = list(self.args)
        for e in self.args:
            if(not self.is_well(e, self.attacks)):
                valide.remove(e)
        return valide
    

    # Retourne tous les arguments non attaqués et ceux défendus par la liste ori
    def defense(self, ori = []):
        valide = []
        if(valide == []):
            valide = self.get_valide()
        invalide = []

        tmp_attack = list(self.attacks)

        for e in ori :
            for a, b in self.attacks:
                if(a == e):
                    # on regarde les attaques des méchants
                    for c, d in self.attacks:
                        if(c == b):
                            # Suppression des attaques invalides
                            if([c, d] in tmp_attack):
                                tmp_attack.remove([c, d])
                    if(b not in invalide):
                        invalide.append(b)

        for e in self.args:
            if(self.is_well(e, tmp_attack)):
                if(e not in valide):
                    valide.append(e)

        for a, b in tmp_attack:
            if(a not in valide) :
                se_fait_attaquer = False
                for c, d in tmp_attack:
                    if(d == a):
                        se_fait_attaquer = True
                        if(d not in invalide):
                            invalide.append(d)
                if(se_fait_attaquer == False):
                    if(a not in valide):
                        valide.append(a)

        if(valide == ori and len(ori) == 1 and self.is_weak(ori[0], self.attacks) and self.is_well(ori[0], self.attacks)):
            return [], invalide
        
        if(valide == ori and len(ori) == 1 and self.is_well(ori[0], self.attacks)):
            return valide, invalide
        return valide, invalide
    

    # Retourne tous les arguments non attaqués et ceux défendus par la liste ori de manière récursive
    def defense_recursive(self, ori = []):
        valide = list(ori)
        tmp_def, tmp_att = self.defense(ori)
        tmp_rep = []
        while(valide != tmp_def):
            if(self.is_cf(tmp_def)):
                return None
            else:
                if(tmp_def not in tmp_rep):
                    tmp_rep.append(tmp_def)
                    valide = tmp_def
                    tmp_def, tmp_att = self.defense(valide)
                else:
                    #boucle infini
                    return None

        
        for e in self.args:
            if(e not in valide and e not in tmp_att):
                for e in self.args:
                    if(e not in valide and e not in tmp_att):
                        for a, b in self.attacks:
                            if(a == e and b in valide):
                                return None
                return valide
        return valide


    # Retourne la sémantique fondée
    def grounded(self):
        res = []
        valide = self.defense_recursive()
        res.append(valide)
        if(res == [None]):
            res = []
            res.append(self.get_valide())
        for a in res:
            a.sort()
        return res


    # Retourne la sémantique complète
    def completed(self):
        res = []
        permutations = list(self.args)
        for i in range(2, len(self.args)+1):
            permutations += list(itertools.combinations(self.args, i))
        for i in range(len(permutations)):
            tmp = list(permutations[i])
            if(self.is_cf(tmp) == False):
                tmp_def = self.defense_recursive(tmp)
                # print(tmp, tmp_def)
                tmp_valide = self.get_valide()
                if(tmp_def != None):
                    if(all(elem in tmp_def for elem in tmp_valide)):
                        if(tmp_def == tmp):
                            res.append(tmp_def)

        gr = self.grounded()
        if(len(gr) == 1 and gr[0] not in res):
            res += gr

        return res


    # Retourne la sémantique préférée
    def preferred(self, completed):
        if(len(completed) == 1):
            return completed
        else:
            res = []
            for i in range(len(completed)):
                tmp = True
                for j in range(len(completed)):
                    if(all(elem in completed[j] for elem in completed[i]) == False):
                        tmp = False
                if(tmp == False):
                    res.append(completed[i])
            return res


    # Retourne la sémantique stable
    def stable(self, preferred):
        res = []
        for i in range(len(preferred)):
            attacked = []
            for a, b in self.attacks:
                if(a in preferred[i]):
                    if(b not in attacked):
                        attacked.append(b)
            tmp = True
            for a in self.args:
                if(not (a in preferred[i] or a in attacked)):
                    tmp = False
            if(tmp):
                res.append(preferred[i])
        return res


    # Si b = True, retourne les arguments acceptés sceptiquement
    # Sinon retourne les arguments acceptés crédulement
    def give_sem(self, list, b):
        res = []
        if(list == [[]]):
            return []
        elif(list == []):
            return []
        else:
            for e in self.args:
                tmp = b
                for i in range(len(list)):
                    if(b == False):
                        if(e in list[i]):
                            tmp = True
                    else:
                        if(e not in list[i]):
                            tmp = False
                if(tmp):
                    res.append(e)
            return res