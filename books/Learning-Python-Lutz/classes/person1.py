# Use Delegation insted of inheritance

class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)
        
class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)
    def giveRaise(self, percent, bonus = 0.1):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    def __str__(self):
        return str(self.person)
        
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 10000)
    print bob
    print sue
    print bob.lastName(), sue.lastName()
    sue.giveRaise(.1)
    print sue.pay
    print sue
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.1)
    print tom.lastName()
    print tom
    print '--All three--'
    for object in (bob, sue, tom):
        object.giveRaise(0.1)
        print object
    