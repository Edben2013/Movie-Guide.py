with open("movies.txt", "w") as file:
    file.write("Cat on a Hot Tin Roof\nOn the Waterfront\nMonty Python and the Holy Grail\n")

def populate_list(file_name):
    movie_list = []
    with open(file_name, "r") as file:
        for line in file:
            movie_list.append(line.strip())
    return movie_list

def display_menu():
    print("The Movie List Program\n")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()

def display_titles(movie_list):
    print("\nMovie Titles: ")
    for idx, title in enumerate(movie_list, start = 1):
        print(f"{idx}. {title}")

def add_title(movie_list, title, file_name):
    movie_list.append(title)
    with open(file_name, "a") as file:
        file.write(title + "\n")
    print(f"\n{title} was added. \n")

def delete_title(movie_list, index, file_name):
    if 1 <= index < len(movie_list):
        deleted_title = movie_list.pop(index - 1)
        with open(file.name, "w") as file:
            file.write("\n".join(movie_list))
        print(f"\n {deleted_title} was deleted.")
    else:
        print("Invalid movie number. \n")

def main():
    movie_file = "movies.txt"
    movie_list = populate_list(movie_file)

    while True:
        display_menu()
        command = input("COMMAND: ")

        if command == "list":
            display_titles(movie_list)
        elif command == "add":
            new_title = input("Enter New Movie Title: ")
            add_title(movie_list, new_title, movie_file)
            display_titles(movie_list)
        elif command == "delete":
            display_titles(movie_list)
            index = int(input("Enter number of movie title to delete: "))
            delete_title(movie_list, index, movie_file)
            display_titles(movie_list)
        elif command == "exit":
            print("Bye!")
            break
            
        else:
            print("Not a valid command. Please try agian.")

    if __name__ == "__main__":
        main()
        
