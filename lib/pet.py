# lib/pet.py

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")

        self.name = name
        self.pet_type = pet_type
        self.set_owner(owner)
        Pet.all.append(self)

    def set_owner(self, owner):
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner or None.")
        self.owner = owner

# Import this at the end to avoid circular import issues
from .owner import Owner
