from classes.Log import Log
import requests

class API :

    def __init__(self) :
        None        

    def __call__(self) :
        None

    def get(self, url) :
        response = requests.get(url)
        if self.check_status_code(response.status_code) :
            return response.json()
        else :
            return response.status_code
        
    def post(self, url, param={}) :
        response = requests.post(url, params=param)
        if self.check_status_code(response.status_code) :
            return response.json()
        else :
            return response.status_code

    def check_status_code(self, status_code) :
        match status_code:
            case 200 :
                return True
            case 301 :
                Log("301 - The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.", 3)
                return False
            case 400 :
                Log("400 - The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.", 3)
                return False
            case 401 :
                Log("401 - The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.", 3)
                return False
            case 403 :
                Log("403 - The resource you’re trying to access is forbidden: you don’t have the right perlessons to see it.", 3)
                return False
            case 404 :
                Log("404 - The resource you tried to access wasn’t found on the server.", 3)
                return False
            case 503 :
                Log("503 - The server is not ready to handle the request.", 3)
                return False
            case _ :
                # Default
                Log(f"{status_code} - Error", 3)
                return False