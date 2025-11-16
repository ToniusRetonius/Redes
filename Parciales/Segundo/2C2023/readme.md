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
| A      | B       | Ack       | 101  | 12   | HOLA    |
| A      | B       | Ack       | 101  | 12   | -       |
| B      | A       | Fin+Ack   | 12   | 105  | -       |
| A      | B       | Fin+Ack   | 105  | 13   | -       |
| B      | A       | Ack       | 13   | 106  | -       |

Vamos a analizar los estados por los que atraviesa esta conexión:
- Cuando \( A \to B\) 


