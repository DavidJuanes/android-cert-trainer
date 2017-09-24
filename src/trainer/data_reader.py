import json


def read_questions():
    json_data = open("data/questions.json").read()
    return json.loads(json_data)["questions"]
