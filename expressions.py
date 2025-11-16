# expressions.py
import re

class ExpressionEvaluator:
    """
    Evaluates expressions stored as strings in YAML files.
    Expressions must be in the form: !{ ... }.
    The variables in expressions are available via the context dictionary.
    Example: !{table['height'] - 30}
    """

    def __init__(self, context=None):
        """
        context: dict
            A dictionary containing top-level variables, e.g., {'table': {...}}
        """
        self.context = context or {}

    def eval_expr(self, expr: str):
        """
        Evaluate a single expression string of the form "!{...}".
        """
        # Remove !{ } wrapper if present
        python_expr = expr[2:-1] if expr.startswith("!{") and expr.endswith("}") else expr

        try:
            # Evaluate with context dict as locals
            return eval(python_expr, {"__builtins__": {}}, self.context)
        except Exception as e:
            raise ValueError(f"Failed to evaluate '{expr}' → '{python_expr}'") from e

    def resolve_value(self, value):
        """
        Resolve a single value. If it's a string starting with !{...}, evaluate it.
        Otherwise, return it as-is.
        """
        if isinstance(value, str) and value.startswith("!{") and value.endswith("}"):
            return self.eval_expr(value)
        return value

    def resolve_dict(self, data):
        """
        Recursively resolve a dictionary, evaluating any expression strings.
        """
        if not isinstance(data, dict):
            return self.resolve_value(data)
        resolved = {}
        for k, v in data.items():
            resolved[k] = self.resolve_dict(v) if isinstance(v, dict) else self.resolve_value(v)
        return resolved
