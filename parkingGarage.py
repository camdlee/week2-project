# Parking Garage Code

#---------Needs to do the following:---------

#----------Enter/take ticket function----------
# Take a ticket when someone enters the garage ---> when someone enters they will need to provide name and car to take a spot
# When ticket is taken, the number of tickets available goes down by 1
# When ticket is take, the number of parking spots should go down by 1
# Needs variable for # of tickets and # of spots -- arbitrary?

#----------Leave/pay for ticket function----------
# When leaving, you should pay for parking so we need to have a $ associated with spot
# Display an input that waits for an amount from the user and store it in a variable
# So this could mean that, it asks the user how many hours the user has been parked in the garage to calculate rate/cost of ticket

#if the payment variable is not empty (ticket has been paid), display message to user that their ticket has been paid and they have 15 mins to leave
# using a if, then statement to print message or will ask again to pay if false
# if true, current_ticket dictionary key "paid" to True

# Loop payment: 
# if paid, then it will display "Thank you, have a nice day"
# if not paid, will prompt user for payment 
# This will update the number of parking spots and # of tickets up by 1 

# Will need a few attributes as well:
# tickets need to be a list
# parking spaces - list
# current_ticket - dictionary meaning it will have a key, value pair, could be "Name, Car"





# class Parking_garage():
#     def __init__(self, name, car) -> None:
#         self.name = name
#         self.car = car

#         # define some class attributes
#         self.number_of_spots = 20
#         self.tickets = []
#         self.parking_spaces = []
#         self.current_ticket = {}


# #---------Function to take ticket--------
#     def take_ticket(self):
#         take_spot = input("Will you need a spot? (Y/N)").lower()
#         if take_spot == 'y':
#             print(f'{self.name} here is your ticket')
            
#             number_of_spots -= 1


# #---------Function to Pay for Parking--------
#     def pay_parking(self):


# #----------Function to Leave Garage---------
#     def leave_garage(self):
