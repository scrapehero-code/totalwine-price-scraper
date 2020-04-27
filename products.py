from selectorlib import Extractor
import requests 
import csv

e = Extractor.from_yaml_file('selectors.yml')

def scrape(url):    
    headers = {
        'authority': 'www.totalwine.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'referer': 'https://www.totalwine.com/store-info/massachusetts-natick/1701',
        'accept-language': 'en-US,en;q=0.9',
    }

    r = requests.get(url, headers=headers)
    return e.extract(r.text, base_url=url)

with open("urls.txt",'r') as urllist, open('data.csv','w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["Name","Price","Size","InStock","DeliveryAvailable","URL"],quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for url in urllist.readlines():
        data = scrape(url) 
        if data:
            for r in data['Products']:
                writer.writerow(r)