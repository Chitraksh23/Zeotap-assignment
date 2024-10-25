from app.ast_structure import Node
def parse_condition(condition_str):
    # Basic parser for a condition (e.g., "age > 30")
    attribute, operator, value = condition_str.split(" ")
    return Node("operand", value={"attribute": attribute, "operator": operator, "value": int(value)})
def parse_rule(rule_str):
    # Simplified parser to construct the AST; this is a stub for illustration.
    # Parse complex rules and generate the root Node accordingly.
    if "AND" in rule_str:
        left, right = rule_str.split(" AND ", 1)
        return Node("operator", left=parse_condition(left.strip()), right=parse_condition(right.strip()), value="AND")
    elif "OR" in rule_str:
        left, right = rule_str.split(" OR ", 1)
        return Node("operator", left=parse_condition(left.strip()), right=parse_condition(right.strip()), value="OR")
def create_rule(rule_string):
    return parse_rule(rule_string).to_dict()
