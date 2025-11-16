# Solve 1C2025

## Ejercicio 1
Para reconocer qué nodo envía cada segmento voy a enfocarme en el ACK que espera. Es decir, el nro de ACK me dice qué SEQ espero recibir a continuación. Por tanto, para el segmento 10, vemos que el Host A envía al Host B un segmento con SEQ=34633 y espera recibir un SEQ=35088, lo deducimos del valor de ACK=35088. A continuación, el host B envía el segmento SEQ=35088 al Host A y espera recibir el segmento SEQ=34647 (de ACK=34647). Luego el Host A le manda un segmento con SEQ=34647 y espera recibir SEQ=35135. Lo interesante es que en el siguiente caso, hay una retransmisión ese segmento desde A a B. Finalmente, lo recibe y el Host B le manda el segmento SEQ=35135 con ACK=34661.
Para calcular la cantidad de datos enviados ACK - SEQi, es decir, si yo mmando un nro de SEQ=x tenemos que mirar qué valor de ACK me manda el receptor a continuación, esto nos permite ver el *nro de byte inicial* que mandamos (**x**) y el *nro de byte que espera recibir* a continuación (**y**). Con esto :
- **10:** A le manda SEQ=34633 ACK=35088 y recibe SEQ=35088 ACK=34647, es porque A le mandó 34647 bytes - 34633 bytes = 14 bytes en ese segmento. 
- **11:** B le manda SEQ=35088 y el ACK de A es 35135, ergo 35135 - 35088 = 47 bytes
- **12:** A le manda SEQ=34647 y recibe de B ACK=34661 es porque en ese segmento le mandó 34661 bytes - 34647 = 14 bytes.
- **13:** es el mismo retransmitido
- **14:** no se sabe


## Ejercicio 2

