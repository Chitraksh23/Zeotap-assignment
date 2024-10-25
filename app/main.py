from flask import request, jsonify
from app import app
from app.models import save_rule, get_rule
from app.rule_parser import create_rule
from app.evaluator import evaluate_rule
@app.route("/create_rule", methods=["POST"])
def create_rule_route():
    rule_string = request.json.get("rule_string")
    rule_id = request.json.get("rule_id")
    ast_structure = create_rule(rule_string)
    save_rule(rule_id, rule_string, ast_structure)
    return jsonify({"rule_id": rule_id, "ast": ast_structure}), 201
@app.route("/evaluate_rule", methods=["POST"])
def evaluate_rule_route():
    rule_id = request.json.get("rule_id")
    data = request.json.get("data")
    rule = get_rule(rule_id)
    result = evaluate_rule(rule["ast_structure"], data)
    return jsonify({"result": result})
