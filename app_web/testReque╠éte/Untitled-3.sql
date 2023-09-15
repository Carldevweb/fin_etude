[
    {'sql': 'SELECT COUNT("ptit_dej_attack"."succesful") FILTER (WHERE "ptit_dej_attack"."succesful") AS "attack_reussi", COUNT("ptit_dej_attack"."succesful") FILTER (WHERE NOT "ptit_dej_attack"."succesful") AS "attack_echoue" FROM "ptit_dej_attack" WHERE "ptit_dej_attack"."attacker_id" = 1', 
    'time': '0.000'}, 
    {'sql': 'SELECT COUNT(*) AS "__count" FROM "ptit_dej_attack" WHERE ("ptit_dej_attack"."attacker_id" = 1 AND "ptit_dej_attack"."succesful")', 
    'time': '0.000'}, 
    {'sql': 'SELECT COUNT(*) AS "__count" FROM "ptit_dej_attack" WHERE ("ptit_dej_attack"."attacker_id" = 1 AND NOT "ptit_dej_attack"."succesful")', 
    'time': '0.000'}
]