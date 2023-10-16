def felhantering_flyttal(inmatningMeddelande: str) -> float:
    """Tar input upprepade gånger tills användaren skriver in ett flyttal"""
    while True:
        try:
            return float(input(inmatningMeddelande)) # returnerar användarens input om det är ett flyttal, annars går koden till except-statementen
        except ValueError:
            print("Det där va inget flyttal") # ger ett felmedelande och upprepar loopen 

def felhantering_heltal(inmatningMeddelande: str) -> int:
    """Tar input upprepade gånger tills användaren skriver in ett heltal"""
    while True:
        try:
            return int(input(inmatningMeddelande)) # returnerar användarens input om det är ett heltal, annars går koden till except-statementen
        except ValueError:
            print("n måste vara ett heltal") # ger ett felmedelande och upprepar loopen 












