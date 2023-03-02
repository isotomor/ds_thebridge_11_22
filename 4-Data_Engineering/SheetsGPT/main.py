import os
import openai # GPT3
import gspread # Google Sheets

# Ruta de trabajo del fichero
os.chdir(os.path.dirname(__file__))

# Conexión al google sheet
# Seguir los pasos
# https://docs.gspread.org/en/latest/oauth2.html
gc = gspread.service_account()

# Obtener pregunta de la celda del fichero
# https://docs.gspread.org/en/latest/user-guide.html
# https://docs.google.com/spreadsheets/d/1N7s_apHtwjp-2JKj9gqyLgInUGHAJAVM_k2drlB4S3o/edit?usp=sharing


# Conexión a GPT3. Registrarse en:
# https://openai.com/product

openai.api_key = open("api_key.txt", "r").read()

# Enviamos pregunta para recibir respuesta de GPT3

response = openai.Completion.create()

# Pegamos respuesta en Google sheet

