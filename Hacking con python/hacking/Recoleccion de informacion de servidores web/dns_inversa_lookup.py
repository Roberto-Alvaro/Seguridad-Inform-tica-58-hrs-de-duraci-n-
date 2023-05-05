import requests
from bs4 import BeautifulSoup

def main():
	objetivo = "achirou.com"
	agente = {'User-Agent':'Firefox'}
	web = requests.get("https://viewdns.info/reverseip/?host={}&t=1".format(objetivo), headers=agente)
	bea = BeautifulSoup(web.text,'html5lib')
	buscar = bea.find(id="null")
	sitios = buscar.find(border="1")
	for x in sitios.find_all("tr"):
		print("Sitios: " + x.td.string)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()