import webbrowser
from sys import argv


def search(lookup):
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    if (lookup.endswith(".com")):
        webbrowser.get(chrome_path).open(lookup)
    else:
        webbrowser.get(chrome_path).open("https://www.google.com/search?q="+lookup)

def main():
    user_website = input("What do you want to search for?")
    search(user_website)
    
    


if __name__ == "__main__":
    main()

