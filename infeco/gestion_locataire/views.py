from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from .models import Locataire
from .models import Appartement, AffectationAppartement, EtatDesLieux, Paiement, QuittanceLoyer


# Create your views here.


#/

def index(request):
    # Locataires = Locataire.objects.all()
    # Locataires_names = [locataire.nom for locataire in Locataires]
    # Locataires_names_str = ", ".join(Locataires_names)
    # return HttpResponse('Les locataire : ' + Locataires_names_str)
    # Locataires = Locataire.objects.all()
    # return render(request, 'gestion_locataire/index.html')
    pass




def index(request):

    return render(request, 'gestion_locataire/index.html')



def appartement_list(request):
    appartements = Appartement.objects.all()
    return render(request, 'gestion_locataire/appartement_list.html', {'appartements': appartements})

def locataire_list(request):
    locataires = Locataire.objects.all()
    return render(request, 'gestion_locataire/locataire_list.html', {'locataires': locataires})

def affectation_appartement_list(request):
    affectation_appartements = AffectationAppartement.objects.all()
    return render(request, 'gestion_locataire/affectation_appartement_list.html', {'affectation_appartements': affectation_appartements})

def etat_des_lieux_list(request):
    etat_des_lieux = EtatDesLieux.objects.all()
    return render(request, 'gestion_locataire/etat_des_lieux_list.html', {'etat_des_lieux': etat_des_lieux})

def paiement_list(request):
    paiements = Paiement.objects.all()
    return render(request, 'gestion_locataire/paiement_list.html', {'paiements': paiements})

def quittance_loyer_list(request):
    quittance_loyers = QuittanceLoyer.objects.all()
    return render(request, 'gestion_locataire/quittance_loyer_list.html', {'quittance_loyers': quittance_loyers})