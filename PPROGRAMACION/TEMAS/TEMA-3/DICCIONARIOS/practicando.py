def busqueda_especifica(alumnos: dict, identificador: str):
    for alumno, campos in alumnos.items():
        for campo, valor in campos.items():
            if campo == identificador:
                print(f"{alumno}:{valor}")


alumnos = {"Ricardo": {"edad": 22,
                       "dirrecion": "Garcia Barbon 102",
                       "telefono": "604219453",
                       "email": "ricardo03-03-02@hotmail.com",
                       "nacionalidad": "Peru"},
           "Andoni": {"edad": 34,
                      "direccion": "Ramon Nieto 134",
                      "telefono": "632458798",
                      "email": "andoni12-06-03@gmail.com",
                      "nacionalidad": "Colombia"},
           "Maria": {"edad": 27,
                     "direccion": "Av. Bolivar 123",
                    "telefono": "678912345",
                     "email": "maria01-02-05@hotmail.com",
                     "nacionalidad": "Venezuela"},
           "Pedro": {"edad": 32,
                    "direccion": "Calle 56 78",
                    "telefono": "654321987",
                    "email": "pedro12-04-04@gmail.com",
                     "nacionalidad": "España"},
           "Juan": {"edad": 29,
                    "direccion": "Carrera 90 12",
                    "telefono": "698745321",
                    "email": "juan01-01-03@hotmail.com",
                    "nacionalidad": "Chile"},
           "Sofia": {"edad": 25,
                    "direccion": "Avenida 23 45",
                    "telefono": "612345678",
                    "email": "sofia01-05-02@hotmail.com",
                    "nacionalidad": "Argentina"}}

print(busqueda_especifica(alumnos, "nacionalidad"))
print("--------------------------------")
