# Link del Video
https://www.canva.com/design/DAGl4se8KGo/tk9OLzl5cmsSx_MNpTh5Mw/edit?utm_content=DAGl4se8KGo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

# Importador de CSV a MongoDB
Este script lee datos de un archivo CSV (sup.csv) e importa los datos a una colección de MongoDB llamada sup en la base de datos lab8. Utiliza operaciones en bloque para una inserción eficiente.

# Características
Lee un archivo CSV y analiza cada fila con las funciones.
  with with open("sup.csv", newline='', encoding='utf-8') as csvfile:

Convierte ciertos campos a tipos int o float y crea la estructura del documento.
  for row in reader:
        # Convert fields to appropriate types if needed
        doc = {
            "Date": row["Date"],
            "Product Name": row["Product Name"],
            "Category": row["Category"],
            "Units Sold": int(row["Units Sold"]),
            "Price": float(row["Price"]),
            "Revenue": float(row["Revenue"]),
            "Discount": float(row["Discount"]),
            "Units Returned": int(row["Units Returned"]),
            "Location": row["Location"],
            "Platform": row["Platform"]
        }
       

Realiza una inserción masiva en MongoDB para mejorar la eficiencia.
   operations.append(InsertOne(doc))

Carga de manera segura los detalles de conexión a MongoDB desde un archivo .env.

Requisitos
Python 3.7+

Instancia de MongoDB

Archivo sup.csv

Instalación
Clona el repositorio o copia el script en tu directorio de proyecto.

Instala los paquetes de Python necesarios:

bash
  pip install python-dotenv pymongo
Crea un archivo .env en el directorio del proyecto con la URL de conexión a tu MongoDB:

env
  MONGO_URI=mongodb://usuario:contraseña@localhost:27017
Aquí tienes un ejemplo de cómo debería lucir el archivo sup.csv:

csv
  Date,Product Name,Category,Units Sold,Price,Revenue,Discount,Units Returned,Location,Platform
  2025-01-01,Example Item,Toys,100,10.5,1050.0,0.1,2,New York,Amazon
Para ejecutar el archivo Python
  python main.py
Si el CSV contiene datos válidos, el script realizará una inserción masiva de todas las filas en MongoDB e imprimirá el número de documentos insertados.