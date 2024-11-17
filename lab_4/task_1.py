# TODO решите задачу
def task() -> float:
   import json
   with open('input.json', 'r') as file:
      ch = json.load(file)
      sum_ = sum( i['score'] * i['weight'] for i in ch )
      return round(sum_, 3)
print(task())
