---
tipo: transcripcion
materia: Algoritmos y Estructura de Datos
clase: 2
tags:
  - AED
  - transcripcion
---

# Clase 2 — Algoritmos y Estructura de Datos

> [!info] Transcripción completa de la clase grabada
> Texto íntegro, sin resumir. Generada con Whisper desde `clase2.wav` y
> depurada con `dedup.py` (colapsa oraciones repetidas consecutivas, que son
> alucinaciones del modelo, no habla real del profesor).
> Video original: `temp_videos/clase2.mp4`

---

Grabando la clase. Después de calcular C y D, ¿qué tengo que hacer? Escribir. Normalmente voy a mostrarle por pantalla que calcule algo. Voy a escribir.

Escribir el valor de C es, dos puntos, y después coma y pongo la C. La C la pongo sin comillas. ¿Por qué? Porque, exacto, todo lo que yo pongo entre comillas me sale como el texto así como yo lo escribí. La C sin comillas, lo que voy a mostrar por pantalla es el valor de la variable.

Y después hago lo mismo. Escribir, comillas, el valor de D es, y después pongo coma y pongo D. Bien. ¿Se entendió? También.

Fíjense, si yo quiero poner todo en una misma línea, tendría que poner C, coma, comillas de nuevo, valor de D es, ¿está? Hay un programa que nos permite ejecutar este algoritmo, ¿sí? Ese programa se llama P-Saint, ¿sí? Hago algunas aclaraciones. El programa está bueno, el programa me sirve para probar estos primeros algoritmos que nosotros vamos a hacer, pero hay algunas diferencias de sintaxis que tiene P-Saint con respecto al pseudocódigo que nosotros y el programa.

en las... El leer y el escribir en P-Saint va sin paréntesis, pero en la hoja haganlo con paréntesis. Bueno, el P-Saint tiene dos cosas que son útiles. Uno es ver el diagrama de flujo del algoritmo. Por ahí ahora que es un algoritmo secuencial, no tiene mucha importancia, pero por ahí después cuando veamos otro tipo de estructuras van a ver la diferencia.

Fíjense, se usa un óvalo para el inicio y para el inicio y para el final del algoritmo. Este sería el algoritmo. Este sería el ambiente. Estos símbolos representan. Este representa un escribir.

Fíjense que tiene una flechita hacia afuera y el leer se representa con la flechita hacia adentro. Los rectángulos son operaciones y después nuevamente tenemos dos escribir. Esa es una de las cosas que tiene P-Saint. Y otra de las cosas es que acá tiene un par de botones que le van a servir para ejecutar su algoritmo. El botón verde este le sirve para ejecutar su algoritmo.

El botón verde este le sirve para ejecutar rápido y el de los dos piecitos le sirve para ejecutar paso a paso. Ustedes acá, acá a la derecha pueden ir cambiando la velocidad de los pasos. Ahora le vamos a dejar acá y vamos a ejecutar paso a paso y fíjense que me va marcando en verde en qué paso está. Hizo el paso 5 de la línea 5 está en el paso 6. Como es un leer está esperando que yo introduzca dos valores.

Entonces vamos a ponerle, no sé, 18 A y 3 AB. Pueden hacerlo todas las veces que quieran y pueden ver. Eso es lo que dije hace un ratito. Se pueden leer, mirá, mirá acá. Se puede hacer así o se puede hacer un leer A y abajo leer B.

Como vos quieras. 3 variables, 4 variables, 5 variables, 6 variables. Y no, 5 variables. Y no, 6 variables. 7 variables.

Y no, 6 variables. 6 variables. 6. en la clase pasada. No hace falta poner punto y coma en PSAIN ni en pseudocodio.

Bueno, gracias. Súper. Bien. ¿Venimos bien hasta acá? En la guía, tanto en la guía web como en la guía PDF, ustedes tienen varios ejercicios.

Entonces, por favor, hagan estos ejercicios. ¿Sí? Venimos todo bien. Venimos con acciones secuenciales. Todo perfecto.

Pero a veces, a veces, vamos a necesitar evaluar alguna condición. Evaluar si alguna variable es mayor que otra, si es menor que otra, si es igual, si es distinta. Entonces, ya vamos a necesitar una acción, una estructura, ¿sí? Que sea un poquito más compleja. Y es, estamos hablando de las estructuras condicionales.

Las estructuras condicionales pueden ser de tres tipos. Simple, condicional alternativo y condicional múltiples. A ver si tengo por acá. Bien. Esto es lo que veníamos haciendo hasta ahora.

¿Sí? Algoritmo secuencial. Ahora, a veces vamos a necesitar evaluar una condición y si esa condición es verdadera, vamos a tener que hacer alguna acción. Y ahí tenemos las dos, los dos condicionales más simples que vamos a ver, que son el condicional simple, que son el condicional alternativo. ¿Cuál es el condicional alternativo?

¿Cuál es la diferencia entre los dos? Si esta condición es verdadera, entonces hacemos una o más acciones. Exacto. En el condicional simple hay solamente una acción o un conjunto de acciones si la condición es verdadera. Nada más.

Ahí terminó. ¿Sí? Fíjense, yo acá podría preguntar si ese total a pagar es mayor a 5 mil dólares. No sé, no sé, no sé, no sé, no sé, no sé, no sé, no sé, no sé, no sé, 5 mil dólares. Y si es mayor a 5 mil dólares, escribo, es muy caro.

Está bien. Entonces, fíjense, sí, cuál es el total a pagar precio de PC más precio de impresora. Yo podría preguntar si estos dos juntos son mayores a un valor. Sí, tranquilamente. Puedo preguntar por una variable o puedo preguntar por la suma de dos variables.

Si esta variable más esta variable es mayor a 5 mil, entonces, escribir muy caro. Y nada más. Fin, sí. Esto es un condicional simple. Evalúo una condición, si esa condición se cumple, hago una acción.

Puedo hacer varias acciones. Vamos a ver cómo funciona acá en el PSAIN. Fíjense cómo se ve el diagrama de flujo de ese condicional. Hay un rombo que tiene adentro la condición. Si esa condición es verdadera, hay una o más acciones.

Hay una o más acciones. Si es falsa, no hay nada. Ejecuto. Costo de PC, bueno, supongamos que la PC es, no sé, 3 mil 500 y de otro va a ser mil. Supuestamente ya con los costos y con las ganancias y los IVA.

¿Sí? El total a pagar dio 5 mil 900. Evalúo la condición. El resultado de esa condición fue verdadero. Ingresó.

¿Qué pasa si es falso? Vamos a hacerlo de nuevo. Vamos a ponerle 1.500. 1.500. Calcula.

Muestra. Muestra total. Evalúo la condición. ¿Cómo era la condición? ¿Verdadero o falsa?

¿Qué hizo? Nada. Si hubiéramos tenido otras acciones abajo, hubiera seguido por las otras acciones. Bien. Ahora, el condicional alternativo, que es el que más vamos a usar, tiene una acción por el verdadero, tiene una o más acciones y una o más acciones por el falso.

¿Sí? ¿Y cómo se escribe? Muy parecido, solamente que además, debajo del sí, voy a poner si no. Si no. Y después de ese si no, voy a tener una o más acciones.

Voy a escribir, puedo pagarla. Si yo voy a ver el diagrama, va a ser muy parecido al otro, con la diferencia que ahora por el falso también tengo acciones. ¿Está? ¿Y la ejecución? Fíjense.

Fíjense por dónde va marcando el verde. Evalúa. Fíjense por dónde va marcando el verde. Evalúa. Fíjense por dónde va marcando el verde.

Evalúa. Fíjense por dónde va marcando el verde. Evalúa. Fíjense por el sino porque era falso. Y entonces escribe.

¿Se entendió? Bien. También puede darse el caso que luego de un condicional, adentro de ese condicional, ya sea por el verdadero o por el falso, los dos, nuevamente tenga un condicional. Y eso se llama condicional, condicionales anidados. ¿Entiendes?

Vamos a hacer este, este ejercicio, lo vamos a hacer con condicionales anidados, el último condicional. Dice, lo que me pide es que yo monitoree los milímetros de agua caída, los milímetros de lluvia, y que emita un mensaje de acuerdo la cantidad de agua que cayó. Si cayó, si cayó, si cayeron más de 150 milímetros, tengo que decir, inundación inminente, ¿está? Cayó mucha agua. Si cayeron entre 100 y 150, muy peligroso.

Entre 70 y 100, y menos de 70, simple. Bien. A ver, ¿cómo sería esto utilizando condicionales anidados? Acción, lluvia, diente, abajo proceso, abajo proceso, y al final fin acción. ¿Está?

Bien. ¿Cuántas variables voy a tener? Lo único que tengo que hacer es pedirle al usuario que me indique cuántos milímetros de lluvia cayeron, y después tengo que evaluar esa cantidad y darle algún mensaje. Una variable que se va a llamar, puede ser cantidad de milímetros, puede ser simplemente milímetros, puede ser de qué tipo. ¿Va ser de qué tipo?

Podría ser real, pero generalmente los milímetros son enteros. Bien. ¿Cómo arranca mi algoritmo? Porque aparte, cuando ustedes escriban en la hoja, yo no vamos a ver si hubo espacio ahí. Yo con que vos me pongas dos puntos y el tipo de datos, ya estoy chocho.

¿Qué hacemos primero? Escribir qué cosa. Ingrese, normalmente cuando yo quiero que ingrese algo, le pido. Ingrese cantidad de milímetros de lluvia caída. ¿Sí?

¿Sí o no? Bien. Ahí está. Yo le digo lo que él tiene que ingresar. Y después de eso, ¿qué hago?

Leer qué cosa. Leer paréntesis, mm. Acuérdense, el P6 no le va a dejar poner paréntesis, pero ustedes en la hoja pongan los paréntesis. Leer milímetros. Bien.

¿Y ahora qué tengo que hacer? Sí, mm. Fíjense, mayor que 150, inundación inminente. Bien. Si mm es mayor a 150, entonces escribir.

Exacto. Inundación inminente. Perfecto. Ahora, ahora, si no es mayor a 150, ¿qué pasa? Si no, mm así suelto.

Si yo quiero hacer un condicional anidado, tengo que volver a poner sí. Si es mayor a 100, ¿está? No hace falta preguntar si es menor a 150. ¿Por qué? Porque como acá ya me dijo que era falso, yo ya sé que es menor a 150.

Menor o igual. ¿Se entiende eso? Si mm es mayor a 100, entonces, ¿qué tengo que escribir? Muy peligroso. Pero puede darse el caso de que tampoco sea mayor a 100.

Entonces, si no, ahí está preguntando en el Zoom si se pone o no se pone el igual. Todo depende en el igual. Todo depende de lo que te diga acá. Acá. Acá dice mayor a 150 y no dice igual.

Entonces, si es igual, esto es falso. Va a venir por acá. Lo mismo pasa con el mayor a 100. Mayor a 100 dice acá. No dice mayor o igual.

Entonces, yo en mi condición voy a poner mayor. ¿Está? Si no es mayor a 100, significa que va a entrar en este o en este. Ahora, ¿cuál es el tercer? La tercera categoría que podría ser que podría ser que sea mayor o igual.

Acá sí voy a poner igual. Acá sí voy a poner igual a 70. Acá sí voy a poner el igual porque me está diciendo mayor o igual a 70. Entonces, ¿qué escribo? Poco peligro.

Y si no, si no es mayor o igual a 70, ¿hace falta que pregunte si es menor a 70? Y no, porque ya no, porque ya no fue mayor a 100, no fue mayor a 100, no fue mayor a 100, no fue mayor a 70. La única que queda que sea menor. Entonces, directamente escribo, escribo sin peligro. Y ahora, tengan cuidado con esto.

Por cada sí, tiene que haber un fin sí. Entonces, yo tengo un fin sí acá, un fin sí acá y un fin sí acá. Son tres sí anidados. Tengo fin sí, fin sí, fin sí, fin sí. ¿Está?

¿Se entendió? Lo probamos en el PC y no a ver si funciona. Acá entonces ponemos definir MM como entero. Proceso no lo ponemos. Y ponemos ingrese cantidad de milímetros de lluvia caída.

Leer, le sacamos el... Y ahora tenemos, fíjense, si MM es mayor a 150, escribimos, si no, si es mayor a 100, es peligroso, si no, etc. Fíjense el diagrama. Por el falso tengo otro condicional. ¿Sí?

También podría darse el caso de que por el verdadero tenga otro condicional. También es válido eso. ¿Sí? Lo probamos. ¿Cuántos milímetros?

200. Fíjense. 200. Pregunta. ¿Vieron?

El primer sí ya era verdadero. Entonces, entró, ejecutó la acción y salió de todo ya. Vamos a hacerlo de nuevo, pero ahora le vamos a poner... Esperen, vamos por parte. Vamos a ponerle exactamente 150.

¿Debería entrar en el primero o en el segundo? En el segundo. Porque 150 no es mayor a 150. Entonces, ponemos 150 y fíjense, evalúa la condición y directamente va al sino. Evalúa la otra, ahí sí es verdadero y dice muy peligroso.

Lo mismo va a pasar si ponemos 100. 100 no es mayor que 100. Debería entrar por cuál. Poco peligroso. Después, si ponemos 70.

Poco peligroso. Después, si ponemos 70 va a entrar por la tercera opción porque 70 sigue igual a 70. Entonces, vamos a ponerle 69 y ahí debería decir sin peligro. Falso. Evalúa otra condición.

Falso. Evalúa la otra. Falso. Bueno, ¿se entendió esto? En estas estructuras condicionales es donde nosotros podemos usar operadores lógicos.

Nosotros podríamos, por ejemplo, si yo tengo tres valores, si yo quiero saber cuál es el valor más alto, yo podría preguntar si A mayor que B y A mayor que C. Entonces ya sé que A es el más grande. ¿Se entiende lo que estoy diciendo? Yo puedo, mira, yo en una condición de estas, yo podría poner, suponete que yo hago un leer ABC, leo tres números, quiero saber cuál es el más grande. Entonces yo podría preguntar si A mayor que B y A mayor que C.

Entonces, si A es mayor que B y A es mayor que C, ¿cuál es el más grande? Lo que les quiero decir es que yo puedo hacer esta condición y unirla con otra condición, con un operador lógico. Exacto. ¿Se entiende? Bueno, después ya lo vamos a ver en algún ejercicio o en muchos ejercicio.

Ahora, vamos a ver el tercer condicional que se llama condicional múltiple. El condicional múltiple es un condicional que no se usa tanto, aunque a muchos les guste y lo quieran usar todo el tiempo. El condicional múltiple tiene algunas reglas para poder ser usado. Una sola variable. Si yo tengo que hacer A mayor que B, chau.

Eso ya no se va a usar condicional múltiple. Tengo que evaluar una sola variable. Y esa variable tiene que tener por lo menos tres valores o tres rangos distintos. ¿Por qué? Porque si esa variable tuviera dos valores, uso el condicional alternativo.

O sea, ¿vale esto o vale esto? Ahora, si tuviera tres valores, ahí sí tiene sentido. Ahí sí tiene sentido que usen un condicional múltiples. Ahí sí tiene sentido que usen un condicional múltiple. Claro, no, pero sí.

Ahí ya tengo dos variables. Pero lo hacen. Ah, bueno, pero no lo tienen que hacer. Bueno, a ver. Les voy a mostrar un ejemplo.

Un ejemplo muy típico del condicional múltiple. Supongamos que yo le pido a alguien que me ingrese en qué día de la semana estamos en el número. Y le voy a decir también un menú también podría ser. Eso lo vamos a ver más adelante. Le pregunto que me diga, supongamos que el lunes es mi día uno y mi domingo es mi día siete.

Digo que me diga qué día y yo le voy a decir qué día la semana estamos. ¿Sí? ¿Cómo sería eso? A ver. Acción día sem.

Vamos a poner ambiente. Y ahí vamos a tener una variable que va a ser día y que podría ponerlo como entero o en segundo código lo puedo poner como de uno a siete. No puede valer ni cero. No puede valer ocho. Entonces, proceso.

Vamos a escribir. Ingrese. Ingrese en número el día de la semana. No puede valer ni cero. Esta estructura condicional.

Fíjense. Rápidamente lo vamos a probar acá en el PESAIN. Definir día como entero. en ese. Ya digo verdadero.

Después de hacer las acciones que estaban ahí, ya salió. Y otra cosa. Solamente va a entrar a evaluar una opción si la que estaba, si todas las que estaban arriba eran falsas. Fíjense si lo pueden ver gráficamente acá. Miren.

Si viene acá y evalúa qué día es igual a uno, va a escribir lunes y después ya no va a volver arriba. Ya directamente viene para acá. Y si entró por el uno, no va a poder entrar por el dos. Si el dos. Si el dos es falso, recién evalúa el tres.

Y así. Acá no le gustó una cosita a mí. No, porque pensé en el regente. No, y cuando hay tres. Ah, pero se supone que el día de la semana es de uno a siete.

Se supone. Bueno, a ver, ejecutémoslo acá. Entonces supongamos que yo le pongo, no sé, que hoy es miércoles. Tres. Digo tres.

Fíjense. Evalúa el uno. Es falso. Evalúa el dos. Es falso.

Evalúa el tres. Es verdadero. Entra. Y ya sale. ¿Está?

Vamos a hacerlo de nuevo. Pero ahora le vamos a poner ocho. A ver qué hace. O le vamos a poner mil quinientos, que también es un entero. ¿Sí?

Evalúa el uno. Falso. Dos. Falso. Y así todo.

Hasta que llega ahí y dice. Bueno. Ahora. Otra cosa. Este ejercicio que habíamos hecho recién.

¿Se puede hacer con un condicional múltiple? Sí o no. A ver. Que levanten la mano lo que dicen sí. ¿Por qué son tan pocos?

Que levanten la mano lo que dicen no. Que levanten la mano lo que dicen no sé. A ver. Evaluemos. ¿Cuántas variables tenemos?

¿Cuántas? Una sola. Que era la cantidad de milímetros caído. Una sola. ¿Cuántos valores posibles?

¿Cuántos rangos? posibles tiene? ¿Cómo seis? ¿Cuatro? ¿Era sin peligro, poco peligro, muy peligroso?

¿O en los dos? ¿Cuatro nomás? ¿Cuatro rangos distintos? ¿Tiene tres o más valores posibles? Sí.

Una variable y tres o más valores posibles sirve para el condicional múltiple. Entonces, vamos a ver. Fíjense. Ingrese cantidad de milímetros de lluvia, leer milímetros, y acá en vez de hacer los condicionales anidados, vamos a hacer un según. Según MM, hacer.

Obviamente, acá al final va a haber un fin según. Bueno, ¿cuál era el primer valor que teníamos? Mayor a 150, no 150. Mayor. Entonces, si es mayor a 150, dos puntos, escribir inundación inminente.

Acuérdense, solamente va a evaluar el segundo valor si el primero dio falso. Entonces, acá no hace falta preguntar menor o igual a 150. No. Directamente pregunto mayor a 100. Porque ya sé que evalúa este si el otro fue falso.

Entonces, ahora el tercer caso mayor o igual a 70. Acá, sí. Escribir poco peligro. Y acá lo que puedo escribir es otro. ¿Sí?

Porque por eso, menor a 70. Por eso, menor a 70 podría poner menor a 70 o podría poner otro. En este caso es lo mismo. Porque si no es mayor a 150, ni es mayor a 100, ni es mayor o igual a 70, la única opción que queda que sea menor a 70. Sí.

No de su criterio solamente. Si en este ejercicio lo ideal es usar un segundo. Porque es más óptimo que todos los si anidados. Pero siempre que se cumplan estas dos condiciones. Una sola variables.

Si se cumplen esas condiciones. Usen un segundo. Si se cumplen esas condiciones. Usen un segundo. Pero tienen que tener bien claro esas dos cosas.

Si no se cumplen esas dos condiciones. No se les ocurra usar un segundo. Un segundo. Siempre va a ser más cortito. Digamos, va a ser más eficiente.

Pero. Dale. ¿Qué? ::::: qué? :::: qué?

:::::::::: qué? :::::::::::::::::: :::::::::::::: ::::::::::::: ::::::::::::: ::::::::::::: :::::::::::::::::::: ::::::::::::::::::::: ::::::::::::::::::::: :::::::::::::::::::::: ::::::::::::::::::: ::::::::::::::::::::::
