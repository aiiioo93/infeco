#test de  la création d'un appartement
appartement = appartement1("1, rue des Fleurs", 500, 1000)
print("Adresse de l'appartement :", appartement.adresse)
print("Prix des charges de l'appartement :", appartement.prix_charges)
print("Loyer de l'appartement :", appartement.loyer)

# test affectation d'un locataire à un appartement
locataire1.affecter_appartement(appartement1)

# Vérification de l'affectation
assert locataire1.appartements[0] == appartement1
assert appartement1.locataire == locataire1