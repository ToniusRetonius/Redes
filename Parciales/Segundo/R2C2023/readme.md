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


