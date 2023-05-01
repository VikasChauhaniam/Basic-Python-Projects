from art import logo
#from replit import clear
print(logo)

other_bidder = True

Bidder_data = {}
max_bidder_name =''
max_bidder_value=0


print("Welcome to the secret auction program.")
print("=======================================")

while other_bidder==True:
  
  name= input('What is your name? : ')
  bid = input('What is your bid? : $')

  if int(bid) > max_bidder_value:
    max_bidder_value = int(bid)
    max_bidder_name = name
    
  Bidder_data[name] = bid
  
  other = input("Are there any other bidders? Type 'yes' or 'no' : ")
  #clear()
  
  if other == 'no':
    other_bidder = False

print(f"The Winner is {max_bidder_name} with a bid of ${max_bidder_value}")





