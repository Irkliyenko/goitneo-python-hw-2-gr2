# Function to parse user input into a command and its arguments
def parse_input(user_input):
    # Split the user input into command and arguments
    cmd, *args = user_input.split()
    # Remove leading and trailing spaces from the command, and convert it to lowercase for consistency
    cmd = cmd.strip().lower()
    return cmd, *args


# Decorator that handles possible errors during execution of add_contact function
def add_contact_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid input. Enter name and numeric phone number."
        except IndexError:
            return "Invalid number of arguments. Please try again."
    return inner


# Decorator that handles possible errors during execution of change_phone function
def change_phone_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact was not found. Ensure that you enter the right name and try again."
        except ValueError:
            return "Invalid number of arguments. Enter contact name and phone number."
    return inner


# Decorator that handles possible errors during execution of show_phone function
def show_phone_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact was not found. Ensure that you enter the right name."
        except IndexError:
            return "Invalid number of arguments. Enter contact name and phone number."
    return inner


# Decorator that handles possible errors during execution of show_all function
def show_all_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "The list of contacts is empty! Add the contact first."
    return inner


# adds name and number to the dict contats
@add_contact_error
def add_contact(args, contacts):
    name, phone = args
    if name == "username" or not phone.isnumeric():
        raise ValueError
    else:
        contacts[name] = str(phone)
        return "Contact added."


# overwrites existed phone number to the new one if user approves that, If contact is not on the
# the list, it raises the error
@change_phone_error
def change_phone(args, contacts):
    name, new_phone = args
    if name in contacts:
        user_input = str(input(
            "Existing contact will be overwrite. If you want to continue enter 'Yes', if not enter 'No' >>> "))
        if user_input.lower() == "yes":
            contacts[name] = str(new_phone)
            return "Contact changed."
        else:
            return "Contact not changed."
    else:
        raise KeyError


# show the phone number for a specific user name. It will inform user if pnone number is not found
@show_phone_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError


# shows all numbers in the list. It will inform user if the contact list is empty
@show_all_error
def show_all(contacts):
    if len(contacts) >= 1:
        phone_numbers = contacts.values()
        contact_list_str = ("\n".join(phone_numbers))
        return contact_list_str
    else:
        raise ValueError


# Main function that handles user interaction with the assistant bot
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    # Start an infinite loop to continuously prompt the user for commands
    while True:
        # Prompt the user to enter a command and parse the input
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello" or command == "hi":
            print("How can I help you?")
        # Add a new contact to the list
        elif command == "add":
            print(add_contact(args, contacts))
        # Change the phone number of an existing contact
        elif command == "change":
            print(change_phone(args, contacts))
        # Show the phone number of a specific contact
        elif command == "phone":
            print(show_phone(args, contacts))
        # Show all phone numbers in the list of contacts
        elif command == "all":
            print(show_all(contacts))
        # Handle invalid commands
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
