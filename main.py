from loader import Loader

loader = Loader()
job = loader.load("yaml/table.yaml")

print("Workshop loaded:")

print(f"Job: {job.name}")

for prod_name, product in job.products.items():
    print(f"  Product: {prod_name}")
    for comp_name, comp in product.components.items():
        print(f"    Component: {comp.name}")
        print(f"      Dimensions: {comp.dimensions}")
        print(f"      Position:   {comp.position}")
        print(f"      Rotation:   {comp.rotation}")
