class Job:
    def __init__(self, name):
        self.name = name
        self.components = []

    def add_component(self, comp):
        self.components.append(comp)

    def summary(self):
        print(f"Job: {self.name}")
        for c in self.components:
            print(f"  {c.name}: {c.dimensions}")
