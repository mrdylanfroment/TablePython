import re

class ExpressionEvaluator:
    EXPR_PATTERN = re.compile(r"!{([^}]+)}")

    def __init__(self, context):
        self.context = context  # Dictionary of all values (table, components, etc)

    def resolve_value(self, value):
        if isinstance(value, str):
            return self.eval_expr(value)
        return value

    def resolve_dict(self, data):
        resolved = {}
        for k, v in data.items():
            if isinstance(v, dict):
                resolved[k] = self.resolve_dict(v)
            else:
                resolved[k] = self.resolve_value(v)
        return resolved

    def eval_expr(self, expr):
        match = self.EXPR_PATTERN.fullmatch(expr.strip())
        if not match:
            return expr  # Not an expression → return raw string

        raw_expression = match.group(1)

        # Convert dot notation to Python dictionary access
        python_expr = re.sub(
            r"([a-zA-Z_]\w*)\.([a-zA-Z_]\w*)",
            r"context['\1']['\2']",
            raw_expression
        )

        try:
            return eval(
                python_expr,
                {"__builtins__": {}},
                {"context": self.context}
            )
        except Exception as e:
            raise ValueError(f"Failed to evaluate '{expr}' → '{python_expr}'") from e
import re # Regular Expression

class ExpressionEvaluator:
    EXPR_PATTERN = re.compile(r"!{([^}]+)}")

    def __init__(self, context):
        self.context = context  # Dictionary of all values (table, components, etc)

    def resolve_value(self, value):
        if isinstance(value, str):
            return self.eval_expr(value)
        return value

    def resolve_dict(self, data):
        resolved = {}
        for k, v in data.items():
            if isinstance(v, dict):
                resolved[k] = self.resolve_dict(v)
            else:
                resolved[k] = self.resolve_value(v)
        return resolved

    def eval_expr(self, expr):
        match = self.EXPR_PATTERN.fullmatch(expr.strip())
        if not match:
            return expr  # Not an expression → return raw string

        raw_expression = match.group(1)

        # Convert dot notation to Python dictionary access
        python_expr = re.sub(
            r"([a-zA-Z_]\w*)\.([a-zA-Z_]\w*)",
            r"context['\1']['\2']",
            raw_expression
        )

        try:
            return eval(
                python_expr,
                {"__builtins__": {}},
                {"context": self.context}
            )
        except Exception as e:
            raise ValueError(f"Failed to evaluate '{expr}' → '{python_expr}'") from e
