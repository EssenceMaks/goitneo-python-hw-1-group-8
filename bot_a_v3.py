def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name.lower()] = (name, phone)
        return "Contact added."
    else:
        return "Invalid arguments for add command."

# def change_contact(args, contacts):
#     if len(args) == 2:
#         name, phone = args
#         name_lower = name.lower()
#         if name_lower in contacts:
#             contacts[name_lower] = (name, phone)
#             return "Contact updated."
#         else:
#             return "Contact not found."
#     else:
#         return "Invalid arguments for change command." 
    

def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name.lower() in contacts:
            contacts[name.lower()] = (name, phone)
            return "Contact updated."
        else:
            return "Contact not found."
    elif len(args) == 1:
        return "Invalid arguments for change command. Please provide both name and phone number.\nFor example, use: change Eddy 333777"
    else:
        return "Invalid arguments for change command."
    
def delete_contact(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name.lower() in contacts:
            del contacts[name.lower()]
            return "Contact deleted."
        else:
            return "Contact not found."
    else:
        return "Invalid arguments for delete command. Please provide the name of the contact to delete."


def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0].lower()
        if name in contacts:
            return contacts[name][1]
        else:
            return "Contact not found."
    else:
        return "Invalid arguments for phone command."

def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, (name, phone) in contacts.items()])
    else:
        return "No contacts available."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["good bye","close", "exit", "q", "quit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "delete":
            print(delete_contact(args, contacts))
        else:
            print("Unknown command. Available commands are: \n hello, add, change, phone, all, delete, close, exit")

            print()  # Print available commands
            print("Available commands:")
             
            print("hello                      -- to get assistance") 
            print("add NAME PHONE             -- to add a contact") 
            print("change NAME PHONE          -- to change a contact's phone number") 
            print("phone NAME                 -- to get a contact's phone number") 
            print("delete NAME                -- to delete a contact") 
            print("all                        -- to show all contacts") 
            print("q/good bye/close/exit/quit -- to exit the assistant")
            print()
            print()

if __name__ == "__main__":
    main()