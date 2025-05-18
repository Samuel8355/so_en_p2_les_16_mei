from abc import ABC, abstractmethod

class Kandidaat(ABC):
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

    @abstractmethod
    def __str__(self):
        pass
    
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

def toon_resultaten(kandidaten):
    print("\nVerkiezingsresultaten:")
    for kandidaat in kandidaten:
        print(f"{kandidaat}: {len(kandidaat.stemmen)} stemmen")