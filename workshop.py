# workshop.py

class Component:
    def __init__(self, name, dimensions=None, position=None, rotation=None):
        self.name = name
        self.dimensions = dimensions or {}
        self.position = position or {"x": 0, "y": 0, "z": 0}
        self.rotation = rotation or {"x": 0, "y": 0, "z": 0}

    def __repr__(self):
        return (
            f"<Component {self.name} dims={self.dimensions} "
            f"pos={self.position} rot={self.rotation}>"
        )


class Product:
    def __init__(self, name):
        self.name = name
        self.components = {}

    def add_component(self, component):
        self.components[component.name] = component

    def __repr__(self):
        return f"<Product {self.name} with {len(self.components)} components>"


class Job:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, product):
        self.products[product.name] = product

    def __repr__(self):
        return f"<Job {self.name} with {len(self.products)} products>"
