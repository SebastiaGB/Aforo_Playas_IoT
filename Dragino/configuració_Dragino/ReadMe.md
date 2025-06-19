En aquest apartat es troba el codi que s'ha dinstalar al Dragino, una carpeta amb les llibreries que emprea i una carpeta on es troba un pdf amb les comandes AT que pot emprear i amb la descripció del seu chip.

# Configuració

Al archiu 'script_dragino' es troba el codi necessari per el seu funcionament.\
Aquest codi conté dos mètodes principals que son el setup(), 
on s'establirà la configuració estàtica al Dragino i el loop() que s'anirà executant constantment dins aquest.

Si es vol saber la Dev_eui del dispositiu, afegir Dalt de la línea "lora.setKey" : 

	        memset(txBuffer, 0, 256);
    		lora.getId(txBuffer, 256, 1);
    		Serial.println(txBuffer);

Si es vol aplicar una nova Dev_eui, afegir Dalt de la línea "lora.setKey" :

		lora.setId("DevAddr", "DevEUI", "AppEUI");

En cas de sols voler possar la Dev_eui possar "" a les altres.

## EXPLICACIÓ CODI:

S'obri una comunicación Serial amb el port que s'ha establert al adruino ide. Si aquest està disponible s'inicia una instancia Lora on s'establiràn:
- Es crea un  buffer, lloc on es guardaràn dades que s'envien i reben. 
- Sobre el port serie amb el baudrate de 115200. 
- Claus del dispositiu (networksesionkey,appsesionkey,appkey). 
- Mode del dispositiu : OTAA
- Data rate a 0 i frequència europea 868 : equival a transmisions a SF12
- Adaptative Data Rate desactivat , adr : off, per a forçar la transmissió a SF 12 
- Classe del dispositiu A
- Realitza el join fins que el dispositiu s'uneixi correctament, en cas contrari ho repateix cada 10 segons fins que s'unesqui. 

### A la part del loop()

1. S'inicialitza un enter longitud.
2. Si el port serie es troba disponible es llegeix el contingut del buffer fins a un salt de linea \n i s'emmagatzema a len.
3. Si el buffer conté dades a transmetre aquestes es transmetràn per LoRa.
4. Degut a l'obertura d'un únic soket per a transmetre i rebre dades amb el mètode 'transferPacket' també es possible rebre downlinks.
5. La terminació del buffer en \0 evita el seu desbordament en el cas d'enviar una cadena.
6. Finalment es netetga el buffer per a assegurarse de que estigui buit al iniciar el loop de nou.

