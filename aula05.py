import random
import math

Player = {"nome": "Player", "vida": 100, "defesa": 100}
inimigo = {"nome": "NPC das sombras", "vida": 100, "defesa": 100}
historico = {"rounds": [], "vida_player": [], "vida_npc": []}
rounds = 1

while Player["vida"] > 0 and inimigo["vida"] > 0:
    print(f"--- ROUND {1} ---")
    print(f"Player -> Vida: {Player["vida"]} Defesa: {Player["defesa"]}")
    print(f"NPC -> Vida: {inimigo["vida"]}  Defesa: {inimigo["defesa"]}")

    def calcular_dano():
        dano = random.radint(15,35)
        return dano
    def atacar(alvo, dano):
        if(alvo["defesa"] > 0):
            alvo["defesa"] = alvo["defesa"] - dano
        else:
            alvo["vida"] = alvo["vida"] - dano
    
    def escolher_acao_player():
        escolha = input("1 - atacar / 2 - defender")
        if(escolha == "1"):
            return "atacar"
        elif(escolha == "2"):
            return "defender"
        else:
            return("inválido")