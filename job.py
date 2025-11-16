class Job:
    def __init__(self, job_id, description="", parameters=None):
        self.id = job_id
        self.description = description
        self.parameters = parameters or {}
        self.products = []  # list of Product objects

    def add_product(self, product):
        self.products.append(product)
