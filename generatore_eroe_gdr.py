# Script: Generatore di Eroe GDR in Python
# Descrizione: Questo script permette di creare un personaggio fantasy scegliendo razza, classe e aggiungendo oggetti all'inventario. Utilizza liste, cicli e input() per interazione utente.

import random

# --- DATI DI GIOCO ---
# Liste di opzioni per razze, classi e armi specifiche
razze = ["Umano", "Elfo", "Nano", "Orco", "Tiefling", "Halfling"]
classi = ["Guerriero", "Mago", "Ladro", "Chierico", "Ranger", "Bardo"]
armi_guerriero = ["Spadone", "Ascia da battaglia", "Martello da guerra"]
armi_mago = ["Bastone runico", "Tomo degli incantesimi", "Pugnale magico"]
armi_ladro = ["Daga affilata", "Cerbottana", "Spada corta"]
armi_chierico = ["Mazza sacra", "Croce dorata", "Bacchetta della fede"]
armi_ranger = ["Arco lungo", "Coltello da caccia", "Lancia leggera"]
armi_bardo = ["Lira incantata", "Pugnale decorato", "Bacchetta melodica"]
equip_base = ["Mantello sdrucito", "Zaino di cuoio", "Torcia", "Razioni (3 giorni)", "Corda"]

# --- FUNZIONE DI SELEZIONE ARMA ---
def scegli_arma(classe):
    """Restituisce un'arma casuale in base alla classe scelta."""
    if classe == "Guerriero":
        return random.choice(armi_guerriero)
    elif classe == "Mago":
        return random.choice(armi_mago)
    elif classe == "Ladro":
        return random.choice(armi_ladro)
    elif classe == "Chierico":
        return random.choice(armi_chierico)
    elif classe == "Ranger":
        return random.choice(armi_ranger)
    elif classe == "Bardo":
        return random.choice(armi_bardo)
    else:
        return "Bastone di legno"

# --- INIZIO GIOCO ---
nome = input("🧙‍♂️ Benvenuto, viandante. Dimmi il tuo nome: ")

# Scelta razza tra opzioni numerate
print("
Scegli la tua razza:")
for i, razza in enumerate(razze, 1):
    print(f"{i}. {razza}")
scelta_razza = int(input("Digita il numero della razza scelta: "))
razza = razze[scelta_razza - 1]

# Scelta classe tra opzioni numerate
print("
Scegli la tua classe:")
for i, classe in enumerate(classi, 1):
    print(f"{i}. {classe}")
scelta_classe = int(input("Digita il numero della classe scelta: "))
classe = classi[scelta_classe - 1]

# Generazione dell'arma iniziale e dell'equipaggiamento base
arma = scegli_arma(classe)
equipaggiamento = [arma] + equip_base.copy()

# Presentazione del personaggio creato
print(f"
⚔️ Benvenuto {nome}, {classe} {razza}!")
print("Hai ricevuto il seguente equipaggiamento iniziale:")
for item in equipaggiamento:
    print(f"- {item}")

# Ciclo per aggiunta oggetti manuale all'inventario
print("
Puoi ora aggiungere altri oggetti al tuo inventario. Scrivi 'fine' per terminare.")
while True:
    nuovo_oggetto = input("> Aggiungi oggetto: ")
    if nuovo_oggetto.lower() == "fine":
        break
    equipaggiamento.append(nuovo_oggetto)

# Riepilogo finale dell'inventario
print("
📜 Inventario finale del tuo eroe:")
for item in equipaggiamento:
    print(f"- {item}")

# Saluto finale con nome e classe
print(f"
Che gli dei proteggano il tuo cammino, {nome} il {classe}!")
