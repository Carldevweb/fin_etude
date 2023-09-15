import rumps
from ptit_dej_data import PtitDej
rumps.debug_mode(True)

class petitDej(rumps.App):

    @rumps.clicked("Fais toi offrir un p'tit dej")
    def button(self, _):
        connect = PtitDej.check_auth()

        if connect == False:
            window = rumps.Window("")
            window.message = ("veuillez vous connecter")
            window.run()
            return None

        window = rumps.Window("Choisis tes offrandes", ok='Aucun')
        window.title = (
            "Aide ton collègue à mieux respecter les consignes de sécurité")
        window.dimensions = (400, 400)

        PtitDej.get_consomable()
        consomables = PtitDej.consomables
        window.add_buttons(consomables)
        
        actions = []

        for _ in range(2):
            res = window.run()
            actions.append(res)
        print(PtitDej.get_consomable)
        
        window = rumps.Window("Code secret")
        window.title = ("fais vite avant qu'il revienne !!")
        window.message = ("entre ton code secret")
        window.default_text = ("")
        window.dimensions = (400, 400)

        r = False
        for _ in range(2):
            code_res = window.run()
            print('code res', code_res)

            r = PtitDej.attack(code=code_res.text, action=[
                               action_res.clicked -2 + 10 for action_res in actions])

            if r:
                break
            else:
                # Se moquer de la personne si au bout de deux essaie elle na pas compris quìl faut rentrer son mot de passe
                window = rumps.Window("")
                window.title = ("Le mot de passe n'est pas bon")
                window.message = ("")
                window.default_text = (
                    "Il semblerait que tu as oublié ton code secret, quel dommage, tu feras mieux la prochaine fois ")
                window.dimensions = (400, 400)
                window.message = ("")

    @rumps.clicked("création d'un flag")
    def attaque2(self, _):
        window = rumps.Window("création d'un drapeau",
                              ok="envoi de la création du drapeau")
        window.title = ("entre ton code secret")
        window.default_text = ("")
        window.dimensions = (400, 400)

        code_res = window.run()

        PtitDej.attack2(code=code_res.text)

    @rumps.clicked("Capture the flags !!")
    def attaque3(self, _):
        window = rumps.Window(
            "Si drapeaux il y a, des petits déj au pluriel tu aura", ok="récupère les drapeaux")
        window.title = ("entre ton code secret")
        window.default_text = ("")
        window.dimensions = (400, 400)

        r = False

        code_res = window.run()

        r = PtitDej.attack2(code=code_res.text)

    @rumps.clicked("authentification")
    def auth(self, _):
        window = rumps.Window("Entre ton nom de compte")
        window.title = ("Bienvenue dans l'authentification")
        window.message = ("Entre ton nom")
        window.default_text = ("")
        window.dimensions = (400, 400)

        r = False

        data = {}
        auth_res = window.run()

        data['name'] = auth_res.text

        window = rumps.Window("Entre ton code secret")
        window.message = ("Entre ton code secret ")
        window.default_text = ("")
        window.dimensions = (400, 400)

        code_res = window.run()
        data['code'] = code_res.text

        r = PtitDej.connection(**data)

        if r:
            window.message = ("Vous êtes connecté")
        else:
            window.message = ("Vous vous êtes trompé de code")
        window.run()

if __name__ == "__main__":
    PtitDej.load_auth()
    petitDej("Tomorrow p'tit dej").run()