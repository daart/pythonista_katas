def main(coins, amount):
    """
    See https://leetcode.com/problems/coin-change/
    You are given coins of different denominations and a total amount of money. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
    >>> main([], 0)
    0
    >>> main([1], 5)
    5
    >>> main([1, 2], 5)
    3
    >>> main([1, 2, 5], 11)
    3
    >>> main([1, 2, 5], 13)
    4
    >>> main([2], 3)
    -1
    >>> main([5], 3)
    -1
    """
    # get max denomination (Counter sort will fit here)
    # check if max is less then amount
    # if max is less then amount, divide amount into max denomination value to know the min number of coins required
    # if module division(%) done and nothing's left (0) return the division result 10 // 2
    # if smth's left after % division add previse division result to final result 11 % 5 = 1, final_res += 11 // 5 => 2
    # subtract (max * amount // max) from amount => 11 - (5 * 2) = 1
    
    sorted_denominations = sorted(coins)
    max_value = max(coins)
    final_res = 0
    
    if max_value > amount:
        if len(coins) == 1:
            return -1
        
        sorted_denominations.pop()
        main (sorted_denominations, amount)
    else:
        min_qty_of_biggest_nominee = amount // max_value
        leftover = amount % max_value
        final_res += min_qty_of_biggest_nominee
        
        if leftover != 0:
            sorted_denominations.pop()
            new_amount = amount - (max_value * min_qty_of_biggest_nominee)
            
            final_res += main(sorted_denominations, new_amount)
        else:
            return final_res
    
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()