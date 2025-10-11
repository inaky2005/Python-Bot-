# Ayuda me quiero morir y no aprendo aun a programar bien
respuesta = input("¿Eres Carlos? (sí/no): ").strip().lower()

if respuesta == "sí":
    si_tu_nombre_es_Carlos = True
else:
    si_tu_nombre_es_Carlos = False

if si_tu_nombre_es_Carlos:
    print("Hola Carlos, soy Iñaky")

no = not si_tu_nombre_es_Carlos
if not no:
    print("¿Quién eres?")

nombre = input("Escribe tu nombre: ").strip()
print(f"Hola {nombre}, soy Iñaky")