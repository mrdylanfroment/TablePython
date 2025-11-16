# loader.py
import yaml
from workshop import Job, Product, Component
from expressions import ExpressionEvaluator

class Loader:
    def load(self, filepath):
        with open(filepath, "r") as f:
            data = yaml.safe_load(f)

        # Build global context for expressions
        context = {k: v for k, v in data.items() if k not in ("products", "name")}
        evaluator = ExpressionEvaluator(context)

        # Create Job
        job = Job(name=data.get("name", "Unnamed Job"))

        # Load products
        for prod_name, prod_data in data.get("products", {}).items():
            product = Product(prod_name)

            for comp_name, comp_data in prod_data.get("components", {}).items():
                dimensions = evaluator.resolve_dict(comp_data.get("dimensions", {}))
                position = evaluator.resolve_dict(comp_data.get("position", {}))
                rotation = evaluator.resolve_dict(comp_data.get("rotation", {}))

                component = Component(
                    name=comp_name,
                    dimensions=dimensions,
                    position=position,
                    rotation=rotation
                )

                product.add_component(component)

            job.add_product(product)

        return job
