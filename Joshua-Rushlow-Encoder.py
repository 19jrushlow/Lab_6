# Joshua Rushlow


def encode(password):
    password = list(password)
    encoded_password = ''
    for i in range(len(password)):
        password[i] = str(int(password[i]) + 3)[-1]
        encoded_password += password[i]
    return encoded_password


def decode(password):
    pass


# main code
print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
while True:
    choice = int(input('Please enter an option: '))
    if choice == 1:
        encoded_pw = encode(input('Please enter your password to encode: '))
        print('Your password has been encoded and stored!')
    elif choice == 2:
        print('The encoded password is ' + encoded_pw + ', and the original password is ' + decode(encoded_pw) + '.')
    elif choice == 3:
        exit()