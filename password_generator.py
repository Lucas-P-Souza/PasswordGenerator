#imports of libraries that will be used    
import random

#defining the variables that will be used
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', 
                      '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '/', '?']

def generate_password(length, choice):
    
    password = []
    
    #verifying if the length is less than 1
    if length < 1:
        return "Password length must be at least 1."
    
    #verifying the choice of the user and defining the characters that will be used
    if choice == 1:
        all_characters = lowercase + uppercase
        password.append(random.choice(lowercase))
        password.append(random.choice(uppercase))
    elif choice == 2:
        all_characters = digits
        password.append(random.choice(digits))
    elif choice == 3:
        all_characters = lowercase + uppercase + digits
        password.append(random.choice(lowercase))
        password.append(random.choice(uppercase))
        password.append(random.choice(digits))
    elif choice == 4:
        all_characters = lowercase + uppercase + digits + special_characters
        password.append(random.choice(lowercase))
        password.append(random.choice(uppercase))
        password.append(random.choice(digits))
        password.append(random.choice(special_characters))
    else:
        return "Invalid option."

    #adding additional random characters to the password
    if length > len(password):
        password.extend(random.choices(all_characters, k=length-len(password)))
    
    #shuffling the password to make it more random
    random.shuffle(password)

    #returning the password as a string
    return ''.join(password)
        
#defining the function that will show the menu
def menu():
    print("Password Generator")
    print("You would like to create a password with:")
    print("1. Only letters?")
    print("2. Only numbers?")
    print("3. Letters and numbers?")
    print("4. Letters, numbers and special characters?")  
    print("5. Sair")
    return input("Choose an option: ")

#defining the main function
def main():
    while True:
        option = menu()

        #verifying the option that the user chose and calling the function that will generate the password 
        # with the chosen option and length
        if option in ['1', '2', '3', '4']:
            length = int(input("Enter the password length: "))
            print(generate_password(length, int(option)))
        #verifying if the user wants to exit the program
        elif option == '5':
            break
        else:
            print("Invalid option")

if __name__ == '__main__':
    main()
