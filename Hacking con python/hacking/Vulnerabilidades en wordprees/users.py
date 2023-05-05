import json
import urllib.request

def main():
	objetivo = urllib.request.urlopen("https://achirou.com/wp-json/wp/users")
	for x in json.loads(objetivo.read()):
		usuario = x['slug']
	print(usuario)

main()