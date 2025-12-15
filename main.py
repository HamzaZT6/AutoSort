import os 
import time 
import shutil
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def render_ui():
    global console
    console = Console()
    main_panel = Panel(
        "[bold]Do You Want To AutoSort Your Donlowdes Folder ? ([green]y[/green]/[red]n[/red]):[/bold]",
        title="AutoSort",
        border_style="yellow"
    )

    console.print(main_panel)

def split_files():
    files = os.listdir("Downloads")

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
    with Progress() as progress:
        task = progress.add_task("Moving files", total=len(files))
        # Images
        for f in files:
            name, ext = os.path.splitext(f)
            if ext in all_ext[0]:
                shutil.move(f"Downloads/{f}", f"Downloads/Images/{f}")
                progress.update(task, advance=1)
        print("[+] - Images Moved")

        # Videos
        for f in files:
            name, ext = os.path.splitext(f)
            if ext in all_ext[1]:
                shutil.move(f"Downloads/{f}", f"Downloads/Videos/{f}")
                progress.update(task, advance=1)
        print("[+] - Videos Moved")

        # Music
        for f in files:
            name, ext = os.path.splitext(f)
            if ext in all_ext[2]:
                shutil.move(f"Downloads/{f}", f"Downloads/Music/{f}")
                progress.update(task, advance=1)
        print("[+] - Musics Moved")

        # Documents
        for f in files:
            name, ext = os.path.splitext(f)
            if ext in all_ext[3]:
                shutil.move(f"Downloads/{f}", f"Downloads/Documents/{f}")
                progress.update(task, advance=1)
        print("[+] - Documents Moved")
        
def create_folders():   
    with Progress() as progress:
        task = progress.add_task("Creating Folders", total=4)
        if not os.path.exists("Downloads/Images"):
            os.makedirs("Downloads/Images")
            print("[+] - Images Folder Created")
            progress.update(task, advance=1)
            time.sleep(0.5)
        if not os.path.exists("Downloads/Videos"):
            os.makedirs("Downloads/Videos")
            print("[+] - Videos Folder Created")
            progress.update(task, advance=1)
            time.sleep(0.5)
        if not os.path.exists("Downloads/Music"):
            os.makedirs("Downloads/Music")
            print("[+] - Music Folder Created")
            progress.update(task, advance=1)
            time.sleep(0.5)
        if not os.path.exists("Downloads/Documents"):
            os.makedirs("Downloads/Documents")
            print("[+] - Documents Folder Created")
            progress.update(task, advance=1)
            time.sleep(0.5)

def main():
    while True:
        clear_screen()
        render_ui()
        choice = input("[Input]: > ").lower()
        
        if choice == "y" or choice == "yes":
            create_folders()
            split_files()
        elif choice == "n" or choice == "no":
            print("[Tool]: Bye, Have A Good Day")
        else:
            print(f"[Tool]: For Real Bro ?, Try (Yes OR No)")

main()
