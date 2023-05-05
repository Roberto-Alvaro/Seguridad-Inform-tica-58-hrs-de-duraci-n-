import dns.resolver

def main():
	try:
		objetivo = dns.resolver.query("achirou.com","NS")
		for x in objetivo:
			print(x)
	except:
		print("No pude obtener información")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()