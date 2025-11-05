import ast, operator as op

class CalculatorTool:
    name = "calculator"
    description = "Safely evaluate a simple arithmetic expression"
    parameters = {"type":"object","properties":{"expr":{"type":"string"}},"required":["expr"]}

    async def __call__(self, expr: str):
        allowed = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv, ast.Pow: op.pow, ast.USub: op.neg}
        def eval_(node):
            if isinstance(node, ast.Num): return node.n
            if isinstance(node, ast.BinOp): return allowed[type(node.op)](eval_(node.left), eval_(node.right))
            if isinstance(node, ast.UnaryOp): return allowed[type(node.op)](eval_(node.operand))
            raise ValueError("Disallowed expression")
        try:
            tree = ast.parse(expr, mode='eval')
            return {"result": float(eval_(tree.body))}
        except Exception as e:
            return {"error": str(e)}
