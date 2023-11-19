from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console

#Define empty dictionary
bids = {}

#Define my funtion to find out who the highest bidder is.
def calc_highest_bidder(bid_dictionary):
  high_bidder_name = ""
  highest_bid = 0

  for bidders in bid_dictionary:
    if bid_dictionary[bidders] > highest_bid:
      high_bidder_name = bidders
      highest_bid = bid_dictionary[bidders]
  print(f"The winner is {high_bidder_name} with a bid of ${highest_bid}.")

#Print Logo for the initial start of the program
print(logo)

#Create while loop to run for as long as bidders are available
bidders_Available = 'True'
while bidders_Available == 'True':
  bidder_name = input('What is your name?: ')
  bid_amount = int(input("What is your bid?: $"))
  bids[bidder_name] = bid_amount
  more_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n")

#If more bidders are available, clear screen.
  if more_bidders == "yes":
    clear()
#No more bidders, then find out who was the highest bidder and declare them the winner.
  elif more_bidders == "no":
    bidders_Available = "False"
    calc_highest_bidder(bids)
 
  