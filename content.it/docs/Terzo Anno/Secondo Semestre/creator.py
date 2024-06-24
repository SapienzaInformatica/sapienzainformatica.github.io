"""
Biologia Computationale
Intelligenza Artificiale
Linguaggi e Compilatori
Matematica Discreta
Modelli e Ottimizzazione
Sicurezza
Tecniche di Programmazione Funzionale e Imperativa
Verifica e Validazione di Sistemi Intelligenti
"""

to_create = [
    "Biologia Computationale",
    "Intelligenza Artificiale",
    "Linguaggi e Compilatori",
    "Matematica Discreta",
    "Modelli e Ottimizzazione",
    "Sicurezza",
    "Tecniche di Programmazione Funzionale e Imperativa",
    "Verifica e Validazione di Sistemi Intelligenti"
]

for f in to_create:
    with open(f + ".md", "w") as file:
        file.write("to-do")
