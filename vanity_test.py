def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if any(s[char].isnumeric() and s[char+1].isalpha() for char in range(len(s)-1)):
        return False
    else:
        return True
        
            
                
        
main()