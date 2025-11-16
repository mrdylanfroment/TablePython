class Product:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.components = []  # list of Component objects

    # You can skip add_component and just append directly:
    # product.components.append(component)


    def __repr__(self):
        return f"<Product {self.name}>"
