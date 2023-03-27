from django.contrib import admin
from .models import Appartement
from .models import Locataire
from .models import EtatDesLieux
from .models import Paiement
from .models import QuittanceLoyer
# Register your models here
admin.site.register(Appartement)
admin.site.register(Locataire)
admin.site.register(EtatDesLieux)
admin.site.register(Paiement)
admin.site.register(QuittanceLoyer)