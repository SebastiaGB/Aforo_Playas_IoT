# People Counter IR, Sensors Infrarrotjos

Com s'ha mencionat, es tenen 2 parelles de sensors IR, es a dir 4 dispositius, formant dues barreres infrrarotjes entre emissor y receptor per a supervisar l'entrada de les covetes.\
Les barreres s'identifiquen amb el nom de A i B. 

A la carpeta 'Documentació' es troben el manual d'usuari i les especificacions d'aquest.

## Característiques
Els dispositius son IP 20 de interior, i funcionen CADA UN amb dues piles AA de 1,5 V. Aquets estan coberts amb una carcasa per a poder funcionar a l'exterior sense cap inconvenient. Es important la forma en que es coloquen els sensors dins la carcasa. Aquesta té un forat a l'interior que indica que la part inferior del sensor es colocarà allà.

* El emissor té: 
  - un botó d'activació.
  - un sol led Infrarrog.
  - una led d'indicació.

* El receptor té:
  - una led destatus.
  - dos led Infrarrotjes.
  - es el que transmet.

PD: Degut al doble mirall que té la carcasa del emissor que tengui un sol led no l'impedeix la sortida de dos feixos de llum per a formar les dues barreres.

### Posada en marcha
Es possen les piles al emissor, es pressiona el botó i la led parpadetja dos voltes en vermell. Llavors es possen les piles al receptor i comença a parpedatjar una led en blau, que indica que s'està conectant a la xarxa. Si parpadetja en varmell indica que la batería sestà baixa. Per comprovar que s'ha conectat exitosament a la xarxa acaba parpadetjant en verd.

## Distribució
A la plataforma IOTIB reben les parelles reben el nom de IRpeoplecounter i IRpeoplecounter2. I els identificarem com a IR e IR2.
De cara a la platja IR es trobarà a la zona de pas de l'esquerra e IR2 a l'altre zona de pas.\
El receptor de les parelles s'ha colocat a l'esquerre i el emissor a la dreta.\
MIRANT DE CARA AL RECEPTOR la barrera A està a la dreta i la B a l'esquerre, per tant si es romp primer A la persona surt i de forma contraria la persona entra al recinte.

La configuració es fa a través de NFC empleant l'aplicació **IMBuildings** sols disponible per android. El keep alive es cada 30 minuts, tenen el adr desactivat, estàn configurats ens DR 0 (SF 12), per a que sempre intenti transmetre amb el major rang possible degut a la seva ubicació.

En aquest URL es veuren totes les opcions disponibles de opcions i configuració, mes la opció de decodificaicó de uplinks: 

    https://support.imbuildings.com/docs/#/./tools/downlink/
Set s'emplea per a realitzar el canvi.\
Request per a fer una petició.\
PD: En aquest URL es pot trobar mes informació com per exemple el decodificador del paylod, calculador de bateria, etc.
  
