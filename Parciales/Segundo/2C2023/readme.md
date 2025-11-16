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




