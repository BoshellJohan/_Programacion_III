import pandas as pd
from sodapy import Socrata


def getIntoApi(limite_registros, nombre_departamento):
    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata("www.datos.gov.co", None)

    # Example authenticated client (needed for non-public datasets):
    # client = Socrata(www.datos.gov.co,
    #                  MyAppToken,
    #                  userame="user@example.com",
    #                  password="AFakePassword")

    # First 2000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get("gt2j-8ykr", limit=limite_registros, departamento = nombre_departamento)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)