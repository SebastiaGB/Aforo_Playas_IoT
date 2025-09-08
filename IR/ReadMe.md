# Sistema de Conteo de Personas con Sensores Infrarrojos (IR)

Este sistema forma parte del proyecto de control de aforo en la Playa de Es Trenc. Se compone de sensores infrarrojos instalados en accesos peatonales clave, concretamente en el camino de entrada de Ses Covetes. Su función es detectar el paso de personas para calcular en tiempo real la ocupación de la playa.

---

## 📦 Componentes del Sistema

El sistema consta de **2 pares de sensores infrarrojos** (4 dispositivos en total), cada par forma una doble barrera entre un **emisor** y un **receptor**. Estas barreras se denominan **A** y **B**, y permiten determinar si una persona entra o sale del recinto según el orden en que se interrumpen.

📂 Documentación técnica completa disponible en la carpeta `IR/`.

---

## ⚙️ Especificaciones Técnicas

- **Dispositivos**: IP20 (uso interior), adaptados para exterior con carcasa protectora.
- **Alimentación**: 2 pilas AA de 1,5 V por unidad.
- **Colocación**: La carcasa incluye una guía para orientar correctamente el sensor.

### 🟢 Emisor
- 1 LED infrarrojo.
- 1 LED indicador.
- Botón de encendido.

### 🔵 Receptor
- 2 LEDs infrarrojos.
- 1 LED de estado.
- Es el dispositivo que recibe y transmite los datos.

📌 *Gracias a un sistema de doble espejo en la carcasa del emisor, una única fuente infrarroja puede generar dos haces de luz independientes.*

---

## 🚀 Puesta en Marcha

1. Insertar las pilas en el **emisor** y presionar el botón: el LED parpadea en rojo dos veces.
2. Insertar las pilas en el **receptor**:
   - LED azul parpadeando: buscando red.
   - LED rojo: batería baja.
   - LED verde: conectado correctamente.

---

## 🌐 Distribución e Identificación en Plataforma

En la plataforma **IoTIB**, los sensores están registrados como:

- `IRpeoplecounter` → zona izquierda del acceso.
- `IRpeoplecounter2` → zona derecha del acceso.

📍 **Ubicación física**:
- Cada par se instala con el **receptor a la izquierda** y el **emisor a la derecha** (visto desde el acceso).
- Si se interrumpe primero la barrera A → se interpreta como **salida**.
- Si se interrumpe primero la barrera B → se interpreta como **entrada**.

---

## 🔧 Configuración

- Se realiza vía **NFC** con la app **IMBuildings** (solo Android).
- Keep alive: cada 30 minutos.
- ADR: desactivado.
- Data Rate: configurado en **DR0 (SF12)** para máxima cobertura.

📖 Más información y herramientas en:
🔗 [IMBuildings Docs & Tools](https://support.imbuildings.com/docs/#/./tools/downlink/)

Incluye:
- Decodificador de payloads.
- Calculador de batería.
- Comandos `SET` y `REQUEST` para configuración remota.

---

## 🛡️ Privacidad y Fiabilidad

- No se almacena ninguna imagen.  
- El conteo es completamente anónimo.  
- Bajo consumo y mantenimiento mínimo.  
-  Adaptado a condiciones exteriores sin conexión eléctrica.

---

> 📝 Este sistema fue desarrollado como parte de un proyecto profesional de infraestructura IoT para control de aforo en espacios naturales. Esta documentación tiene fines demostrativos y no contiene datos sensibles ni accesos reales.
