import requests
from bs4 import BeautifulSoup

def crawler (user_id) : 
    
    url = f"https://www.acmicpc.net/status?user_id={user_id}&result_id=4"
    headers = {"User-Agent" : "Chrome"}

    '''
    response = requests.get(url, headers = headers)

    if (response.status_code != 200) :
        return response.status_code

    soup = BeautifulSoup(response.text, "html.parser")
    '''

    print(url)
