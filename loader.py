import yaml
from expression import ExpressionEvaluator
#from job import Job
#from product import Product
#from component import Component
from workshop import Workshop, Job, Product, Component

class Loader:
    def load(self, filename):
        with open(filename, "r") as f:
            data = yaml.safe_load(f)

        # Create the workshop
        workshop = Workshop()

        # Root context for expression evaluation
        context = data
        evaluator = ExpressionEvaluator(context)

        # Create a Job
        job = Job(job_id=data.get("name", "job1"), description=data.get("description", ""))

        # Create a Product
        product = Product(name=data.get("name", "table"), description=data.get("description", ""))

        # Create Components from YAML
        for comp_data in data.get("components", []):
            # Resolve dimensions and transforms
            dims = evaluator.resolve_dict(comp_data.get("dimensions", {}))
            trans = evaluator.resolve_dict(comp_data.get("transform", {}))

            component = Component(
                name=comp_data["name"],
                ctype=comp_data["type"],
                dimensions=dims,
                transform=trans
            )
            # Add to product
            product.components.append(component)

        # Add product to job
        job.products.append(product)

        # Add job to workshop
        workshop.jobs.append(job)

        return workshop
