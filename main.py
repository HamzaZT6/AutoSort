import os 
import time 
import rich



def create_folders():
    print("[Tool]: We Are Now On The First Step")
    print("[Tool]: I Will Create 4 Folders (Images, Videos, Musics, Documents) In Downlode Folder")
    choice = input("[Tool]: Can I Create Them? (y/n): ").lower()

    if choice == "y" or choice == "yes":
        pass
    elif choice == "n" or choice == "no":
        pass
    else:
        print("[Tool]: Try With (yes or no)")
    

def main():
    print("[Tool]: Welcome, Im Here To Organiez Your Files")
    choice = input("[Tool]: Do You Want Me To Organiez Your Donlowdes Folder ? (y/n): ").lower()
    
    if choice == "y" or choice == "yes":
        print("[Tool]: Cool")
    elif choice == "n" or choice == "no":
        print("[Tool]: What a wierdo")
    else:
        print(f"[Tool]: For Real Bro ? You had One Job, Try (Yes OR No)")
