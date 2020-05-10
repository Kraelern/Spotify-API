import csv
loginDict = {"Spotipy":"testpword"}
print("Create a local Account\n")#do in tkinter
username = str(input("Please enter your preferred username.\n"))#use tkinter
passcode = str(input("Thank you, now enter a password as well.\n"))#tkinter
loginDict[username] = passcode
#print(loginDict)    
#create a new csv with a unique name
def csvCreator():
    with open(f"{username}File.csv", 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Recommended Songs','Recommended Artists','Recommended Genres'])


#if loginDict.get(username) == passcode:
    # Correct username and password match
#    pass
#else:
    # Incorrect username/password match
#    print("Inavlid Credentials. Try Again.")
    
