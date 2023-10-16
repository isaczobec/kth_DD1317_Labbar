def felhantering_flyttal(inmatningMeddelande):
    while True:
        try:
            return float(input(inmatningMeddelande))
        except ValueError:
            print("Det där va inget flyttal")

def felhantering_heltal(inmatningMeddelande):
    while True:
        try:
            return int(input(inmatningMeddelande))
        except ValueError:
            print("n måste vara ett heltal")












