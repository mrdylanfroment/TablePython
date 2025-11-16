from loader import Loader

loader = Loader()
workshop = loader.load("table.yaml")

# Loop through all jobs, products, and components
for job in workshop.jobs:
    print(f"Job: {job.id}")
    for product in job.products:
        print(f"  Product: {product.name}")
        for component in product.components:
            print(f"    Component: {component.name}")
            print(f"      Dimensions: {component.dimensions}")
            print(f"      Transform: {component.transform}")
