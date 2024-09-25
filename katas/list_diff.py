def list_diff(numbers):
    new_list = [numbers[0]]
    for i in range(1,len(numbers)):
        new_list.append(numbers[i] - numbers[i-1])

    return new_list



numbers = [10, 20, 15, 25, 30]
result = list_diff(numbers)
print(result)  # Expected output: [10, 10, -5, 10, 5]


numbers = [5, 3, 8, 2]
result = list_diff(numbers)
print(result)  # Expected output: [5, -2, 5, -6]


"""
To complete this exercise:
--------------------------
Create a new list where each element at index `i` is calculated as:

`numbers[i] - numbers[i-1]`
 
for all `i` from 1 to the end of the list.

Leave the first element unchanged in the result list.


Exercise Breakdown:
-------------------
A common technique for iterating over indices of a list is:

for i in range(len(list))

This allows you to access both the element and its predecessor when performing calculations.

"""