from datetime import datetime

nom = input("Quel est votre nom ? : ")
age = int(input("Votre âge actuel ? : "))
ageLast = int(input("Rajouter quelque années à votre âge : "))

ageResult = age + ageLast

print(f"Bonjour {nom}, Vous avez actuellement {age} ans. Dans {ageLast} ans, vous aurez {ageResult} ans.")

futurAge = int(input("Si on ajoute encore quelques années de plus : "))

finalAge = futurAge + ageResult

if finalAge <= 100 :
    print(f"Vous auriez {finalAge} ans")
elif finalAge == 110:
    print(f"Bravo à vous si vous parvenez à atteindre {finalAge} ans")
elif finalAge > 110:
    print(f"Il n'est pas encore possible d'atteindre {finalAge} ans.")