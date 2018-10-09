## Turno del ordenador

Ahora es el turno del ordenador. Puedes usar la función `randint` para generar un número aleatorio para decidir entre piedra, papel y tijeras.

+ Usa `randint` generar un número aleatorio para decidir si la computadora ha elegido piedra, papel o tijera.
    
    ![captura de pantalla](images/rps-randint.png)

+ Ejecuta el programa muchas veces (deberás introducir 'r', 'p' o 't' cada vez)
    
    Verás que 'elegido' está configurado aleatoriamente como 1, 2 ó 3.

+ Digamos:
    
    + 1 = piedra (r)
    + 2 = papel (p)
    + 3 = tijera (t)
    
    Usa ` if ` para verificar si el número elegido es `1` (`==` se usa para ver si 2 cosas son iguales).
    
    ![captura de pantalla](images/rps-if-1.png)

+ Python usa la **sangría** (mover el código hacia la derecha) para mostrar qué código está dentro del `if`. Puedes usar dos espacios (pulsa la barra espaciadora dos veces) o pulsar la **tecla Tab** (generalmente encima de Bloq Mayús en el teclado)
    
    Configura `ordenador` a 'r' dentro del `if` usando sangría:
    
    ![captura de pantalla](images/rps-indent.png)

+ Puedes añadir una comprobación alternativa usando `elif` (abreviatura de *else if*):
    
    ![captura de pantalla](images/rps-elif-2.png)
    
    Esta condición solo se comprobará si la primera condición falla (si el ordenador no eligió `1`)

+ Y finalmente, si el ordenador no eligió `1` ó `2`, entonces debe haber elegido `3`.
    
    Esta vez solo podemos usar `else`, lo que significa "de otra manera".
    
    ![captura de pantalla](images/rps-else-3.png)

+ Ahora, en lugar de imprimir el número aleatorio que eligió el ordenador, puedes imprimir la letra.
    
    ![captura de pantalla](images/rps-print-computer.png)
    
    Puedes, o bien eliminar la línea `print (elegido)`, o hacer que el ordenador la ignore añadiendo `#` al principio de la línea.

+ Prueba tu código haciendo clic en Ejecutar y eligiendo tu opción.

+ Hmm, la elección del ordenador se imprime en una nueva línea. Puedes arreglar eso añadiendo `end = ' '` después de `contra`, que le dice a Python que termine con un espacio en lugar de hacerlo con una nueva línea.
    
    ![captura de pantalla](images/rps-same-line.png)

+ Juega el juego varias veces haciendo clic en Ejecutar y tomando una decisión.
    
    Por ahora, tendrás que calcular quién ganó por ti mismo. Luego añadirás el código de Python para resolverlo.