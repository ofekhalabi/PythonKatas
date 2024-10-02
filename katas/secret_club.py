def secret_club(keys, values):
    """
    Constructs a dictionary to map club members to their secret codes.
    - keys: A list of club member names.
    - values: A list of secret codes.
    """
    dict_keys_value = dict(zip(keys,values))
    return dict_keys_value
"""    dict_keys_value = {}
    for i in range(len(keys)):
        dict_keys_value[keys[i]] = values[i]
    return dict_keys_value
    """




# Example usage
members = ["Alice", "Bob", "Charlie"]
codes = ["X123", "Y456", "Z789"]

club_dict = secret_club(members, codes)
print(club_dict)  # {'Alice': 'X123', 'Bob': 'Y456', 'Charlie': 'Z789'}

"""
To complete this exercise:
--------------------------
Built a dict based on two list. 
Before start, you must ensure that both members and codes lists are the same length. 


Exercise Breakdown:
-------------------
Constructing a dictionary from two lists involves using the names from one list as keys and 
values from another list on the same length. 

There is a function to do it: zip(). But try to do it manually using loops and dictionary operation.
Since the zip() function returns an iterator, you can convert it into a dictionary using the `dict()` constructor.
"""
