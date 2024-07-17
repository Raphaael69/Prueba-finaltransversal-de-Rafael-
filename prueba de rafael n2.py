import random
trabajadores=["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]
sueldos=[]

def asignar_sueldos_alatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(len(trabajadores))]
    print("sueldos alatorios asignados:")
    for i in range(len(trabajadores)):
          print(f"{trabajadores[i]}: ${sueldos[i]:,.2f}")          
                
def clasificar_sueldo():
    global sueldos
    sueldos.sort()
    print("sueldo ordenados de menor a mayor")
    for i in range(len(trabajadores)):
        print(f"{trabajadores[i]}: {sueldos[i]:,.2f}")

def ver_estadisticas():
    global sueldos
    promedio = sum(sueldos) / len(sueldos)
    minimo = min(sueldos) 
    maximo = max(sueldos)
    minimo = min(sueldos)
    print("estadisticas de sueldos:")
    print(f"prmedio {promedio:.2f}")
    print(f"maximo {maximo:.2f}")
    print(f"minimo {minimo:.2f}")


def ver_reporte_de_sueldo():
    global sueldos
    print("Reporte de sueldos")
    for i in range(len(trabajadores)):
         print(f"{trabajadores[i]}: {sueldos[i]:,.2f}")

        
def main():
    while True:
        try:
            print("Menu de opciones")
            print('1.-Asignar sueldos alatorios')
            print('2.-Clasificar sueldos')
            print('3.-ver estadisticas')
            print('4.-reportes de sueldo')
            print('5.-salir del prigrama')
            opc=input('ingrese opciones')
            if opc==1:
                    asignar_sueldos_alatorios()
            elif opc==2:
                    if sueldos:
                     clasificar_sueldo()
            elif opc==3:
                    if sueldos:
                     ver_estadisticas()
            elif opc==4:
                    if sueldos:
                     ver_reporte_de_sueldo()
            elif opc==5:
                    break
            else:
                print('opcion invalida')
        except:
                print('error')