from verkiezing import Kandidaat, Stem, Kiezer, Verkiezing

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self._opleiding = opleiding

    @property
    def opleiding(self):
        return self._opleiding

    def __str__(self):
        return f"{self._naam} (Decaan: {self._opleiding})"
    
class DecaanStem(Stem):
    def __init__(self, kandidaat, opleiding):
        super().__init__(kandidaat)
        self._opleiding = opleiding

    @property
    def opleiding(self):
        return self._opleiding

    def __str__(self):
        return f"Stem op {self._kandidaat} (Opleiding: {self._opleiding})"
    
class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self._opleiding = opleiding

    @property
    def opleiding(self):
        return self._opleiding

    def stem(self, kandidaat):
        if kandidaat.opleiding == self._opleiding:
            stem = DecaanStem(kandidaat, self._opleiding)
            kandidaat.geef_stem(stem)
            print(f"{self._naam} heeft gestemd op {kandidaat} ({self._opleiding})")
        else:
            print(f"{self._naam} kan niet stemmen op {kandidaat} ({kandidaat.opleiding})")

# Test scenario
if __name__ == "__main__":
    # Create een decaan verkiezing
    verkiezing = Verkiezing("Decaan Verkiezing 2025")

    # Maak kandidaten aan
    kandidaat1 = DecaanKandidaat("Dr. De Vos", "Informatica")
    kandidaat2 = DecaanKandidaat("Dr. Janssens", "Wiskunde")
    kandidaat3 = DecaanKandidaat("Dr. Peeters", "Informatica")

    # Voeg kandidaten toe aan de verkiezing
    for kandidaat in [kandidaat1, kandidaat2, kandidaat3]:
        verkiezing.voeg_kandidaat_toe(kandidaat)

    # Maak kiezers aan
    kiezers = [
        DecaanKiezer("Prof. Van den Berg", "Informatica"),
        DecaanKiezer("Prof. Wouters", "Wiskunde"),
        DecaanKiezer("Prof. De Smet", "Informatica"),
        DecaanKiezer("Prof. Claes", "Wiskunde"),
        DecaanKiezer("Prof. Willems", "Informatica")
    ]

    # Voeg kiezers toe aan de verkiezing
    for kiezer in kiezers:
        verkiezing.voeg_kiezer_toe(kiezer)

    # Laat kiezers stemmen
    kiezers[0].stem(kandidaat1)  # Kan stemmen (Informatica)
    kiezers[1].stem(kandidaat1)  # Kan niet stemmen (Wiskunde vs Informatica)
    kiezers[2].stem(kandidaat3)  # Kan stemmen (Informatica)
    kiezers[3].stem(kandidaat2)  # Kan stemmen (Wiskunde)
    kiezers[4].stem(kandidaat1)  # Kan stemmen (Informatica)

    # Toon de resultaten
    verkiezing.toon_resultaten()