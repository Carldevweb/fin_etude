from datetime import datetime, timedelta
from random import random
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.db.models import Count, Q

from django.db import connection

import json
from .models import Consumable, Attack, TomorrowTeam, PetitDej


def login_view(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        
    return render(request, 'login.html')


@login_required()
def home(request):
    
    top_attaquants = TomorrowTeam.objects.annotate(nb_attaque=Count('attack_ransom')).filter(nb_attaque__gt=0).order_by('-nb_attaque')[:3]
    attaquants_object = TomorrowTeam.objects.filter(id__in=top_attaquants).prefetch_related('user').order_by('id')
    attaques = Attack.objects.filter(attacker__in=attaquants_object).order_by('-id')[:10]
    
    context = {'attaques': attaques,'top_attaquants': top_attaquants}
    
    return render(request, 'home.html', context=context) 


@login_required()
def team(request):   
    
    staffs = TomorrowTeam.objects.all()
     
    context = {'staffs': staffs}
    
    return render(request, 'team.html', context=context)


@login_required() 
def palmeOr(request):
    
    monthago = datetime.now() - timedelta(days=31)
    
    if random() > .9:
        method = 'Tomorrow Team annotate'
        staffs = TomorrowTeam.objects.filter(attack_ransom__created_at__gte=monthago).prefetch_related('user').annotate(nb_attaque=Count("attack_ransom")).order_by('-nb_attaque')[:1]
        #scores = Attack.objects.filter(attacker__in=staffs).order_by("-id")[:10]
    else:
        #method = 'Attack + process data'
        attaques = Attack.objects.filter(created_at__gte=monthago).values('attacker').annotate(nb_attaque=Count('attacker')).order_by('-nb_attaque')[:1]
        attaques = list(attaques)
        attaquants_id = [i.get('attacker') for i in attaques]
        attaquants_object = TomorrowTeam.objects.filter(id__in=attaquants_id).prefetch_related('user').order_by('id')
        staffs = [{**x, 'attacker': y} for x,y in zip(attaques, attaquants_object)]

        scores = Attack.objects.filter(attacker__in=attaquants_object).prefetch_related('victim').order_by("-id")[:10]
    
    # print(staffs)
    # print("|".join([str(x.get('sql')) for x in connection.queries]))
    #print(f"Sum des sql {method} (s):",sum([float(x.get('time')) for x in connection.queries]))
    
    context = {'staffs': staffs, 'scores': scores}
    
    return render(request, 'palmeOr.html', context=context)

@login_required()
def palmeDej(request):
     
    # teams = TomorrowTeam.objects.all().order_by("id").annotate(nb_attaque=Count("victim_pay"))
    # attaques_recente = list(Attack.objects.filter(created_at__gte=monthago).values_list('id',flat=True))
    # print(attaques_recente)
    # victimes = TomorrowTeam.objects.filter(victim_pay__pk__in=attaques_recente).annotate(nb_attaque=Count("victim_pay")).filter(nb_attaque__gt=0).order_by('-nb_attaque')
    # attaques = Attack.objects.all()
    # teams = TomorrowTeam.objects.all().aggregate(Max('victim_pay'))
    # context = {'attaques': attaques, 'teams': teams}

    monthago = datetime.now() - timedelta(days=31)
    
    victimes = Attack.objects.filter(created_at__gte=monthago).values('victim').annotate(nb_attaque=Count("victim")).order_by('-nb_attaque')[:1]
    victimes = list(victimes)
    # victimes = [{'victim':1, 'nb_attaque': 12234}]
    victimes_id = [i.get('victim') for i in victimes]
    victimes_object = TomorrowTeam.objects.filter(id__in=victimes_id).prefetch_related('user').order_by('id')
    staffs = [{**x, 'victim': y} for x,y in zip(victimes, victimes_object)]
    #staffs = [{'victim': TomoTeam, 'nb_attaque': 12234}]

    scores = Attack.objects.filter(victim__in=victimes_object).prefetch_related('attacker').order_by("-id")[:10]

    #print(victimes)
    
    context = {'staffs': staffs, 'scores': scores}
    
    #print(f"Sum des sql (s):",sum([float(x.get('time')) for x in connection.queries]))
    
    return render(request, 'palmeDej.html', context=context)

@login_required
def offrandes(request):
    
    consommables = PetitDej.objects.annotate(attacker=Count('attaque')).order_by('-id')[:30]
    #print(consommables)
    context = {"consomables": consommables}
    
    return render(request, 'offrandes.html', context=context)

@login_required()
def useFlag(request):  
    
    consomables = Consumable.objects.get()
    
    context = {'consomables': consomables}  
    
    return render(request, 'useFlag.html', context=context)

@login_required
def victim(request):
    
    top_victimes = TomorrowTeam.objects.annotate(nb_attaque=Count("victim_pay")).filter(nb_attaque__gt=0).order_by('-nb_attaque')[:3]
    victimes_object = TomorrowTeam.objects.filter(id__in=top_victimes).prefetch_related('user').order_by('id')
    scores = Attack.objects.filter(victim__in=victimes_object).order_by("-id")[:10]
    
    context = {'victimes': top_victimes, 'scores': scores}        
    
    return render(request, 'victim.html', context=context)   


@login_required()
def account(request):
    
    if not request.user.is_authenticated:
        return redirect('home')
    
    user_connected:TomorrowTeam = request.user.tomorrowteam
    
    attack_user = Attack.objects.filter(Q(attacker=user_connected)).order_by('-id')
    attack_infos = attack_user.aggregate(attack_reussi=Count('succesful', filter=Q(succesful=True)), attack_echoue=Count('succesful', filter=Q(succesful=False)))
    
    compteurs = 0 
    
    monthago = datetime.now() - timedelta(days=31)
    
    attaques = Attack.objects.filter(created_at__gte=monthago).values('attacker').annotate(nb_attaque=Count("attacker")).order_by('-nb_attaque')
    palmes = Attack.objects.filter(Q(attacker=user_connected)).order_by('-id')
    palmes_infos = palmes.aggregate(palme_or=Count('succesful', filter=Q(succesful=True)), palme_dej=Count('succesful', filter=Q(succesful=False)) )
    
    while attaques and palmes_infos:
        if attaques and palmes_infos == True:
            compteurs +=1
        else:
            break
    
    print(compteurs)
        
    #attack_echoue = attack_user.aggregate(Count('succesful', filter=Q(succesful=False)))
    #attack_reussi = attack_user.filter(succesful=True).count()
    #attack_echoue = attack_user.filter(succesful=False).count()
    
    context = {'attack_infos': attack_infos , 'user': user_connected, 'compteurs': compteurs}
    
    return render(request, 'account.html', context=context)

# Application client

def consomables(request):
    _consomables = [x.name for x in Consumable.objects.all()]
    return JsonResponse({'consomables': list(_consomables)})

@csrf_exempt
def attack(request):
    """
    Create a new attack. We check if password is correct
    and then retrieve cunsomables and victim of the attack
    """
    
    try: 
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'status' : 'error', 'msg' : 'Json data invalid'})
    
    # Alors l'erreur json.JSONDecodeError est seulement pour quand tu essaie de faire JSON -> Dict python
    # Une fois que tu as décodé, c'est un dictonnaire
    password_post:str = data.get('code' , None)
    consommable_post:list = data.get('action', None)
    victim_post:int = data.get('victime', None)
    
    # Ton erreur "Attack doesn't exist refere à la ligne Attack.objects.get(victim=victim_post)"
    # Donc tu dois gerer l'erreur Model.DoesNotExist
    try:
        # We check if a user exist with this password
        attaquant:TomorrowTeam = TomorrowTeam.objects.get(code=password_post)
    except TomorrowTeam.DoesNotExist:
        # If not, none of the users have this password
        return JsonResponse({'status' : 'error','msg' : 'Wrong password','attaque_sucess' : False})
    
    # Retrieve all the consumables choices by the attaquant
    print(consommable_post)
    consommables = []
    # consommables = Consumable.objects.filter(name__in=consommable_post)
    for i in consommable_post:
        cons = Consumable.objects.get(id=i)
        print('consommable', consomables)
        if cons.quantites == 0:
            return JsonResponse({'status' : 'error','msg' : 'Wrong consumables','attaque_sucess' : False})
        consommables.append(cons.name)
        
    # consommables = Consumable.objects.filter(id=consommable_post)
    # if consommables.count() == 0:
    #     return JsonResponse({'status' : 'error','msg' : 'Wrong consumables','attaque_sucess' : False})
    
    # Retrive an old attack to get a instance of the victim
    # If the victime is his first attack, he will not exist
    # Renvoie une erreur de type Attack.DoesNotExist
    #old_attack_of_victime:Attack = Attack.objects.get(victim__id=victim_post)
    #victime:TomorrowTeam = old_attack_of_victime.victim

    # Retrive the victime from the id send in the post request
    # Check that the victim exist 
    victime:TomorrowTeam = TomorrowTeam.objects.get(id=victim_post)
    
    # In this case, the attack type is 1
    # See docs for more information
    type_attaque = '1'
    
    attack = Attack.objects.create(attacker=attaquant, victim=victime, type_attack=type_attaque)

    # tester si l'attaque 1 créer bien les consomables dans la BDD 
    
    ptit_dej = PetitDej.objects.create(attaque=attack, payer=victime)
    ptit_dej.consomable.set(consommable_post)
    print(consommables)
    return JsonResponse({'attaque_sucess' : True})


def attack2(request):
    """Create new attack2 we check if the password is correct and then""" 
    """retrieve the flags if the flags exists to the attacker. """""

    try: 
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'status' : 'error', 'msg' : 'Json data invalid'})

    password_post:str = data.get('code' , None)
    flag_post:int = data.get('action', None)
    victim_post:int = data.get('victime', None)

    try:
        # We check if a user exist with this password
        attaquant:TomorrowTeam = TomorrowTeam.objects.get(code=password_post)
    except TomorrowTeam.DoesNotExist:
        # If not, none of the users have this password
        return JsonResponse({'status' : 'error','msg' : 'Wrong password','attaque_sucess' : False})
    
    return render(request, 'api/attack2')

@csrf_exempt
def login_app(request):
    
    try: 
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'status' : 'error', 'msg' : 'Json data invalid'})
    
    code_post = data.get('code', None)
    team_post = data.get('name', None)
   
    try:
        # We check if a user exist with this password
        team:TomorrowTeam = TomorrowTeam.objects.get(code=code_post, user__last_name=team_post)
    except TomorrowTeam.DoesNotExist:
        # If not, none of the users have this password
        return JsonResponse({'status' : 'error','msg' : 'Wrong password','login' : False})

    if not code_post or not team :
        return json.JSONDecodeError({'status': 'error'})
    
    return JsonResponse({'conn': team.id})