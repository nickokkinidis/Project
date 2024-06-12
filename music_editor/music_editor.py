# imports
import os

def main():
    # ask the user for the folder path there is music in
    welcome_user()
    folder_path = get_folder_path()

    # create a new folder in the folder path
    new_folder_name = input("Enter the name of the new folder where the edited music will be saved: ")
    if new_folder_name == "":
        new_folder_name = "edited_music"

    new_folder_path = create_new_folder(folder_path, new_folder_name)

    # copy the fist song to the new folder


    # confirm the user for the song's title 


    # go to bgmdb and get the info


    # confirm with the user


    # replace the info in the song


    # save the song


    # go to the next song



def welcome_user():
    print("Welcome to the Music Editor!")
    print("This program will help you edit your music.")
    user_input = input("Do you want to continue? (y/n) ")
    if user_input.lower() == "y":
        return True
    elif user_input.lower() == "n":
        exit()
    else:
        print("Invalid input. Please try again.")
        return welcome_user()

def get_folder_path():
    while True:
        folder_path = input("Enter the path to the folder containing your music: ")
        if os.path.exists(folder_path):
            return folder_path
        else:
            print("Invalid path. Please try again.")

def create_new_folder(next_to_folder_path, new_folder_name):
    parent_directory = os.path.dirname(next_to_folder_path)
    new_folder_path = os.path.join(parent_directory, new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)
    return new_folder_path

if __name__ == "__main__":
    main()