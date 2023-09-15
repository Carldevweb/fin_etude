import requests
import json

class PtitDej(object):

    BASE_API = "http://127.0.0.1:8000"

    consomables = []
    
    victime = None

    @classmethod
    def get_consomable(cls):
        """This function get from the server a list of consomable;
        Then set class variable actions with this list
        """
        res = requests.get(f"{cls.BASE_API}/api/consomables")
        res = res.json()

        cls.consomables = res.get('consomables')
        
    @classmethod
    def get_consomables_names(cls, actions: list):
        return [cls.consomables[x - 1] for x in range (len(actions))]

    @classmethod
    def attack(cls, code, action):
        
        if code == '':
            return False

        # We need to retrieve consumables name before sending it to the server
        # action = [cls.consomables]
        actions = cls.get_consomables_names(actions=action)

        data = {'code': code, 'action': action, 'victime': cls.victime} # todo replace 'action' par 'actions'

        try:
            data = json.dumps(data)
        except json.JSONDecodeError:
            return json.JSONDecodeError({'status': 'error', 'msg': 'Json data invalid'})

        res = requests.post(f"{cls.BASE_API}/api/attack", data=data)
        res = res.json()

        return True

    @classmethod
    def attack2(cls, code, attaquant):
        if code == '':
            return False

        data = {'code': code, 'vicime': cls.victime,
            'attaquant': attaquant}

        try:
            data = json.dumps(data)
        except json.JSONDecodeError:
            return json.JSONDecoder({'status': 'error', 'msg': 'Json data invalid'})

        res = requests.post(f"{cls.BASE_API}/api/attack2", data=data)
        res = res.json

        return True

    # Création de la fonction connection pour se connecter sur son compte.

    @classmethod
    def connection(cls, code, name):

        # Création d'une condition pour vérifier si l'utilisateur ne s'est pas trompé ou s'il n'a

        if code == '' or name == '':
            return False

        # Création d'une instance qui contiendra le code secret et le nom du personel.

        data = {'name': name, 'code': code}

        # Envoi des données en requête http au serveur qui va traiter les informations.

        try:
            data = json.dumps(data)
        except json.JSONDecodeError:
            return json.JSONDecodeError({'status': 'error', 'msg': 'Json data invalid'})

        # Création d'une URL qui sera envoyée au serveur

        res = requests.post(f"{cls.BASE_API}/api/login", data=data)

        try:
            res = res.json()
        except json.JSONDecodeError:
            return json.JSONDecodeError({'status': 'error', 'msg': 'Json data invalid'})

        # Check if server response is correct
        if res.get('conn'):
            cls.victime = res.get('conn')
            
            with open('auth.json', 'w') as auth:
                data = {}
                data['victime'] = cls.victime
                auth.seek(0)
                auth.write(json.dumps(data))
                auth.truncate()

            return True

        return False

    @classmethod
    def check_auth(cls):

        if cls.victime:
            return True

        return False

    @classmethod
    def load_auth(cls):
        """load json file auth.json to know if user is connected
        """
        with open('auth.json') as auth:
            data = json.load(auth)
            cls.victime = data["victime"]

            return data

        
      
      