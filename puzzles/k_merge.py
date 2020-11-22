import heapq as hq
    
def k_merge(*args):
    """
    Given an arbitrary number of sorted lists, build a merged sorted list.
    >>> k_merge()
    >>> k_merge([])
    []
    >>> k_merge([1], [1])
    [1, 1]
    >>> k_merge([1, 3], [5], [2, 4])
    [1, 2, 3, 4, 5]
    >>> k_merge([1, 1, 1], [3], [2, 2])
    [1, 1, 1, 2, 2, 3]
    >>> k_merge([1,4,5], [1,3,4], [2,6])
    [1, 1, 2, 3, 4, 4, 5, 6]
    >>> k_merge([1,4,5,8,11,25], [1,3,4,7,22], [2,6,10])
    [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 10, 11, 22, 25]
    """
    
    res = []
    
    if len(args) == 0:
        return 
    
    # create heap from first elements of subLists
    # we store sublists current value, sublist's index (depends on how many sublists in input), and element's index
    heap = [(sublist[0], sublist_index, 0) for sublist_index, sublist in enumerate(args) if sublist] 
    hq.heapify(heap)        
            
    while heap:
        val, list_index, el_index = hq.heappop(heap) # retrieve element from top of the heap
        res.append(val) # insert value to final result list
        if el_index + 1 < len(args[list_index]): #check if there is next element in current sublist
            next_tuple = (args[list_index][el_index + 1], list_index, el_index + 1) # form next_tuple (sublist) payload data
            hq.heappush(heap, next_tuple) #push next element to heap
    
    return res
    # indexes = [0, 0, 0]
    # min heap
    # traverse through sublists
    # append first el into heap use heappush
    # result list. Append root node of the heap
    # remove root el from the heap, rebuild the heap
    # add 
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()