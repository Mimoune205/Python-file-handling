# Nom :Elfakir
# Prénom :Mimoune
# Filière : RSI


# Exercice 01 :
print("-"*25,"Exercice 01","-"*25)

with open("fichier.txt", "r") as file:
	file=file.readlines()
	occurence=1
	valeur="mi" #input("Quelle valeur souhaitez-vous rechercher ?")
	for i in file:
		if valeur in i:
			break
		occurence+=1
	print("occurences :",occurence)



# Exercice 02 :
print("-"*25,"Exercice 02","-"*25)

lines=[]
with open("source.txt", "r") as src:
	src=src.readlines()
	for i in src:
		lines.append(i)
for i in lines:
	with open("destination.txt","a") as des:
		des.write(i.strip()+"\n")

# Exercice 03 :
print("-"*25,"Exercice 03","-"*25)

allow=[]
with open("source.txt","r") as delete:
	delete=delete.readlines()
	mot=input("Entrez un mot pour supprimer toutes les lignes contenant ce mot: ")
	for i in delete:
		if mot in i:
			pass
		else:
			allow.append(i)
with open("source.txt","w") as add:
	for i in allow:
		add.write(i.strip()+"\n")


# Exercice 04:
print("-"*25,"Exercice 04","-"*25)

def ajouter_contact(nom , numéro):
	with open("contacts.txt","a") as ajout:
		contact=f"{nom}:{numéro}+\n"
		ajout.write(contact)
nom=input("Entez un nom :")
numéro=input("Entrez un numéro: ")
ajouter_contact(nom,numéro)


def rechercher_contact(nom):
	with open("contacts.txt","r") as num:
		num=num.readlines()
		for i in num:
			if nom in i:
				print(i.split(":")[1])
				break
			
		else:
			print("Contact introuvable.")

recherche=input("Quel nom voulez-vous rechercher dans le fichier contacts.txt ? ")
rechercher_contact(recherche)


# Exercice 5
print("-"*25,"Exercice 05","-"*25)

def tache(titre,description,statut):
	with open("taches.txt","a") as f:
		f.write(f"Tache: {titre}\ndescription:\n\t{description}\nstatut:{statut}\n")
for i in range(3):
	titre=input("Titre de tache s'il vous plait: ")
	description=input("La description de la tache: ")
	statut=input("Statut, s'il vous plaît: ")
	tache(titre,description,statut)


def affiche_tache():
	with open("taches.txt","r") as file:
		file=file.readlines()
		for i in file:
			print(i.strip())
affiche_tache()

