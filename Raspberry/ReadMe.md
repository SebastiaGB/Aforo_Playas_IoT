## Raspberry/ – Configuración y Scripts de la Raspberry Pi

La Raspberry Pi actúa como el núcleo local del sistema. A través de ella se gestionan las comunicaciones entre los dispositivos de captura (cámaras y sensores) y los transmisores LoRa.
A continuación se explican los pasos a seguir para tener la raspberry pi bien configurada, facilidades y las opciones que deben añadirse dependiendo del receptor LoRa que esta posea.

### Especificaciones Generales

Para más detalles técnicos sobre las Raspberry Pi, consultar:
https://www.raspberrypi.com/documentation/

---

### 🛠 Instalación del Sistema Operativo

Dependiendo del modelo de Raspberry Pi, se debe instalar un sistema operativo compatible.  
Se recomienda usar la herramienta oficial Raspberry Pi Imager:

👉 https://www.raspberrypi.com/software/

- Usar una microSD de mínimo 32 GB.
- Usar la versión de 32 bits si la Raspberry tiene 4 GB de RAM o menos.
- Conectar HDMI **antes de encender** la Raspberry, para garantizar la visualización.

---

### 🔄 Actualización del Sistema

Una vez encendida y realizada la configuración inicial:

```bash
sudo apt update && sudo apt full-upgrade
```

---

### 🌐 Configuración de IP Estática

Usar Network Manager:

```bash
sudo nmtui
```

1. Seleccionar la interfaz `eth0`.
2. Cambiar IPv4 de automático a manual.
3. Asignar IP privada dentro del rango de red de la cámara.
4. Guardar y salir.
5. Reiniciar:

```bash
sudo reboot
```

Verificar con:

```bash
ip a
```

---

### ⏱ Automatización con Crontab

- Para **Dragino**, se configura para enviar datos cada 'X0 minutos.
- También se automatiza el **reinicio diario de contadores**.
- En el caso de **Milesight**, no se usa `crontab`, sino un bucle `while True` persistente.

#### Configurar crontab:

```bash
crontab -e
```

Al final del archivo, añadir por ejemplo:

```bash
* 2 * * * python3 /ruta/al/script.py
```

Significado de los asteriscos:
- Minuto (0-59)
- Hora (0-23)
- Día del mes (1-31)
- Mes (1-12)
- Día de la semana (1-7)

---

### 🧩 Configuración como Servicio para Milesight

1. Crear archivo de servicio:

```bash
sudo nano /etc/systemd/system/milesight_controller.service
```

2. Ejemplo de configuración:

```
[Unit]
Description=Script de control Milesight
After=network.target

[Service]
ExecStart=python3 /ruta/al/script.py
WorkingDirectory=/ruta/al/
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

3. Activar y lanzar el servicio:

```bash
sudo systemctl enable milesight_controller.service
sudo systemctl start milesight_controller.service
```

4. Comprobar estado (opcional):

```bash
sudo systemctl status milesight_controller.service
```

---

### 🔌 Identificación de Puertos

#### Puerto Dragino

```bash
dmesg | grep tty
```

> Aparecerá como: `ttyACM0`

#### Puerto Milesight

```bash
dmesg | grep tty
```

> Aparecerá como: `ttyUSB0`

---

### 🖥 Conectar la Raspberry Pi a un PC como monitor

1. Asignar IP estática tanto a la Raspberry como al PC.
2. Conectar mediante cable Ethernet.
3. Realizar conexión SSH desde terminal del PC:

```bash
usuario_raspberry@ip_estatica
```
