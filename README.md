# Polizador V3.0
**Aplicacion Web para Carga y Seguimiento de Pólizas de Seguro - IPDUV Chaco**

# TODO List: #

1. [ ] Add Recover & Change password functions/templates.
    - [ ] Setup Gmail Account for the app.
    - [ ] Redo login screen to match "color palette".
    - Create Templates:
        - [ ] Register
        - [ ] Recover Password
        - [ ] Change Password
2. [x] Add success_url to CreateViews.
3. [x] Make UniqueContraint for polizas.
4. [X] Add validation to input/update form.
5. [x] Setup scheduled Database backups to the cloud.

# Monthly Certification View

1. [ ] Create Model
    - [ ] Fields: Programa, ACU, Numero_de-orden, empresa, cant_viv, denominacion, localidad, n_expte, n_ant, n_cert, n_dev_ant, periodo, mes_pesos, mes_%, ante_%, acum_%, n_expte_devolucion, devolucion, monto_cobrar, uvis
# Certificador #

# TODO List: #

1. [ ] Create models
    - [x] "Certificados"
        - [ ] Add progress percentiles
    - [x] "Obra"
    - [x] "Programa"
    - [x] "Empresa"
    - [x] "Localidad"
       - [x] Add parent models "Departamento" & "Municipio"
    - [x] "Agentes"
    - [x] "Prototipos"
3. [ ] Create views for "Certificados"
    - [x] Certificados API endpoint
    - [x] ListView
    - [x] CreateView
    - [x] UpdateView
    - [x] Datatables View
4. [x] Add Admin Import/Export functions for the models.
5. [ ] -
6. [ ] Create "Prototipos" model/views
    - [x] "Prototipo" model
    - [ ] "Prototipo" CreateView
    - [ ] "Prototipo" UpdateView
7. [ ] Create "Contrato" models/views
    - [x] "Contrato" model
    - [ ] "Contrato" form to attach CreateWithInlines
    - [ ] "Contrato" CreateView
    - [ ] "Contrato" UpdateView
8. [ ] Create "Obra" model/views
    - [x] "Obra" model
    - [x] "Obra" API endpoint
    - [x] "Obra" CreateView
    - [x] "Obra" UpdateView

# TO FIX: #

- [x] Localization in Datatables Numbers
- [x] Localization in Datatables Dates
- [x] Data columns
- [x] Increase max_char in nomenclatura_catastral