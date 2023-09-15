news_attaques = []
attacker = TomorrowTeam.objects.get(id=2)
victim = TomorrowTeam.objects.get(id=1)
for i in range(5_000_000):
    news_attaques.append(Attack(attacker=attacker, victim=victim, type_attack=1))

Attack.objects.bulk_create(news_attaques)