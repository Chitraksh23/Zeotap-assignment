def evaluate_node(node, data):
    if node["type"] == "operand":
        attr = node["value"]["attribute"]
        op = node["value"]["operator"]
        val = node["value"]["value"]
        return eval(f"{data.get(attr, 0)} {op} {val}")
    elif node["type"] == "operator":
        left_result = evaluate_node(node["left"], data)
        right_result = evaluate_node(node["right"], data)
        return (left_result and right_result) if node["value"] == "AND" else (left_result or right_result)
def evaluate_rule(json_ast, data):
    return evaluate_node(json_ast, data)
