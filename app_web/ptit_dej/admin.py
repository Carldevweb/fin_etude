from django.contrib import admin
from .models import TomorrowTeam, Attack, Flag, PetitDej, Consumable

admin.site.register(TomorrowTeam)
admin.site.register(Attack)
admin.site.register(Flag)
admin.site.register(Consumable)

class PetitDejAdmin(admin.ModelAdmin):
    model = PetitDej
    
    raw_id_fields = ("attaque",)


admin.site.register(PetitDej, PetitDejAdmin)
