contacts = {
    "number": 4,
    "students": [
        {
            "name": "Alice Smith",
            "phone": "555-1234",
            "email": "alice.smith@example.com"
        },
        {
            "name": "Bob Jones",
            "phone": "555-5678",
            "email": "bob.jones@example.com"
        },
        {
            "name": "Charlie Brown",
            "phone": "555-9876",
            "email": "charlie.brown@example.com"
        },
        {
            "name": "David Lee",
            "phone": "555-4321",
            "email": "davide.lee@example.com"
        }
    ]
}

print("Student emails")
for student in contacts["students"]:
    print(student["email"])