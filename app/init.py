from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)
# Configure MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client.rule_engine_db  # Database
from app import main
