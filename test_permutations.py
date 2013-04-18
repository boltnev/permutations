#!/usr/bin/python
from permutations import *

def test_check_lst_is_permutator():
    a = PermutationCycle([])
    
    assert a.check_lst_is_permutator([1])
    assert a.check_lst_is_permutator([1, 2, 3])
    assert not a.check_lst_is_permutator([1, -1, -4 ])
    assert not a.check_lst_is_permutator([1, -1, -4 ])
    assert not a.check_lst_is_permutator([0, 3 ,4])
    
    try:
        a.check_lst_is_permutator(123) 
    except(InvalidPermutator):
        assert True
    
    try:
        a = PermutationCycle([1, "not_int", 2]) 
    except(InvalidPermutator):
        assert True
    
    a = Permutation(*[[1, 3, 2], [2, 3, 1]])
    
def test_permutate():
    a = Permutation([1, 3, 2])
    assert a.permutate([1, 2, 3 ]) == [2, 3, 1]
    assert a.permutate([1, 2, 3, 4 ]) == [2, 3, 1, 4]
    assert a.permutate(["John", "Bob", "Sarah" ]) == [ "Bob", "Sarah", "John"]
        
    b = Permutation([1, 4, 2, 3])
    
    try:
        b.permutate(["John", "Bob", "Sarah" ]) 
    except(TooShortListToPermutate):
        assert True
    
    assert b.permutate([5, 6, 7, 8]) == [7, 8, 6, 5]
    
    c = Permutation([2, 3])
    assert c.permutate([1, 2, 3]) == [1, 3, 2]
    
    d = Permutation([1, 2], [3, 4])

    assert d.permutate([1, 2, 3, 4]) == [2, 1, 4, 3]
    
    
def test_length():
    a = Permutation([1, 3, 2])
    assert len(a) == 3
    
    a = Permutation([1, 3, 2, 5, 4])
    assert len(a) == 5
    
    a = Permutation([5, 6])
    assert len(a) == 2
    
    a = Permutation([5, 6], [7, 8])
    
    assert len(a) == 4
    
def test_mul():
    a = Permutation([1, 3, 2])
    b = Permutation([2, 3, 1])
    c = b * a
    
    assert c.permutate([1, 2, 3 ]) == [1, 2, 3]
    
    a = Permutation([1, 2]) *  Permutation([3, 4]) 
    
    assert a.permutate([1, 2, 3, 4]) == [2, 1, 4, 3] 
    

test_check_lst_is_permutator()
print "OK"
test_permutate()
print "OK"
test_length()
print "OK"
test_mul()
print "ALL OK"