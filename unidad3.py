# Ejercicio 1

nombre = input("Ingrese su nombre: ").strip()

while not nombre.isalpha():
    nombre = input("Error. Ingrese solo letras: ").strip()

cantidad = input("Ingrese la cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Error. Ingrese una cantidad mayor que 0")

cantidad = int(cantidad)

total_sin_descuentos = 0
total_con_descuentos = 0.0

for i in range(1, cantidad + 1):
    precio_texto = input(f"\nProducto {i} - Ingrese el precio: ")

    while not precio_texto.isdigit():
        precio_texto = input("Error. Ingrese un precio entero: ")

    precio = int(precio_texto)

    descuento = input("¿Tiene descuento? (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        descuento = input("Error. Responda S o N: ").lower()

    total_sin_descuentos += precio

    if descuento == "s":
        precio_con_descuento = precio * 0.90
    else:
        precio_con_descuento = precio

    total_con_descuentos += precio_con_descuento

ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

print("\n--- RESUMEN DE COMPRA ---")
print("Cliente:", nombre)
print("Cantidad de productos:", cantidad)
print(f"Total sin descuentos: {total_sin_descuentos}")
print(f"Total con descuentos: {total_con_descuentos:.2f}")
print(f"Ahorro: {ahorro:.2f}")
print(f"Promedio por producto: {promedio:.2f}")

# Ejercicio 2

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso_concedido = False

while intentos < 3 and not acceso_concedido:
    intentos += 1
    usuario = input(f"Intento {intentos}/3 - Usuario: ")
    clave = input("Clave: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso_concedido = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")

if not acceso_concedido:
    print("Cuenta bloqueada.")

if acceso_concedido:
    opcion = ""
    while opcion != "4":
        print("\n--- MENÚ DEL CAMPUS ---")
        print("1) Ver estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mensaje motivacional")
        print("4) Salir")
        
        opcion_ingresada = input("Opción: ")
        
        if not opcion_ingresada.isdigit():
            print("Error: ingrese un número válido.")
        else:
            num_opcion = int(opcion_ingresada)
            if num_opcion < 1 or num_opcion > 4:
                print("Error: opción fuera de rango.")
            else:
                opcion = opcion_ingresada
                
                if opcion == "1":
                    print("Inscripto")
                elif opcion == "2":
                    nueva_clave = input("Nueva clave: ")
                    if len(nueva_clave) < 6:
                        print("Error: mínimo 6 caracteres.")
                    else:
                        confirmacion = input("Confirmar clave: ")
                        if nueva_clave == confirmacion:
                            clave_correcta = nueva_clave
                            print("Clave cambiada con éxito.")
                        else:
                            print("Error: Las claves no coinciden.")
                elif opcion == "3":
                    print("¡El éxito es la suma de pequeños esfuerzos repetidos día tras día!")
                elif opcion == "4":
                    print("Saliendo del sistema...")

#Ejercicio 3

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

nombre = ""
while not nombre.isalpha():
    nombre = input("Ingrese nombre del operador: ")
    if not nombre.isalpha():
        print("Error: El nombre debe contener solo letras.")

opcion = ""
while opcion != "5":
    print(f"\n--- AGENDA DE TURNOS (Operador: {nombre}) ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del dia")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion_ingresada = input("Opcion: ")
    if not opcion_ingresada.isdigit():
        print("Error: Ingrese un número valido.")
        continue
    
    num_opcion = int(opcion_ingresada)
    if num_opcion < 1 or num_opcion > 5:
        print("Error: Opcion fuera de rango.")
        continue
        
    opcion = opcion_ingresada

    if opcion == "1":
        dia = ""
        while dia != "1" and dia != "2":
            dia = input("Elegir dia (1=Lunes, 2=Martes): ")
            if dia != "1" and dia != "2":
                print("Dia no valido.")

        paciente = ""
        while not paciente.isalpha():
            paciente = input("Nombre del paciente: ")
            if not paciente.isalpha():
                print("Error: Solo letras.")

        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: El paciente ya tiene un turno asignado este dia.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado en Lunes (Turno 1).")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado en Lunes (Turno 2).")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado en Lunes (Turno 3).")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado en Lunes (Turno 4).")
            else:
                print("Lunes esta completo.")
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: El paciente ya tiene un turno asignado este dia.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado en Martes (Turno 1).")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado en Martes (Turno 2).")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado en Martes (Turno 3).")
            else:
                print("Martes esta completo.")

    elif opcion == "2":
        dia = ""
        while dia != "1" and dia != "2":
            dia = input("Elegir dia (1=Lunes, 2=Martes): ")
            if dia != "1" and dia != "2":
                print("Dia no valido.")

        paciente = ""
        while not paciente.isalpha():
            paciente = input("Nombre del paciente a cancelar: ")
            if not paciente.isalpha():
                print("Error: Solo letras.")

        encontrado = False
        if dia == "1":
            if lunes1 == paciente:
                lunes1 = ""
                encontrado = True
            elif lunes2 == paciente:
                lunes2 = ""
                encontrado = True
            elif lunes3 == paciente:
                lunes3 = ""
                encontrado = True
            elif lunes4 == paciente:
                lunes4 = ""
                encontrado = True
        else:
            if martes1 == paciente:
                martes1 = ""
                encontrado = True
            elif martes2 == paciente:
                martes2 = ""
                encontrado = True
            elif martes3 == paciente:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado exitosamente.")
        else:
            print("Paciente no encontrado.")

    elif opcion == "3":
        dia = ""
        while dia != "1" and dia != "2":
            dia = input("Ver agenda del dia (1=Lunes, 2=Martes): ")
            if dia != "1" and dia != "2":
                print("Dia no valido.")

        if dia == "1":
            print("\n--- Agenda Lunes ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print("\n--- Agenda Martes ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    elif opcion == "4":
        ocupado_lunes = (1 if lunes1 != "" else 0) + (1 if lunes2 != "" else 0) + (1 if lunes3 != "" else 0) + (1 if lunes4 != "" else 0)
        disponible_lunes = 4 - ocupado_lunes
        
        ocupado_martes = (1 if martes1 != "" else 0) + (1 if martes2 != "" else 0) + (1 if martes3 != "" else 0)
        disponible_martes = 3 - ocupado_martes

        print("\n--- RESUMEN GENERAL ---")
        print(f"Lunes: {ocupado_lunes} ocupados, {disponible_lunes} disponibles.")
        print(f"Martes: {ocupado_martes} ocupados, {disponible_martes} disponibles.")
        
        if ocupado_lunes > ocupado_martes:
            print("Dia con mas turnos: Lunes")
        elif ocupado_martes > ocupado_lunes:
            print("Dia con mas turnos: Martes")
        else:
            print("Empate en cantidad de turnos entre Lunes y Martes.")

print("Cerrando sistema de turnos...")

#Ejercicio 4 

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidos = 0

nombre_agente = ""
while not nombre_agente.isalpha():
    nombre_agente = input("Nombre del agente: ")
    if not nombre_agente.isalpha():
        print("Error: El nombre debe contener solo letras.")

print(f"\n¡Bienvenido Agente {nombre_agente}! La mision comienza.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\n[ESTADO] Energia: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    print("1. Forzar cerradura (-20 Energia, -2 Tiempo)")
    print("2. Hackear panel (-10 Energia, -3 Tiempo)")
    print("3. Descansar (+15 Energia, -1 Tiempo)")
    
    opc = input("Acción: ")
    if not opc.isdigit():
        print("Error: Ingrese un numero valido.")
        continue
    
    num_opc = int(opc)
    if num_opc < 1 or num_opc > 3:
        print("Error: Opcion invalida.")
        continue

    if num_opc == 1:
        forzar_seguidos += 1
        energia -= 20
        tiempo -= 2
        
        if forzar_seguidos == 3:
            alarma = True
            print("¡La cerradura se trabo por forzar repetidamente! ALARMA ACTIVADA.")
        else:
            riesgo = False
            if energia < 40:
                print("¡Energia baja! Riesgo de activar alarma.")
                num_riesgo = ""
                while not num_riesgo.isdigit() or int(num_riesgo) < 1 or int(num_riesgo) > 3:
                    num_riesgo = input("Elija numero de maniobra (1-3): ")
                if int(num_riesgo) == 3:
                    alarma = True
                    riesgo = True
                    print("¡Cometiste un error! ALARMA ACTIVADA.")
            
            if not riesgo:
                cerraduras_abiertas += 1
                print("¡Has forzado y abierto 1 cerradura!")

    elif num_opc == 2:
        forzar_seguidos = 0
        energia -= 10
        tiempo -= 3
        
        print("Hackeando panel...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso hackeo... Codigo parcial: {codigo_parcial}")
            
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Codigo descifrado! Se abrio 1 cerradura.")

    elif num_opc == 3:
        forzar_seguidos = 0
        energia += 15
        if energia > 100:
            energia = 100
        
        tiempo -= 1
        if alarma:
            energia -= 10
            print("Descansaste, pero el estres de la alarma encendida te quita 10 de energia extra.")
        else:
            print("Has descansado y recuperado energia.")

print("\n=== FIN DEL JUEGO ===")
if cerraduras_abiertas == 3:
    print("¡VICTORIA! Abriste la boveda a tiempo.")
elif alarma and tiempo <= 3:
    print("DERROTA. El sistema se bloqueo debido a la alarma.")
else:
    print("DERROTA. Te has quedado sin tiempo o energia.")

#Ejercicio 5

print("=== BIENVENIDO A LA ARENA ===")

nombre_gladiador = ""
while not nombre_gladiador.isalpha():
    nombre_gladiador = input("Nombre del Gladiador: ")
    if not nombre_gladiador.isalpha():
        print("Error: Solo se permiten letras.")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
dano_pesado = 15
dano_enemigo = 12
juego_activo = True

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0 and juego_activo:
    print(f"\n{nombre_gladiador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")
    
    opcion_valida = False
    opcion = 0
    
    while not opcion_valida:
        ingreso = input("Opcion: ")
        if not ingreso.isdigit():
            print("Error: Ingrese un numero valido.")
        else:
            opcion = int(ingreso)
            if opcion < 1 or opcion > 3:
                print("Error: Opcion invalida. Elija 1, 2 o 3.")
            else:
                opcion_valida = True

    if opcion == 1:
        dano_final = float(dano_pesado)
        if vida_enemigo < 20:
            dano_final = dano_final * 1.5
            print("¡Golpe Critico!")
        
        vida_enemigo -= int(dano_final)
        print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")

    elif opcion == 2:
        print(">> ¡Inicias una rafaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"Te has curado 30 HP. Te quedan {pociones} pociones.")
        else:
            print("¡No quedan pociones!")

    if vida_enemigo > 0:
        vida_jugador -= dano_enemigo
        print(f">> ¡El enemigo te ataco por {dano_enemigo} puntos!")

print("\n=== FIN DEL COMBATE ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate.")





