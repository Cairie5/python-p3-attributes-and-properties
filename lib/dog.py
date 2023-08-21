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
        self.name = None
        self.breed = None
        self.name = name
        self.breed = breed
        
        
    def name(self):
        return self.name
    
    def name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
            self.name = name
        else:
            print ("Name must be a string between 1 and 25 characters.")
            
    def breed(self):
        return self.breed
    
    def breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print ("Breed must be in list of approved breeds.")
