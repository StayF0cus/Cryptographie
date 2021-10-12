#!/usr/bin/python3
import argparse

def vigenere(texte, key, decrypt = False):
	resultat = ""

	for i in range(0, len(texte)):
		current_str = (ord(texte[i]) - 65)
		current_key = (ord(key[i % len(key)]) - 65)
		if not decrypt:
			new = current_str + current_key
		else:
			new = current_str - current_key
		if 65 <= ord(texte[i]) <= 90:
			resultat += chr(new % 26 + 65)
		else:
			resultat += texte[i]

	return resultat

parser = argparse.ArgumentParser()

parser.add_argument('-e', '--encrypt', action='store_true')
parser.add_argument('-d', '--decrypt', action='store_true')
parser.add_argument('-t', '--text', action='store', type=str, required=True)
parser.add_argument('-k', '--key', action='store', type=str, required=True)

args = parser.parse_args()

if args.text and args.key:
	if args.encrypt:
		encrypted = vigenere(args.text, args.key)
		print(encrypted)
	elif args.decrypt:
		decrypted = vigenere(args.text, args.key, True)
		print(decrypted)
	else:
		exit(1)
