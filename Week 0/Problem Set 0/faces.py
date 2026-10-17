def convert(message):
    message = message.replace(":))", "hi")
    message = message.replace(":((", "bye")
    return message

def main():
    message = input("Enter your message : ")
    print(convert(message))

main()
