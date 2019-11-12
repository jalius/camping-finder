import requests
import json
campsite_types = ["STANDARD NONELECTRIC"]
campsite_ids = {"Lower Pines":"232450","Upper pines":"232447","North Pines":"232449"}
date_start = "2019-11-01" #YYYY-MM-DD: first of the month only (i.e. only change the month)
for site_name, id in campsite_ids.items():
    response = requests.get("https://www.recreation.gov/api/camps/availability/campground/"+ id +"/month?start_date=" + date_start +"T00:00:00.000Z", headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"})
    response_json = json.loads(response.text)
    for campsite_key, campsite_val in response_json["campsites"].items():
        if campsite_val["campsite_type"] in campsite_types:
            available_consecutively = 0
            for availability_key, availability_val in campsite_val["availabilities"].items():
                if availability_val == "Available":
                    available_consecutively += 1
                    print(site_name + ": " + "campsite " + campsite_val["site"] + ": " + availability_key + " " + availability_val)
                else:
                    available_consecutively = 0
                if available_consecutively > 1:
                    print("consecutive days available: " + str(available_consecutively))
                
        
