# lib/owner.py

from .pet import Pet

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Must add an instance of Pet.")
        pet.set_owner(self)

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
