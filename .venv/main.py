import json, os

JSON_FILE = "data/contacts.json"

def main():
    display()

def clear_console():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display():
    clear_console()
    print("*" * 50)
    print("Welcome to your contact manager!")
    print("See your contacts below.")
    list_contacts()

def get_contact_names():
    name_list = []
    with open(JSON_FILE) as json_file:
        data = json.load(json_file)
        names = []
        for contact in data.get("contacts"):
            names.append(contact["name"])

        return names

def list_contacts():
    for name in get_contact_names():
        print(name)


if __name__ == "__main__":
    main()