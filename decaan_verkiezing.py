from verkiezing import Kandidaat, Stem, Kiezer, toon_resultaten

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.__opleiding = opleiding

    @property
    def opleiding(self):
        return self.__opleiding

    def __str__(self):
        return f"{self._naam} (Decaan: {self.__opleiding})"
    
class DecaanStem(Stem):
    def __init__(self, kandidaat, opleiding):
        super().__init__(kandidaat)
        self.__opleiding = opleiding

    @property
    def opleiding(self):
        return self.__opleiding

    def __str__(self):
        return f"Stem op {self._kandidaat} (Opleiding: {self.__opleiding})"
    
class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.__opleiding = opleiding

    @property
    def opleiding(self):
        return self.__opleiding

    def stem(self, kandidaat):
        if kandidaat.opleiding == self.__opleiding:
            stem = DecaanStem(kandidaat, self.__opleiding)
            kandidaat.geef_stem(stem)
            print(f"{self._naam} heeft gestemd op {kandidaat} ({self.__opleiding})")
        else:
            print(f"{self._naam} kan niet stemmen op {kandidaat} ({kandidaat.opleiding})")

# Testscenario

    # Maak kandidaten aan
kandidaten = [
    DecaanKandidaat("Dr. De Vos", "Informatica"),
    DecaanKandidaat("Dr. Janssens", "Wiskunde"),
    DecaanKandidaat("Dr. Peeters", "Informatica")
]

# Maak kiezers aan
kiezers = [
    DecaanKiezer("Prof. Van den Berg", "Informatica"),
    DecaanKiezer("Prof. Wouters", "Wiskunde"),
    DecaanKiezer("Prof. De Smet", "Informatica"),
    DecaanKiezer("Prof. Claes", "Wiskunde"),
    DecaanKiezer("Prof. Willems", "Informatica")
]

# Laat kiezers stemmen
kiezers[0].stem(kandidaten[0])  # Kan stemmen (Informatica)
kiezers[1].stem(kandidaten[0])  # Kan niet stemmen (Wiskunde vs Informatica)
kiezers[2].stem(kandidaten[2])  # Kan stemmen (Informatica)
kiezers[3].stem(kandidaten[1])  # Kan stemmen (Wiskunde)
kiezers[4].stem(kandidaten[0])  # Kan stemmen (Informatica)

# Toon de resultaten
toon_resultaten(kandidaten)