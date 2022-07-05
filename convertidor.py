from carga import models

obras = models.Obra.objects.all()
contadorobras = 0

for i in obras:
    if i.obra_contrato_provincia_pesos == None:
        i.obra_contrato_provincia_pesos = 0
        contadorobras += 1
        print(i.id, " - Contrato Provincia is None, Setting it to 0")
    else:
        print(i.id, " - Skipping")
    if i.obra_contrato_provincia_uvi == None:
        i.obra_contrato_provincia_uvi = 0
        contadorobras += 1
        print(i.id, " - Contrato Provincia UVI is None, Setting it to 0")
    else:
        print(i.id, " - Skipping")
    if i.obra_contrato_nacion_uvi == None:
        i.obra_contrato_nacion_uvi = 0
        contadorobras += 1
        print(i.id, " - Contrato Nacion UVI is None, Setting it to 0")
    else:
        print(i.id, " - Skipping")
    if i.obra_contrato_nacion_pesos == None:
        i.obra_contrato_nacion_pesos = 0
        contadorobras += 1
        print(i.id, " - Contrato Nacion Pesos is None, Setting it to 0")
    else:
        print(i.id, " - Skipping")
    if i.obra_contrato_terceros_uvi == None:
        i.obra_contrato_terceros_uvi = 0
        contadorobras += 1
        print(i.id, " - Contrato Terceros UVI is None, Setting it to 0")
    else:
        print(i.id, " - Skipping")
    if i.obra_contrato_terceros_pesos == None:
        i.obra_contrato_terceros_pesos = 0
        contadorobras += 1
        print(i.id, " - Contrato Terceros is None, Setting it to 0")
    else:
        print(i.id, " - Skipping")
    print("Nacion:",i.obra_contrato_nacion_uvi, "- Terceros:", i.obra_contrato_terceros_uvi, "- Provincia:", i.obra_contrato_provincia_pesos)
    i.save()

for i in obras:
    if i.obra_contrato_provincia_pesos == None and i.obra_contrato_nacion_pesos == None:
        pass
    else:
        if i.obra_contrato_provincia_pesos != None and i.obra_contrato_nacion_pesos != None:
            i.obra_contrato_total_pesos = i.obra_contrato_provincia_pesos + i.obra_contrato_nacion_pesos
            i.obra_contrato_total_uvi = i.obra_contrato_provincia_uvi + i.obra_contrato_nacion_uvi
            contadorobras += 1
            i.save()
            print ("--------------")
            print (i.id, "-", i.obra_nombre, "- Total Contrato Pesos set to:", i.obra_contrato_provincia_pesos + i.obra_contrato_nacion_pesos)
            print (i.id, "-", i.obra_nombre, "- Total Contrato UVI set to:", i.obra_contrato_provincia_uvi + i.obra_contrato_nacion_uvi)
            print ("--------------")
        elif i.obra_contrato_provincia_pesos != None and i.obra_contrato_nacion_pesos == None:
            i.obra_contrato_total_pesos     = i.obra_contrato_provincia_pesos
            i.obra_contrato_total_uvi       = i.obra_contrato_provincia_uvi
            contadorobras += 1
            i.save()
            print ("--------------")
            print (i.id, "-", i.obra_nombre, "- Total Contrato Pesos set to:", i.obra_contrato_provincia_pesos)
            print (i.id, "-", i.obra_nombre, "- Total Contrato UVI set to:", i.obra_contrato_provincia_uvi)
            print ("--------------")
        elif i.obra_contrato_nacion_pesos != None and i.obra_contrato_provincia_pesos == None:
            i.obra_contrato_total_pesos     = i.obra_contrato_nacion_pesos
            i.obra_contrato_total_uvi       = i.obra_contrato_nacion_uvi
            contadorobras += 1
            i.save()
            print ("--------------")
            print (i.id, "-", i.obra_nombre, "- Total Contrato Pesos set to:", i.obra_contrato_nacion_pesos)
            print (i.id, "-", i.obra_nombre, "- Total Contrato UVI set to:", i.obra_contrato_nacion_uvi)
            print ("--------------")
print("************************************")
print ("Modificados ", contadorobras, "Registros")
print("************************************")

certificados = models.Certificado.objects.all()
contadorcertificados = 0
for i in certificados:
    if i.certificado_periodo == "Agosto/21":
        print ("-------------------------")
        print ("Se encontró período", i.certificado_periodo, "en certificado_periodo.")
        i.certificado_fecha = "2021-08-01"
        print ("Certificado Fecha establecido en:", i.certificado_fecha)
        contadorcertificados += 1
        i.save()
    elif i.certificado_periodo == "Septiembre/21":
        print ("-------------------------")
        print ("Se encontró período", i.certificado_periodo, "en certificado_periodo.")
        i.certificado_fecha = "2021-09-01"
        print ("Certificado Fecha establecido en:", i.certificado_fecha)
        contadorcertificados += 1
        i.save()
    elif i.certificado_periodo == "Octubre/21":
        print ("-------------------------")
        print ("Se encontró período", i.certificado_periodo, "en certificado_periodo.")
        i.certificado_fecha = "2021-10-01"
        print ("Certificado Fecha establecido en:", i.certificado_fecha)
        contadorcertificados += 1
        i.save()
    elif i.certificado_periodo == "Noviembre/21":
        print ("-------------------------")
        print ("Se encontró período", i.certificado_periodo, "en certificado_periodo.")
        i.certificado_fecha = "2021-11-01"
        print ("Certificado Fecha establecido en:", i.certificado_fecha)
        contadorcertificados += 1
        i.save()
    elif i.certificado_periodo == "Diciembre/21":
        print ("-------------------------")
        print ("Se encontró período", i.certificado_periodo, "en certificado_periodo.")
        i.certificado_fecha = "2021-12-01"
        print ("Certificado Fecha establecido en:", i.certificado_fecha)
        contadorcertificados += 1
        i.save()
    elif i.certificado_periodo == "Enero/22":
        print ("-------------------------")
        print ("Se encontró período", i.certificado_periodo, "en certificado_periodo.")
        i.certificado_fecha = "2022-01-01"
        print ("Certificado Fecha establecido en:", i.certificado_fecha)
        contadorcertificados += 1
        i.save()
    elif i.certificado_periodo == "Febrero/22":
        print ("-------------------------")
        print ("Se encontró período", i.certificado_periodo, "en certificado_periodo.")
        i.certificado_fecha = "2022-02-01"
        print ("Certificado Fecha establecido en:", i.certificado_fecha)
        contadorcertificados += 1
        i.save()
    elif i.certificado_periodo == "FEBRERO/22":
        print ("-------------------------")
        print ("Se encontró período", i.certificado_periodo, "en certificado_periodo.")
        i.certificado_fecha = "2022-02-01"
        print ("Certificado Fecha establecido en:", i.certificado_fecha)
        contadorcertificados += 1
        i.save()
    elif i.certificado_periodo == "Marzo/22":
        print ("-------------------------")
        print ("Se encontró período", i.certificado_periodo, "en certificado_periodo.")
        i.certificado_fecha = "2022-03-01"
        print ("Certificado Fecha establecido en:", i.certificado_fecha)
        contadorcertificados += 1
        i.save()
    elif i.certificado_periodo == "Abril/22":
        print ("-------------------------")
        print ("Se encontró período", i.certificado_periodo, "en certificado_periodo.")
        i.certificado_fecha = "2022-04-01"
        print ("Certificado Fecha establecido en:", i.certificado_fecha)
        contadorcertificados += 1
        i.save()
    elif i.certificado_periodo == "Mayo/2022":
        print ("-------------------------")
        print ("Se encontró período", i.certificado_periodo, "en certificado_periodo.")
        i.certificado_fecha = "2022-05-01"
        print ("Certificado Fecha establecido en:", i.certificado_fecha)
        contadorcertificados += 1
        i.save()
    elif i.certificado_periodo == "Junio/22":
        print ("-------------------------")
        print ("Se encontró período", i.certificado_periodo, "en certificado_periodo.")
        i.certificado_fecha = "2022-06-01"
        print ("Certificado Fecha establecido en:", i.certificado_fecha)
        contadorcertificados += 1
        i.save()

print("************************************")
print ("Modificados ", contadorcertificados, "Registros")
print("************************************")