from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receptor(models.Model):
    class Meta:
        verbose_name = "Receptor"
        verbose_name_plural = "Receptores"
    
    receptor_nombre = models.CharField("Receptor", max_length=100)

    def __str__(self):
        return self.receptor_nombre

class Area(models.Model):
    class Meta:
        verbose_name  = "Area"
        verbose_name_plural = "Areas"
    
    area_nombre = models.CharField("Area", max_length=50)

    def __str__(self):
        return self.area_nombre

class Aseguradora(models.Model):
    class Meta:
        verbose_name = "Aseguradora"
        verbose_name_plural = "Aseguradoras"
    
    aseguradora_nombre = models.CharField("Nombre Empresa Aeguradora", max_length=255)

    def __str__(self):
        return self.aseguradora_nombre

class Empresa(models.Model):
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
    
    empresa_nombre  = models.CharField("Nombre Empresa Tomadora:", max_length=255)
    empresa_cuit    = models.CharField("CUIT:", max_length=11, blank=True, null=True)

    def __str__(self):
        return self.empresa_nombre

class Poliza(models.Model):
    CONCEPTO = (
        ("C", "Garantía de Ejecución de Contrato"),
        ("F", "Garantía de Sustitución de Fondo de Reparo"),
        ("A", "Garantía de Anticipo Financiero")
    )

    class Meta:
        constraints = [models.UniqueConstraint(fields=["poliza_numero", "poliza_aseguradora","poliza_receptor"], name="poliza-constraint")]
        verbose_name = "Póliza"
        verbose_name_plural = "Pólizas"

    poliza_fecha            = models.DateField("Fecha")
    poliza_expediente       = models.CharField("Número de Expediente", max_length=17)
    poliza_receptor         = models.ForeignKey("Receptor", on_delete=models.CASCADE)
    poliza_area             = models.ForeignKey("Area", on_delete=models.CASCADE)
    poliza_numero           = models.IntegerField("Número de Póliza")
    poliza_concepto         = models.CharField("Concepto", max_length=1, choices=CONCEPTO)
    poliza_anexo            = models.CharField("Anexo de póliza", max_length=40, blank=True, null=True)
    poliza_recibo           = models.CharField("Número de Recibo", max_length=100)
    poliza_aseguradora      = models.ForeignKey("Aseguradora", on_delete=models.CASCADE)
    poliza_tomador          = models.ForeignKey("Empresa", on_delete=models.CASCADE)
    poliza_obra_nombre      = models.TextField("Obra")
    poliza_obra_convenio    = models.CharField("Convenio", max_length=50, blank=True, null=True)
    poliza_obra_expediente  = models.CharField("Número de Expediente de la Obra", max_length=17, blank=True, null=True)
    poliza_monto_pesos      = models.DecimalField("Monto Sustituido Pesos", max_digits=12, decimal_places=2, blank=True, null=True)
    poliza_monto_uvi        = models.DecimalField("Monto Sustituido UVI", max_digits=12, decimal_places=2, blank=True, null=True)
    poliza_creador          = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    poliza_editor           = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="poliza_editor", editable=False)
    
    def get_absolute_url(self):
        return f"/polizas/update/{self.id}"