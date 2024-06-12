import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import shutil


def main():
    # Ask the user for the folder path where the music is stored
    welcome_user()
    folder_path = get_folder_path()

    # Create a new folder
    new_folder_name = input("Enter the name of the new folder where the edited music will be saved: ")
    if new_folder_name == "":
        new_folder_name = "edited_music"

    new_folder_path = create_new_folder(folder_path, new_folder_name)

    # Edit the music
    process_mp3_files(folder_path, new_folder_path)


def welcome_user():
    print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
    print("Welcome to the Music Editor!")
    print("This program will help you edit your music's info.")
    print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
    check_to_continue()


def check_to_continue():
    while True:
        user_input = input("Do you want to continue? (y/n) ")
        if user_input.lower() == "y":
            return True
        elif user_input.lower() == "n":
            exit()
        else:
            print("Invalid input. Please try again.")


def get_folder_path():
    while True:
        folder_path = input("Enter the path to the folder containing your music: ")
        if os.path.exists(folder_path):
            return folder_path
        else:
            print("Invalid path. Please try again.")


def create_new_folder(folder_path, new_folder_name):
    parent_directory = os.path.dirname(folder_path)
    new_folder_path = os.path.join(parent_directory, new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)
    return new_folder_path


def process_mp3_files(folder_path, new_folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            source_path = os.path.join(folder_path, filename)
            audio = MP3(source_path, ID3=EasyID3)

            print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
            print(f"Processing: {filename}")
            print(f"Title: {audio.get('title', ['Unknown'])[0]}")
            print(f"Composer: {audio.get('composer', ['Unknown'])[0]}")
            print(f"Artist: {audio.get('artist', ['Unknown'])[0]}")
            print(f"Album: {audio.get('album', ['Unknown'])[0]}")
            print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
            
            audio['title'] = input("Enter new title: ")
            audio['composer'] = input("Enter new composer: ")
            audio['artist'] = input("Enter new artist: ")
            audio['album'] = input("Enter new album: ")

            # Rename the destination file based on the new title
            new_filename = audio['album'][0] + ' - ' + audio['title'][0] + '.mp3'
            destination_path = os.path.join(new_folder_path, new_filename)

            # Copy the original file to the new folder
            shutil.copy2(source_path, destination_path)
            
            # Save the edited tags to the copied file
            audio.save(destination_path)
            print(f"Saved modified file to: {destination_path}\n")

            check_to_continue()


if __name__ == "__main__":
    main()
