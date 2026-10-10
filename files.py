# Assignment 3: Daily Journal
# Create a program that:

# Asks the user to write a short journal entry about their day.
# Saves the entry in a file called journal.txt.
# Reads the file and displays the journal entry.


print("=== Daily Journal ===")
entry = input("Write about your day: ")

with open("journal.txt", "a") as file:
    file.write(entry + "\n")

print("\nEntry saved to journal.txt!")

print("\n--- Your Journal ---")
with open("journal.txt", "r") as file:
    print(file.read())