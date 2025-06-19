# 📡 Configuración de Transmisores Milesight

Esta carpeta contiene la documentación y scripts relacionados con la configuración de dispositivos **Milesight LoRaWAN** utilizados en el sistema de control de aforo del proyecto.

---

## ⚙️ Configuración Aplicada

Los transmisores han sido configurados con los siguientes parámetros:

- 🔄 **Modo**: OTAA (Over-The-Air Activation)
- 🔋 **Clase**: C (recepción continua de downlinks)
- 🧭 **ADR**: Desactivado
- 📶 **Spreading Factor**: SF12 (máxima cobertura)

---

## 🛠️ Instalación y Uso de ToolBox

Para configurar los dispositivos Milesight se ha utilizado la herramienta oficial **Milesight ToolBox**, disponible en:

🔗 [Milesight Download Center](https://www.milesight.com/iot/resources/download-center/#marketing-collateral)

### 🔐 Credenciales de acceso

- **Contraseña por defecto**: `123456`

Una vez conectado el dispositivo al PC (se detecta como puerto COM), ToolBox permite:

1. **Actualizar el firmware** (disponible en el mismo enlace, sección *Firmware & SDK*).
2. Visualizar el identificador **DevEUI**.
3. Establecer o verificar:
   - Modo OTAA
   - Clase C
   - SF12
   - AppKey personalizada
4. Guardar y aplicar la configuración.

---

> 📝 Esta configuración fue aplicada en el contexto de un sistema IoT desplegado en un entorno natural protegido. La información aquí expuesta es genérica y no compromete datos sensibles del proyecto real.
