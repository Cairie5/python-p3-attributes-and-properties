#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):
        self.name = name
        if breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            print("Breed not approved.")

# Example usage
dog1 = Dog(name="Buddy", breed="Pug")
dog2 = Dog(name="Max", breed="Golden Retriever")  # This breed is not in the approved list
