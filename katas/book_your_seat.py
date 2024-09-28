from operator import index
index_start_Bus = 0
index_start_first = 10
index_start_Economy = 20

def add_passenger(seats, seat_class, passenger_name):
    """
    Adds a passenger to the first available seat in the correct section.
    First 10 seats are for 'Business' Class.
    Next 10 seats are for 'First' Class.
    The remaining seats are for 'Economy' Class.
    """
    global index_start_Bus
    global index_start_first
    global index_start_Economy
    index_end_Bus = 10
    index_end_first = 20

    if seat_class == "Business":
        if index_start_Bus < index_end_Bus:
            if seats[index_start_Bus] is None:
                seats[index_start_Bus] = passenger_name
                index_start_Bus += 1

    if seat_class == "First":
        if index_start_first < index_end_first:
            if seats[index_start_first] is None:
                seats[index_start_first] = passenger_name
                index_start_first += 1






aircraft_seats = [None] * 100   # creates list of None of length 100

add_passenger(aircraft_seats, "Business", "Alice")
add_passenger(aircraft_seats, "Business", "Eve")
add_passenger(aircraft_seats, "Business", "Alice")
add_passenger(aircraft_seats, "Business", "Eve")
add_passenger(aircraft_seats, "Business", "Alice")
add_passenger(aircraft_seats, "Business", "Eve")
add_passenger(aircraft_seats, "Business", "Alice")
add_passenger(aircraft_seats, "Business", "Eve")
add_passenger(aircraft_seats, "Business", "Alice")
add_passenger(aircraft_seats, "Business", "Eve")
add_passenger(aircraft_seats, "Business", "Alice")
add_passenger(aircraft_seats, "Business", "Eve")
add_passenger(aircraft_seats, "First", "Bob")

print(aircraft_seats[:15])  # Expected output: ['Alice', 'Eve', None, None, None, None, None, None, None, None, 'Bob', None, None, None, None]

"""
To complete this exercise:
--------------------------
The aircraft seating is divided into Business Class (first 10 seats), First Class (next 10 seats), 
and Economy Class (remaining seats).
We use the `None` value to represent empty seats.


Exercise Breakdown:
-------------------
To find the first available seat, use the `is None` to check if the seat is free.
"""
