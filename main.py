import os
from mbr import mbr
from fat32Directory import fat32Directory
from fat32InfoSector import fat32InfoSector
from fat32SectorBoot import fat32SectorBoot
import pdb

sections=set()
fichier=None

def main():
	fichier = input("Rentrez le nom du fichier à parser\n")
	taille = os.path.getsize(fichier)
	for adresse in range(0, 0x1c00000, 0x10):
		# Attention, tester le fat32SectorBoot avant le mbr car ils ont le meme number magic, mais le fat32SectorBoot
		# a besoin d'un deuxieme element pour etre identifié
		for forme in [fat32SectorBoot, mbr, fat32Directory, fat32Directory, fat32Directory]:
			try:
				test_parse=forme(fichier, adresse)
				sections.add(test_parse)
				print(type(test_parse))
				# on continue a avancer
				break
			# on except toutes les exceptions, donc attention a etre sur que les lignes autres que "test_parse..." n'ont pas de bug !!!!
			except:
				# on teste une autre classe
				continue

if __name__ == '__main__':
	main()