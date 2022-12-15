import itertools

class ArgF:
    def __init__(self):
        self.args = []
        self.attacks = []

    def add_args(self, a):
        self.args.append(a)

    def add_attacks(self, a, b):
        self.attacks.append([a, b])

    def print_argf(self):
        print("Arguments : ", end = ' ')
        print(self.args)
        print("Attacks : ", end = ' ')
        print(self.attacks)

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

    def is_weak(self, e):
        for a, b in self.attacks:
            if(a == e):
                return False
        return True
    
    def is_well(self, e):
        for a, b in self.attacks:
            if(a == e):
                return False
            if(b == e):
                return False
        return True

    def is_cf(self, list):
        for a, b in self.attacks:
            if(a in list and b in list):
                return True
        return False
    
    def get_valide(self):
        valide = list(self.args)
        for a, b in self.attacks:
            if(b in valide):
                valide.remove(b)
        return valide
    
    def defense(self, ori = []):
        valide = list(ori)
        if(valide == []):
            valide = self.get_valide()
        invalide = []
        for e in valide:
            for a, b in self.attacks:
                if(a == e):
                    if(b not in invalide):
                        invalide.append(b)
                        if(b in valide):
                            valide.remove(b)
                        for c, d in self.attacks:
                            if(c == b):
                                if(d not in valide and d not in invalide):
                                    valide.append(d)
        if(valide == ori and len(ori) == 1 and self.is_well(ori[0])):
            return valide
        if(valide == ori and len(ori) == 1 and self.is_weak(ori[0])):
            return []
        return valide

    def grounded(self):
        res = []
        res.append(self.defense())
        return res

    def completed(self):
        res = []
        permutations = list(self.args)
        for i in range(2, len(self.args)+1):
            permutations += list(itertools.combinations(self.args, i))
        for i in range(len(permutations)):
            tmp = list(permutations[i])
            if(self.is_cf(tmp) == False):
                tmp_def = self.defense(tmp)
                tmp_valide = self.get_valide()
                if(all(elem in tmp_def for elem in tmp_valide)):
                    if(tmp_def == tmp):
                        res.append(tmp_def)
        if(self.get_valide() == []):
            res.append([])
        return res

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