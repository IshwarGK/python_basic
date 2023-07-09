class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name} ({self.age} years old)"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __len__(self):
        return self.age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

# Create Person objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Test magic methods

# __str__()
print(str(person1))  # Output: "Person: Alice (30 years old)"
print(person2)      # Output: "Person: Bob (25 years old)"

# __repr__()
print(repr(person1))  # Output: "Person(name=Alice, age=30)"
print(person2)       # Output: "Person(name=Bob, age=25)"

# __len__()
print(len(person1))  # Output: 30
print(len(person2))  # Output: 25

# __eq__()
print(person1 == person2)           # Output: False
print(person1 == Person("Alice", 30))  # Output: True
