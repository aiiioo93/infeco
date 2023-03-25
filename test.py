from class_infeco import Appartement
from class_infeco import Locataire
from class_infeco import EtatDesLieux
from class_infeco import Paiement
import datetime


# test création d'un appartement
appartement1 = Appartement("12 rue de la Paix", "Appt 101", "Paris", "75000", 200, 1000, 1500)

# test Création d'un locataire
locataire1 = Locataire("John Doe", "12 rue de la Paix", "0123456789", "johndoe@email.com")

# test affectation d'un locataire à un appartement
locataire1.affecter_appartement(appartement1)

# Vérification de l'affectation d'un locataire à un appartement
assert locataire1.appartements[0] == appartement1
assert appartement1.locataire == locataire1

# test ajout d'un paiement
locataire1.ajouter_paiement("01/01/2022", 500)
locataire1.ajouter_paiement("02/01/2022", 600)

# test affichage de tous les paiements
print('')
print("AFFICHE TOUS LES PAIEMENTS")
print("------------------------------------")
for i, paiement in enumerate(locataire1.liste_paiements):
    print("Paiement {} :".format(i+1))
    print("Date : ", paiement["date"])
    print("Montant : ", paiement["montant"])

# test modification d'un paiement
locataire1.modifier_paiement(0, "01/02/2022", 700)

# test affichage de tous les paiements après modification
print('')
print("AFFICHE TOUS LES PAIEMENTS APRES MODIFICATION")
print("------------------------------------")
for i, paiement in enumerate(locataire1.liste_paiements):
    print("Paiement {} :".format(i+1))
    print("Date : ", paiement["date"])
    print("Montant : ", paiement["montant"])

# test suppression d'un paiement
locataire1.supprimer_paiement(0)

# test affichage de tous les paiements après suppression
print('')
print("AFFICHE TOUS LES PAIEMENTS APRES SUPPRESSION")
print("------------------------------------")
for i, paiement in enumerate(locataire1.liste_paiements):
    print("Paiement {} :".format(i+1))
    print("Date : ", paiement["date"])
    print("Montant : ", paiement["montant"])

# test ajout d'un état des lieux
etat_des_lieux1 = EtatDesLieux("25-02-2022", "Remarques observées 1")
appartement1.ajouter_etat_des_lieux(etat_des_lieux1)
print('')
print("AFFICHE L'AJOUT  D'UN ETAT DES LIEUX")
print("------------------------------------")
print("Adresse : ", appartement1.adresse)
print("Nombre d'états des lieux : ", len(appartement1.etats_des_lieux))
for etat_des_lieux in appartement1.etats_des_lieux:
    print("Date : ", etat_des_lieux1.date)
    print("Remarques : ", etat_des_lieux1.remarques)

# test modification d'un état des lieux
etat_des_lieux2 = EtatDesLieux("26-02-2022", "Remarques observées 2")
appartement1.modifier_etat_des_lieux(0, etat_des_lieux2)
print('')
print("AFFICHE LA MODIFICATION D'UN ETAT DES LIEUX")
print("------------------------------------")
print("Adresse : ", appartement1.adresse)
print("Nombre d'états des lieux : ", len(appartement1.etats_des_lieux))
for etat_des_lieux in appartement1.etats_des_lieux:
    print("Date : ", etat_des_lieux2.date)
    print("Remarques : ", etat_des_lieux2.remarques)

# test suppression d'un état des lieux
appartement1.supprimer_etat_des_lieux(0)
print('')
print("TEST LA SUPPRESSION D'UN ETAT DES LIEUX")
print("------------------------------------")

# Vérification de la gestion des états des lieux
print('')
print("VERIFIE LA GESTION DES ETAT DES LIEUX")
print("------------------------------------")
print("Adresse : ", appartement1.adresse)
print("Prix des charges : ", appartement1.prix_charges)
print("Loyer : ", appartement1.loyer)
print("Dépôt de garantie : ", appartement1.depot_garantie)
print("États des lieux : ", appartement1.etats_des_lieux)

# test ajout de quittances de loyer
locataire1.ajouter_quittance("Janvier-Février 2022", 800)
locataire1.ajouter_quittance("Mars-Avril 2022", 800)

# Vérification des quittances
print('')
print("AFFICHE L'AJOUT D'UNE QUITTANCE")
print("------------------------------------")
print("Locataire : ", locataire1.nom)
for quittance in locataire1.quittances:
    print("Période : ", quittance.periode)
    print("Montant : ", quittance.montant)

# test ajout de paiements pour le locataire
payment1 = Paiement(datetime.datetime(2022, 1, 1), 1000)
locataire1.add_payment(payment1)
payment2 = Paiement(datetime.datetime(2022, 2, 1), 1000)
locataire1.add_payment(payment2)

# Récupération du bilan des comptes des loyers pour le mois de janvier 2022
periode = datetime.datetime(2022, 1, 1)
balance = locataire1.get_balance(periode)
print('')
print("AFFICHE LE BILAN DES COMPTE LOYER POUR JANVIER 2022")
print("------------------------------------")
print("Bilan des comptes des loyers pour", periode.strftime("%B %Y"), ":", balance)