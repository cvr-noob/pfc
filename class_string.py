class IOString:
    def __init__(self):
        self.str1 = ''

    def get_str(self):
        print("Enter the string: ")
        self.str1 = input()

    def print_str(self):
        print(self.str1.upper())

str_obj = IOString()
str_obj.get_str()
str_obj.print_str()
