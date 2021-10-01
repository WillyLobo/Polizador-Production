# Polizador V3.0
**Aplicacion Web para Carga y Seguimiento de Pólizas de Seguro - IPDUV Chaco**

# TODO List: #

1. [ ] Add Recover & Change password functions/templates.
    - [ ] Setup Gmail Account for the app.
    - Create Templates:
        - [ ] Register
        - [ ] Recover Password
        - [ ] Change Password
2. [x] Add success_url to CreateViews.
3. [x] Make UniqueContraint for polizas.
4. [X] Add validation to input/update form.
5. [x] Setup scheduled Database backups to the cloud.

# Certificador #

# TODO List: #

1. [ ] Create models
    - [x] "Certificados"
    - [x] "Obra"
    - [x] "Programa"
    - [x] "Empresa"
    - [x] "Localidad"
       - [x] Add parent models "Departamento" & "Municipio"
    - [x] "Agentes"
    - [x] "Prototipos"
3. [ ] Create views for "Certificados"
    - [ ] Certificados API endpoint
    - [x] ListView
    - [ ] CreateView
    - [ ] UpdateView
    - [ ] Datatables View
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