# 1. Liste mit Früchten erstellen
fruechte = ["Apfel", "Banane", "Kirsche", "Orange", "Traube"]

# 2. Kiwi in die Liste hinzufügen
fruechte.append("Kiwi")

# 3. Mango in die Index Stelle 1 in der Liste einfügen
fruechte.insert(1, "Mango")

# 4. Letztes Element der Liste entfernen
fruechte.pop()

# 5. Überprüft ob Banane in der Liste ist und entfernt sie dann
if "Banane" in fruechte:
    fruechte.remove("Banane")

# 6. Dreht die Liste um
fruechte.reverse()

# 7. Gibt die Länge der Liste aus
print(f"Länge der Liste: {len(fruechte)}")

# 8. Erstellt eine Kopie der Liste und gibt deren Speicheradressen aus.
fruechte_copy = fruechte.copy()

print(f"Originale Liste: {fruechte} | Speicheradresse: {id(fruechte)}")
print(f"Kopierte Liste: {fruechte_copy} | Speicheradresse: {id(fruechte_copy)}")
