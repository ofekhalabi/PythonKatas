def start_end(text, n, m):
    if ( n or m ) < 0 or (n or m ) > len(text):
        return ""
    else:
        return text[:n] + text[-m:]


text = 'Elvis has left the building'
result = start_end(text, 3, 5)
print(result)  # Expected output: 'Elvlding'

result = start_end(text, 7, 2)
print(result)  # Expected output: 'Elvis hng'

result = start_end(text, 5, 4)
print(result)  # Expected output: 'Elvisding'

result = start_end('Pythonista', 4, 3)
print(result)  # Expected output: 'Pythsta'

result = start_end(text, 100, 1)  # Invalid input (too large)
print(result)  # Expected output: ''

"""
To complete this exercise:
--------------------------
No any implementation notes. 
"""
