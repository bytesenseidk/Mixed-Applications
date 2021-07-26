import json
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from urllib.request import urlopen

class NumberAnalyzer(object):
    def __init__(self, number):
        self.number = phonenumbers.parse(number)
        self.url = "https://ipinfo.io/"

    def analyze(self):
        description = geocoder.description_for_number(self.number, "en")
        supplier = carrier.name_for_number(self.number, "en")
        response = urlopen(self.url)
        data = json.load(response)
        return [description, supplier, data]
    
    def parse_data(self):
        country, supplier, device = self.analyze()
        region = device["region"]
        city = device["city"]
        location = device["loc"]
        postal = device["postal"]
        timezone = device["timezone"]
        server = device["org"]
        hostname = device["hotsname"]
        ip = device["ip"]
        return [country, region, city, location, postal, timezone, server, hostname, supplier, ip]

if __name__ == "__main__":
    number = input("Enter Number: ")
    test = NumberAnalyzer(number)
    print(test.parse_data())
    
