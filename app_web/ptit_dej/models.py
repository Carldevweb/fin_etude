from django.db import models
from django.contrib.auth import get_user_model
 
User = get_user_model()

class TomorrowTeam(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='tomorrowteam')
    code = models.CharField(max_length=18, null=False,)
    picture = models.ImageField(upload_to='image_profile', max_length=100, null=True)
    
    def __str__(self):
        return str(self.user)

class Attack(models.Model):
    attacker = models.ForeignKey(TomorrowTeam, null=True, related_name='attack_ransom', on_delete=models.CASCADE)
    victim = models.ForeignKey(TomorrowTeam, null=True, related_name='victim_pay', on_delete=models.CASCADE)
    type_attack = models.IntegerField(default=1)
    succesful = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    
    def __str__(self):
        return str(self.attacker)
      
class Flag(models.Model):
    user = models.ForeignKey(TomorrowTeam, on_delete=models.CASCADE)
    code = models.CharField(max_length=40)
    used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    offensive = models.ForeignKey(Attack, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
    
class ConsumableChoices(object): 
    PAIN_AU_CHOCOLAT = 'pain au choco'
    CROISSANT = 'croissant'
    JUS_ORANGE = "jus d'orange"
    JUS_POMME = 'jus de pomme'
    CAFE = 'Café'
    DSP = 'maison'
    
    CHOICES = [
    (PAIN_AU_CHOCOLAT, 'pain au choco'),
    (CROISSANT, 'Croissant'),
    (JUS_ORANGE, "jus d'orange"),
    (JUS_POMME, 'Jus de pomme'),
    (CAFE, 'Café'),
    (DSP, 'maison'),
]
    
names = {
    'PAIN_AU_CHOCOLAT': 'Pain au choco',
    'CROISSANT': 'Croissant',
    'JUS_ORANGE': "Jus d'orange",
    'JUS_POMME': 'Jus de pomme',
    'CAFE': 'CAFEEEEEEEEEE',
    'DSP': 'despé maison',
    }
    
class Consumable(models.Model):
    name = models.CharField(
        max_length=15,
        choices=ConsumableChoices.CHOICES,
        default=ConsumableChoices.CAFE
    )
    quantites = models.IntegerField(default=1)
    
    @property
    def name2(self):
        try:
            print(self.name)
            return str(names[self.name])
        except:
            return 'err'
    
class PetitDej(models.Model):
    attaque = models.ForeignKey(Attack, related_name='PetitDej_Pay', on_delete=models.CASCADE, null=True)
    payer = models.ForeignKey(TomorrowTeam, on_delete=models.CASCADE)
    consomable = models.ManyToManyField(Consumable)
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return str(self.consomable)