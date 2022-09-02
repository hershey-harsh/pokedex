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
        
        self.name = self.info["pokemon"]
        
        self.description = self.info["description"]
        
        names = []
        for i in self.info["names"].split(", "):
            names.append(i)
        self.names = names
        
        self.region = self.info["region"]
        
        types = []
        for i in self.info["types"].split(", "):
            names.append(i)
        self.types = types
        
        self.evolution = self.info["evolution"]
        
        self.dex_number = self.info["dex_number"]
        
        self.appearance = self.info["appearance"]
        self.appearance.height = self.appearance["height"]
        self.appearance.weight = self.appearance["weight"]
        
        self.base_stats = self.info["base_stats"]
        self.base_stats.attack = self.base_stats["attack"]
        self.base_stats.defense = self.base_stats["defense"]
        self.base_stats.hit_points = self.base_stats["hit_points"]
        self.base_stats.speed = self.base_stats["speed"]
        self.base_stats.speed_Attack = self.base_stats["speed_Attack"]
        self.base_stats.speed_Defense = self.base_stats["speed_Defense"]
        
        
        
