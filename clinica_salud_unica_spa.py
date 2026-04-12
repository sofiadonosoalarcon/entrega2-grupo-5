import os

def clinica_salud_unica_spa():
    MAX = 100
    VALOR_UF_HOY = 39841
    COSTO_CONSULTA_UF = 0.5

    consultas = []
    insumos = []

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("--- SISTEMA CLÍNICA SALUD ÚNICA SPA ---")
        print("(1) Registrar Atención Médica (Nueva Consulta)")
        print("(2) Registrar Insumos y Proveedores")
        print("(3) Consultar Historial Clínico por Paciente")
        print("(4) Consultar Montos Individuales (Médico/Paciente)")
        print("(5) Reporte General y Listados")
        print("(0) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if len(consultas) < MAX:
                print("\n--- REGISTRO DE ATENCIÓN ---")
                nom_medico = input("Nombre Médico: ")
                run_medico = input("RUN Médico: ")
                nom_paciente = input("Nombre Paciente: ")
                run_paciente = input("RUN Paciente: ")
                ant_hered = input("Antecedentes Hereditarios: ")
                diag = input("Síntomas y Diagnóstico: ")
                receta = input("Receta Médica emitida: ") 

                atencion = {
                    "medico": nom_medico,
                    "run_medico": run_medico,
                    "paciente": nom_paciente,
                    "run_paciente": run_paciente,
                    "antecedentes": ant_hered,
                    "diagnostico": diag,
                    "receta": receta,
                    "costo_uf": COSTO_CONSULTA_UF
                }
                consultas.append(atencion)
                print(f"\nAtención registrada. Costo: {COSTO_CONSULTA_UF} UF")
            else:
                print("Error: Capacidad llena.")
            input("\nPresione Enter...")

        elif opcion == "2":
            if len(insumos) < MAX:
                nombre = input("Nombre del Insumo: ")
                proveedor = input("Proveedor: ")  
                try:
                    costo = float(input("Costo individual (CLP): "))
                    insumos.append({"nombre": nombre, "proveedor": proveedor, "costo": costo})
                    print("Insumo y proveedor registrados.")
                except ValueError:
                    print("Error: Costo no válido.")
            input("\nPresione Enter...")

        elif opcion == "3":
            run_busca = input("\nIngrese RUN del paciente para ver historial: ")
            encontrado = False
            print(f"\n--- HISTORIAL CLÍNICO: {run_busca} ---")
            for c in consultas:
                if c['run_paciente'] == run_busca:
                    print(f"Médico: {c['medico']} | Diagnóstico: {c['diagnostico']}")
                    print(f"Receta: {c['receta']}")
                    print(f"Antecedentes: {c['antecedentes']}")
                    print("-" * 30)
                    encontrado = True
            if not encontrado:
                print("No se encontraron registros para este RUN.")
            input("\nPresione Enter...")

        elif opcion == "4":
            print("\n(A) Recaudación por Médico | (B) Gastos por Paciente")
            sub = input("Seleccione: ").upper()
            run_busca = input("Ingrese el RUN correspondiente: ")

            total_uf = 0
            conteo = 0

            for c in consultas:
                if (sub == "A" and c['run_medico'] == run_busca) or \
                        (sub == "B" and c['run_paciente'] == run_busca):
                    total_uf += c['costo_uf']
                    conteo += 1

            print(f"\nResultados para {run_busca}:")
            print(f"Cantidad de consultas: {conteo}")
            print(f"Monto total: {total_uf} UF (${total_uf * VALOR_UF_HOY:,.0f} CLP)")
            input("\nPresione Enter...")

        elif opcion == "5":
            total_recaudado_uf = len(consultas) * COSTO_CONSULTA_UF
            total_insumos = sum(ins['costo'] for ins in insumos)

            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== REPORTE GLOBAL DE OPERACIONES ===")
            print(f"Total de Atenciones: {len(consultas)}")
            print(f"Recaudación Global: {total_recaudado_uf} UF (${total_recaudado_uf * VALOR_UF_HOY:,.0f} CLP)")
            print(f"Inversión en Insumos: ${total_insumos:,.0f}")

            print("\n--- LISTADO DE PROVEEDORES E INSUMOS ---")
            for i in insumos:
                print(f"Insumo: {i['nombre']} | Proveedor: {i['proveedor']} | ${i['costo']:,.0f}")

            input("\nPresione Enter para volver...")

        elif opcion == "0":
            break
