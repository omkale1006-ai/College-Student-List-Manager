names = [
    "Neha", "Aryan", "Chirag", "Meena", "Avni", "Irfan", "Bobby", "Jatin", "Esha", "Gaurav",
    "Kiran", "Aditya", "Deepak", "Brijesh", "Aisha", "Heena", "Aarav", "Dinesh", "Manav", "Chetan",
    "Divya", "Jaya", "Imran", "Nilesh", "Gita", "Charu", "Aarya", "Leena", "Lakshya", "Alok",
    "Harsh", "Kunal", "Nikita", "Abhay", "Ekta", "Dolly", "Dhruv", "Bhavya", "Chandan", "Bharat",
    "Isha", "Kavya", "Anaya", "Jyoti", "Amit", "Farhan", "Fatima", "Bina", "Himanshu", "Tarun"
]

# ✅ Print names starting with a specific letter
def names_starting_with_letter():
    print("\n🔍 Search Names Starting With:")
    letter = input("Enter the starting letter: ").upper()
    for index, name in enumerate(names, start=1):
        if name.startswith(letter):
            print(f"{index}. {name}")

# ✅ Add a name at the beginning
def add_name():
    name = input("Enter the name to add: ").title()
    names.append(name)
    print(f"✅ {name} has been added at the beginning of the list.")

# ✅ Print list length
def list_length():
    print(f"\n📏 Total number of students: {len(names)}")

# ✅ Sort the list alphabetically
def sort_names():
    names.sort()
    print("\n🔤 List has been sorted alphabetically.")

# ✅ Find index of a name
def find_name_index():
    user = input("Enter the name to find: ").title()
    if user in names:
        position = names.index(user) + 1
        print(f"✅ {user} is at position {position}.")
    else:
        print("❌ Name not found in the list.")

# ✅ Print full list with index
def full_list_print():
    print("\n📋 Full List of Students:")
    for index, name in enumerate(names, start=1):
        print(f"{index}. {name}")

# ✅ Main menu
def main():
    while True:
        print("\n🎓 Welcome to OM’s College Student Registry")
        print("1. Search names by first letter")
        print("2. Add a new name")
        print("3. Check total number of students")
        print("4. Find your name’s position in the list")
        print("5. Sort names alphabetically")
        print("6. Show full list of students")
        print("7. Exit the program")

        try:
            user = int(input("Enter your choice (1–7): "))

            if user == 1:
                names_starting_with_letter()
            elif user == 2:
                add_name()
            elif user == 3:
                list_length()
            elif user == 4:
                find_name_index()
            elif user == 5:
                sort_names()
            elif user == 6:
                full_list_print()
            elif user == 7:
                print("👋 Thank you for using the program. Goodbye!")
                break
            else:
                print("⚠️ Invalid option. Please choose between 1 and 7.")
        except ValueError as e:
            print("❌ Error:", e)

# Run the program
main()
