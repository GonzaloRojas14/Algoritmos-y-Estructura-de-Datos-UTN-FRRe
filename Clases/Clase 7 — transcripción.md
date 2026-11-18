---
tipo: transcripcion
materia: Algoritmos y Estructura de Datos
clase: 7
tags:
  - AED
  - transcripcion
---

# Clase 7 — Algoritmos y Estructura de Datos

> [!info] Transcripción completa de la clase grabada
> Texto íntegro, sin resumir. Generada con Whisper desde `clase7.wav` y
> depurada con `dedup.py` (colapsa oraciones repetidas consecutivas, que son
> alucinaciones del modelo, no habla real del profesor).
> Video original: `temp_videos/clase7.mp4`

---

Ahí está. ¿Qué tipo de secuencias vimos la clase pasada? Secuencias de datos elementales. Bien. ¿Y esos datos elementales cuáles podían ser?

Carácter y numérico. ¿Sí? Los numéricos específicamente, ¿qué tipo de números? Enteros. O sea, tenemos secuencia de carácter y secuencia de enteros.

Solo eso. La secuencia de carácter, cuando nosotros avanzamos la secuencia, ¿qué avanzamos? Avanzamos la ventana y vamos leyendo carácter por carácter. ¿Está? Y si tenemos una secuencia de enteros, leemos un número completo, un entero completo.

¿Está? Cada vez que avanzamos. Las secuencias, podemos tener secuencias de entrada y secuencias de salida. Las secuencias de entrada, ¿qué acciones vamos a usar con la secuencia de entrada? Arrancar es lo primero que tenemos que hacer para poder trabajar con una secuencia de entrada y después avanzar para ir leyendo cada uno de los elementos de la secuencia hasta que llegamos al fin de secuencia.

¿Sí? Al fin de secuencia. Bien. Esa es la secuencia de entrada. ¿Se acuerdan la clasificación de las secuencias?

Puras e impuras. Y antes de eso, definida e indefinida. ¿Cuándo sabemos cuál es la cantidad de elementos. ¿Sí? Yo no la voy a tratar como un elemento de la secuencia?

Es impura. ¿Ah? Porque ahora vamos a ver un ejercicio donde dice que tenemos una cantidad de números de quit y que un quit es cero. Ese cero es un entero igual que los otros. ¿Sí?

Y conozco cuál es, pero sigue siendo impura porque a mí no me interesa ese quit cero. Ese quit cero o otra marca de fin de secuencia a mí me da lo mismo. No tengo que hacer nada con eso. ¿Se entiende? Ok.

Bueno. Secuencias de salida. Cuando yo tengo que crear una secuencia. ¿Cuáles son las acciones que voy a usar? Crear secuencia.

Perfecto. Escribir secuencia y ventana. Lo que voy a hacer en ese caso es insertando elementos en esa secuencia. Y cuando termino de trabajar con la secuencia, ¿qué tengo que hacer? Cerrar la secuencia.

Exacto. Las secuencias que usé inclusive las secuencias de entrada. ¿Ok? Bien. Ahora vamos a hacer algunos ejercicios acá, entre todos.

Y después ustedes van a hacer un par de ejercicios más. Y después vamos a comenzar con el próximo tema que es subsecuencias. Solamente va a ser una introducción hoy. ¿Está? Fíjense.

Muy rápidamente vamos a hacer. El ejercicio 2, 1, 4, 10, se dispone. Se dispone. Se dispone de una secuencia de número de socios y se dispone de una secuencia de número de socios y se dispone de una secuencia de número de socios y se desea saber la cantidad de socios que están registrados. Fácil, difícil.

Muy parecido al ejercicio que hicimos la semana pasada. ¿Se acuerdan que la semana pasada hicimos un ejercicio donde íbamos avanzando y íbamos contando los elementos? Esto sería lo mismo. Exacto. Entonces, fíjense.

Acción, ejercicio 2, 1, 4, 4, es ambiente. Tenemos una secuencia que en este caso es una secuencia de qué? Secuencia de entero. ¿Sí? Y nuestra ventana que es un qué?

Entero. Muy bien. ¿Y qué me dice? ¿Qué me pide el...? Entonces, ¿qué necesito?

Necesito un contador. Exacto. ¿Qué va a ser de qué tipo? Entonces lo puedo... Dale.

Un poquito. Sí. Proceso. ¿Cómo comienza mi algoritmo. Perfecto.

Arrancando mi secuencia. Y después de arrancar, avanzo e inicializo el contador. Puedo hacer en distinto orden eso. Avanzar. Secuencia.

Sec B. Perfecto. Avanzo secuencia ventana. Inicializo mi contador. En C.

Bien. ¿Y después? ¿Qué hago? Mientras que no fin de secuencia. Y acuérdense.

Y acuérdense siempre tengo que poner el nombre de la secuencia a cero. Y acá, ¿qué hago? Entonces, con más uno. Y después avanzo. Fin.

Mientras. ¿Y terminó? Después hago una escribir y muestro el contador. Y listo. Y después cierro.

Dijimos una buena práctica. Cierro mi secuencia. ¿Sí? Y fin. Acción.

¿Estamos? Fácil o no? Fácil o no. Escribir. Y acá tengo sec 1.

¿Cómo a qué? Cómo a B. Yo puedo usar la misma variable ventana. El contenido de ventana lo voy a grabar en la secuencia de salida. ¿Está?

Bien. Perfecto. Ahora, supongamos, supongamos que no quiero copiar todos los números. Supongamos que quiero copiar solamente los números pares. No sé por qué.

Se me ocurrió. Y que quiero contar solo los pares. ¿Qué tengo que hacer acá? Poner un condicional. ¿Qué pregunto?

Si vemos dos es igual a cero, entonces lo cuento, lo copio en la secuencia de salida, y si no, ¿qué hago? No, porque dije que voy a contar solamente los pares, solamente los que copio a la otra. Y acuérdense, si es par, tengo que avanzar, y si no es par, también tengo que avanzar. Entonces, cuando yo algo tengo que hacer tanto por el sí como por el sí no, lo tengo que hacer afuera del condicional. Entonces, lo tengo que hacer afuera del condicional.

Entonces, cierro mi condicional y avanzo. Entonces, fíjense qué hago acá. Estoy preguntando si es par, si es par, lo cuento, lo copio a la secuencia de salida, y después, ya sea que haya sido par o no, avanzo. Y así hasta toda la... ¿Cómo?

¿Cómo por el anterior? Esperá, esperá. Yo cambié la consigna. Yo dije que voy a contar solamente los pares. Voy a contar solamente los que copio a la secuencia de salida.

¿Está? Cambié la consigna. ¿Estamos de acuerdo? Bueno. ¿La creé?

Acá, este escribir... Eso es importante, lo que pregunta el compañero. Si yo hago escribir benomas, lo voy a mostrar por pantalla. Si yo hago escribir y tengo dos parámetros, sec, sec, b, lo que estoy haciendo es grabando en una secuencia de salida. No estoy mostrando por pantalla.

¿Está? ¿Sí? O sea, eso es distinto a un escribir b. ¿Está? Ya está, ya hablamos.

Ya vimos. ¿Estamos? Bien, exacto. Acá cierro la secuencia y cierro la sec 1. ¿Está?

No vayan a hacer esto. Sec, sec 1. Porque está mal. No puedo cerrar dos sec 1. Porque está mal.

No puedo cerrar dos secuencias con una misma acción. Se cierra con una. Así como si yo tuviera dos secuencias de entrada, tengo que hacer arrancar cada una de ellas. ¿Está? Lo mismo cuando inicializo variables.

Exacto. Bueno. Ahora que te he entendido este ejercicio, vamos al fácil, vamos al difícil. La secuencia de socios del problema anterior tiene un inconveniente. Los números están ordenados, pero no son correlativos.

Se desea generar una secuencia que contenga los números de socios que no figuran en la secuencia de socios. A ver, le voy a mostrar. Supongamos que yo tengo el socio número 1, después tengo el 4, después tengo el 10, después tengo el 11, después tengo el 15, después tengo el fin de secuencia. ¿Sí? ¿Se entiende?

Los números están ordenados de menor a mayor, pero no son correlativos. ¿Está? Entonces, ¿qué me pide la consigna? Que yo genere una secuencia que contenga los números de socios que no figuran en la secuencia original. En ese caso, mi secuencia de salida, ¿qué números tendría que tener?

2, 3, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 11, 12, 13, 14, 12, 13, 14. Bueno. Pensemos. Yo tengo mi secuencia de entrada. ¿Cómo voy a, a ver, cómo imaginan el algoritmo?

¿Cómo podríamos hacerlo? Exacto. Tiene que ir comparando entre los dos elementos. Primero tiene que comparar el 1 con el 4, el 10. Así.

Entonces, para eso, ¿qué necesito almacenar esa ventana en un auxiliar y avanzar. Entonces, voy a tener los dos valores. ¿Sí? Bien. Entonces, pensemos.

¿Por qué? ¿No? No, vos solo, tu algoritmo solo tiene que hacerlo. Tiene que, todos los números que no están acá, que están en el medio, tienen que, estar en tu secuencia de salida. O sea, no tenés que preguntarle si es 2 o si es 3.

Sí. Ajá. Sí. No, no, no. No estamos hablando de registro.

Estamos hablando de secuencias. Lo único que tenés son números. No tenés otros datos. No tenés nombre. No tenés nada.

Acuérdate, estamos en secuencia de datos elementales. Ahora tenemos números. Bien. Entonces, yo lo primero que tendría que hacer, es, ¿cuál es, cuál es, cuál es mi ambiente. No.

Cada vez que vos haces un avanzar, cada vez que vos haces un avanzar, ¿cuál es mi ambiente? No. Cada vez que vos haces un avanzar, ¿cuál es mi ambiente? Sí. Primero, uno pasa.

Uno, lo guardás automáticamente en la lista de... No, no, no guardás automáticamente nada. No podés guardar automáticamente nada. A ver, a ver. Sí, pero no.

No automáticamente nada se hace automáticamente acá. Nosotros tenemos el ambiente va a ser mi secuencia. Sí. Vamos a ponerle nombres más descriptivos. Es, ¿qué decía?

Socios. Entonces vamos a ponerle socios y después vamos a ponerle no socios y vamos a ponerle secuencia de entero. ¿Está? Y a mi B mi B voy a hacer de tipo entero y voy a usar también un auxiliar de tipo entero. Voy a usar también un auxiliar de tipo entero.

¿Está bien? Listo. Creo que por ahí nomás. Entonces, proceso. ¿Qué es lo primero que tengo que hacer?

Arrancar cuál. ¿Qué es? Socios. Perfecto. ¿Y qué más tengo que hacer?

Avanzar. Socios. B. ¿Y después? ¿Cómo?

Crearnos socios. Perfecto. ¿Y después? Dijimos que teníamos que hacer algo. Claro, claro, claro, claro, claro, claro, claro, claro, claro, claro, claro, claro, claro, claro, claro, tengo que comparar, pero para poder comparar, pero para poder comparar, tengo que tener con qué comparar.

Yo en este momento, si esta fuera mi, si esta fuera mi, si esta fuera mi, mi secuencia, ¿sí? ¿Dónde estaría parado yo? En el 1. ¿Y tengo con qué comparar? Entonces, ¿qué tengo que hacer?

A la variable auxiliar, ¿qué le asigno? B. Y después, avanzo de nuevo. Entonces, ahora, mi auxiliar, ¿qué va? ¿Dónde está?

En el 1. Auxiliar está en el 1. Y B. Perfecto. ¿Qué?

Yo sé qué números tengo que escribir en la salida. ¿Sí o no? Los que no están en la secuencia de entrada. ¿Sí? En este caso, ¿qué números serían?

Sí, sí, pero pará. No nos apuremos. Estamos en el 1 y en el 4. Entre esos dos números, entre esos dos números, entre el 1 y el 4, nos falta el 2 y el 3. ¿Sí?

Si yo tengo, esperemos, esperemos. Una estructura que a mí me permita ir desde un número hasta otro número. Si yo conozco esos dos números. Ajá. ¿Y yo conozco los números o no?

No, ¿cómo de 1 a 15? Eso es un ejemplo, pero no. ¿Y de...? ¿Cómo? No es hasta el auxiliar.

Yo el auxiliar. El auxiliar tiene un 1. Yo el 1. ¿Lo quiero escribir en la salida? No.

¿Pero qué número sí quiero escribir en la salida? Auxiliar más 1. ¿Sí? Hasta B menos 1. Entonces, para I que va desde auxiliar más 1 a B menos 1 a ser B.

Exacto. No voy a escribir auxiliar, voy a escribir I. Porque el I va a ir desde el 2. Hasta el I. No tengo.

No hace falta que compare. Cuando yo ya terminé de escribir el 2 y el 3. Yo sé que ya no. Hasta este momento. Cuando estoy parado acá en este fin para.

Ya no. No tengo que escribir más nada. Ahora sí tengo que avanzar mi B. Para ver los otros dos números. Pero antes de avanzar B.

¿Qué tengo que hacer? Tengo que hacer estas dos acciones. Resguardo. Mi B en el auxiliar. Y recién después.

Avanzo. Así también. Acá. ¿Se dan cuenta? Y después.

Vamos a ver. Miren. La primera vez. Vinimos hasta acá. Y dice para I que vas desde 2 hasta 3.

Hacer. Y escribe el 2. Escribe el 3. Y sale. Cuando sale.

¿Qué hace? Auxiliar que le asigna. Cuando sale. 4. Y ven pasa a 10.

Perfecto. Acá ya escribió el 2 y escribió el 3. Sube de nuevo a la línea 33. Y pregunta. ¿Es fin de secuencia socios?

No. Entonces entra. Y ahora ¿qué hace? Un paraí que va desde qué hasta qué? Desde 5 hasta 9.

Y entonces escribe 5, 6, 7, 8, 9. Y sale. Cuando sale. Cuando sale de ahí. ¿Qué hace?

Auxiliar le asigna 10. Y a B, 11. Bien. Vuelve a la línea 33. ¿Eh?

Fin de secuencia. Y ahora. De 11 a 10. Y sí. Tendríamos que ver esto.

Tendríamos que ver qué hace ahí. Sí. Porque. Tendríamos que ver. Tendríamos que ver qué hace ahí.

Tendríamos que ver. No tengo más. No tengo otra cosa que números. Es una secuencia de enteros. Solo tengo números.

Claro. Si B menos Aux. ¿Está bien? Sí. Ahora recién.

A ver. Vamos a ver. ¿Cómo? No importa. Va a analizar desde el 2 en adelante.

El 1 no. El 1 no ponemos. Lo mismo que no ponemos ningún número de anterior al primero ni posterior al último. ¿Sí? En el D.

Autista. Ok. A ver. Secuencia entero. Este me va a agregar el número que falta.

Arranca. Avanza. Crea la salida. A comp le pone 1. Por favor que comienza en 1 y sigue el orden lógico que debería tener.

Mientras no piense en secuencia. Si B es distinto de comp. A ver. Si B es distinto de comp. Entonces grabar.

No. No usen grabar. Usen escribir. Sal comp. A comp le pone.

Comp más 1. Ajá. Si B igual a comp. Entonces avanza. Y si B no es comp.

Podría funcionar. O sea. Vos lo que haces es desde el 1. Desde el 1 hasta el último. Puede funcionar.

¿Se entiende? Sí. Igual está en el Discord. Así que después lo analizan. Pero creo que está bien.

Bien. Vamos con este. Con el 2, 1, 7. Tenemos una secuencia de enteros que contiene todos los quits de los empleados de una empresa y la misma termina con el quits de los empleados de una empresa y la misma termina con el quits de los empleados de una empresa y la misma termina con el quits cero. Entonces es una secuencia definida o indefinida.

Indefinida. No sé cuántos empleados tengo. No sé cuántos quits tengo. Y es pura o impura. Impura.

¿Por qué? Porque el cero para mí es lo mismo que una marca. No es un quits que yo tenga que tratar. ¿Está? Bien.

Entonces, ¿qué? ¿Qué estructura voy a usar para recorrer esta secuencia. Un mientras. Bien. ¿Todos saben lo que es el quits de una persona?

¿Sí? No necesariamente. Quits es la clave única de identificación tributaria. Cualquier empresa o cualquier persona que sea monotributista tiene quits. Si no, tiene un quits que es clave única de identificación laboral pero el mismo número.

O sea que el quits o quits es lo mismo. Y es un número de cuántos dígitos. 11. Y al final tiene un dígitos. Documento.

No al último dígito del quits. Al último dígito del documento. Generar una secuencia con los quits de las personas cuyo número de documento termine con 0, 1, 2 o 3. ¿Se entendió? ¿Qué tenemos que hacer?

Ese. Esa pregunta es buenísima. Porque es un error muy común. Es un entero. No voy a pararme.

No voy a ir avanzando dígitos. Porque no es una secuencia de caracteres. Es una secuencia entero. Cuando yo hago avanzar ya estoy parado en el quits entero. Entonces fíjense.

Eso es muy bueno que lo tengan en claro. Si yo tengo una secuencia de caracteres y yo tengo un quits. Si yo tuviera un quits 20, 24 o lo que sea. Yo tendría un 2, un 0. Eso sería una secuencia de caracteres.

Pero si yo tengo una secuencia de enteros voy a tener en cada posición. En cada posición. En cada posición voy a tener el quits completo. Puede ser que sí. Puede ser que no.

A ver. ¿Cómo? Con mod 10 yo voy. A ver. Espérenme.

Si yo tengo 20. 8. Miren. Este quits tendría que ir en la secuencia de salida. ¿Sí o no?

¿Por qué no? Bien. Y si yo cambio este y le pongo acá. Al hacerle div 10. Le tengo que hacer mod 10.

¿Se dan cuenta? Al hacerle div 10. Yo estoy separando esto. Y me quedo con este número. Pero sin el 8.

Y a eso le hago el mod. Y me quedo con el 3. ¿Sí? Si hacemos 100. ¿Cuánto te queda?

38. Y 38 no te va a dar nunca. Div 10. ¿Eh? No.

Mod 100. ¿Entendés? Pero así. A ver. Esta me parece la manera más fácil.

Si le hacemos div. Me quedo con todo el número menos el último. El último lo pierdo. ¿Está? Pero el último igual no me importa.

Porque el último es del quits. Y a ese le hago mod 10. Y ahí me quedo solo con el último. ¿Se entiende? Más o menos.

Almacenando no. Lo tengo que usar en la pregunta. Lo tengo que usar en la pregunta nomás. Pero yo no tengo que modificar mi quits. ¿Por qué?

Porque lo que me pide la consigna es que el quits entero lo guarde en la secuencia de salida. Entonces yo no tengo que modificar en ningún momento el quits. A ver. Entonces. 1.7.

Ambiente. ¿Qué voy a tener de ambiente? Sí. Empleados. Vamos a ponerle.

Empleados. Y después. No sé. Salida nomás. Vamos a ponerle para que.

¿Está? ¿Qué va a ser una secuencia de? Secuencia de entero. Perfecto. Y después voy a tener que va a ser mi ventana.

Perfecto. Me gusta. Vamos a ponerle cero a tres. Que va a ser un conjunto. Entonces si es un conjunto va a ser igual.

Abro el paréntesis. Y pongo cero. Dos. Tres. ¿Está bien así o entre comillas?

Así está bien porque son números. Exacto. Muy bien. Entonces. Proceso.

Menor a cuatro. ¿Qué podría ser? También. El conjunto. Sí.

Puede ser. Ahí lo vemos. Entonces. ¿Cómo empiezo? Ni duden.

Eso tiene que ser rápido. Arrancar ¿qué? Arrancar empleados. Perfecto. Después.

Avanzar. Empleados. Dos. Coma. Quit.

Y después. Crear. Salida. Bien. Muy bien.

Ahora. Mientras que. No. Fin de secuencia. Dijimos que era.

Impura. Sí. Ah. Podemos preguntar esto. Como la consigna me dijo que va a terminar con el quit cero.

Vamos a hacer así. Mientras quit sea distinto de cero. Entonces. Mientras quit sea distinto de cero. Entonces.

Mientras quit sea distinto de cero. ¿Qué hacemos? Hacemos esta pregunta. Exactamente esta pregunta que puede ser poquito compleja pero la podemos hacer en una sola en una sola en un solo renglón. Decimos si quit div diez.

Div diez y a eso le hacemos mod diez y es como dijo Guido podemos preguntar como es un número podemos preguntar si va a ser menor a cuatro. Menor a cuatro porque es cero, uno, dos, tres. ¿Qué hacemos si es menor a cuatro? Salida. ¿Sí?

Vieron que el quit me pide la consigna que sea entero. Entonces no tengo que modificarlo por nada del mundo. Puedo hacerle div, mod, lo que sea pero no tengo que guardar esa operación porque lo necesito entero. Bien. Si quit.

Entonces escribo y si no. Y si no. Y si sí. También avanzo. Entonces.

Acuérdense. Cuando algo lo tengo que hacer por el sí y por el no va afuera del condicional. Termina mi condicional y ahora avanzo. Y después. Y mientras.

Cerrar salida. Cerrar empleado. Y no. Ahí dice esto. Esto no haría falta.

Y no. Ahí dice esto. Claro. Si ustedes ven que por ahí se olvidó. No.

Ahí dice esto. Bueno. Vamos a cambiar. Bueno. Vamos a ver primero el 222 porque es más fácil.

Y van a ser desde acá. Desde acá para allá van a ser el 2 y de acá para allá van a ser el 1. Dice. Dada una secuencia de caracteres de entrada. Caracteres.

No números. No enteros. Desarrollar un algoritmo que produzca dos secuencias de salida. Una con los caracteres numéricos y otra con los que no son numéricos. Y tienen que decir la cantidad de caracteres de cada una de las secuencias de salida.

Y hay un ejemplo. Si en la secuencia de entrada viniera a 1, 2, 5, e, b porcentaje. En la en una salida tendría que ir el 1, el 2 y el 5. Obviamente en en tres escribir distinto. 1, 2, 5 y en la otra salida a, e, b porcentaje.

Se entiende. Tienen 5. Sí. Y ahora el 2.2.1 para acá. El 2.2.1 para acá.

Bueno. Se entiende. 2, 5. 3.2. 3.2.1.

¿Leyeron algo de subsecuencias? Son secuencias, son mini secuencias que están dentro de otras secuencias. ¿Qué tenemos que saber de las subsecuencias? Que cumplen con los mismos requisitos que las secuencias grandes. Tienen un primer elemento, tienen un último elemento, cada elemento tiene un elemento posterior, salvo el último, esas subsecuencias pueden ser definidas, indefinidas, puras o impuras.

Y hay una clasificación de las subsecuencias que lo vamos a ver en la clase que viene, pero vamos a hacer un pequeño adelanto y ahora vamos a hacer un ejercicio. Las subsecuencias entre sí pueden tener dos tipos de relación. Pueden ser subsecuencias enlazadas, eso significa que va a venir una después de la otra, o podemos tener subsecuencias jerárquicas, que significa que va a estar una adentro de la otra. ¿Se entiende? ¿No se entiende?

Las subsecuencias jerárquicas lo vamos a ver bien en la clase que viene, pero solamente lo menciono para que ustedes sepan que hay dos clases. Las subsecuencias jerárquicas, y las subsecuencias jerárquicas lo vamos a ver bien en la clase que tienen una clase que tienen una clase que tiene una clase que tiene una clase que tienen una clase que tiene una clase que tiene una clase que tiene una clase que tiene ¿Está el control? ¿Alguien pido el control? ¿Se apagó? ¿Cómo que no tiene control?

¿Nos chorrieron el control? ¿Si está en la clase pasada? A ver... Bueno, a ver, entonces, decimos que una subsecuencia, chicos, la subsecuencia palabra comienza con un carácter distinto de blanco y termina con un carácter distinto de blanco. Esas subsecuencias que van a ser palabras inválidas, podemos llamarle, o blancos.

Si esas subsecuencias están una después de la otra, ¿cómo son? ¿Enlazadas o jerárquicas? Enlazadas. Ahora, después vamos a ver que esas palabras van a estar dentro de una oración, pero entonces ahí, ¿cómo son esas subsecuencias? ¿Cómo son esas oraciones jerárquicas, porque una oraciones jerárquicas, porque una están adentro de la otra, ¿sí?

Esas oraciones pueden estar adentro de un párrafo, y ese párrafo va a estar adentro, o sea, podemos tener más de un párrafo que están adentro de la secuencia general, ¿sí? ¿Para qué me sirve determinar si dos subsecuencias son enlazadas o son jerárquicas? Por lo siguiente, cuando yo tengo, cuando yo tengo, cuando yo tengo, cuando yo tengo subsecuencias enlazadas, los ciclos enlazadas, los ciclos con los que yo los voy a manejar, van a estar uno después del otro, ¿sí? Entonces, ahora vamos a ver un ejemplo de palabras y espacios en blanco, donde vamos a tener un ciclo que va a manejar los espacios en blanco, y un ciclo que va a manejar las palabras, y van a estar uno debajo del otro. Por el contrario, cuando tengamos, subsecuencias jerárquicas, los ciclos van a estar uno dentro del otro.

Entonces, supongamos que yo tengo que tratar una oración que termina con un punto, entonces voy a hacer mientras mi ventana sea distinto de punto, y adentro de ese mientras voy a tratar los blancos y las palabras. Porque los blancos y las palabras son jerárquicos con respecto a las oraciones. ¿Se entiende? Más o menos. Esa es toda la introducción que vamos a dar hoy, ahora vamos a hacer un ejercicio.

Fíjense. Dice, se dispone de una secuencia de caracteres. Se desea determinar la cantidad de palabras que comienzan con la letra I. Siempre vamos a asumir, cuando tengamos una secuencia de caracteres, vamos a asumir por las dudas que es una secuencia donde tengamos palabras y blancos, vamos a asumir que podría empezar con un blanco. ¿Por qué?

Porque podría empezar con un blanco, y si no empieza con un blanco, no pasa nada. Ahora lo vemos. Entonces, supongamos que yo tengo un blanco acá, y después acá tengo dos blancos, y acá viene el fin de secuencia. ¿Sí? Supongamos que esta es mi secuencia.

Y a mí me dicen, necesito que vos cuentes la cantidad de palabras que comienzan con una letra I. Bien. ¿Cómo haríamos? Acción, ejercicio 2.1.9. Tenemos una secuencia que le vamos a llamar secuencia de carácter, ventana, y el proceso.

Entonces, ¿qué hago primero? Arranco la secuencia. Después, avanzo secuencia ventana. Bien. Me pide que cuente las palabras con hino, ¿cierto?

Entonces, vamos a necesitar un contador. Dentro de, dentro de, dentro de, dentro de, dentro de, dentro de, dentro de la secuencia, yo solamente tuviera palabras y blancos. Esas palabras y blancos con respecto a la secuencia general, ¿cómo son? ¿Cómo, qué relación tienen? Jerárquica o enlazada.

Son enlazadas entre ellas, pero con respecto a la secuencia general son jerárquicas porque están adentro. Las palabras están adentro de todas las, de la secuencia, y los blancos están adentro de todas las secuencias. Entonces, el ciclo que yo voy a usar para manejar esos blancos y esas palabras está, adentro de todas las secuencias. Adentro de todas las secuencias. ¿Sí?

¿Y ahora qué tengo que hacer para saber si esa palabra empieza con i o no? ¿Qué pregunto? Si b es igual a i, entonces, ¿qué hago? Al contador de palabras con i, ahí, más uno. Tengo una palabra más que comenzó con i.

¿Eh? ¿Y después qué hago? In sí, porque si no empieza con i no tengo que hacer nada. ¿Está? ¿Se contó?

Y ahora, ¿un solo avanzar? Tengo que avanzar toda la palabra. Entonces, fíjense, esta es la subsecuencia de blancos. Y debajo va a venir la subsecuencia de palabra. Y como son enlazadas, está un mientras debajo del otro.

Entonces, mientras, b, distinto de blanco, hacer. Pero ojo, eso... Eso no es todo. Porque fíjense acá. En este ejemplo.

En hola. Me funciona. Yo voy a avanzar acá. Voy a avanzar acá. Y fin de secuencia es distinto de blanco.

Entonces, cuando yo llegue acá, si yo no controlo esto, va a querer seguir avanzando y eso me va a dar un error. Entonces, cuando yo pregunto por distinto de blanco también tengo que preguntar por no fin de secuencia. Porque puede pasar que después de avanzar los blancos te encuentres con una letra y después de la letra te encuentres con el fin de secuencia y no te va a dar tiempo para llegar acá. Entonces, acá, ¿qué hago? En este caso, en esta consigna, solamente avanzo.

Y cuando salgo a la letra te encuentre con la letra. Con pal lo tengo que inicializar también acá. Con pal. Dígame la línea. ¿Puedo decir?

Espérenme, espérenme. A ver, tenemos dos opciones acá. Uno es contar las palabras que comienzan con i y las que no comienzan con i y después sumarlas. Esa es una. Y la otra es contar las palabras que comienzan con i y todas las palabras.

¿O no? Yo al contador de palabras lo podría poner acá. Con pal. Así, ¿no? Con pal más uno.

¿Eso? Yo cuando llegué acá yo sé que tengo una palabra. ¿Sí? Y si además esa palabra comienza con i y si además esa palabra comienza con i lo voy a contar acá. Los espacios con blanco no son palabras.

¿Por qué si acá está el fin mientras de los blancos? Acá terminó el de los blancos. Ahí. Acá en la línea 118 yo sé que estoy al comienzo de una palabra. No sé todavía si comienza o no comienza con i pero no me importa.

La cuento y después pregunto si comienza con i. Entonces cuento palabra con i. ¿Está? Entonces con este contador yo ya tengo las palabras que comienzan con i y todas las palabras que tienen mi secuencia. ¿Sí o no?

Y entonces ¿qué tengo que hacer? Exacto. Entonces. Pero no hace falta porque puedo hacer el cálculo en el escribir nomás. Escribo.

Porcentaje de palabra. Tras. Con i. Coma. Y ahí hago la cuenta.

Hago. Cont. Pal. I. Sobre.

Cont. Pal. Porcentaje. ¿Listo? ¿Está bien?

Exacto. Voy a cerrar. Sec. Y nada más. ¿Sí?

Bueno. Bien. Coma. Comilla. Porcentaje.

¿Sí? ¿Está bien o no? Pero lo que más quiero que ustedes comprendan de tema de subsecuencias es esta diferencia de cuando son jerárquicas cuando son enlazadas. Enlazadas una después otra. Supongamos que fíjense qué interesante.

Supongamos este ejemplo que tenemos acá. Por más que no esté muy lindo acá viene un nombre de una persona un guión y su número de otra persona. Un guión y su número de otra persona. Un guión y su número de documento. Y así podrían venir un montón.

¿No es cierto? ¿Sí? Ese nombre y ese número de documento. ¿Cómo son? Subsecuencias enlazadas.

Porque viene una después de la otra. ¿Sí? Y yo. Entonces si dijimos que tenemos subsecuencias enlazadas vamos a tener una estructura cíclica y abajo otra estructura cíclica y abajo otra estructura cíclica. Bien.

La subsecuencia de nombre. ¿Cómo es? Siempre. O sea. Siempre cuando veamos esto van a ser de caracteres.

Pero es indefinida. O sea que yo necesito tener un carácter que me indique que el nombre terminó. En este caso ¿Cuál es el carácter? El guión. Entonces cuando yo trate esta una secuencia como esta tengo que poner un parácter.

Mientras ve distinto guión. Porque eso me va a indicar que yo voy a estar tratando el nombre. ¿Ok? Debajo de ese ciclo cuando termina mi fin mientras tengo que tratar el documento. ¿Ok?

El documento ¿Cómo es? Definida. Porque yo sé que tiene ocho caracteres el DNI. Y entonces ¿Qué estructura cíclica voy a usar? Un par.

Para ahí que va de uno a ocho y yo voy a ir tratando cada uno de los caracteres del documento. Y yo voy a ir tratando cada uno de los caracteres del documento. Sí. Eso blanco. No le hagan caso.

Ustedes asuman que es todo seguido. Sí, sí. Ahí viene dos, cinco, cuatro, cinco, seis. No, eso es mi pantalla. Sí.

Sí, fíjate que viene. ¿Está? ¿Se entiende? Pero fíjense. Tenemos una estructura que es impura la tratamos con un mientras.

Otra estructura que es definida y la tratamos con un para. Esas dos subsecuencias. Esas dos subsecuencias entre sí son enlazadas. Viene una estructura repetitiva y debajo otra estructura repetitiva. ¿Ok?

¿Y así como está ahí no se puede usar el espacio en blanco? No, no, pero el espacio en blanco está mal. En una secuencia de así de datos de personas no deberías tener ahí ese. A ver, si el nombre de la persona fuera un nombre completo, segundo nombre, segundo nombre y apellido, ahí adentro vas a tener que tratar también palabras y blancos. ¿Está?

Puede pasar eso también. Sigue siendo enlazada. Pero fíjate una cosa. Si vos asumís que tenés una secuencia, una subsecuencia que se llama nombre completo, que termina con un guión, vas a tener mientras, ve, distinto de guión, adentro de ese nombre completo vas a tener palabras y blancos. ¿Y esas palabras y blancos cómo son con respecto al nombre completo?

Herárquica. Entonces, los mientras que van a tratar los blancos y las palabras tienen que estar adentro del mientras ve distinto de guión. ¿Sí? ¿Se entiende? Súper.

Entonces, ahora, con esto que dimos, ustedes ya pueden hacer los ejercicios de... El DOG110, por ejemplo, lo pueden hacer. Porque es muy parecido al que hicimos. Porque es muy parecido al que hicimos solamente que le tienen que pedir al usuario que ingrese una letra. El DOG111 también lo pueden hacer.

El DOG111 también. Fíjense que acá cantidad de palabras que tengan cuatro letras. ¿Cómo harían? Pero ¿cómo? Acá, en este algoritmo, ¿dónde metemos algo?

¿Dónde metemos el contador de las letras? Exacto. Acá. Mientras vos vas avanzando las letras de una palabra, vas contando. Contador de letras.

hagamos un ejercicio tipo parcial de años anteriores para que ustedes tengan una idea de cómo son los ejercicios. Dale. Ok. Sí, nos dirámos. Mirámos la grabación.

¿A qué hora empieza el...? ¿Está bien? Sí, está bien. ¿Está bien? Sí, está bien.
