from formula.logic import calcular_propina, calcular_total_con_propina
import os

def design():
    opcion = 1 
    while opcion:
        print(f""" 
        =============================================
                    Cálculo de Propina
        =============================================""")
        total = float((input("\tIngrese el monto total de la cuenta: $")))
        porcentaje = int((input("\tIngrese el porcentaje de propina (por ejemplo: 10, 15, 20): ")))
        propina = calcular_propina(total, porcentaje)
        print(f""" 
        =============================================
        La propina calculada es: ${propina}
        El total a pagar es: ${calcular_total_con_propina(total, propina)}
        =============================================
        """)
        opcion = int(input("        ¿Deseas calcular nuevamente? (1-S, 0 -N): "))
        os.system('clear')