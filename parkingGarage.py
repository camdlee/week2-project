# Parking Garage Code

#---------Needs to do the following:---------

class Parking_garage():
    def __init__(self, capacity):
        self.capacity = capacity   
        self.tickets = []
        self.parkingSpaces = []
        self.currentTicket = {} 
        
# ------Take ticket function------

# Ask user which parking spot they want within capacity -- input("Pick a spot between 1-{capacity}")
    def takeTicket(self):
        print('----------TICKET MENU---------')
        # check to see if garage is at capacity
        if self.capacity == len(self.tickets):
            print('Sorry, this garage is at capacity')
        else:
            ticket_num = input(f'Pick a parking spot between 1-{self.capacity}: ')
        # check if number is within range
            if int(ticket_num) > self.capacity:
                print('Invalid number')
            else:
            # check if that spot is already taken in the list
                if ticket_num in self.tickets:
                    print(f'Sorry that spot is already taken. Choose another spot')
                else:
                    # then append dicitonary with the variable input and automatically assign that key with a value of False
                    self.tickets.append(ticket_num)
                    self.parkingSpaces.append(ticket_num)
                    self.currentTicket[ticket_num] = False
                    # then decrease parkingSpaces by 1
                    spots_left = (int(self.capacity)-len(self.parkingSpaces)) 
                    # print (there are x number of spots left)
                    print(f'There are {spots_left} number of parking spots left')
                    print(f'Here is your ticket for parking spot #{ticket_num}')


# -------- Pay for Parking function---------

# Ask the user for their ticket #
    def payforParking(self):
        print('----------PAYMENT MENU---------')
        ticket_num = input('What is your ticket number? ')
        #check to see if ticket number is in use/in the list
        if ticket_num in self.tickets:
            # if ticket num is in the list, tell them the cost and ask to enter amount
            while True:
                print(f'That will be $10')
                payment = input('Enter payment: ')
                # if payment input matches cost then change dictionary key-value
                if payment == '10':
                    self.currentTicket[ticket_num] = True
                    print('Your ticket has been paid, you have 15 minutes to leave. Thank you, have a nice day!')
                    # trigger leave parking garage function
                    self.leave_garage()
                    break
                # if payment input doesn't match, then tell them it is incorrect
                else: 
                    print(f'Incorrect amount. Please input the full amount')
        else:
            print('Invalid ticket number')


# -------- Leave garage function ---------

# Ask the user for their ticket number
    def leave_garage(self):
        print('----------EXIT MENU---------')
        ticket_num = input('What is your ticket number? ')
        # check to see if ticket number is in list
        if ticket_num in self.tickets:
        #check to see if ticket_num in dictionary is true
            if self.currentTicket[ticket_num] == True:
                # print have a nice day
                print('Thank you have a nice day')
                # remove number from parkingSpaces list and tickets list
                self.parkingSpaces.remove(ticket_num)
                self.tickets.remove(ticket_num)
                # recalculate # of spots left = capacity - new value of length of parkingSpaces list
                spots_left = (int(self.capacity)-len(self.parkingSpaces)) 
                print(f'There are now {spots_left} parking spot(s) left.')
            # if not true, then tell them to pay for parking and then trigger pay parking function
            else:
                print('Please pay parking ticket')
                self.payforParking()
        else:
            print('Invalid ticket number')


#---------RUNNER FUNCTION---------
    def runner(self):
        while True:
            choice = input("What do you want to do? (Park, Pay, Leave, or Quit) ").lower()
            if choice == "park" :
                self.takeTicket()
            elif choice == 'pay':
                self.payforParking()
            elif choice == "leave":
                self.leave_garage()
            elif choice == "quit":
                break
            else:
                print("Invalid choice!")



ten = Parking_garage(10)
ten.runner()

#twenty = Parking_garage(20)
#twenty.runner()


#--------PREVIOUS WORK--------

#----------Enter/take ticket function----------
# Take a ticket when someone enters the garage ---> when someone enters they will need to provide name and car to take a spot
# When ticket is taken, the number of tickets available goes down by 1
# When ticket is take, the number of parking spots should go down by 1
    # def takeTicket(self):
    #     ticket_1 = input("Will you need a parking spot (Y/N)").lower()

    #     self.num_spots_left = 10
    #     self.num_tickets_left = 10     
    #     if self.num_tickets_left <= 0:
    #         print(f'There are no more parking spots available')
    #     else:
    #         if ticket_1 == 'y':
    #             print(f'{self.name}, here is your ticket')
    #             self.num_spots_left -= 1
    #             self.num_tickets_left -= 1
    #             self.tickets.append(self.name)
    #             self.parkingSpaces.append(self.name)
    #             print(f'There are now {self.num_spots_left} spots left and {self.num_tickets_left} tickets left.')
    #         else:
    #             pass

# cameron = Parking_garage('Cameron')
# cameron.takeTicket()


#----------Leave/pay for ticket function----------
# When leaving, you should pay for parking so we need to have a $ associated with spot
# Display an input that waits for an amount from the user and store it in a variable
# So this could mean that, it asks the user how many hours the user has been parked in the garage to calculate rate/cost of ticket
    # def payForParking(self):
    #     #hours = int(input('How many hours were you parked?'))
    #     #print(f'Your ticket costs {hours * 10} dollars')
    #     while True:
    #         payment = input('Please pay ticket (Y/N)').lower()
    #         if payment == 'y':
    #             print(f'Thank you, have a nice day')
    #             self.num_spots_left += 1
    #             self.num_tickets_left += 1
    #             self.currentTicket['paid'] = True
    #             break
    #         else:
    #             print('Please pay ticket')
       

# if the payment variable is not empty (ticket has been paid), display message to user that their ticket has been paid and they have 15 mins to leave
# using a if, then statement to print message or will ask again to pay if false
# if true, current_ticket dictionary key "paid" becomes True

# Loop payment: 
# if paid, then it will display "Thank you, have a nice day"
# if not paid, will prompt user for payment 
# This will update the number of parking spots and # of tickets up by 1 

#----------Runner Function---------
#     def Runner(self):
#         while True:
#             choice = input("What do you want to do? (Park, Leave, or Quit)").lower()
#             if choice == "park" :
#                 self.takeTicket()
            
#             elif choice == "leave":
#                 self.payForParking()

#             elif choice == "quit":
#                 break

#             else:
#                 print("Invalid choice!")


# ten = Parking_garage(10)
# ten.takeTicket()

# ten.Runner()

