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
    print("\n\n\n\n")
    choice = input("v(iew) contact, a(dd), contact, r(emove) contact>>> ")
    if choice == "v":
        contact_selection = input("Enter the number of the contact you wish to view>>> ")
        print(view_contact(int(contact_selection)))
    if choice == "a":
        add_contact()
        display()

def get_contact_names():
    name_list = []
    with open(JSON_FILE) as json_file:
        data = json.load(json_file)
        names = []
        for contact in data.get("contacts"):
            names.append(contact["name"])

        return names

def list_contacts():
    counter = 1
    for name in get_contact_names():
        print(str(counter) + ". " + name)
        counter += 1

def view_contact(contact_choice):
    with open(JSON_FILE) as json_file:
        data = json.load(json_file)
        contact = data["contacts"][contact_choice]
        name = contact["name"]
        phone = contact["phone"]
        return f"Contact Name:  {name} \nContact Phone: {phone}"

def add_contact():
    name = input("Enter the name of the new contact>>> ")
    phone = input("Enter the phone number of the new contact>>> ")
    new_contact = {"name": name, "phone": phone}
    with open(JSON_FILE, 'r+') as json_file:
        data = json.load(json_file)
        print(data)
        data["contacts"].append(new_contact)
        print(data)
        json_file.seek(0)
        json.dump(data, json_file, indent=4)




if __name__ == "__main__":
    main()