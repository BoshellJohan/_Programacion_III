import data.departamentos as data
import matplotlib.pyplot as plt


def get_inputs():
    department = str(input("Digite el departamento: ")).upper()
    record_count = int(input("Digite la cantidad de registros: "))

    return department, record_count

def test_valid_data(department, record_count):
    if record_count <= 0:
        return False

    return department in data.departamentosColombia

def display_data(filtered_df):
    renamed_df = filtered_df.rename(columns={
        "ciudad_municipio_nom": "Ciudad",
        "departamento_nom": "Departamento",
        "edad": "Edad",
        "fuente_tipo_contagio": "Tipo de Contagio",
        "estado": "Estado",
        "recuperado": "Recuperado"
    })
    print(renamed_df)

def display_secundary_info(organized_data, records):
    print("Number of rows::",organized_data.shape[0])
    print("Number of columns::",organized_data.shape[1] )

    print("Column Names::",organized_data.columns.values.tolist())
    print("Column Data Types::\n",organized_data.dtypes)
    print("Columns with Missing Values::",organized_data.columns[organized_data.isnull().any()].tolist())
    missing_rows = organized_data.isnull().any(axis=1).sum()
    print("Number of rows with Missing Values:", missing_rows)
    missing_indices = organized_data.index[organized_data.isnull().any(axis=1)].tolist()[0:records]
    print("Sample Indices with missing data:", missing_indices)

    print("General Stats::")
    print(organized_data.info())
    print("Summary Stats::" )
    print(organized_data.describe())

    organized_data["edad"] = organized_data["edad"].astype(int)
    organized_data["edad"].plot(kind="hist", bins=25, edgecolor="black")
    plt.xlabel("Edad")
    plt.ylabel("Número de casos")
    plt.title("Número de casos por edad")
    plt.grid(True, which="both", axis="both", linestyle="--", linewidth=0.5)  # Agregar cuadrícula
    plt.show()

