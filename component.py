class Component:
    def __init__(self, name, ctype, dimensions, transform=None):
        self.name = name
        self.type = ctype
        self.dimensions = dimensions
        self.transform = transform or {"translate": {"x": 0, "y": 0, "z": 0}}


    def __repr__(self):
        return f"<Component {self.name}: {self.type}, dims={self.dimensions}, pos={self.transform}>"
