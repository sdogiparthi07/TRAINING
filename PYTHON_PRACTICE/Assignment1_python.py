#using for loop.
#1.ATM PIN Verification
#Your cousin works at a bank and is testing a simple ATM simulator. A user gets up to 3 attempts to enter the correct PIN. After each wrong attempt, the program should print how many tries are left. If they run out of attempts, the card gets locked.
#Given a correct_pin and a list entered_pins (the attempts in order), write a program that loops through the attempts (max 3), checks each one against correct_pin, and prints "Access Granted" if it matches, otherwise "Wrong PIN, X tries left". If all 3 attempts fail, print "Card Locked".

correct_pin = "0704"
entered_pins = ["1234", "0704", "5678"]
attempts = 3

for i in range(3):               #loop runs mx 3 times
    if entered_pins[i] == correct_pin:       #check if entered pin matches the correct pin 
        print("Access Granted")              #returns access granted if pin matches
        break                                #stops the loop if pin matches
    else:
        attempts = attempts-1                #reduce the attempts by 1 pin if matches
        if attempts > 0:                    #if attempts still left
            print("Wrong PIN", attempts," tries left,")  #show remaining tries
        else:
             print("Card Locked")       #no attempts left, card locked
###using while loop
correct_pin = "0704"
entered_pins = ["1234", "0704", "5678"]
attempts = 3

i = 0

while i < 3:
    if entered_pins[i] == correct_pin:
        print("Access Granted")
        break
    else:
        attempts = attempts - 1
        if attempts > 0:
            print("Wrong PIN", attempts, "tries left")
        else:
            print("Card Locked")

    i = i + 1

#2. Grocery Checkout Total
#Your mom asked you to build a quick checkout tool for her small shop. Items are entered one at a time and added to a running total. If the total crosses ₹1000 at any point, a 10% discount should automatically apply to the rest of the checkout.
#Given a list item_prices, write a program that loops through the prices, adding each to a running total. Once the total crosses ₹1000, apply a 10% discount to all further items added. Print the final total.

item_prices = [200, 300, 400, 500, 600]
total = 0
discount = False
for price in item_prices:
    if total > 1000:      # checks if total is greater than 1000
        discount = True
    if discount:
        total+= price * 0.9  # Apply 10% discount  #add the price with 10% discount
    else: 
        total+= price      #add the price without discount
print(total)

###while loop
item_prices = [200, 300, 400, 500, 600]
total = 0
discount = False

i = 0

while i < len(item_prices):
    price = item_prices[i]

    if total > 1000:
        discount = True

    if discount:
        total += price * 0.9  # Apply 10% discount
    else:
        total += price

    i = i + 1

print(total)
#3.Number Guessing Game
#Your little brother wants a guessing game where the computer picks a number and he keeps guessing until he gets it right. After each guess, the program should print "Too High", "Too Low", or "Correct".
#Given a secret_number and a list guesses (in the order they were made), write a program that loops through the guesses, printing "Too High" or "Too Low" for each using if-else, and stops as soon as it finds the correct guess, printing "Correct" along with how many guesses it took.
secret_number = 74
guesses = [50, 80, 70, 74]


for i in range(len(guesses)):   #loop through each guess
    if guesses[i] > secret_number:   #checks if guess is > secret number
        print("Too High")
    elif guesses[i] < secret_number:  #checks if guess is < secret number
        print("Too Low")
    else:
        print("Correct")
        print("Guesses taken:", i + 1)   #print the number of guesses taken 
        break

##while loop
secret_number = 74
guesses = [50, 80, 70, 74]

i = 0

while i < len(guesses):
    if guesses[i] > secret_number:
        print("Too High")
    elif guesses[i] < secret_number:
        print("Too Low")
    else:
        print("Correct")
        print("Guesses taken:", i + 1)
        break

    i = i + 1
#4. Movie Ticket Booking
#You're helping at a local cinema's booking counter. Tickets are sold one at a time until either all seats are sold or someone tries to book more seats than are available (in which case that request is rejected and booking stops).
#Given total_seats and a list booking_requests (seats requested per booking, in order), write a program that loops through the requests, reducing the available seats each time. If a request asks for more seats than are available, print "Not enough seats" and stop the loop. Print the number of seats remaining at the end.
total_seats = 80
booking_requests = [25, 30, 40, 15]

for seats in booking_requests:    
    if seats <= total_seats:             
        total_seats = total_seats - seats    #reduce the total seats by no. of seats boooked
    else:
        print("Not enough seats")
        break

print("Seats remaining:", total_seats)

##while loop
total_seats = 80
booking_requests = [25, 30, 40, 15]

i = 0

while i < len(booking_requests):
    seats = booking_requests[i]

    if seats <= total_seats:
        total_seats = total_seats - seats
    else:
        print("Not enough seats")
        break

    i = i + 1
print("Seats remaining:", total_seats)

#5.Study Streak Tracker
#You're building a habit tracker for your study group. Each day's quiz score is checked one at a time. The streak continues as long as the score is 60 or above; the moment a score drops below 60, the streak breaks and processing stops.
#Given a list scores (daily quiz scores in order), write a program that loops through the scores, using if-else to check each one: if it's 60 or above, increase the streak count; if it drops below 60, print "Streak broken" and stop the loop. Print the final streak length.
scores = [75, 80, 65, 90, 50, 70]
streak = 0

for score in scores:
    if score >= 60:
        streak = streak + 1        #increase the streak count if score is >= 60
    else: 
        print("Streak broken")
        break

print("Streak length:", streak)
##while loop
scores = [75, 80, 65, 90, 50, 70]
streak = 0
i = 0

while i < len(scores):
    score = scores[i]

    if score >= 60:
        streak = streak + 1
    else:
        print("Streak broken")
        break

    i = i + 1
print("Streak length:", streak)