import glob
split_debug = False

def splitline(ligne):
	"""chaine définie comme : "champ_sans_virgule,"champ_avec_virgule, mais entre guillements"" -> ["champ_sans_virgule","champ_avec_virgule, mais entre guillements"]"""
	#ligne = ligne.rstrip('\)
	sep = " "
	sep_magique = "}"
	sep_virgule = ","
	is_open = False
	quote = '"'
	mot = ""
	for c in ligne:
		if c in quote:
			is_open = not is_open
		elif c in sep:
			if not is_open:
				c = sep_magique
		mot += c
	if split_debug:
		print(repr(mot))	
	champs = mot.split(sep_magique)
	return champs

def quote(ch):
	q = '"'
	if ch[0] != q:
		ch = q + ch
	if ch[-1] != q:
		ch = ch + q
	return ch	
	
	

def pondre(nom_table,liste_clefs,liste_valeurs,skipfirst=False):
	chaine = "INSERT INTO " 
	chaine +=  nom_table   
	chaine +=  " ( " 
	flag_premier_liste_clefs = True
	flag_premier_liste_valeurs = True 
	for k in liste_clefs:
		if skipfirst and flag_premier_liste_clefs:
			flag_premier_liste_clefs = False
			continue
		chaine += k
		chaine += ","
	chaine = chaine[:-1]
	chaine += " ) "
	chaine += "values ("
	for v in liste_valeurs:
		if skipfirst and flag_premier_liste_valeurs:
			flag_premier_liste_valeurs = False
			continue
		chaine += quote(v)
		chaine += ","
	chaine = chaine[:-1]
	chaine += " );"	
	return chaine
	

		
	
	
	
with open("saisie_documents.txt",'r') as r:
	clefs = ['id', 'date_doc', 'intitule_doc','type_doc','remarques','debut_planning','fin_planning']
	with open("dest.sql",'w') as w:
		for ligne in r:
			valeurs = splitline(ligne)
				
			w.write(pondre("documents",clefs,valeurs,skipfirst=True))
		

