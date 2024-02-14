from DBmethods import DBmethods
import json

DB = DBmethods()
categories = json.dumps(['BUSINESS', 'ENVIRONMENT', 'POLITICS', 'SCIENCE', 'SPORTS', 'TECH'])
print(DB.create_jsonl('gpt', 'train_dataset.csv', categories))
print(DB.create_jsonl('gpt', 'validation_dataset.csv', categories))
