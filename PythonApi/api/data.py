import pandas as pd
from sodapy import Socrata
import numpy as np

def get_client():
     return Socrata("www.datos.gov.co", None)

def consume_api(user_department, limit, client):
    results = client.get("gt2j-8ykr", where=user_department.upper(), limit=limit)
    return pd.DataFrame.from_records(results)

def filter_data(results_df):
    columns_to_display = [
        "ciudad_municipio_nom",
        "departamento_nom",
        "edad",
        "fuente_tipo_contagio",
        "estado",
        "recuperado"
    ]
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    results_df.replace("N/A", np.nan, inplace=True)
    results_df = results_df.dropna(subset=['estado', 'recuperado', 'fuente_tipo_contagio', 'edad', 'departamento_nom', 'ciudad_municipio_nom'])

    return results_df[columns_to_display]
