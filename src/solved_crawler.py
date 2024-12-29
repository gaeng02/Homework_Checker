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

    return soup


