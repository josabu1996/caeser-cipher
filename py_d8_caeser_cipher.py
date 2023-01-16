print('''
 /$$$$$$
 /$$__  $$
| $$  \__/ /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$
| $$      |____  $$ /$$__  $$ /$$_____/ /$$__  $$ /$$__  $$
| $$       /$$$$$$$| $$$$$$$$|  $$$$$$ | $$$$$$$$| $$  \__/
| $$    $$/$$__  $$| $$_____/ \____  $$| $$_____/| $$
|  $$$$$$/  $$$$$$$|  $$$$$$$ /$$$$$$$/|  $$$$$$$| $$
 \______/ \_______/ \_______/|_______/  \_______/|__/



  /$$$$$$  /$$                     /$$
 /$$__  $$|__/                    | $$
| $$  \__/ /$$  /$$$$$$   /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$
| $$      | $$ |____  $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$      | $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$    $$| $$ /$$__  $$| $$  | $$| $$  | $$| $$_____/| $$
|  $$$$$$/| $$|  $$$$$$$| $$$$$$$/| $$  | $$|  $$$$$$$| $$
 \______/ |__/ \_______/| $$____/ |__/  |__/ \_______/|__/
                        | $$
                        | $$
                        |__/
''')

#a:97 - z:122
status = True
en_msg2lst=[]
de_msg2lst=[]
encoded_msg=[]
decoded_msg=[]

#Encode
def encode(msg, shift):
    for letter in msg:
        en_msg2lst.append(letter)

    for letter in range(len(en_msg2lst)):
        if (ord(en_msg2lst[letter]) + shift) > 122:
            encoded_msg.append(chr(((ord(en_msg2lst[letter]) + shift) - 122) + 96))
        else:
            encoded_msg.append(chr(ord(en_msg2lst[letter]) + shift))

    print(''.join(encoded_msg))

#Decode
def decode(msg, shift):
    for letter in msg:
        de_msg2lst.append(letter)

    for letter in range(len(de_msg2lst)):
        if (ord(de_msg2lst[letter]) - shift) < 97:
            decoded_msg.append(chr(122-(shift-(ord(de_msg2lst[letter])-96))))
        else:
            decoded_msg.append(chr(ord(de_msg2lst[letter]) - shift))

    print(''.join(decoded_msg))

#Main Body
while status == True:

    option = input("Type 'encode' to encrypt, type 'decode' to decrypt.\n").lower()

    if option == 'encode':
        message = input("Type your message: ").lower()
        shift_check = True
        while shift_check == True:
            shift = int(input("Type the shift number(between 1 to 26): "))
            if shift > 26:
                print("Shift greater than 26. Please enter again.")
            elif shift >= 1 and shift <= 26:
                shift_check = False
        encode(msg = message, shift = shift)
    elif option == 'decode':
        message = input("Type your message: ").lower()
        shift_check = True
        while shift_check == True:
            shift = int(input("Type the shift number(between 1 to 26): "))
            if shift > 26:
                print("Shift greater than 26. Please enter again.")
            elif shift > 1 and shift < 26:
                shift_check = False
        decode(msg=message, shift=shift)

    #Exit Game
    exit_game = input("Type 'yes' if you wish to exit. Press any other key to continue.\n").lower()
    if exit_game == 'yes':
        status = False
    else:
        encoded_msg.clear()
        decoded_msg.clear()
        en_msg2lst.clear()
        de_msg2lst.clear()