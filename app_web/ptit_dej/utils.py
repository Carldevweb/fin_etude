from .models import TomorrowTeam, Attack
from random import randint
from django.shortcuts import HttpResponse

def create_fake_info():
    victimes = [TomorrowTeam.objects.create(name='Victime1',last_name='Nom de famille',password='victime1'),
        TomorrowTeam.objects.create(name='Victime2',last_name='Nom de famille',password='victime2'),
        TomorrowTeam.objects.create(name='Victime3',last_name='Nom de famille',password='victime3'),
        TomorrowTeam.objects.create(name='Victime4',last_name='Nom de famille',password='victime4'),
        TomorrowTeam.objects.create(name='Victime5',last_name='Nom de famille',password='victime5'),
        TomorrowTeam.objects.create(name='Victime6',last_name='Nom de famille',password='victime6'),
        TomorrowTeam.objects.create(name='Victime7',last_name='Nom de famille',password='victime7'),
        TomorrowTeam.objects.create(name='Victime8',last_name='Nom de famille',password='victime8'),
        TomorrowTeam.objects.create(name='Victime9',last_name='Nom de famille',password='victime9'),
        TomorrowTeam.objects.create(name='Victime10',last_name='Nom de famille',password='victime10'),
    ]
    
    attaquants = [TomorrowTeam.objects.create(name='Attaquant1',last_name='Nom de famille',password='Attaquant1'),
        TomorrowTeam.objects.create(name='Attaquant2',last_name='Nom de famille',password='Attaquant2'),
        TomorrowTeam.objects.create(name='Attaquant3',last_name='Nom de famille',password='Attaquant3'),
        TomorrowTeam.objects.create(name='Attaquant4',last_name='Nom de famille',password='Attaquant4'),
        TomorrowTeam.objects.create(name='Attaquant5',last_name='Nom de famille',password='Attaquant5'),
        TomorrowTeam.objects.create(name='Attaquant6',last_name='Nom de famille',password='Attaquant6'),
        TomorrowTeam.objects.create(name='Attaquant7',last_name='Nom de famille',password='Attaquant7'),
        TomorrowTeam.objects.create(name='Attaquant8',last_name='Nom de famille',password='Attaquant8'),
    ]
    victimes = [TomorrowTeam.objects.get(name='Victime1',last_name='Nom de famille',password='victime1'),
        TomorrowTeam.objects.get(name='Victime2',last_name='Nom de famille',password='victime2'),
        TomorrowTeam.objects.get(name='Victime3',last_name='Nom de famille',password='victime3'),
        TomorrowTeam.objects.get(name='Victime4',last_name='Nom de famille',password='victime4'),
        TomorrowTeam.objects.get(name='Victime5',last_name='Nom de famille',password='victime5'),
        TomorrowTeam.objects.get(name='Victime6',last_name='Nom de famille',password='victime6'),
        TomorrowTeam.objects.get(name='Victime7',last_name='Nom de famille',password='victime7'),
        TomorrowTeam.objects.get(name='Victime8',last_name='Nom de famille',password='victime8'),
        TomorrowTeam.objects.get(name='Victime9',last_name='Nom de famille',password='victime9'),
        TomorrowTeam.objects.get(name='Victime10',last_name='Nom de famille',password='victime10'),
    ]
    
    attaquants = [TomorrowTeam.objects.get(name='Attaquant1',last_name='Nom de famille',password='Attaquant1'),
        TomorrowTeam.objects.get(name='Attaquant2',last_name='Nom de famille',password='Attaquant2'),
        TomorrowTeam.objects.get(name='Attaquant3',last_name='Nom de famille',password='Attaquant3'),
        TomorrowTeam.objects.get(name='Attaquant4',last_name='Nom de famille',password='Attaquant4'),
        TomorrowTeam.objects.get(name='Attaquant5',last_name='Nom de famille',password='Attaquant5'),
        TomorrowTeam.objects.get(name='Attaquant6',last_name='Nom de famille',password='Attaquant6'),
        TomorrowTeam.objects.get(name='Attaquant7',last_name='Nom de famille',password='Attaquant7'),
        TomorrowTeam.objects.get(name='Attaquant8',last_name='Nom de famille',password='Attaquant8'),
    ]
    
    news_attaques = []
    attacker = attaquants[randint(0,4) % 4]
    victim = victimes[randint(0,4) % 4]
    
    for i in range(10 * 4):
        for k in range(100_000):
            news_attaques.append(Attack(attacker=attacker, victim=victim, type_attack=1))
        Attack.objects.bulk_create(news_attaques)
        news_attaques = []
        print(f"BULK CREATE {k*(i+1)} attaques")
    return HttpResponse('oki')