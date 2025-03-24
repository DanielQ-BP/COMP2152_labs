from Person import Person


class Student(Person):
    def __init__(self, p_name, p_age, p_height, p_major):
        # Call the parent constructor
        super().__init__(p_name, p_age, p_height)

        # Set the new public property
        self.major = p_major

        print("This time it's a Student object")


# Creating an instance of Student with sample data
student1 = Student("Maria", 22, 6, "Computer Science")

# Accessing properties
print("The name of the student is:", student1.name)
print("The major of the student is:", student1.major)
