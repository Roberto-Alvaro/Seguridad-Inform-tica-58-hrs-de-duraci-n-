import requests #importamos eso para traernos el codigo de la pagina web
from bs4 import BeautifulSoup

def main():
	agente = {'User-Agent':'Firefox'}
	objetivo = requests.get(url="https://www.festinagroup.com/es/",headers=agente) #obtenemos la informacion de la pagina web, con requests.get
	parseamos = BeautifulSoup(objetivo.text,'html5lib')
	for link in parseamos.find_all('link'):#buscar las palabras "link"
		if 'wp-content/themes/' in link.get('href'):
			tema = link.get('href')
			tema = tema.split('/')
			if 'themes' in tema:
				posicion = tema.index('themes')
				temas = tema[posicion+1]
				print("El tema que usa es: " + temas)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()