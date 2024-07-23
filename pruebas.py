from books.models import Genre
print("Hello")


class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} tiene {self.age} years old"


juan = Employee('Juan', 34)

print(juan.__str__())


b = Genre(genre='Fantasy')  # Creamos una instancia de la clase
b.save()  # esto es como hacer un insert en SQL
