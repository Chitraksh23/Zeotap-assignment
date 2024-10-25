def save_rule(rule_id, rule_string, ast_structure):
    db.rules.insert_one({
        "_id": rule_id,
        "rule_string": rule_string,
        "ast_structure": ast_structure
    })
def get_rule(rule_id):
    return db.rules.find_one({"_id": rule_id})
