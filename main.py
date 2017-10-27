import os


def main():
	sections={}
	fichier = input("Rentrez le nom du fichier à parser\n")
	taille = os.path.getsize(fichier)
	for adresse in range(0, taille, 0x10):
		

if __name__ == '__main__':
	main()