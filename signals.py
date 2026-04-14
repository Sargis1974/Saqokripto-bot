import requests

def fetch_signal(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        return None
    except:
        return None
