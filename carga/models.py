from django.db import models
from django.core.validators import MinValueValidator

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
    
    empresa_nombre      = models.CharField("Nombre Empresa Tomadora:", max_length=255)
    empresa_cuit        = models.CharField("CUIT:", max_length=11, blank=True, null=True)
    empresa_titular     = models.CharField("Titular de la Empresa", max_length=140, blank=True, null=True)
    empresa_direccion   = models.CharField("Dirección de la Empresa", max_length=255, blank=True, null=True)
	

    def __str__(self):
        return self.empresa_nombre

class Poliza(models.Model):
    CONCEPTO = (
        ("C", "Garantía de Ejecución de Contrato"),
        ("F", "Garantía de Sustitución de Fondo de Reparo"),
        ("A", "Garantía de Anticipo Financiero")
    )

    class Meta:
        constraints = [models.UniqueConstraint(fields=["poliza_fecha", "poliza_numero", "poliza_aseguradora","poliza_receptor"], name="poliza-constraint")]
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
    poliza_monto_pesos      = models.DecimalField("Monto Sustituido Pesos", max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    poliza_monto_uvi        = models.DecimalField("Monto Sustituido UVI", max_digits=12, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)])
    
    def get_absolute_url(self):
        return f"/polizas/update/{self.id}"

class Programa(models.Model):
    class Meta:
        verbose_name = "Progrma"
        verbose_name_plural = "Programas"
    
    programa_nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.programa_nombre

class Departamento(models.Model):
	class Meta:
		ordering			= ["departamento_nombre"]
		verbose_name_plural = "Departamentos"

	id					= models.IntegerField(unique=True, primary_key=True)
	departamento_nombre = models.TextField("Nombre Departamento", unique=True)
	
	def __str__(self):
		return self.departamento_nombre

class Localidad(models.Model):
	class Meta:
		ordering			= ["localidad_nombre"]
		verbose_name_plural = "Localidades"

	localidad_nombre		= models.TextField("Nombre Localidad", unique=True)
	id                      = models.IntegerField(unique=True, primary_key=True) 
	localidad_centroide_lat	= models.DecimalField(max_digits=15, decimal_places=13,blank=True, null=True)
	localidad_centroide_lon	= models.DecimalField(max_digits=15, decimal_places=13,blank=True, null=True)
	localidad_funcion       = models.CharField(max_length=40,blank=True, null=True)
	localidad_departamento	= models.ForeignKey("Departamento", on_delete=models.RESTRICT)
	localidad_municipio     = models.ForeignKey("Municipio", on_delete=models.CASCADE)

	def __str__(self):
		return self.localidad_nombre
		# return "{} - Departamento {}".format(self.localidad_nombre, self.localidad_departamento)

class Municipio(models.Model):
	class Meta:
		ordering 			= ["municipio_nombre"]
		verbose_name_plural = "Municipios"
	
	municipio_nombre        = models.CharField(max_length=40, unique=True)
	id                      = models.IntegerField(unique=True, primary_key=True)
	municipio_departamento  = models.ForeignKey("Departamento", on_delete=models.CASCADE)
	
	def __str__(self):
		return self.municipio_nombre


class Obra(models.Model):
    COMPULSA = (
        ("L", "Licitación Pública"),
        ("P", "Licitación Privada"),
        ("C", "Concurso de Precios"),
        ("D", "Contratación Directa")
    )
    
    class Meta:
        verbose_name = "Obra"
        verbose_name_plural = "Obras"
    
    obra_nombre			    = models.TextField("Nombre de la Obra tal como figura en el contrato")
    obra_soluciones		    = models.DecimalField("Cantidad de soluciones", max_digits=4, decimal_places=0, null=True, blank=True)
    obra_empresa		    = models.ForeignKey("Empresa", on_delete=models.CASCADE, verbose_name="Empresa")
    obra_localidad		    = models.ForeignKey("Localidad", on_delete=models.CASCADE)
    obra_grupo              = models.CharField("Grupo", max_length=4, blank=True, null=True)
    obra_plazo              = models.CharField("Plazo de Ejecución", max_length=10, blank=True, null=True)
    obra_programa		    = models.ForeignKey("Programa", on_delete=models.CASCADE)
    obra_convenio		    = models.CharField("Convenio/ACU", max_length=60, blank=True, null=True)
    obra_expediente 	    = models.CharField("Expediente", max_length=17)
    obra_resolucion         = models.CharField("Resolución de Adjudicación", max_length=15, blank=True, null=True)
    obra_licitacion_tipo    = models.CharField("Compulsa", max_length=1, choices=COMPULSA, blank=True, null=True)
    obra_licitacion_numero  = models.DecimalField("Número de Licitación", max_digits=3, decimal_places=0, blank=True, null=True)
    obra_licitacion_ano     = models.DecimalField("Año de Licitación", max_digits=4, decimal_places=0, blank=True, null=True)
    obra_nomenclatura       = models.CharField("Nomenclatura Catastral", max_length=100, blank=True, null=True)  
    obra_nomenclatura_plano = models.CharField("Número de Plano", max_length=10, blank=True, null=True)
    obra_fecha_entrega      = models.DateField("Fecha de Entrega de la Obra", blank=True, null=True)
    obra_fecha_contrato     = models.DateField("Fecha de Firma de Contrato", blank=True, null=True)
    obra_expediente_costo   = models.CharField("Expediente de Costos", max_length=17, blank=True, null=True)
    obra_inspector          = models.ManyToManyField("Agente", related_name="obra_inspector")
    # obra_nomenclatura_secc
    # obra_nomenclatura_ch
    # obra_nomenclatura_qta
    # obra_nomenclatura_fr
    # obra_nomenclatura_mz
    # obra_nomenclatura_pc
    # obra_prototipos
        # cantidad del prototipo
        # superficie m2
        # incremento por infraestructura
        # uvi x m2
    
    def __str__(self):
        return f"{self.obra_nombre} - {self.obra_localidad}"

class Agente(models.Model):
	class Meta:
		verbose_name_plural = "Agentes"
	
	PROFESION = (
		("A", "Arquitecto"),
		("IC", "Ingeniero Civil"),
		("IE", "Ingeniero Electromecánico"),
		("MO", "Maestro Mayor de Obras")
	)

	agente_nombre 			= models.CharField("Nombre/s:", max_length=60)
	agente_apellido			= models.CharField("Apellido/s:", max_length=60)
	agente_dni				= models.DecimalField("DNI:", max_digits=9, decimal_places=0, blank=True, null=True, validators=[MinValueValidator(0)])
	agente_telefono 		= models.CharField("Telefono:", max_length=20, blank=True, null=True)
	agente_email 			= models.EmailField("Email:", blank=True,null=True)
	agente_profesion		= models.CharField("Profesion", max_length=2, choices=PROFESION, default=None, blank=True, null=True)
	agente_matricula		= models.CharField("Matricula Profesional", max_length=10, blank=True, null=True)
	
	def __str__(self):
		return f"{self.agente_nombre} {self.agente_apellido}"
	
class Certificado(models.Model):
    
    class Meta:
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"

    certificado_programa            = models.ForeignKey("Programa", on_delete=models.CASCADE)
    certificado_obra                = models.ForeignKey("Obra", on_delete=models.CASCADE)
    certificado_localidad           = models.ForeignKey("Localidad", on_delete=models.CASCADE)
    certificado_empresa             = models.ForeignKey("Empresa", on_delete=models.CASCADE)
    certificado_rubro_obra          = models.DecimalField("Certificado de Obra N°", max_digits=3, decimal_places=0, null=True, blank=True)
    certificado_rubro_anticipo      = models.DecimalField("Certificado de Anticipo N°", max_digits=3, decimal_places=0, null=True, blank=True)
    certificado_rubro_devanticipo   = models.DecimalField("Certificado de Devolución de Anticipo N°", max_digits=3, decimal_places=0, null=True, blank=True)
    certificado_rubro_691           = models.DecimalField("Certificado de Redeterminación Decreto N°691/16 N°", max_digits=3, decimal_places=0, null=True, blank=True)
    certificado_rubro_Terreno       = models.DecimalField("Certificado de Terreno | Cuota N°", max_digits=3, decimal_places=0, null=True, blank=True)
    certificado_rubro_recomposicion = models.DecimalField("Certificado de Recomposición Período Anterior N°", max_digits=3, decimal_places=0, null=True, blank=True)
    certificado_expediente          = models.CharField("Número de Expediente", max_length=17)
    certificado_fecha               = models.DateField("Fecha de Salida")
    certificado_monto_pesos         = models.DecimalField("Monto en Pesos", max_digits=12, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])
    certificado_monto_pesos         = models.DecimalField("Monto en UVI", max_digits=12, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])