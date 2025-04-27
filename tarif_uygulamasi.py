import json
import os

class Tarif:
    def __init__(self, ad, malzemeler, asamalar):
        self.ad = ad
        self.malzemeler = malzemeler
        self.asamalar = asamalar

    def to_dict(self):
        return {
            "ad": self.ad,
            "malzemeler": self.malzemeler,
            "asamalar": self.asamalar
        }

class TarifVeriYonetimi:
    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi
        self.tarifler = self.tarifleri_yukle()

    def tarifleri_yukle(self):
        if not os.path.exists(self.dosya_adi):
            return []

        with open(self.dosya_adi, "r", encoding="utf-8") as f:
            try:
                veriler = json.load(f)
                return [Tarif(v["ad"], v["malzemeler"], v["asamalar"]) for v in veriler]
            except json.JSONDecodeError:
                return []

    def tarif_ekle(self, tarif):
        self.tarifler.append(tarif)

    def tarifleri_kaydet(self):
        with open(self.dosya_adi, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tarifler], f, ensure_ascii=False, indent=4)
