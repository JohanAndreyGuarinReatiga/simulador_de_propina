from formula.logic import calcular_propina, calcular_total_con_propina, dividir_total
import os
def design():
    opcion = 1
    while opcion: 
        print(f"""
        =============================================
          Dividir Cuenta entre Varias Personas
        =============================================""")
        total = float(input("\tIngrese el monto total de la cuenta: $"))
        porcentaje = int(input("\tIngrese el porcentaje de propina (por ejemplo: 10, 15, 20): "))
        personas = int(input("\tIngrese el número de personas: "))
        propina = calcular_propina(total, porcentaje)
        totalMasPropina = calcular_total_con_propina(total, propina)
        print(f"""
        =============================================
        La propina calculada es: ${propina}
        El total a pagar es: ${totalMasPropina}
        Monto por persona: ${dividir_total(totalMasPropina, personas)}
        =============================================""")
        opcion = int(input("\t¿Deseas calcular nuevamente? (1-S, 0-N): "))
        os.system('clear')