def monotonic_array(lst):
    """
    This function returns True/False if the given list is monotonically increased or decreased
    """
    inc = 0
    dec = 0
    for i in range(len(lst)-1):
        if lst[i+1] < lst[i]:
            inc += 1
        elif lst[i+1] >= lst[i]:
    return True




print(monotonic_array([1, 2, 3, 6, 8, 9, 0]))  # False
print(monotonic_array([1, 2, 2, 2, 8, 9, 10]))  # True
