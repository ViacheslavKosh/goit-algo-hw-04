def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise ValueError("Contact")
    contacts[name] = phone
    return "Contact updated successfully"

def show_contact(args, contacts):
    name = args[0]
    return contacts[name]


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))
            # print(contacts)

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_contact(args, contacts))
        
        elif command == "all":
            print(f'All contacts: {contacts}')
        else:
            print("Invalid command.")
            # print(contacts)


if __name__ == "__main__":
    main()