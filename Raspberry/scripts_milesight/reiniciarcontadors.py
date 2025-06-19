> ⚠️ Este script es una **recreación técnica anónima y adaptada** con fines demostrativos. No incluye contraseñas, direcciones IP ni configuraciones reales utilizadas en entornos de producción.

import requests
import warnings

# Ignorar advertencies SSL
warnings.filterwarnings("ignore")

# Credencials
username = "<usuario>"
password = "<contraseña>"

# URL de la càmara Bosch IP y comanda para obtenir els valores de els contadores IVA
url_reset_counters = "https://<dirección_ip>/rcp.xml?command=0x0b4a&type=P_OCTET&direction=WRITE"

# Mètode per a reiniciar els contadors
def reset_counters(url):
    try:
        # Enviar solicitud HTTPS GET amb credencials
        response = requests.get(url, auth=(username, password), verify=False)
        # Verificar si la solicitud té èxit
        if response.status_code == 200:
            return response.content
    except requests.exceptions.ConnectionError as e:
        e

# Executar mètode
reset_counters(url_reset_counters)
