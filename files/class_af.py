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