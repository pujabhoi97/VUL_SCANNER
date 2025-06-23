# scan_modules/dir_check.py

import requests

def check_directory_listing(url):
    try:
        response = requests.get(url)
        if response.status_code == 200 and "<title>Index of /" in response.text:
            return True
        else:
            return False
    except requests.RequestException:
        return False
