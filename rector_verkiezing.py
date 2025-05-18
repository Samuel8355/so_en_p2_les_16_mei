from verkiezing import Kandidaat, Stem, Kiezer, toon_resultaten

class RectorKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self.__faculteit = faculteit

    @property
    def faculteit(self):
        return self.__faculteit

    def __str__(self):
        return f"{self._naam} (Rector: {self.__faculteit})"
    
class RectorStem(Stem):
    def __init__(self, kandidaat, faculteit):
        super().__init__(kandidaat)
        self.__faculteit = faculteit

    @property
    def faculteit(self):
        return self.__faculteit

    def __str__(self):
        return f"Stem op {self._kandidaat} (Faculteit: {self.__faculteit})"

# Test scenario
# Maak kandidaten aan
kandidaten = [
    RectorKandidaat("Prof. Dr. De Vos", "Wetenschappen"),
    RectorKandidaat("Prof. Dr. Janssens", "Letteren"),
    RectorKandidaat("Prof. Dr. Peeters", "Rechten")
]

# Maak kiezers aan
kiezers = [
    Kiezer("Dr. Van den Berg"),
    Kiezer("Dr. Wouters"),
    Kiezer("Dr. De Smet"),
    Kiezer("Dr. Claes"),
    Kiezer("Dr. Willems")
]

# Laat kiezers stemmen
kiezers[0].stem(kandidaten[0])  # Stemt op De Vos
kiezers[1].stem(kandidaten[1])  # Stemt op Janssens
kiezers[2].stem(kandidaten[0])  # Stemt op De Vos
kiezers[3].stem(kandidaten[2])  # Stemt op Peeters
kiezers[4].stem(kandidaten[0])  # Stemt op De Vos

# Toon de resultaten
toon_resultaten(kandidaten)
