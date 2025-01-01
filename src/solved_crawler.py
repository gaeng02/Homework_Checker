import csv
import json
import requests

def get_solved (user_id) : 

    # url = "https://solved.ac/api/v3/user/show?handle={user_id}"
    url = f"https://solved.ac/api/v3/user/problem_stats?handle={user_id}"
    headers = {"User-Agent" : "Chrome"}

    response = requests.get(url, headers = headers)

    if (response.status_code != 200) :
        return response.status_code

    data = json.loads(response.text)

    return data


def preprocessing (data) :
    
    stats = []
    for level in range (31) :
        stats.append(data[level]["solved"])

    tier = [0] * 6
    # Bronze, Silver, Gold, Platinum, Diamond, Ruby
    for level in range (1, 31) :
        tier[(level-1) // 5] += stats[level]

    return tier


def save (user_id, data) :

    file = "../info.csv"
    
    with open(file, mode = "r", encoding = "utf-8") as f :
        reader = csv.reader(f)
        rows = list(reader)

    rows.append(data)

    with open(file, mode = "w", encoding = "utf-8", newline = "") as f :
        writer = csv.writer(f)
        writer.writerows(rows)


if (__name__ == "__main__") :

    name = "gaeng_02"
    data = get_solved(name)

    data = preprocessing(data)

    save (name, data)
