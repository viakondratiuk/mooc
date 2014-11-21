import sets

def test_issubstr(test_set, expected_result):        
    for k, s in enumerate(test_set):
        if sets.isSubstr(s[0], s[1]) == expected_result[k]:
            print '+ Test for "{}", "{}" is equal to "{}". Test passed.'.format(s[0], s[1], expected_result[k])
        else:
            print '- Test for "{}", "{}" isn\'t equal to "{}". Test failed.'.format(s[0], s[1], expected_result[k])
            
def test_union(test_set, expected_result):        
    for k, s in enumerate(test_set):
        if sets.union(s[0], s[1]) == expected_result[k]:
            print '+ Test for "{}", "{}" is equal to "{}". Test passed.'.format(s[0], s[1], expected_result[k])
        else:
            print '- Test for "{}", "{}" isn\'t equal to "{}". Test failed.'.format(s[0], s[1], expected_result[k])

def test_intersect(test_set, expected_result):        
    for k, s in enumerate(test_set):
        if sets.intersect(s[0], s[1]) == expected_result[k]:
            print '+ Test for "{}", "{}" is equal to "{}". Test passed.'.format(s[0], s[1], expected_result[k])
        else:
            print '- Test for "{}", "{}" isn\'t equal to "{}". Test failed.'.format(s[0], s[1], expected_result[k])    
    
def test_difference(test_set, expected_result):    
    for k, s in enumerate(test_set):
        if sets.difference(s[0], s[1]) == expected_result[k]:
            print '+ Test for "{}", "{}" is equal to "{}". Test passed.'.format(s[0], s[1], expected_result[k])
        else:
            print '- Test for "{}", "{}" isn\'t equal to "{}". Test failed.'.format(s[0], s[1], expected_result[k])    

test_set = (
    ('', ''),
    ('1', ''),
    ('', '2'),
    ('1', '2'),
    ('12', '34'),
    ('23', '1234'),
    ('', '1234'),
    ('123', '1234'),
    ('234', '1234'),
    ('24', '1234'),
    ('1234', '1234'),
    ('123456', '1234')    
)
expected_result = (
    (True),
    (False),
    (False),
    (False),
    (False),
    (True),
    (False),
    (True),
    (True),
    (False),
    (True),
    (False)
)
print '----------------------'
print 'Test of isSubstr operation:'
print '----------------------'
test_issubstr(test_set, expected_result)
print '----------------------'
test_set = (
    ('', ''),
    ('1', ''),
    ('', '2'),
    ('1', '2'),
    ('12', '34'),
    ('123456', '67890'),
    ('123456', '123456'),        
    ('123456', '1234567'),
    ('123456', '123456789')        
)
expected_result = (
    (''),
    ('1'),
    ('2'),
    ('12'),
    ('1234'),
    ('1234567890'),
    ('123456'),
    ('1234567'),
    ('123456789')
)
print '----------------------'
print 'Test of union operation:'
print '----------------------'
test_union(test_set, expected_result)
print '----------------------'
expected_result = (
    (''),
    (''),
    (''),
    (''),
    (''),
    ('6'),
    ('123456'),
    ('123456'),
    ('123456')
)
print 'Test of intersect operation:'
print '----------------------'
test_intersect(test_set, expected_result)
print '----------------------'
expected_result = (
    (''),
    ('1'),
    (''),
    ('1'),
    ('12'),
    ('12345'),
    (''),
    (''),
    ('')        
)
print 'Test of difference operation:'
print '----------------------'
test_difference(test_set, expected_result)
print '----------------------'