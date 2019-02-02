import json
with open('users.json') as data_file:    
    data = json.load(data_file)

users = data['users']

for user in users:
    print user