# Takes room status and returns the action
def room_cleaner_bot(status):
    if status == "Dirty":    # If the room is dirty…
        return "Clean"       # …then clean it
    else:                    # Otherwise…
        return "Do Nothing"  # …do nothing

# Test the function
#print(room_cleaner_bot("Dirty"))       # Output: Clean
#print(room_cleaner_bot("Clean"))       # Output: Do Nothing
