# ACTIVIDAD FINAL - JUEGO DEL LABERINTO.

## OBJETIVOS.
En nuestra actividad final, el objetivo era realizar un juego utilizando los recursos y habilidades vistos en clase, en este caso, Turtle Graphics y FreeGames, nuestro equipo optó por realizar un laberinto...
### COMPLICACIONES .
Al empezar la programación del laberinto, se nos complicó el adaptar el movimiento del "personaje" dentro de este, siento que la parte dificil fue darle forma al sistema gráfico.
## DESARROLLO.
* Primero, se importan las librerias de Turtle, freegames y Random, las primeras dos se utilizarán para el desarrollo gráfico del juego, mientras que random se usa para elegir entre laberintos.
* Después se crean variables que serán utilies, como la llave y el comparador, la llave sirve para poder pasar el nivel abriendo la puerta, sin llave no hay final.
* Seguido de esto, se declaran los mapas de laberinto, en nuestro caso son 3, cada uno distinta generación y distinta posición de la llave.
* Creando un numero random entre 0 y 2, se elige el mapa en el que se jugará.
* Se declaran las funciones del mapa y de las entidades dentro de estas, representadas por world() y square().
* Se declaran funciones de movimiento, dentro de estas, se elige a que dirección irá el personaje y al final de cada una, se limpia la pantalla para que el "paso" se vea reflejado.
* Por ultimo, se declara el tamaño de la ventana del juego, y se mete en un ciclo while las líneas que llaman a la función de dirección, para que estas funciones se puedan realizar múltiples veces.
* Al terminar el laberinto, saltará una pagina en negro, que tendrá reflejada el mensaje "GANASTE, FELICIDADES, COMPLETASTE EL MAPA".
##### Marco Tulio Montoya - A01254155
