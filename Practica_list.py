notas = [10,8,9,5]
print (notas)
notas.append(9)
print (notas)
print (max(notas))
notas.remove(5)
print (notas)
print (sorted(notas))
print (notas [0], notas [3])
print (notas [-1])
print (notas [-2])
print (notas [:-1])

#TUPLAS

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
print (meses [0])
print (meses [6])
print (meses [11])
print (meses [-1])

estudiante = {"nombre": "Steven", "apellido": "Ortiz", "edad": 24, "ciudad": "Cuenca"}
notas = {"nota1": 10, "nota2": 8, "nota3": 9, "nota4": 5}
print ("Estudiante: " + estudiante.get("nombre"))
print (estudiante.get("apellido"))
print (estudiante.get("edad"))
print (estudiante.get("ciudad"))
print ("NOTAS DEL ESTUDIANTE: " + str(notas ["nota1"]))

#Conjuntos

conjunto_a = {1, 5, 4, 6,8}
conjunto_b = {1, 9, 6, 5, 4}
print (conjunto_a)
print (conjunto_b)
print (conjunto_a & conjunto_b)
print (conjunto_a | conjunto_b)

##Caso practico

socio = {"cedula": "01068350705", "nombre": "Steven Josue Ortiz Lopez", "edad": "24", "activo": "True", "garante": "None", "cuentas": [{"numero": "AH-001", "tipo": "ahorro", "saldo": 2500.50}, {"numero": "AH-002", "tipo": "ahorro", "saldo": 1500.00}, {"numero": "CC-001", "tipo": "planfijo", "saldo": 500.00},{"numero": "CC-002", "tipo": "ahorro", "saldo": 1000.00}]}
print (socio.get("nombre").strip())
print (socio.get("edad"))
print (socio.get("activo"))
print (socio.get("cuentas")[0].get("numero"))

print (f"Activo: {socio.get('activo')}")
print (f"Saldos: {socio.get('cuentas')[0].get('saldo')}")