# Solve 2C2023

## Ejercicio 1

Se tiene la siguiente tabla :
| Origen | Destino | FLAGS     | #SEQ | #ACK | Payload |
|--------|---------|-------    |------|------|---------| 
| B      | A       | Ack       | 13   | 106  | -       |
| A      | B       | Ack       | 101  | 12   | HOLA    |
| A      | B       | Ack       | 101  | 12   | -       |
| A      | B       | Syn       | 100  | -    | -       |
| B      | A       | Syn+Ack   | 11   | 101  | -       |
| B      | A       | Fin+Ack   | 12   | 105  | -       |
| A      | B       | Fin+Ack   | 105  | 13   | -       |

Nos piden :
- Reordenar la lista
- Aclarar los estados de los extremos

Reordenamos:

| Origen | Destino | FLAGS     | #SEQ | #ACK | Payload |
|--------|---------|-------    |------|------|---------| 
| A      | B       | Syn       | 100  | -    | -       |
| B      | A       | Syn+Ack   | 11   | 101  | -       |
| A      | B       | Ack       | 101  | 12   | -       |
| A      | B       | Ack       | 101  | 12   | HOLA    |
| B      | A       | Fin+Ack   | 12   | 105  | -       |
| A      | B       | Fin+Ack   | 105  | 13   | -       |
| B      | A       | Ack       | 13   | 106  | -       |

Vamos a analizar los estados por los que atraviesa esta conexión:
- Cuando A -> B el segmento con *SYN* A pasa de *CLOSED -> SYN_SENT* y B, dado que tiene que estar en estado *LISTEN*, sino descartaría el segmento, pasa de *LISTEN -> SYN_RCVD*

- A continuación, como B recibe el segmento con el *SYN* prendido de A, B responde un segmento *SYN+ACK* y A, al recibirlo pasa de *SYN_SENT -> ESTABLISHED* como consecuencia..

- A envía el segmento con *ACK* prendido y B pasa *SYN_RCVD -> ESTABLISHED*

Para el escenario que continua, 
(*dato : Enviar datos incrementa el número de secuencia. Enviar solo un ACK (sin datos) NO incrementa el número de secuencia*)

- A le manda un segmento con datos : *HOLA (4 bytes)* por tanto, tanto A como B siguen en estado *ESTABLISHED*.

- B le responde que recibió los 4 bytes del HOLA correctamente y le manda con él el flag *FIN* para cerrar la conexión. Pasa de *ESTABLISHED -> FYN_WAIT 1*

- A recibe el *FIN* y pasa *ESTABLISHED -> CLOSING* y decide cerrar la conexión y manda *FIN+ACK* confirmando que recibió el segmento con *FIN* de B, como consecuencia, su estado es *LAST_ACK*

- B recibe el *FIN+ACK* y pasa a *TIME_WAIT* que tomará cierto timeout para finalmente recibir si quedaron segmentos por llegar, y terminar en estado *CLOSED*. Le manda el *ACK* a A.

- Al recibirlo, A, pasa *LAST_ACK -> CLOSED*

## Ejercicio 2
Datos del problema :
- RTT = 100ms
- Cantidad de datos a transmitir = 80KB
- Límite del proveedor = 32KB
- RWND = 64KB
- A partir de los 600ms RWND = 16KB

|RTT | CWND | RWND | SSTHRESH | FlightSize | LastByteSent | Comentarios        |
|----|------|------|----------|------------|--------------|--------------------|
|1   | 4KB  | 64KB | 64KB     | 4KB        | 4KB          | CWND = IW = 2 *SMSS|
|2   | 8KB  | 64KB | 64KB     | 8KB        | 12KB         | CWND += 2 * SMSS   |
|3   | 16KB | 64KB | 64KB     | 4KB        | 28KB         | CWND += 4 * SMSS   |
|4   | 32KB | 64KB | 64KB     | 32KB       | 60KB         | CWND += 8 * SMSS   |
|5   | 32KB | 64KB | 64KB     | 32KB       | 60KB         | Timeout            |
|6   | 2KB  | 16KB | 16KB     | 2KB        | 30KB         | CWND = LS (1 SMSS), SSTHRESH = max(fs/2, 2 * SMSS) |
|7   | 4KB  | 16KB | 16KB     | 4KB        | 34KB         | CWND += 1 * SMSS   |
|8   | 8KB  | 16KB | 16KB     | 8KB        | 42KB         | CWND += 2 * SMSS   |
|9   | 16KB | 16KB | 16KB     | 16KB       | 58KB         | CWND += 4 * SMSS   |
|10  | 16KB | 16KB | 16KB     | 16KB       | 72KB         | *Additive increase* CWND += SMSS  pero > RWND, tomamos el min |
|11  | 16KB | 16KB | 16KB     | 8KB        | 80KB         | *Additive increase* CWND += SMSS pero > RWND, tomamos el min   |

Respuesta : CWND vale 16KB una vez terminada la transferencia.

## Ejercicio 3
Para el primer acceso desde HostA tenemos un mensaje como:
*GET /index.html HTTP/1.1*
*Host: www.onlyonepicture.com*
Con lo cual el proxy al que está conectado HostA hace la solicitud al web server que tiene el HTML de la página web. Este le responde algo como:
*HTTP/1.1 200 OK*
*Content-type: txt/html*
*Content-length: 500*
Esta longitud es por el código HTML (500 bytes). A continuación, el HostA detecta que le falta algo en el documento HTML, la imagen, entonces debe pedirla:
*GET img.png HTTP/1.1*
*Host: www.onlyonepicture.com*
Con lo cual, el proxy le consulta al web server y este último se la manda :
*HTTP/1.1 200 OK*
*Content-type: imgage/png*
*Content-length: 1024*
Tenemos 8 mensajes HTTP en el primer acceso.

Para el segundo acceso, como se realiza a través del mismo proxy, todo lo tiene en cache. El HostB hace el pedido:
*GET /index.html HTTP/1.1*
*Host: www.onlyonepicture.com*
El proxy responde sin consultar al web server, y lo mismo con la imagen.

## Ejercicio 4
La idea es encontrar el registro de tipo *MX* para el nombre de dominio *es.wikipedia.org* y luego el de tipo *A* para el servidor indicado por ese MX. 
- Lo primero que sucede es que el resolver le consulta al Root por el registro MX de es.wikipedia.org, que no lo tiene y delega la consulta resolviendo el registro NS del TLD (.org)y el glue record. 
- A continuación, le consultará al NS del TLD (.org) por el registro MX con nombre de dominio es.wikipedia.org que delegará con el registro de tipo NS del autoritativo (wikipedia.org) con el glue record para consultarle. 
- El resolver preguntará a este último por el registro MX con nombre de dominio es.wikipedia.org, este finalmente contiene los registros de este tipo, y devuelve los servidores que se encargan de recibir los correos (MTA). 
- Una vez que se tiene el registro MX, el resolver busca la IP de ese servidor, o sea, el registro tipo A. El resolver le entrega al servidor de correo saliente la IP.
- El servicio de correo saliente inicia una conexión SMTP a ese servidor y envía el mail.


## Ejercicio 5
El problema que tiene este sistema es que se conectapor internet a un *resolver* que no está autenticado como tal. Para mitigar ese problema, podemos establecer primero una comunicación de clave pública donde los actores deben autenticarse, en particular, el resolver (las PCs de la empresa no es necesario, podemos "confiar"). Con esto en mente, cada parte genera el par de claves, se generan los certificados como vimos (primero la RA asegura que sea de quién dice ser la pública, luego se firma el certificado por la CA), se instala la clave pública de la CA root en los dispositivos y se inicia la comunicación. Primero nos conectamos desde una PC al *resolver* quién mandará su certificado firmado,con la pública de la CA Root chequeamos que su pública le pertenece, generamos la clave simétrica efímera para la comunicación, y cada vez que nos devuelve el registro de la consulta, le exigimos que mande *M+F*, o sea, mensaje más firma (el hash del mensaje firmado), donde luego con la pública del *resolver* obtenemos el digest y comparamos con H(M) calculado localmente.  

*en general usamos el de la CA intermediaria que está firmado por Root, o sea, Root nos asegura que la autoridad certificante es quien dice ser y su clave es X. Ahora bien, Root no nos firma nunca a nosotros porque es suuuper importante y sólo firma intermedias de confianza. La idea es que si desciframos el certificado de la CA intermedia con la pública de Root, vamos a poder confiar en ella, y por tanto, si la intermedia nos firmó el nuestro, el otro puede confiar que somos quien decimos ser y nuestra PK es Y*