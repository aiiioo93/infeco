from django.db import models

class Locataire(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    numero_telephone = models.CharField(max_length=20)
    adresse_email = models.EmailField()
    
    def __str__(self):
        return self.nom

class Appartement(models.Model):
    adresse = models.CharField(max_length=200)
    complement_adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    prix_charges = models.DecimalField(max_digits=10, decimal_places=2)
    loyer = models.DecimalField(max_digits=10, decimal_places=2)
    depot_garantie = models.DecimalField(max_digits=10, decimal_places=2)
    locataire = models.ForeignKey(Locataire, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.adresse

class EtatDesLieux(models.Model):
    appartement = models.ForeignKey(Appartement, on_delete=models.CASCADE)
    date = models.DateField()
    remarques = models.TextField()

class Paiement(models.Model):
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    date = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)

class QuittanceLoyer(models.Model):
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    periode = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
