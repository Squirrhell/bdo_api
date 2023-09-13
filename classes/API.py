from classes.Log import Log
import requests

class API :

    def __init__(self) :
        None        

    def __call__(self) :
        None

    def get(self, url, param={}, json=False) :
        response = requests.get(url, params=param)
        if self.check_status_code(response.status_code) :
            if json :
                return response.json()
            return response
        else :
            return response.status_code
        
    def post(self, url, param={}, json=False) :
        response = requests.post(url, params=param)
        if self.check_status_code(response.status_code) :
            if json :
                return response.json()
            return response
        else :
            return response.status_code

    def check_status_code(self, status_code) :
        match status_code:
            case 200 :
                return True
            case 301 :
                Log("301 - Moved Permanently", 3)
                return False
            case 400 :
                Log("400 - Bad Request", 3)
                return False
            case 401 :
                Log("401 - Unauthorized", 3)
                return False
            case 403 :
                Log("403 - Forbidden", 3)
                return False
            case 404 :
                Log("404 - Not Found", 3)
                return False
            case 503 :
                Log("503 - Service Unavailable", 3)
                return False
            case _ :
                # Default
                Log(f"{status_code} - Error", 3)
                return False