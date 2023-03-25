# Classe Locataire
class Locataire:
    def __init__(self, nom, adresse, numero_telephone, adresse_email):
        self.nom = nom
        self.adresse = adresse
        self.numero_telephone = numero_telephone
        self.adresse_email = adresse_email
        self.appartements = []
        self.liste_paiements = []
        self.quittances = []
        self.payments = []
    
    def affecter_appartement(self, appartement):
        self.appartements.append(appartement)
        appartement.locataire = self

    def ajouter_paiement(self, date, montant):
        paiement = {"date": date, "montant": montant}
        self.liste_paiements.append(paiement)

    def modifier_paiement(self, index, date, montant):
        self.liste_paiements[index]["date"] = date
        self.liste_paiements[index]["montant"] = montant

    def supprimer_paiement(self, index):
        del self.liste_paiements[index]

    def ajouter_quittance(self, periode, montant):
        quittance = QuittanceLoyer(periode, montant)
        self.quittances.append(quittance)

    def add_payment(self, payment):
        self.payments.append(payment)
        
    def remove_payment(self, payment):
        self.payments.remove(payment)
        
    def get_balance(self, periode):
        balance = 0
        for payment in self.payments:
            if payment.date.year == periode.year and payment.date.month == periode.month:
                balance += payment.montant
        return balance

# Classe Appartement
class Appartement:
    def __init__(self, adresse, complement_adresse, ville, code_postal, prix_charges, loyer, depot_garantie):
        self.adresse = adresse
        self.complement_adresse = complement_adresse
        self.ville = ville
        self.code_postal = code_postal
        self.prix_charges = prix_charges
        self.loyer = loyer
        self.depot_garantie = depot_garantie
        self.locataire = None
        self.etats_des_lieux = []

    def ajouter_etat_des_lieux(self, etat_des_lieux):
        self.etats_des_lieux.append(etat_des_lieux)
    
    def modifier_etat_des_lieux(self, index, etat_des_lieux):
        self.etats_des_lieux[index] = etat_des_lieux
    
    def supprimer_etat_des_lieux(self, index):
        del self.etats_des_lieux[index]

# Classe pour représenter un état des lieux
class EtatDesLieux:
    def __init__(self, date, remarques):
        self.date = date
        self.remarques = remarques

# classe Paiement
class Paiement:
    def __init__(self, date, montant):
        self.date = date
        self.montant = montant

class QuittanceLoyer:
    def __init__(self, periode, montant):
        self.periode = periode
        self.montant = montant

