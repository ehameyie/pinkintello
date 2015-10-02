class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
        print("Chid Constructor Called")
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        print("Number of Toys - "+str(self.number_of_toys))

# test: bad practice to combine classes and instances billy_cyrus = Parent("Cyrus", "blue")
# test print(billy_cyrus.last_name)

# test: miley_cyrus=Child("Cyrus", "blue", 10)
# test: print(miley_cyrus.number_of_toys)
# test: miley_cyrus.show_info()
