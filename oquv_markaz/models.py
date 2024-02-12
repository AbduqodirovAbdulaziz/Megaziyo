from django.db import models


class Yonalish(models.Model):
    nomi = models.CharField(max_length=20)
    narx = models.PositiveIntegerField()

    def __str__(self):
        return f"Nomi: {self.nomi} narxi: {self.narx} ming so'm"


class Xona(models.Model):
    raqam = models.PositiveIntegerField()
    nom = models.CharField(max_length=20)

    def __str__(self):
        return f"raqam: {self.raqam} nom: {self.nom}"


class Ustoz(models.Model):
    ism = models.CharField(max_length=20)
    familiya = models.CharField(max_length=20)
    yonalish_id = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    tel_raqam = models.CharField(max_length=20)
    manzil = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.ism} {self.familiya} {self.yonalish_id}"


class Guruh(models.Model):
    nom = models.CharField(max_length=30)
    yonalish_id = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    tashkil_topgan = models.DateField()
    ustoz_id = models.ForeignKey(Ustoz, on_delete=models.CASCADE)
    xona_id = models.ForeignKey(Xona, on_delete=models.CASCADE)
    dars_vaqti = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nom} {self.yonalish_id} Ustoz: {self.ustoz_id}"


class Oquvchi(models.Model):
    ism = models.CharField(max_length=30)
    familya = models.CharField(max_length=30)
    tugilgan_sana = models.DateField()
    guruh_id = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    tel_raqam = models.CharField(max_length=20)
    manzil = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.ism} {self.familya} {self.guruh_id.nom}"


class Tolov(models.Model):
    oquvchi_id = models.ForeignKey(Oquvchi, on_delete=models.CASCADE)
    guruh_id = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    summa = models.FloatField()
    qarz = models.FloatField()
    chegirma = models.FloatField()

    def __str__(self):
        return f"O'quvchi: {self.oquvchi_id} Guruh: {self.guruh_id} Summa: {self.summa} Qarz: {self.qarz} Chegirma:{self.chegirma}"
