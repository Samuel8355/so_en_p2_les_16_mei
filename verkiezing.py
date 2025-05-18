class Kandidaat:
    def __init__(self, naam):
        self._naam = naam
        self._stemmen = []

    @property
    def naam(self):
        return self._naam
    
    @property
    def aantal_stemmen(self):
        return len(self._stemmen)

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
        self._heeft_gestemd = False

    @property
    def naam(self):
        return self._naam
    
    @property
    def heeft_gestemd(self):
        return self._heeft_gestemd

    def stem(self, kandidaat):
        if self._heeft_gestemd:
            raise ValueError(f"{self._naam} heeft al gestemd!")
        stem = Stem(kandidaat)
        kandidaat.geef_stem(stem)
        self._heeft_gestemd = True
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
        if kandidaat not in self._kandidaten:
            self._kandidaten.append(kandidaat)
    
    def voeg_kiezer_toe(self, kiezer):
        if kiezer not in self._kiezers:
            self._kiezers.append(kiezer)
    
    def toon_resultaten(self):
        print(f"\nResultaten van {self._naam}:")
        gesorteerde_kandidaten = sorted(self._kandidaten, key=lambda k: k.aantal_stemmen, reverse=True)
        for kandidaat in gesorteerde_kandidaten:
            print(f"{kandidaat}: {kandidaat.aantal_stemmen} stemmen")