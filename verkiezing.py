class Kandidaat:
    def __init__(self, naam):
        self._naam = naam
        self._stemmen = []

    @property
    def naam(self):
        return self._naam
    
    @property
    def stemmen(self):
        return self._stemmen

    def geef_stem(self, stem):
        self._stemmen.append(stem)

    def __str__(self):
        return f"{self._naam}"
    
class Stem:
    def __init__(self, kandidaat):
        self._kandidaat = kandidaat

    @property
    def kandidaat(self):
        return self._kandidaat

    def __str__(self):
        return f"Stem op {self._kandidaat}"
    
class Kiezer:
    def __init__(self, naam):
        self._naam = naam

    @property
    def naam(self):
        return self._naam

    def stem(self, kandidaat):
        stem = Stem(kandidaat)
        kandidaat.geef_stem(stem)
        print(f"{self._naam} heeft gestemd op {kandidaat}")

class Verkiezing:
    def __init__(self, naam):
        self._naam = naam
        self._kandidaten = []
        self._kiezers = []
    
    @property
    def naam(self):
        return self._naam
    
    def voeg_kandidaat_toe(self, kandidaat):
        self._kandidaten.append(kandidaat)
    
    def voeg_kiezer_toe(self, kiezer):
        self._kiezers.append(kiezer)
    
    def toon_resultaten(self):
        print(f"\nResultaten van {self._naam}:")
        for kandidaat in self._kandidaten:
            print(f"{kandidaat}: {len(kandidaat.stemmen)} stemmen")