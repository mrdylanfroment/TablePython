import yaml
from expression import ExpressionEvaluator
from job import Job
from component import Component

class Loader:
    def load(self, filename):
        with open(filename, "r") as f:
            data = yaml.safe_load(f)

        # Full YAML becomes the root context
        context = data

        evaluator = ExpressionEvaluator(context)
        job = Job(name=data["name"])

        for comp_data in data["components"]:
            dims = evaluator.resolve_dict(comp_data["dimensions"])
            component = Component(
                name=comp_data["name"],
                ctype=comp_data["type"],
                dimensions=dims
            )
            job.add_component(component)

        return job
