def coup_possible(lst, k, coup, rang):

    return not coup <= len(lst[rang]) and not coup < k

print(coup_possible([[1,2,3,4,5], [2,7,0,1], [3,1], []], 3, 2, 3))
        
    
        


