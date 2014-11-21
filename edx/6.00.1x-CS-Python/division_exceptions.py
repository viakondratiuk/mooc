def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Division on 0 is not allowed'
    except:
        raise ValueError('Call with bad arguments')
    finally:
        print 'We are finally here.', type(x)
    
try:
    print divide(1, 2)
    print divide(4, 2)
    print divide(1, 0)
    print divide('10', '2')
    print divide('10')
except ValueError, e:
    print e