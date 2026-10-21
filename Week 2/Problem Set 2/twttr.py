message = input("Input : ")

def is_consonent(character):
    character = character.lower()
    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
        return False

    
for c in message:
    if is_consonent(c):
        print(c, end = "")