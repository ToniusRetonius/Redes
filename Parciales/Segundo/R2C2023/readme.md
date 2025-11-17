# Solve R2C2023

## Ejercicio 1
El caso de *simultaneous open* ocurre cuando dos hosts envían segmentos con el flag SYN prendido y ambos se intentan conectar al mismo puerto destino (mismo socket). En estos escenarios, la conexión es activa y por tanto, cuando envían el SYN ambos pasan de *closed -> SYN_SENT*. Lo que ocurre es que reciben de la contraparte un SYN, por ello, mandan el segmento *SYN+ACK* lo cual pasa directo a *ESTABLISHED* sin pasar por el estado *SYN_RCVD*.

##  Ejercicio 2
Datos : AW = 64KB ; si los paquetes son de 12KB o más, los descarta. 

| RTT | CWND | RWND | SSTHRESH | FligthSize | LastByteSent |Comentario            |
|-----|------|------|----------|------------|--------------|----------------------|
|1    |4KB   |64KB  |64KB      |4KB         |4KB           | CWND = IW = 2 * SMSS |
|2    |8KB   |64KB  |64KB      |8KB         |12KB          | CWND += 2 * SMSS     |
|3    |16KB  |64KB  |64KB      |16KB        |28KB          | Límite del proveedor |
|4    |16KB  |64KB  |64KB      |16KB        |28KB          | RTO = 2*RTT (timeout)|
|5    |2KB   |64KB  |8KB       |2KB         |14KB          | CWND = LW (1 SMSS) y SSTHRHRESH = FS/2  |
|6    |4KB   |64KB  |8KB       |4KB         |18KB          | CWND += 1 *SMSS      |
|7    |8KB   |64KB  |8KB       |8KB         |26KB          | CWND += 2 *SMSS      |
|8    |10KB  |64KB  |8KB       |10KB        |36KB          | CWND += SMSS         |
|9    |12KB  |64KB  |8KB       |12KB        |48KB          | CWND += SMSS         |
|10   |12KB  |64KB  |8KB       |12KB        |48KB          | Timeout              |
|11   |2KB   |64KB  |6KB       |2KB         |38KB          | CWND = LW (1 SMSS) y SSTHRHRESH = FS/2  |
|12   |4KB   |64KB  |6KB       |4KB         |42KB          | CWND += SMSS         |
|13   |8KB   |64KB  |6KB       |8KB         |50KB          | CWND += SMSS         |


## Ejercicio 3
*claudio@peterson.com* le quiere mandar un mail a *ernesto@tanenbaum.com*.
El MTA (mail transfer agent) del emisor es el encargado de toda la lógica de ruteo, por tanto, el emisor no debe hacer ninguna consulta DNS. Estas serán realizadas por el mail server saliente. 
Lo que hace el emisor es redactar el mail y se lo manda al mail server mediante una conexión SMTP (simple mail transfer protocol) y a continuación, el mail server saliente:
- Consulta al Root server por el registro MX para el nombre de dominio tanenbaum.com, el Root le responde con un registro NS del TLD (.com) con el glue record que contiene la IP para poder consultarle.
- Consulta al TLD (.com) por el registro MX de tanenbaum.com, no lo tiene, pero sabe el registro NS del autoritativo tanenbaum.com y con el glue record podemos a continuación...
- Consultarle al autoritativo tanenbaum.com por el registro MX. Que nos dará la información para comunicarnos con el mail server de ese nombre de dominio. Será con él que tendrá que establecer la conexión SMTP y mandarle el mail escrito por claudio@peterson.com

## Ejercicio 4
El flujo del mail es el siguiente:
- El emisor (HostA) redacta el mail y mediante SMTP:TCP se conecta al servidor de correo saliente. 
- El servidor de correo saliente se conecta mediante SMTP:TCP al servidor de correo de entrada del receptor (HostB).
- Como el HostB utiliza webmail, el servidor de correo de entrada tendrá que conectarse mediante POP3:TCP al web server del servicio utilizado por el HostB para poder realizar la descarga del mail.
- Cuando el usuario quiere hacer la lectura del mail, deberá establecer una conexión HTTP:TCP con el web server.
