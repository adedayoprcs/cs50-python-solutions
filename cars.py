class Capitalize:

    def __init__(self, uppercase, lowercase):
        self.uppercase = uppercase
        self.lowercase = lowercase


    def uppercase(self, upper):
        if upper.isalpha():
            self.uppercase.upper()
        else:
            print("input cannot be converted to uppercase")

class Capitalize:
    user_input = Capitalize(Henry, madaline)
    print(user_input.uppercase(hello))


      