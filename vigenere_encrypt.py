#!/usr/bin/python3

def vigenere_encrypt(texte, key):
	resultat = ""

	for i in range(0, len(texte)):
		if 65 <= ord(texte[i]) <= 90:
			current_str = (ord(texte[i]) - 65)
			current_key = (ord(key[i % len(key)]) - 65)
			new = current_str + current_key
			resultat += chr(new % 26 + 65)
		else:
			resultat += texte[i]

	return resultat

text = "AUJOURD'HUI EST UN JOUR PARTICULIER"
key = "CRYPTOGRAPHIE"

encrypted = vigenere_encrypt(text, key)
print(encrypted)
