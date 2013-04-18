class PermutationError(Exception):
    pass
class InvalidPermutator(PermutationError):
    pass
class TooShortListToPermutate(PermutationError):
    pass
          
class PermutationCycle:
    def __init__(self, obj):
        if(self.check_lst_is_permutator(obj)):
            self.permutator = obj
        else:
            raise InvalidPermutator
    
    def check_lst_is_permutator(self, lst):
        i = 0
        if not isinstance(lst, (list)):
            raise InvalidPermutator
        for el in lst:
            if el <= 0:
                return False
        if len(set(lst)) == len(lst):
            return True
            
    def permutate(self, lst):
        p = self.permutator
        
        if len(lst) < max(p):
            raise TooShortListToPermutate
        for n in range(len(p)):
            old_pos = p[0] - 1
            new_pos = p[n] - 1
            lst[old_pos], lst[new_pos] = lst[new_pos], lst[old_pos]
        return lst
        
    def __len__(self):
        return len(self.permutator)
        
class Permutation:
    def __init__(self, *args):
        self.compos_list = []            
        for cycle in args:
            perm = PermutationCycle(cycle)
            self.compos_list.append(perm)
        
    def permutate(self, lst):
        for cycle in self.compos_list:
            lst = cycle.permutate(lst)
        return lst
    
    def __mul__(self, perm):
        perm_cycle_list = [cycle.permutator for cycle in perm.compos_list]
        self_cycle_list = [cycle.permutator for cycle in self.compos_list]
        
        complete_compos_list = perm_cycle_list + self_cycle_list

        compos = Permutation(*complete_compos_list)
        return compos
        
    def __len__(self):
        return sum([len(i) for i in self.compos_list] )
    