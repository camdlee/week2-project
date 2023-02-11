# Parking Garage Code

#---------Needs to do the following:---------

class Parking_garage():
    def __init__(self, name):
        self.name = name
        self.num_spots_left = 10
        self.num_tickets_left = 10        
        self.tickets = list(range(1,self.num_tickets_left))
        self.parkingSpaces = list(range(1,self.num_spots_left))
        self.currentTicket = {}
        
# cameron = Parking_garage('Cameron')
# charlie = Parking_garage('Charlie')

#----------Enter/take ticket function----------
# Take a ticket when someone enters the garage ---> when someone enters they will need to provide name and car to take a spot
# When ticket is taken, the number of tickets available goes down by 1
# When ticket is take, the number of parking spots should go down by 1
    def takeTicket(self):
        ticket_1 = input("Will you need a parking spot (Y/N)").lower()
        if self.num_tickets_left <= 0:
            print(f'There are no more parking spots available')
        else:
            if ticket_1 == 'y':
                print('Here is your ticket')
                self.num_spots_left -= 1
                self.num_tickets_left -= 1
                print(f'There are now {self.num_spots_left} spots left and {self.num_tickets_left} tickets left.')
            else:
                pass

# cameron = Parking_garage('Cameron')
# cameron.takeTicket()


#----------Leave/pay for ticket function----------
# When leaving, you should pay for parking so we need to have a $ associated with spot
# Display an input that waits for an amount from the user and store it in a variable
# So this could mean that, it asks the user how many hours the user has been parked in the garage to calculate rate/cost of ticket
    def payForParking(self):
        hours = int(input('How long were you parked?'))
        print(f'Your ticket costs {hours * 10} dollars')
        while True:
            payment = input('Please pay ticket (Y/N)').lower()
            if payment == 'y':
                print(f'Thank you, have a nice day')
                self.num_spots_left += 1
                self.num_tickets_left += 1
                break
            else:
                print('Please pay ticket')
       

# if the payment variable is not empty (ticket has been paid), display message to user that their ticket has been paid and they have 15 mins to leave
# using a if, then statement to print message or will ask again to pay if false
# if true, current_ticket dictionary key "paid" becomes True

# Loop payment: 
# if paid, then it will display "Thank you, have a nice day"
# if not paid, will prompt user for payment 
# This will update the number of parking spots and # of tickets up by 1 

#----------Runner Function---------
    def Runner(self):
        while True:
            choice = input("Will you need a parking spot or will you leave the parking spot: (1. Park), (2. Leave), (3. Quit): ")
            if choice == "1":
                self.takeTicket()
            
            elif choice == "2":
                self.payForParking()

            elif choice == "3":
                break

            else:
                print("Invalid choice!")

cameron = Parking_garage('Cameron')
cameron.Runner()


# Will need a few attributes as well:
# tickets need to be a list
# parking spaces - list
# current_ticket - dictionary meaning it will have a key, value pair



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
