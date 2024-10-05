def add_acronyms():
    acronym = input("What is the acronym that you would like to add?\n")
    meaning = input("What does the acronym stand for?\n")

    word_list = meaning.split()
    meaning = " ".join([word.capitalize() for word in word_list])
    
    try:
        with open("acronyms.txt", "a") as file:
            file.write(acronym.upper() + " - " + meaning + "\n")
    except FileNotFoundError:
        print("File not found. Please create the file acronyms.txt before running this program.")
    except:
        print("An error occurred. Please try again.")
    print("Acronym added successfully.")

def find_acronym():
    acronym = input("What is the acronym that you would like to find?\n")
    
    found = False
    try:
        with open("acronyms.txt", "r") as file:
            for line in file:
                if acronym.upper() in line:
                    print(line)
                    found = True
                    break    
    except FileNotFoundError:
        print("File not found. Please create the file acronyms.txt before running this program.")
        return
    except:
        print("An error occurred. Please try again.")
        return
    if not found:
            print("Acronym not found.")


def main():
    while True:
        choice = input("Do you want to add an acronym or find an acronym? Type 'add' or 'find'. Type 'exit' to quit.\n")
        if choice == "add":
            add_acronyms()
        elif choice == "find":
            find_acronym()
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()