def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if 2 <= s <= 6:
        for c in s[0 : 2]:
            if c.isdigit():
                return False
        for c in s:
            if c.isnumeric():
                None
            else:
                return False
        for c in s:
            char = 0
            if c.isdigit():
                if c == "0":
                    return False
                else:
                    char += 1
                    continue
            else:
                if char != 0:
                    return False
        return True
       
    else:
        return False


main()