import random

def ejercicio_3(baldosas):
    baldosas = list(baldosas)
    replacements = ["B", "N", "G"]
    for i in range(len(baldosas)): 
        if baldosas[i] == "R":
            if i > 0 and baldosas[i - 1] == "N" and "N" in replacements:
                replacements.remove("N")
            if i < len(baldosas) - 1 and baldosas[i + 1] == "N" and "N" in replacements:
                replacements.remove("N")
            if i > 0 and baldosas[i - 1] == "B" and "B" in replacements:
                replacements.remove("B")
            if i < len(baldosas) - 1 and baldosas[i + 1] == "B" and "B" in replacements:
                replacements.remove("B")
            if i > 0 and baldosas[i - 1] == "G" and "G" in replacements:
                replacements.remove("G")
            if i < len(baldosas) - 1 and baldosas[i + 1] == "G" and "G" in replacements:
                replacements.remove("G")
            baldosas[i] = random.choice(replacements)
            replacements = ["B", "N", "G"]
    print(baldosas)

ejercicio_3("RGNRRNRRRBRN")