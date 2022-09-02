import requests
import json

BASE_URL = "http://127.0.0.1:5000/"

class Pokemon:
    
    def __init__(self, pokemon = None, url = None):
        if pokemon is None and url:
          response = requests.get(f"{BASE_URL}/identify/{url}")
        
        if pokemon and url is None:
          response = requests.get(f"{BASE_URL}/pokemon/{pokemon}")
        
        self.info = json.loads(response.text)
        
    def name(self):
      return self.info["pokemon"]
        
