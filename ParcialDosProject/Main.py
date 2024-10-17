Salario_base_mensual = int(input("Ingrese el salario base : "))
Cargo_Empleado = input("ingrese el cargo: ")
Nivel_Desempeño = input("ingrese el nivel:")
BONIFICACION = 0.2

def calcular_precio(directivo, operativo, bonificacion):
   if directivo == 1:
       salario = Salario_base_mensual
       descripcion = "Alto"
   elif directivo == 2:
       salario = Salario_base_mensual
       descripcion = "Medio"
   elif operativo == 3:
       salario = Salario_base_mensual
       descripcion = "Bajo"
   elif operativo == 4:
       salario = Salario_base_mensual
       descripcion = "MEDIO"

   else:
       return None

   total = Salario_base_mensual
   if bonificacion == 1:
       bono = round(total + BONIFICACION)
   else:
       bono = 0

       total_recibir = round(total + bono)
       return Cargo_Empleado, salario, descripcion, bono, total_recibir







def generar_mensaje(Cargo_Empleado, salario, descripcion, bono, total_recibir):
    return (f"Cargo: {Cargo_Empleado}\n"
            f"Nivel de desempeño: {descripcion}\n"
            f"Salario Base: {salario}\n"
            f"Bonificacion: {bono}\n"
            f"Total a Recibir: {total_recibir}\n")

def validar_datos(directivo, operativo, bonificacion):
    if 1 <= directivo <= 4 and 1<= operativo <= 2 and bonificacion > 0:
        resultado = calcular_precio(directivo, operativo, bonificacion)

        Cargo_Empleado, salario, descripcion, bono, total_recibir = resultado
        mensaje = generar_mensaje(Cargo_Empleado, salario, descripcion, bono, total_recibir)
        print("------Resumen del Pago-----\n" + mensaje)
    else:
        print("Verifique las opciones Ingresadas.")

directivo = int(input("Ingrese el directivo \n1. alto\n2. medio\n3. \n"))
operativo = int (input("Ingrese el operativo\n1. bajo\n2. medio \n."))
bonificacion = int(input("Ingrese la bonificacion :"))
print("---------------------------------------------\n")


validar_datos(directivo, operativo, bonificacion)


















