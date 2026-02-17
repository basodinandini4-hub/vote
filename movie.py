# Simple Movie Ticket Booking System

print("🎬 Welcome to Movie Ticket Booking")

movie_name = input("Enter movie name: ")
ticket_price = 10  # price per ticket
tickets = int(input("Enter number of tickets: "))

total_cost = ticket_price * tickets

print("\nBooking Details")
print("-----------------------")
print("Movie Name :", movie_name)
print("Number of Tickets :", tickets)
print("Price per Ticket : $", ticket_price)
print("Total Cost : $", total_cost)
print("\n✅ Booking Confirmed! Enjoy your movie 🎉")
