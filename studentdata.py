Student_data = {"id1":{ 'name':'sara', 'class': '5', 'subject': 'math'}, 'id2':{ 'name':'ryan', 'class': '6', 'subject': 'science'}, 'id3':{ 'name':'sara', 'class': '5', 'subject': 'math'}, 'id4':{ 'name':'lila', 'class': '4', 'subject': 'english'}, 'id5':{ 'name':'ansh', 'class': '8', 'subject': 'history'}}
print(Student_data)
result = {}
for key, value in Student_data.items():
    if value not in result.values():
        result[key] = value
print(result)   