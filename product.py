class Product:
    def __init__(self, name, description, components):
        self.name = name
        self.description = description
        self.components = components  # list of Component objects

    def __repr__(self):
        return f"<Product {self.name}>"
