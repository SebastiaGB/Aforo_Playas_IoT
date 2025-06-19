# 🏖️ Proyecto de Control de Aforo en la Playa de Es Trenc (Mallorca)

> ⚠️ Proyecto desarrollado durante mi etapa como técnico IoT en colaboración con FUEIB. Esta versión es una **recreación técnica** con fines demostrativos. No incluye datos sensibles ni contraseñas.

---

## 📌 Resumen General

Este proyecto consistió en diseñar e implementar un sistema IoT para el **control de aforo** en la Playa de Es Trenc, un espacio natural protegido con una gran afluencia de visitantes durante los meses de verano.

El sistema permite:

- 👣 Contabilizar el acceso y salida de personas en diferentes entradas de la playa.
- 🚗 Contabilizar los vehículos en el aparcamiento.
- 📡 Enviar los datos en tiempo real a una plataforma de visualización remota (**IoTIB**).
- ✅ Operar de forma automatizada, respetando la privacidad y con bajo mantenimiento.

---

## 🧠 Tecnologías Utilizadas

- **Cámaras Bosch IP (7000i y 8000i)** con analítica de vídeo (VCA).
- **Sensores infrarrojos bidireccionales** para conteo por ruptura de haz.
- **Raspberry Pi** como nodo de procesamiento local y enlace.
- **Transmisores LoRa** (Milesight y Dragino).
- **Scripts Python** para comunicación serial, lectura de contadores y sincronización horaria.
- **Plataforma IoTIB** para visualización en tiempo real.

---

## 🛠️ Infraestructura del Sistema

Los dispositivos se instalaron en diferentes puntos clave:

| Ubicación                        | Dispositivo instalado             | Función principal                     |
|----------------------------------|-----------------------------------|----------------------------------------|
| Colònia de Sant Jordi (Na Tirapel) | Cámara Bosch + Dragino LoRa       | Conteo de personas                    |
| Aparcamiento de la Salinera       | Cámara Bosch + Milesight LoRa     | Conteo de vehículos                   |
| Entrada de Ses Covetes           | Sensores infrarrojos dobles       | Conteo bidireccional de peatones      |

➡️ El sistema **no almacena imágenes** ni identifica personas o vehículos. Solo realiza conteo de forma anónima.

---

## ⚙️ Funcionamiento General

1. La cámara o sensor recoge eventos de paso (persona o vehículo).
2. La Raspberry recoge y procesa los datos.
3. La Raspberry envía los datos por **RS485** al transmisor LoRa.
4. El transmisor LoRa envía los datos a **IoTIB**.
5. La plataforma muestra el aforo en tiempo real.

---

## 🧩 Estructura del Repositorio

📁 Distribució_camares/       → Esquema y claves de ubicación de cámaras  
📁 IR/                        → Documentación y calibración de sensores infrarrojos  
📁 Milesight/                 → Configuración de transmisores con ToolBox  
📁 Dragino/                   → Guía y firmware para Dragino con Arduino IDE  
📁 Raspberry/  
├── 📁 scripts_dragino/       → Scripts Python para enviar datos por RS485 a Dragino  
└── 📁 scripts_milesight/     → Scripts Python para dispositivos Milesight

---

## 🔧 Componentes Técnicos

### 🎥 Cámaras Bosch IP (7000i y 8000i)

- Calibración con **Configuration Manager** y/o **Project Manager**.
- Uso de **Video Analytics (VCA)** para detectar y contar objetos.
- Configuración de perfiles, líneas de conteo y sincronización de hora.
- El modelo 8000i soporta WiFi; el 7000i no.

### 🍓 Raspberry Pi

- Sistema operativo: Raspbian.
- Interfaz Ethernet con la cámara.
- Comunicación serial con LoRa.
- Scripts Python personalizados:
  - Lectura de contadores Bosch (API RCP).
  - Sincronización horaria vía downlink.
  - Envío periódico de datos.

### 📶 Transmisores LoRa

| Modelo     | Clase | Downlink | Notas técnicas                                   |
|------------|-------|----------|--------------------------------------------------|
| Dragino    | A     | Solo tras uplink | Usa puerto 1, formato decimal (ej. `1230`)    |
| Milesight  | C     | Cualquier momento excepto durante uplink | Usa puerto 2, hexadecimal (`31323330`) |

---

## 📡 Comunicación con Plataforma IoTIB

### Envío de datos (uplink)

- Datos en formato hexadecimal separados por `FF`.
- Ejemplo: `303146463234464632` → `01 FF 24 FF 2`
- Interpretación: 3 contadores activos.

### Recepción de instrucciones (downlink)

- Sincronización horaria automática.
- Ejemplo de hora:
  - **Dragino (decimal)**: `1230` (hora)
  - **Milesight (hex)**: `31323330` = `12:30`

---

## 🔍 Ejemplo de Lógica en Raspberry

Los scripts `lecturacontadors.py` y `reiniciarcontadors.py` incluyen:

- Lectura de XML de la cámara vía HTTPS.
- Decodificación hexadecimal → valores numéricos.
- Guardado en `.txt` con marca de tiempo.
- Envío vía serial (RS485) al transmisor.
- Escucha activa de comandos (sincronización horaria).

---

## 🔒 Seguridad y Privacidad

✅ El sistema está diseñado para ser **totalmente anónimo**.  
✅ Solo se almacenan datos numéricos de conteo.  
✅ No se capturan ni almacenan imágenes ni datos personales.  
✅ En esta versión pública **no se incluye** ninguna contraseña, dirección IP real ni credenciales.

---

## ✅ Resultados Obtenidos

- ✅ Instalación estable y operativa durante la temporada.
- ✅ Monitorización en tiempo real de aforo en la plataforma IoTIB.
- ✅ Automatización completa sin necesidad de intervención constante.
- ✅ Sistema adaptable y escalable para otros entornos naturales.

---

📬 **¿Quieres saber más sobre cómo funciona el sistema o ver el código en acción?**  
Puedes explorar los scripts en las carpetas `Raspberry/scripts_dragino` y `Raspberry/scripts_milesight`.

---

⭐ *Este proyecto representa una experiencia real de campo en soluciones IoT aplicadas a espacios naturales. Fue una gran oportunidad para aplicar conocimientos técnicos, trabajo en equipo e innovación sostenible.*


