import api.data as api
import ui.user as ui
import pandas as pd




def main():
    department, records = ui.get_inputs()
    client = api.get_client()
    if ui.test_valid_data(department, records):

        data = api.consume_api(f"departamento_nom='{department}'", records, client)

        organized_data = api.filter_data(data)
        ui.display_data(organized_data)

        verificacion = str(input("Desea ver la información secundaria del conjunto de datos (S: Sí / N: No): ")).upper()
        if verificacion == "S":
            ui.display_secundary_info(organized_data, records)

    else:
        print("Información ingresada inválida")

main()
