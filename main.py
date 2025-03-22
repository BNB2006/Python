import json
# JSON string
json_string = '{"name": "John", "age": 30, "is_student": false, "courses": "Science","address": "Nagpur"}'
# Serialize to JSON string
python_obj = json.dumps(json_string)
print(python_obj)
# Deserialize JSON string to Python object
json_string = json.loads(python_obj)
print(json_string)