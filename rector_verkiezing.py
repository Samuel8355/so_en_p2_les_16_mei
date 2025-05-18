from verkiezing import Kandidaat, Stem, Kiezer, Verkiezing

class RectorKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self._faculteit = faculteit

    @property
    def faculteit(self):
        return self._faculteit

    def __str__(self):
        return f"{self._naam} (Rector: {self._faculteit})"
    
class RectorStem(Stem):
    def __init__(self, kandidaat, faculteit):
        super().__init__(kandidaat)
        self._faculteit = faculteit

    @property
    def faculteit(self):
        return self._faculteit

    def __str__(self):
        return f"Stem op {self._kandidaat} (Faculteit: {self._faculteit})"

# Test scenario
if __name__ == "__main__":
    # Create een rector verkiezing
    verkiezing = Verkiezing("Rector Verkiezing 2025")

    # Maak kandidaten aan
    kandidaat1 = RectorKandidaat("Prof. Dr. De Vos", "Wetenschappen")
    kandidaat2 = RectorKandidaat("Prof. Dr. Janssens", "Letteren")
    kandidaat3 = RectorKandidaat("Prof. Dr. Peeters", "Rechten")

    # Voeg kandidaten toe aan de verkiezing
    for kandidaat in [kandidaat1, kandidaat2, kandidaat3]:
        verkiezing.voeg_kandidaat_toe(kandidaat)

    # Maak kiezers aan
    kiezers = [
        Kiezer("Dr. Van den Berg"),
        Kiezer("Dr. Wouters"),
        Kiezer("Dr. De Smet"),
        Kiezer("Dr. Claes"),
        Kiezer("Dr. Willems")
    ]

    # Voeg kiezers toe aan de verkiezing
    for kiezer in kiezers:
        verkiezing.voeg_kiezer_toe(kiezer)

    # Laat kiezers stemmen
    kiezers[0].stem(kandidaat1)
    kiezers[1].stem(kandidaat2)
    kiezers[2].stem(kandidaat1)
    kiezers[3].stem(kandidaat3)
    kiezers[4].stem(kandidaat1)

    # Toon de resultaten
    verkiezing.toon_resultaten()
