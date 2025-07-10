import json


def load_data(filename):
    with open(filename,'r') as file:
        data = json.load(file)
        return data
def people_you_may_know(user_id,data):
    user_friends = {}

    for user in data['users']:
        user_friends[user['id']] = set(user['friends'])
    
    if user_id not in user_friends:
        return []
    
    deirect_friends = user_friends[user_id]
    suggestion = {}

    for friend in deirect_friends:
        for mutual in user_friends[friend]:
            if mutual != user_id and mutual not in deirect_friends:
                suggestion[mutual] = suggestion.get(mutual,0) + 1
    
    sorted_suggestion = sorted(suggestion.items(), key = lambda x : x[1],reverse=True)
    
    return[user_id for user_id,_ in sorted_suggestion]

# Load data

data = load_data("large_data.json")
user_id = 1
recc = people_you_may_know(user_id,data)
print(recc)