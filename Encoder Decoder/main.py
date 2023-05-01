import art

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(art.logo)

def encode(message_name, shift_number):
    output = ""
    for letter in message_name:
        indx = int(alphabet.index(letter)) + int(shift_number)
        if indx >= 26:
            indx = indx - 26
        output += alphabet[indx]
    print(f'encoded text is : {output}.\n')
    print('===============================')


def decode(message_name, shift_number):
    output = ""
    for letter in message_name:
        indx = int(alphabet.index(letter)) - int(shift_number)
        if indx < 0:
            indx = indx + 26
        output += alphabet[indx]
    print(f'Decoded text is : {output}.\n')
    print('===============================')
  
should_continue = True

while should_continue:
  operation_name = input("Type 'encode' to encrypt, Type 'decode' to decrypt :")
  message_name = input('Type your message :').lower()
  shift_number = input('Type the shift number in range 0 to 25 :')
  output = ""
  
  if operation_name == 'encode':
      encode(message_name, shift_number)
  
  elif operation_name == 'decode':
      decode(message_name, shift_number)
  else:
      print("Wrong input")

  result = input("Type 'yes' if you want to go again. Otherwise ype 'no'.\n")
  if result == 'no':
    should_continue = False
    print('Good bye')