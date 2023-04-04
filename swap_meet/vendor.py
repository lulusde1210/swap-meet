
class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True
        return False

    def swap_first_item(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            my_first_item = self.inventory[0]
            other_first_item = other_vendor.inventory[0]
            self.remove(my_first_item)
            self.add(other_first_item)
            other_vendor.remove(other_first_item)
            other_vendor.add(my_first_item)
            return True
        return False
