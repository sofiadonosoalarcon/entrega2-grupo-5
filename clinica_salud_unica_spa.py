import os


def clinica_salud_unica_spa():
    MAX = 100
    VALOR_UF_HOY = 39841
    COSTO_CONSULTA_UF = 0.5

    pacientes = []
    insumos = []

    recauda_insumos_global = 0.0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("--- CLÍNICA SALUD ÚNICA SPA ---")
        print("(1) Registrar Consulta Médica")
        print("(2) Registrar Insumos")
        print("(3) Reporte General (Listados)")
        print("(0) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if len(pacientes) < MAX:
                print("\n--- DATOS DEL MÉDICO ---")
                nom_medico = input("Nombre Médico: ")
                run_medico = input("RUN Médico: ")

                print("\n--- DATOS DEL PACIENTE ---")
                nom_paciente = input("Nombre Paciente: ")
                run_paciente = input("RUN Paciente: ")
                ant_hered = input("Antecedentes Hereditarios: ")
                diag = input("Síntomas y Diagnóstico: ")

                # Guardamos la consulta como un diccionario
                consulta = {
                    "medico": nom_medico,
                    "run_medico": run_medico,
                    "paciente": nom_paciente,
                    "run_paciente": run_paciente,
                    "antecedentes": ant_hered,
                    "diagnostico": diag
                }
                pacientes.append(consulta)
                print(f"\nRegistro exitoso. Costo: {COSTO_CONSULTA_UF} UF")
            else:
                print("Error: Capacidad de registros llena.")
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            if len(insumos) < MAX:
                nombre_insumo = input("Nombre del Insumo: ")
                try:
                    costo_insumo = float(input("Costo individual (CLP): "))
                    insumos.append({"nombre": nombre_insumo, "costo": costo_insumo})
                    recauda_insumos_global += costo_insumo
                    print("Insumo registrado correctamente.")
                except ValueError:
                    print("Error: Ingrese un valor numérico válido para el costo.")
            else:
                print("Error: No se pueden registrar más insumos.")
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            cant_consultas = len(pacientes)
            recauda_uf_global = cant_consultas * COSTO_CONSULTA_UF
            recauda_clp_global = recauda_uf_global * VALOR_UF_HOY

            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== REPORTE DE ATENCIONES ===")
            print(f"Total Consultas: {cant_consultas}")
            print(f"Total Recaudado: {recauda_uf_global} UF (${recauda_clp_global:,.0f} CLP)")
            print(f"Gasto en Insumos: ${recauda_insumos_global:,.0f}")
            print("-" * 43)

            print("LISTADO DE PACIENTES ATENDIDOS:")
            for idx, p in enumerate(pacientes, 1):
                print(f"{idx}. {p['paciente']} | Médico: {p['medico']} | Diag: {p['diagnostico']}")

            print("-" * 43)
            print("LISTADO DE INSUMOS:")
            for idx, ins in enumerate(insumos, 1):
                print(f"{idx}. {ins['nombre']} - ${ins['costo']:,.0f}")

            input("\nPresione Enter para volver al menú...")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
            input("\nPresione Enter para intentar de nuevo...")