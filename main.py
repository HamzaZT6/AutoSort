import os 
import time 
import rich

def split_files():
    files = os.listdir("Donwloads")

    all_ext = [
        # Images
        [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".ico"],

        # Videos
        [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm", ".mpeg", ".mpg"],

        # Music / Audio
        [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma"],

        # Documents
        [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv", ".md", ".rtf"]
    ]

    for file in files:
        name, ext = os.path.splitext(file)

        if ext in all_ext:
            print(file)
    


def create_folders():
    print("[Tool]: We Are Now On The First Step")
    print("[Tool]: I Will Create 4 Folders (Images, Videos, Musics, Documents) In Downlode Folder")
    choice = input("[Tool]: Can I Create Them? (y/n): ").lower()

    if choice == "y" or choice == "yes":
        if not os.path.exists("Downloads/Images"):
            os.makedirs("Downloads/Images")
            print("[+] - Images Folder Created")
        if not os.path.exists("Downloads/Videos"):
            os.makedirs("Downloads/Videos")
            print("[+] - Videos Folder Created")
        if not os.path.exists("Downloads/Music"):
            os.makedirs("Downloads/Music")
            print("[+] - Music Folder Created")
        if not os.path.exists("Downloads/Documents"):
            os.makedirs("Downloads/Documents")
            print("[+] - Documents Folder Created")

    elif choice == "n" or choice == "no":
        print("[Tool]: Why Even You Opend Me ???")
    else:
        print("[Tool]: ... Try With (yes or no)")
    

def main():
    print("[Tool]: Welcome, Im Here To Organiez Your Files")
    choice = input("[Tool]: Do You Want Me To Organiez Your Donlowdes Folder ? (y/n): ").lower()
    
    if choice == "y" or choice == "yes":
        create_folders()
        split_files()
    elif choice == "n" or choice == "no":
        print("[Tool]: What a wierdo")
    else:
        print(f"[Tool]: For Real Bro ? You had One Job, Try (Yes OR No)")

main()
