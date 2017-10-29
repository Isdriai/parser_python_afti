import os
from mbr import mbr
from fat32Directory import fat32Directory
from fat32InfoSector import fat32InfoSector
from fat32SectorBoot import fat32SectorBoot
import pdb

sections=[]
fichier=None

def main():
	fichier = input("Rentrez le nom du fichier à parser\n")
	taille = os.path.getsize(fichier)
	index = 0
	for adresse in range(0, 0x1c00000, 0x10):
		# Attention, tester tout avant le mbr car le mbr a juste un number magic a vérifier
		# Les autres ont des fonctions de pre parsage plus fine
		for forme in [fat32SectorBoot, fat32Directory, fat32InfoSector, mbr]:
			try:
				test_parse=forme(fichier, adresse)
				sections.append(test_parse)
				print(type(test_parse), end="")
				print("   " + hex(adresse) + "   " + str(index))
				index+=1
				# on continue a avancer
				break
			# on except toutes les exceptions, donc attention a etre sur que les lignes autres que "test_parse..." n'ont pas de bug !!!!
			except:
				# on teste une autre classe
				continue

if __name__ == '__main__':
	main()