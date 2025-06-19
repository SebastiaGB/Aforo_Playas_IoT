## Aclaració inicial
A part dels dos arxius `.py`, a la Raspberry també hi haurà d'haver un arxiu `.txt` on es guardaran les dades dels objectes de perfil de les càmeres. Aquest arxiu ha de tenir el nom desitjat, però cal tenir en compte que aquest nom ha de coincidir amb el que es defineix a la "ruta/a/fitxer.txt" en el codi. Per a crear aquest arxiu:

1. Crear un fitxer `.txt` a la Raspberry.
2. Fer clic dret sobre l'arxiu i seleccionar "Copiar ruta d'accés".
3. Enganxar la ruta exacta al lloc on indica `"ruta/a/fitxer.txt"` en el codi.

## Part a modificar
A continuació es detallen les línies del codi que s'han de modificar per al seu correcte funcionament.

>Al respositori **LabCodi_privat** a la carpeta distribució_camares es troben les claus.

### **Fitxer `lecturacontadors.py`**
Per configurar aquest fitxer, cal modificar les següents línies:

* **Línia 13**: Assignar la contrasenya (`password`).
* **Línia 16**: Definir l'adreça IP de la càmera (`direcció_ip`).
* **Línia 85**: Especificar la ruta correcta de l'arxiu `.txt` (`ruta/a/fitxer.txt`).
* **Línia 161**: Definir el port sèrie Dragino (`port_dragino`).

### **Fitxer `reiniciarcontadors.py`**
Per configurar aquest fitxer, cal modificar les següents línies:

* **Línia 9**: Assignar la contrasenya (`password`).
* **Línia 12**: Definir l'adreça IP de la càmera (`direcció_ip`).

## Explicació dels scripts
Per al funcionament correcte, cal tenir un nom d'usuari (sempre "service"), una contrasenya i una URL que, mitjançant l'adreça IP de la càmera i la comanda RCP, es comunica amb aquesta fent servir l'API de Bosch.

### **`lecturacontadors.py`**
Aquest script llegeix els valors dels contadors d'una càmera Bosch i els processa.

#### **1. `get_response(url)`**
Aquest mètode realitza una petició HTTPS GET a la càmera per obtenir els valors mitjançant les credencials (`username` i `password`).

```python
warnings.filterwarnings("ignore")
```
Aquesta línia serveix per a desactivar les advertències SSL, ja que no es disposa d'un certificat per a la connexió.

#### **2. `decode_xml_response(xml_response)`**
Aquesta funció processa la resposta XML de la petició.

1. Extreu la longitud i el valor de la cadena (`string`) de la resposta XML.
2. Elimina espais en blanc per obtenir una cadena neta.
3. Obtè els dos primers caràcters de la `string` per determinar el nombre de contadors (`number_counters`).
4. Verifica si la longitud de la `string` és coherent amb el nombre de contadors (cada contador ocupa 70 caràcters).
5. Si la resposta té longitud 1, indica que la càmera no està configurada correctament, i per tant `counters = [0,0,0]`.
6. Si no:
   - Processa els contadors de 140 en 140 caràcters (70 bytes en hex).
   - Extreu els valors a partir de la posició 128.
   - Converteix-los a decimal.
   - Guarda els valors en `counters`.
7. Retorna `counters`.

#### **3. `set_system_time(datetime_str)`**
Executa una comanda a la Raspberry per canviar la seva hora.

#### **4. `guardar_contadores_en_txt(counters)`**
Emmagatzema els valors dels contadors en un arxiu `.txt`. 

- Obre el fitxer en mode "append" (`'a'`).
- Obtè la data actual de la Raspberry.
- Escriu cada valor amb la seva data corresponent.

#### **5. `enviar_serie(counters, ser)`**
Aquesta funció envia les dades pel port sèrie al Dragino:
- Concatena els valors dels contadors separats per "FF".
- Finalitza el missatge amb `\n`.
- Escriu al port sèrie en codificació UTF-8.

#### **6. `escuchar_serie(ser)`**
Aquest mètode escolta el port sèrie durant un màxim de 15 segons. Si rep dades:
1. Llegeix i decodifica en UTF-8.
2. Filtra els valors rebuts per la finestra RX.
3. Si la resposta té **4 caràcters**, es considera una hora (`HHMM`), s'obté la data actual, es fusiona amb l'hora rebuda i s'actualitza el sistema.
4. Si la resposta té **14 caràcters**, es considera una data completa (`YYYYMMDDHHMMSS`), i també s'actualitza el sistema.
5. Finalment, es tanca el port sèrie per evitar errors.

#### **7. Bucle principal**
1. Obtenim la resposta de la càmera.
2. Obrim el port sèrie.
3. Si la resposta XML és vàlida, decodifiquem els contadors. En cas contrari, `counters = [0,0,0]`.
4. S'envien les dades pel port sèrie.
5. S'escolten dades pel port sèrie.
6. Es guarden els valors en un `.txt`.

---

### **`reiniciarcontadors.py`**
Aquest script envia una petició HTTP a la càmera per reiniciar els contadors a zero.

---


