class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all=[]

    def __init__(self,name, pet_type, owner="Jeff"):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        Pet.all.append(self)


class Owner:
    def __init__(self,name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        
        else:
            raise Exception("Is not an instance.")
        
    def get_sorted_pets(self):
        pet_list = sorted(self.pets(),key = lambda pet: pet.name)
        return pet_list