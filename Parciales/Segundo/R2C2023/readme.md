# Solve R2C2023

## Ejercicio 1
El caso de *simultaneous open* ocurre cuando dos hosts envían segmentos con el flag SYN prendido y ambos se intentan conectar al mismo puerto destino (mismo socket). En estos escenarios, la conexión es activa y por tanto, cuando envían el SYN ambos pasan de *closed -> SYN_SENT*. Lo que ocurre es que reciben de la contraparte un SYN, por ello, mandan el segmento *SYN+ACK* lo cual pasa directo a *ESTABLISHED* sin pasar por el estado *SYN_RCVD*.