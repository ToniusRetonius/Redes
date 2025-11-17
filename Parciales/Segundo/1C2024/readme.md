# Solve 1C2024

## Ejercicio 1
En TCP podemos mostrar los cierres de conexión como un diagrama de estados. 
La forma tradicional (four-way handshake) es cuando un cliente realiza un close pasando de *ESTABLISHED -> FIN_WAIT 1* cuando le envía al servidor un segmento con el flag *FIN*, indicando que no va a mandar más datos. Luego el servidor puede responder un *ACK* para iniciar el cierre,y este pasa al estado *CLOSE_WAIT* ya que todavía está enviando segmentos de datos (reconoce el cierre parcial del flujo). Es por ello, que el cliente recibe es *ACK* y pasa al estado *FIN_WAIT 2* a la espera del segmento *FIN* por parte del servidor (indicando que ya no enviará más datos), este segmento es el que le garantizará pasar al estado *TIME_WAIT* esperando que lleguen segmentos que están on-the-fly (timeout) y en ese momento, le manda al servidor el segmento con el *ACK* para que pueda pasar al último estado, *CLOSED*. El servidor luego de enviar el *FIN* pasará *CLOSE-WAIT -> LAST ACK* que espera ese *ACK* que hablamos recién, garantizando el *CLOSED* del servidor. El cliente cumplido el timeout, pasa finalmente al estado *CLOSED*.

Otra manera, ocurre cuando ambos, cliente y servidor inician activamente el cierre en simultaneo, es decir, ambos envían el segmento con el flag *FIN*. Esto hace que ambos estén pasen de  estado *ESTABLISHED -> FIN_WAIT 1*, pero como reciben un segmento con *FIN*, mandan el *ACK* y pasan momentaneamente a *CLOSING* hasta recibir el *ACK* de su contraparte, que los llevará al estado *TIME_WAIT* que finalizado el timeout los llevará al estado *CLOSED*

La última forma es cuando el cliente inicia el cierre con un segmento *FIN* y el servidor ya no tiene segmentos que mandar y por tanto manda el segmento con *FIN+ACK* encausando una transición del cliente *FIN_WAIT 1 -> TIME_WAIT (timeout) -> CLOSED* y como consecuencia el cliente le manda el segmento con el *ACK* que permitirá el cierre del servidor (pasaje de *LAST ACK -> CLOSED*).


## Ejercicio 2
En TCP no hay manera de saber directamente si hay congestión en cierta red. Por ello, se utiliza un mecanismo intuitivo para obtener esa información. La idea es, a partir de esa información, tomar decisiones para controlar la comunicación e implementar mecanismos para controlar la congestión. Necesitamos primero enviar un segmento con cierto tamaño definido por el *SMSS (sender maximum segment size)* y ver si llega el ACK del mismo. Si llega rápido, está bien la red, entonces podemos aumentar el valor de *CWND (congestion window)* que será la variable dinámica que nos permitirá controlar la cantidad de datos *en-vuelo*. Para aumentarla, se utiliza la siguiente regla : *CWND += min(N, SMSS)* donde N es la cantidad de bytes que se reconocen, esta regla se aplica por cada ACK que recibimos. Este es un escenario de retroalimentación positiva, ya que podemos aumentar la cantidad de datos transmitidos en la comunicación. 
El tema está cuando los acknoledgements de los segmentos que mandamos tardan mucho en llegar, incluso si hay casos de timeouts o duplicación de ACKS. Estos son escenarios de retroalimentación negativa, y se debe modificar la variable CWND de manera de no sobrecargar la red. Se utiliza para reiniciar CWND el valor de *LW (loss window)* o modificaciones en *SSTHRESH* para recalcular los segmentos *en-vuelo*.

## Ejercicio 3
En el caso de tener almacenado un registro DNS tipo A con un valor de TTL=3 días con nombre de dominio= dc.uba.ar y valor=157.92.27.128 en cierto cliente, si se realiza una modificación del registro por parte de un *name server autoritativo* como la modificación de la IP del nombre de dominio, el cambio no se replica como un push en Git. Lo que sucede es que, si bien es efectivo el cambio en el autoritativo, en los name server que contengan el registro desactualizado no impactará el cambio hasta que no haya expirado el mismo (tiempo determinado por el TTL). Cuando haya expirado, recién ahí, cuando el resolver haga la consulta, podrá impactar el cambio.

## Ejercicio 4

En el protocolo HTTP, las peticiones del cliente al servidor tienen un formato como:
*request line : método--recurso--version*
*header line: header field:---value*
*...*
*blank*
*data*
En este contexto, nos piden comparar dos métodos: GET y POST.
- Cuando el cliente realiza una petición al servidor con el método **GET** está pidiendo recibir un recurso que se encuentra alojado en dicho servidor. Por ejemplo :
*GET /index.html HTTP/1.1*
*Host: www.dc.uba.ar*
En esta solicitud, el cliente quiere acceder a un recurso de tipo HTML alojado en el servidor. La respuesta del servidor tiene el formato: 
*status line : version---status---phrase*
*header line: header field:---value*
*blank*
*data*
Y como consecuencia, si lo tiene al recurso responde:
*HTTP/1.1 200 OK*
*content-type: text/html*
puede contener longitud, fecha, servidor,... 

- En el caso de que el cliente quiera enviar datos al servidor, por ejemplo para crear un nuevo recurso, lo puede hacer mediante el método **POST** como sigue:
*POST logo.jpg HTTP/1.1*
*Host: www.dc.uba.ar*

