class Workshop:
    def __init__(self):
        self.jobs = []

    def add_job(self, job):
        self.jobs.append(job)

class Job:
    def __init__(self, job_id, description="", parameters=None):
        self.id = job_id
        self.description = description
        self.parameters = parameters or {}
        self.products = []  # list of Product objects

    def add_product(self, product):
        self.products.append(product)

class Product:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.components = []  # list of Component objects

    # You can skip add_component and just append directly:
    # product.components.append(component)


    def __repr__(self):
        return f"<Product {self.name}>"

class Component:
    def __init__(self, name, ctype, dimensions, transform=None):
        self.name = name
        self.type = ctype
        self.dimensions = dimensions
        self.transform = transform or {"translate": {"x": 0, "y": 0, "z": 0}}


    def __repr__(self):
        return f"<Component {self.name}: {self.type}, dims={self.dimensions}, pos={self.transform}>"
