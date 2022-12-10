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
                return False
            if(a == "args" or a == "att"):
                return False
        for a, b in self.attacks:
            if(a not in self.args or b not in self.args):
                return False
        return True