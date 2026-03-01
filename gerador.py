import random

def gerar_milhar():
    numero = random.randint(0, 9999)
    return f"{numero:04d}"  # Garante 4 dígitos

def gerar_varios_palpites(quantidade):
    palpites = []
    for _ in range(quantidade):
        palpites.append(gerar_milhar())
    return palpites

# ====== EXECUÇÃO ======
qtd = int(input("Quantos palpites você deseja gerar? "))
resultado = gerar_varios_palpites(qtd)

print("\n🎯 Palpites Gerados:")
for p in resultado:
    print(p)
