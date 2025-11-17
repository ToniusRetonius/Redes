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
Si cierta aplicación tiene que resolver una IP de un servidor web con nombre de dominio www.dominio.com.ar lo que hará es llamar al *stub resolver* que corre localmente para que haga la consulta al *local name server (ISP)* (recursivo). En caso de no tenerlo este último en cache, deberá hacer el siguiente flujo de consultas :

- *Local name server -> Root server, Root server -> Local name server * : el recurser consulta al root por el TLD .ar, este devolverá registro NS responable de (.ar) con el *glue record*: la ip asociada a ellos para poder comunicarse y continuar la consulta.

- *Local name server -> (.ar) , (.ar) -> Local name server* : le consulta el resolver recursivo al name server TLD el registro para www.dominio.com.ar, con lo cual, el TLD conoce el registro NS del autoritativo (com.ar), y si corresponde, el *glue record* : del mismo con su IP asociada.

- *Local name server -> (.com.ar) , (.com.ar) -> Local name server*: en este caso, le consulta por www.dominio.com.ar y el autoritativo (.com.ar) NS conoce el registro del NS de dominio.com.ar con lo cual responde el registro NS y el glue record con la IP.

- *Local name server -> (.dominio.com.ar),(.dominio.com.ar) -> Local name server * : al autoritativo se le consulta por www.dominio.com.ar y este tiene el registro tipo A de la consulta, responde con la IP.

- *Local name server -> aplicación*: una vez resuelta la consulta DNS, el local name server le envía al cliente la IP de la consulta para que la capture el DNS resolver del SO y que le pase la información a la aplicación que la necesitaba


## Ejercicio 3
La secuencia de envío es como sigue:
*Emisor -> Web server -> mail server saliente -> Internet -> mail server entrante <- Receptor*
La secuencia es de esta manera ya que el cliente(emisor) hace uso de un webmail para enviarlo. Por tanto, la aplicación web corre en un servidor web. Con esto en mente, la conexión del emisor al web server es por HTTP(S):TCP. Luego, el web server se conecta mediante SMTP:TCP al mail server y luego, entre mail servers se conectan mediante SMTP:TCP. Dando como resultado, 3 conexiones TCP. Para el caso del receptor, deberá iniciar una conexión con IMAP o POP3 (que también están sobre TCP) para poder realizar la lectura o podría hacer uso de un webmail y en ese escenario, tendríamos una conexión HTTP:TCP desde el receptor al web server y del web server al mail server entrante a través de IMAP o POP3. Como consecuencia, 2 conexiones TCP más. *(consultar)*