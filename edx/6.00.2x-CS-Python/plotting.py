import pylab

def first_figure():
    pylab.figure(1)
    pylab.plot([1,2,3,4], [1,7,3,5])
    pylab.show()

def second_figure():
    pylab.figure(1)
    pylab.plot([1,2,3,4],[1,2,3,4])
    pylab.figure(2)
    pylab.plot([1,4,2,3],[5,6,7,8])
    pylab.show()
    #pylab.savefig('figure_2')
    pylab.figure(1)
    pylab.plot([5,6,10,3])
    pylab.show()
    #pylab.savefig('figure_1')    

def compound_interest():
    calculated = 1000
    interestRate = 0.05
    years = 20
    values = []
    for y in xrange(years + 1):
        values.append(calculated)
        calculated += calculated * interestRate
    pylab.plot(range(years + 1), values, 'ro')
    pylab.title('5% Growth, Compounded Anually')
    pylab.xlabel('Years of Compounding')
    pylab.ylabel('Value of Principal ($)')
    pylab.show()
                
#first_figure()
#second_figure()
compound_interest()