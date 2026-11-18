---
tipo: transcripcion
materia: Algoritmos y Estructura de Datos
clase: 4
tags:
  - AED
  - transcripcion
---

# Clase 4 — Algoritmos y Estructura de Datos

> [!info] Transcripción completa de la clase grabada
> Texto íntegro, sin resumir. Generada con Whisper desde `clase4.wav` y
> depurada con `dedup.py` (colapsa oraciones repetidas consecutivas, que son
> alucinaciones del modelo, no habla real del profesor).
> Video original: `temp_videos/clase4.mp4`

---

Bueno, hasta ahora, a ver, hagamos un breve repaso de qué temas dimos en las primeras clases. A ver, ¿quién me puede decir qué dimos en la primera clase? Bien, bien. En la primera clase dimos la estructura de un algoritmo, ¿sí? A ver, peren, voy a compartir mi pantalla acá para los chicos del Zoom y para ustedes también.

Ahí vamos, ahí vamos. Bien. Lo que vimos, entonces, en la primera clase fue la estructura de un algoritmo, ¿sí? ¿Qué era? Acción.

Le poníamos un nombre. Es. Y después poníamos, ¿qué palabra? Ambiente. Ahí definíamos las variables.

Si teníamos varias variables con el mismo tipo de datos, las podíamos definir todas juntas en el mismo renglón. Si teníamos variables con otro tipo de datos, las definíamos en otro renglón. Bien. Y después poníamos proceso. Y después, todas las acciones simples.

Escribir, leer, asignar. Eso es lo que dimos en la primera clase. Perfecto. Y después, al final de todo, ¿qué poníamos? Fin action.

Muy bien. Perfecto. En la segunda clase, ¿qué vimos? Operadores. Sí.

En la segunda clase, ya empezamos a ver las estructuras condicionales. ¿Se acuerdan cuáles eran las estructuras condicionales. Simple, alternativo y múltiples. Sí. La anidación es una posibilidad que tenemos con los condicionales múltiples.

Pero básicamente tenemos tres tipos de condicionales. Entonces, el condicional simple era si determinada condición, entonces, acá venía una cierta cantidad de acciones y después ¿qué? Fin sí. En el condicional simple no teníamos ninguna acción por si esa condición era falsa. Después teníamos el condicional alternativo que al condicional simple ¿qué se le agregaba?

El si no. Y acá tenemos acá tenemos acciones si la condición es verdad, y acá vamos a tener acciones si la condición es falsa. Bien. Esta condición ¿cómo podía ser? Podría ser una condición muy simple como por ejemplo si A mayor que B o A menor que B o B menor que C.

Podíamos poner B. ¿Se acuerdan de eso? Bien. Y después teníamos el condicional múltiple. Para poder aplicar el condicional múltiple.

Para poder aplicar el condicional múltiple, cuántas características se tienen que cumplir. Tenemos que analizar una sola variable con tres opciones o más. Entonces era según. Según. Par.

Hacer. Y acá. El condicional múltiple tradicional es poner valores. Valor uno. Valor dos.

Valor tres. Y después teníamos una última opción que era otro otro. ¿Sí? Que era la opción si tenía cualquier otro valor. Y después poníamos pin segundo.

Los de allá del fondo están todos de acuerdo? Porque no opinan nada. Bueno. Y después dijimos que a esto le podíamos agregar qué cosa. Está bien que yo le ponga igual a B1, igual a B2, igual a B3.

¿Sí o no? No. Cuando comparamos por valores exactos no ponemos el igual. Ponemos directamente el valor. ¿Sí?

Tampoco hay que poner var igual así. La variable que vamos a analizar se pone solamente acá arriba. ¿Ok? Y acá ponemos B1. También podemos poner B1.

Exacto. Mayor, menor. ¿Sí? Ponemos por ejemplo si es mayor a B1 tal cosa, mayor igual a B2 tal otra. ¿Sí?

Ponemos por ejemplo si es mayor a B1 tal cosa, mayor igual a B2 tal otra. ¿Sí? Acuérdense. Acuérdense que el condicional múltiple va a entrar en la primera opción que sea verdadera. Entonces, si viene acá y esta es verdadera ya entra acá ya no verifica las otras opciones y ya sale.

Si esta es falsa va a venir a analizar la segunda. Si esta es verdadera entra y no es verdadera va a seguir con la otra. Así. ¿Ok? Bien.

Y hasta ahí llegamos en la clase 2. Y en la clase 3. ¿Qué vimos? Estas también son estructuras. Estas son estructuras condicionales.

En la clase 3. En la clase 3 vimos estructuras repetitivas. ¿Y cuántas estructuras repetitivas vimos? ¿Y cómo se llaman? Pre-test, post-test y manejada por contador.

Perfecto. La pre-test comienza con la palabra mientras. Perfecto. Mientras. Y mientras, ¿qué cosa?

Se va a ejecutar ese ciclo. Mientras. Mientras, la condición sea verdadera. Mientras, condición verdadera ser. Acá va a haber un conjunto de acciones.

Y después, fin mientras. Una de las acciones que tiene que haber normalmente se pone cerca del final. Una de las acciones. ¿Qué tiene que hacer? Tiene que modificar de alguna manera la variable que está en la condición.

¿Sí? A condición se le tiene que asignar. Se le tiene que asignar algo. Pero lo importante es que siempre se le asigne que de alguna manera que cambia el valor antes de volver a hacer la pregunta. Bien.

¿Cuál era la cantidad mínima de veces que se van a ejecutar estas acciones? Cero. Porque puede darse el caso que esta condición de entrada ya sea falsa y entonces no entra nunca al mientras. Bien. Después vimos el post-test.

También llamado repetir. Repetir. Y una cierta cantidad de acciones. Hasta que. Hasta que la condición sea verdadera.

Entonces. ¿Cuándo sale de este ciclo? Cuando la condición es verdadera. O sea que va a volver a ingresar siempre que la condición sea falsa. ¿Sí?

Tienen que ser muy cuidadosos con eso. Porque en el repetir. Repetir. Repetimos el ciclo cuando la condición es falsa. En el mientras repetimos cuando la condición es verdadera.

¿Está? Y en este en esta estructura también la condición tiene que variar acá adentro. ¿Sí o no? Sí o no? Sí.

Porque si no, no va a salir nunca. ¿Está? ¿Se entiende? Ok. ¿Por qué?

Porque vos las acciones ya las hiciste una vez. Entraste acá, viniste, ejecutaste estas acciones y después ahí tenés tenés que volver a asignarle un valor a esa condición y después evaluarla. ¿Está? Puede ser que se evalúe una sola, que se ejecuten una sola vez las acciones y después cambie la condición y ya no se ejecuten más. O puede ser que tengan que volver a ingresar.

¿Está? Sí. Exacto. El repetir se ejecuta como mínimo una vez. ¿Por qué?

Porque vos entras a la estructura, ejecutas todas las acciones, y después recién y después recién evaluadas la condición. Entonces cuando tus acciones se ejecutan como mínimo una vez. Podés usar un repetir. Y después vimos la manejada por contador. En la manejada por contador, ¿qué palabra usamos?

Para. Y después tenemos que usar una variable que muchas veces usamos la letra. Pero podemos usar una variable cualquiera. Y ¿cómo es la sintaxis? Dos puntos igual, le asignamos.

Bien. Normalmente hacemos el para desde 1 hasta n, pero en realidad es un valor inicial hasta un valor final. El valor inicial puede ser 1, puede ser 2, puede ser menos 10, lo que sea. Y después, ponemos coma y el paso. Y después ponemos la palabra hacer.

Si el paso va a ser 1, es decir, que la variable se va incrementando de 1 en 1, no hace falta que lo pongamos. Podemos obviar esto. Pero si va a ir yendo de 2 en 2, de 3 en 3, o va a ir decrementándose. Supongamos que mi valor inicial sea 10 y mi valor final sea 10 y mi valor final sea 0. En ese caso, ¿cuánto sería?

Menos 1. Porque yo arranco un valor alto y voy decrementando. Exacto. Si vos pones de 1 hasta 10 y le pones menos 1, va a haber un error. Pero si vos le pones desde 10 hasta 0 y no le pones esto, también va a haber un error.

Bien. Para. Y acá al final vamos a poner fin para. Vieron que hasta ahora el único que no tiene un fin es el repetir. Tiene un hasta que.

Bien. Acá va a ir un conjunto de acciones y pregunto. Acá, a la variable que maneja el ciclo, ¿se le puede asignar algo? Sí, y además porque lo que le asignes ahí puede llegar a romper el ciclo. Y eso está mal.

No sé, esto está directamente prohibido. No se le puede asignar un valor. Solamente esta instrucción es la que va a ir manejando el incremento de la variable que maneja el ciclo. ¿Está? Bien.

Sí. ¿Vos decís acá el valor final? Sí. El valor final, el valor inicial. ¿Vos podés pedirle los dos valores?

Por ejemplo, vos decís. Sí, exacto. Siempre, si vos querés hacer, por ejemplo, mostrar, no sé, todos los números pares entre dos números que ingresa el usuario. Entonces vos haces un leer, primero un escribir, obviamente, después haces un leer N1 y leer N2. Y entonces acá pones para var que va desde N1 hasta N2.

A ver, ahí tengo una idea. Si yo les dijera. Si yo les dijera que quiero mostrar por pantalla todos los números pares que están entre N1 y N2 que ingresa el usuario. ¿Está? ¿Cómo lo hacemos?

Acá está el esqueleto. Leo N1 y N2 y N2 y N2 y para un I. Vamos ponerle un I. Que va desde N1 hasta N2 a hacer qué cosa. Se puede, sí.

Esperá. ¿Y cómo vos estás seguro que N1 es par? Yo le puedo poner acá un paso 2, sí. Pero qué. N1 sería el inicio de I.

N1. Sí. Ok, pero yo cómo sé si N1 es par? Un sí, a ver, a ver, un sí antes del para. A ver, sí, ¿qué?

¿Qué número? ¿N1? N1. Si N1 mod 2 es igual a cero, es igual a cero. Entonces, ¿qué hago?

Que entre al para, recién ahí. ¿Y si no? Y en el sí, sí, ¿qué? ¿Cómo está? Y entonces para eso hago un condicional simple y pregunto por distinto, ¿o no?

A ver, fíjense lo que estamos analizando acá. Si a N1 mod 2 es igual a cero, significa que N1 va a ser para. ¿Está bien? En ese caso, yo a N1, ¿qué tengo que asignarle? Nada.

O sea, el mismo N1, porque tiene que quedar igual. Esa acción no tiene sentido. Y solamente tengo que hacer algo por el sino. Que si N1 no es par, ¿cómo lo convierto en par? Le sumo 1.

Porque los números son par, impar, par, impar, par, impar. Entonces, a N1 tendría que asignarle N1 más 1. ¿Sí? Pero fíjense que acá. Pero fíjense que acá esta acción no tiene sentido.

Entonces, cuando nos pase eso, lo que tenemos que hacer es un condicional simple y cambiar esto. Si el número es impar, entonces voy a hacer esto. Y si no, no hago nada. ¿Se dan cuenta? ¿Lo ven o no.

Entonces, si el número es impar, lo convierto en par. Si era par, lo convierto en par. Si era par, no hago nada. Y para ahí, que va desde 1 a N2, y acá, ¿qué le pongo? Coma 2.

Entonces yo sé que va a arrancar en un número par, que va a ser N1, va a ser el siguiente a N1. Y de ahí va a ir hasta N2. ¿Y qué tengo que hacer? Escribir qué. No, ¿cómo?

Eso ya le escribí allá arriba. Yo ya leí N1 y N2 acá. Acá lo único que tengo que hacer es escribir Y. ¿Se entiende? ¿Sí?

¿Por qué? ¿Por qué abre el coma 2? Porque lo que yo dije que lo que quiero hacer es mostrar todos los números. ¿Sí? Mostrar todos los números pares que hay entre N1 y N2.

Fijate que con el sí que yo hice en la línea 29, de 30, 31, 31. Yo lo que me aseguro es que N1 sea par. Porque o ya era par antes de eso, o le sumo 1 y lo transformo en par. ¿Está? Y entonces, en la línea 33, mi para va a ir desde un número par, y para la próxima vez, no voy a sumarle 1, porque después de un par, ¿qué viene?

Un impar. Entonces, si yo le sumo 2, voy a otro par, y le sumo 2, y voy a otro par, y le sumo 2, y voy a otro par, y le sumo 2, y voy a así. ¿Se entiende? No, se pone coma 2. Si yo no le pongo nada acá, significa que es positivo.

¿Está? Si yo quisiera que sea negativo, le pongo un menos. ¿Ok? ¿Está? Bueno.

Hoy en el curso anterior tuvimos una dificultad para resolver el ejercicio de cómo sabemos si el número es primo o no. ¿Hicieron ese ejercicio o no? ¿Sí? ¿Eh? ¿Mándalo al disco?

¿Eh? No, un número. Un solo número. Si es primo o no. ¿Qué?

A ver, vamos a ver. El 19. Escribe un algoritmo que determine si un número es primo. A ver, levanten la mano quién hizo por lo menos una hora de ejercicio en la semana. Es un lindo número, pero igual sigue siendo la mitad.

A todos los que hicieron ejercicio en la semana. A todos los que hicieron ejercicio, los felicito. Y a los que no hicieron ejercicio, metanle pata. Metanle pata. Porque estos ejercicios son fáciles, pero después se van a ir haciendo más complicados.

En la semana del 25 de mayo, por ahí. Probablemente sí. Puede ser que sí. Bueno. A ver, hasta que el compañero manda el ejercicio, vayamos pensando.

¿Cómo sabemos si el número es primo? Chicos, vuelvan acá. ¿Cómo sabemos si el número es primo? ¿Qué condición tienen que cumplir? ¿Qué condición tienen que cumplir los números primos?

Pueden dividirse solo por uno y por sí mismos. ¿Está? Porque básicamente todos los números pueden dividirse por uno y por sí mismos. Pero los primos solamente pueden dividirse por esos números. ¿Ok?

Bien. ¿Cómo sabemos que nosotros leemos? ¿Qué tendríamos que hacer? ¿Qué tendríamos que hacer para saber si un número es primo o no? Tendríamos que dividirlo?

¿Por algo no? El resto de la división de cero, pero la división de cero, pero la división de qué? ¿De qué? ¿De qué hay qué? A ver, escuchen.

NDIV1. No, NDIV no, NMOD. NMOD. NMOD 1 va a ser cero seguro. Y NMOD N va a ser cero también.

En realidad, esos dos son los que a mí no me importan. Porque todos los números cumplen con eso. Me importan todos los otros. A partir de dos. Ajá.

Sí, más o menos. A ver, díctenme acá. ¿Qué hago? A ver, tengo que dividirlo, ¿cierto? Ese N lo tengo que dividir por varios números.

O sea, necesito un ciclo. Bien. De los ciclo. De los ciclos, de las estructuras que vimos. ¿Cuál podría usar?

Mientras. También puedo usar un para o no. Sí. Pero no es óptimo. Exacto.

Podría. Desde dos hasta NN-1. Está bien. El rango ese está bien. Pero ¿qué pasa?

¿Eso funcionaría o no? Si yo hago un para, ¿sí? Acá hago un para ahí que va desde dos hasta N-1. ¿Y acá qué hago? ¿Qué podría hacer yo acá?

¿Qué pasa? Ir sacando el módulo. Un para. Puede ser hasta el valor que ingresa el usuario. Valentina dice hasta el valor que ingresa.

En realidad hasta el valor menos uno. Sí. Pero acá. A ver. Yo sé que todos los números.

Yo sé que todos los números tienen dos y dos. ¿Cierto? Uno y el mismo. Como mínimo tienen dos divisores. Los números primos.

¿Qué pasa? Solamente tienen esos dos. Supongamos que saco el uno y ese número. Entonces. Si yo no cuento el uno y el mismo N.

¿Cuántos divisores debería tener un número primo? Cero. Si no cuento esos dos. ¿Está? Entonces.

Yo acá. A una variable div. Podría ponerle. Cero. Y acá.

Cero. Y acá pregunto. Cero. Y acá pregunto. Si.

N mod. Y. Si es igual a cero no hago nada. Si es distinto de cero. Si N mod.

Y es distinto de cero. Ah, no. Pará, pará, perdón. Si es igual. Si es igual significa que Y lo divide a N.

Si es igual a cero. Significa que Y también es un divisor de N. Entonces. A div. ¿Qué le asigno?

Entonces no es primo. Está bien. ¿Qué le asigno? Div más uno. Y si N mod.

Distinto de cero. No le hago nada. Entonces ahí termina. Es un condicional. Simple.

¿Está? Y ahí. Fin para. Esto va a funcionar. Y cuando yo salgo.

Cuando yo salgo. De esto. ¿Qué tengo que preguntar para saber si el número es primo o no. Si div es como. Mayor igual que uno.

Porque yo dije que al uno y a N no los voy a considerar como divisores. ¿Está? Entonces. Si div sigue siendo cero. ¿El número cómo es?

Es primo. Si div sigue siendo cero. ¿Qué escribo? ¿Funciona esto? Sí.

¿Es óptimo? No. ¿Por qué no es óptimo? Porque controla todos los números hasta N-1. Supongamos que yo ingreso el número mil.

El número mil. ¿El número mil es primo? ¿Eh? No. Mil.

Peor todavía te digo. El número tres mil. El número tres mil se puede dividir por dos. Se puede dividir por tres. Se puede dividir por seis.

Se puede dividir por cinco. Se puede dividir por diez. ¿Está? Ahora. Si yo.

Ingreso N. Ingreso acá el tres mil. Va a ejecutar este para. Desde el dos. ¿Hasta qué número?

Hasta el dos mil novecientos noventa y nueve. Va a ser un montón de vueltas innecesarias. Entonces. Yo lo que puedo hacer es. Leer N.

También. También lo podría hacer hasta N dividido dos. Con lo cual. Me ahorro la mitad. Pero no gano mucho.

Vamos a usar. Una variable. Juliana. Y vamos a. Considerar.

Que primo. Es verdadero. Vamos a. Suponer. Vamos a.

Suponer de entrada que es primo. Y después. Está bien. Entonces. Espera.

¿De dónde arranco? Arranco desde I. Ahí le voy a asignar qué número. Porque ya. Si uso un pretest.

Tengo que inicializar la variable. ¿Con qué variable arranco? Con qué número arranca la I. Con dos. Lo mismo que allá arriba.

Bien. Mientras I. Sea. Menor que N. Hacer.

Y ahí yo podría hacer lo mismo. Que dice acá arriba. En realidad. Así sería mi pregunta. Si.

Y yo acá. Y yo acá hago la. Esta pregunta. Si n mod. Y yo acá hago la.

Esta pregunta. Si n mod y igual a cero. Entonces. ¿Qué hago acá? A primo.

Le asigno. Falso. Y acá. Fin mientras. ¿Está bien?

¿O falta algo? Falta algo? Falta algo. Acuérdense que yo siempre dijimos. Siempre dijimos.

Que dentro de un ciclo. De un pretest. O de un protest. De un posttest. Tenemos que modificar la variable que estoy evaluando.

Yo a I no le dice nada acá. Entonces lo que tengo que hacer con I es. Asignarle. Y más uno. Incrementarlo.

Y cuando sale. ¿Qué pregunto? Pregunto si primo igual a verdadero. No. Se pone porque primo.

Se pone porque primo ya es una variable booleana. Entonces si primo nomás. Entonces. ¿Está? Y entonces ¿Qué escribo?

Si primo es verdadero. Significa que es como? Es primo. Y si no. ¿Qué escribo?

Y terminó. ¿Está bien? Fíjense que en este caso. Si yo ingreso el número 3000. ¿Qué va a ser?

¿Con qué valor empieza I? 2 es menor a 3000. Sí. Primo. La primera vez.

¿Es verdadero? Sí. Divide. 3000 dividido 2. El resto es 0.

No. Y ahí ya sale. ¿Cuántas división. ¿Cuántas división hizo? Una.

¿Cuántas división hizo? Una. ¿Cuántas veces entró al ciclo? Una. ¿Está bien?

¿Vos lo había hecho más o menos así? ¿Qué? Y vos fuiste incrementando. Si divisor igual a 0. A motociclo.

Si divisor igual a 0. A motociclo. Sí. Acordate. Las variables tienen que ser un poco más.

Descriptivas. Pero bueno, está bien. A es tu número. A. Ciclo arranca.

Ciclo arranca valiendo A. Y tu contador 0. Mientras ciclo mayor a 0. A divisor le asignás. A modciclo.

O sea, el resto. Claro. Divisor. Si divisor. Si divisor es igual a 0.

Ahí. Fíjate una cosa. Ahí vos podrías haberte ahorrado una línea directamente haciendo si amodciclo igual a 0. Si amodciclo igual a 0. Eso ya está bien.

Bien. A contador, contador más 1. Entonces vos llegás. Vos hiciste todas las divisiones. Desde ese número hasta el 1.

Y hizo todas las divisiones significa que cuántos divisor debería tener el 1. Para ser primo. Está bien. Funciona. Está bien.

Funciona. Está bien. Vos hiciste desde ese número hacia abajo. Pero el inconveniente que tiene es que no detectaste si había un divisor más allá y ahí saliste. El 2 tiene dos divisores.

Que es 2 y 1. Pero el 1 tiene un mejor. Pero el 1 es primo. ¿Y está bien? El número es primo.

Ah, está. Y no va a dar. Claro. Acá, escuchá. Acá, ¿cómo es tu nombre?

Benjamín. Acá lo que dice tu compañero es ¿Qué pasa si ingresás el 1? El 1. Sigue primo. El 1 es primo.

Entonces, acá en este último sí tuyo. Tendría que ser si cont es menor o igual a 2. Porque si cont es 1 también. ¿Quién hizo? Robles.

Robles Francisco. No se consigue. Bueno. Podríamos discutirlo. ¿Ok?

Bueno. Podríamos discutirlo. ¿Ok? Bueno. ¿Dónde está el otro chico?

Bueno. Si manda el Ah, en el chat. Bueno. Que lo mande al Discord. Bueno.

Ahora van a hacer van a hacer van a hacer un ejercicio ustedes. 1, 2, 3, 4, 5, 6. Hasta esta fila hasta esta fila van a hacer van a hacer un ejercicio. Entonces, hasta acá. 4, 5, 6.

2, 3, 4, 5, 6. No. 6, 6, 6, 6. 6. 1 a 1.

4. 6. 7. 6. 7.

6. 7. Si el número no es negativo, tienen que calcular la clave. Sumando cada dígito que compone el número y a esa suma se le calcula el módulo 7. Acá está un ejemplo.

Para 513 la clave va a ser 5 más 1 más 3 que da 9 y 9 mod 7 da cuánto? 2. Número de 513 la clave es 2. Ustedes tienen que hacer un algoritmo que permita leer varios valores y que determine para cada uno de esos si fue negativo o decir cuál es la clave. Si fue negativo la clave es menos 1.

Y si es positivo la clave que le corresponde. De acá para acá. De ahí para allá hagan el 3206. Escribe una función que lea la cantidad de unidades y el precio de un producto que se quiere comprar y en función de las unidades introducidas calcule el descuento o no. Cuando las unidades excedan media docena tienen que aplicarle el 4% y si excede la docena tienen que hacerle un descuento del 10%.

Ustedes tienen que devolver cuál es el descuento que el monto del descuento que se le va a aplicar al cliente. Estos ejercicios si están en la guía PDF así que si quieren lo pueden leer de ahí. Gracias. De la cantidad de dígitos que sea. Y ya está.

No, no, no, no. no. No, no, no, no. no. No, no.

Miren, acá un ratito nada más. El 08. Dice, acciones 8, ambiente puntuación real, pago entero. Leer puntuación. Acá, ¿quién mandó este ejercicio?

Maxi? Maxi. Está bien, pero antes de leer siempre tiene que escribir. Ingreses, la puntuación de no sé qué. Y después, según puntuación, hacer 0.0, escribir su rendimiento es inaceptable y no recibirá dinero.

en la pago. pago. in. pago. in.

pago. pago.ago. pago. Chicos, miren, acá un compañero mandó, un compañero que está en la casa, creo, David Sarza, mandó el 3204. Número, suma, clave, cifra como entero y respuesta como carácter.

Este carácter yo, lo hubiera definido como S, N. Porque él pregunta si desea continuarse o no, así que es más preciso ponerle los valores. Ingrese su número para obtener la clave, leer número. Si número es menor a cero, a clave le asigna menos uno. ¿Está bien?

Era lo que decía la consigna, si el número es negativo, menos uno. Chau. Si no, arranca con una variable que llama suma, que también podría ser clave nomás. Me parece que usó una variable de más. Yo hubiera usado solamente clave, pero suma.

Mientras número sea distinto de cero, también podría haber usado mayor a cero, porque siempre tiene que ser un número entero. Positivo. A cifra, ¿sí? A la cifra, la unidad sería, la calcula como número mod 10. ¿Sí?

Número mod 10. Fíjense, si yo tengo un número como este, no sé si alcanza a ver, 95.423, si yo hago dividido 10, ¿cuánto me da? Me da 9.542,3. Si yo hago dividido 10. Quitándole esa unidad haciendo número 10.

Si yo acá hacía la división entera, me quedaba con 9542. O sea, el mismo número sin la unidad. ¿Se entiende? ¿Cómo? ¿Vos querés hacer la división común y truncar?

Es lo mismo que hacer el DIP. La división común truncada es exactamente lo mismo que el DIP. ¿Se entiende? Y el DIP es más fácil, digamos. Igual.

Por eso, o sea, siempre vamos a preferir usar el mod y el DIP. Como función, la función truncar existe. Por ahí en algún ejercicio, quizás la ocupamos, pero en principio vamos a manejar nomás con el DIP. Si nosotros, a ver, si en algún ejercicio necesitamos usar la función, le vamos a avisar. Entonces, ¿qué hace con esta instrucción, con esta acción de la línea 17?

Le quita la unidad al número. Se queda con todo el número menos la unidad. Y vuelve ahí arriba. ¿Número es distinto de cero? Sí.

Vuelve a entrar. A cifra le asigna nuevamente el número 10. O sea, le quita la nueva unidad y se la suma a la clave. Y le vuelve a quitar la unidad al número y así hasta que el número va a quedar en qué número? En cero.

Cuando yo, este número 9542, le quite el 2 me va a quedar 954. Cuando le quite el 4 me va a quedar 95. Cuando le saque el 5 me va a quedar un 9. Y la próxima vez me va a quedar un 9. Porque si yo hago 9 mod 10, 9 mod 10, ¿cuánto me da?

No. 9 mod 10, ¿cuánto me da? Me da 9. Le sumo 9 a la clave y cuando hago 9 DIP 10, ¿qué me da? Cero.

Vuelve a ir arriba y cuando hago 10. Y escribiendo la clave. No hubiera usado la variable suma. Y acá, acá no estoy de acuerdo. Dice, si clave igual a menos 1, entonces escribir error.

No dice eso el enunciado. El enunciado dice, si el número es negativo, la clave es menos 1. Entonces, yo directamente sacaría este sí y dejaría esto. Escribir su clave es clave. Ya sea que la clave hubiera sido menos 1 o que la clave hubiera sido lo que construye acá.

Y después pregunta, ¿desea continuar sí o no? Lee la respuesta y termina el ciclo y dice que va a repetir todo esto hasta que la respuesta sea igual a n. Fíjense que acá arriba, como está usando un repetir, no hace falta inicializar en ningún lado y no hace falta de la respuesta. En realidad tienen que estar en el mismo nivel que la respuesta. En realidad tienen que estar al mismo nivel que el mientras.

Yo podría preguntar si número mayor a cero y hacer todo esto. ¿Está bien? ¿Sí o no? ¿Alguien dice sí? ¿Quién dice no?

Está casi bien. ¿Por qué? Porque si es cero, también tiene que entrar por acá. Entonces, si yo invierto esta pregunta, tengo que preguntar si número mayor o igual a cero. Porque si no, si yo pregunto mayor no más a cero, va a venir acá y le va a asignar clave menos uno cuando en realidad no es negativo.

Está bien, está bien. Pero la pregunta tiene que ser si número mayor o igual a cero. No solo mayor. Tienen que ser cuidadosos con eso del tema del igual. Si vos en la cosa.

Si vos lo preguntás al revés, tenés que poner si número mayor o igual a cero. Porque fíjate que acá está entrando. Acá entra por acá a la línea 11 solamente si es negativo. Si es cero, no entra acá. Viene por acá.

Si el número es cero, ¿cuánto te va a dar la clave? Cero. ¿Está bien? Porque vos haces cero. O sea, le pusiste cero a la clave.

Mientras número C distinto es cero. Nunca va a entrar acá. Y cero mod 7 te da cero. ¿Está? Y la clave te da cero, pero no es menos uno.

¿Está? ¿Ok? ¿Se entendió? Súper. A ver, veamos el que mandó acá José.

El 32-06. Dice. Precio PROD real. Uni entero. Valor decimal real.

Ingrese las unidades de su producto. Lee unidades. Ingrese el precio de su producto. Lee precio PROD. Dice.

A ver. Si uni es mayor a seis. Y uni menor a trece. Hacer. Valor descuento.

Uni por precio PROD. Por cero, cero, cuatro. Y escribir el descuento desde. Tata. Si no.

Si uni mayor o igual a trece. Hacer valor descuento. Uni por precio PROD. Por cero, diez. Y escribir el descuento desde.

Peso. Valor descuento. Y si no. Cero. Y aparte.

Quiero ver una cosa. Y aparte. Quiero ver una cosa. Funciona. Pero lo ideal sería hacerlo con un segundo.

Ok. Veamos. Acá. Chicos. Acá.

Maxi mandó también al Discord. A ver. Dice. Escribir. Ingrese las unidades de producto.

Leer cantidad. Ingrese el precio por unidad. Leer precio uni. A precio fin. Acá.

Quiero creer que. Quiso asignarle. Se le faltó el igual. Precio unidad. Precio final.

Y si es más de seis. Y hasta doce. Hacele un cuatro por ciento descuento. Y si es menos de seis. No.

No le haga. Si es seis o menos. No le haga ningún descuento. Y dice. Pero el enunciado decía.

Mostrar el valor del descuento. ¿Está bien esto? Sí o no. ¿Por qué? Porque lo que él hizo es multiplicar el valor, el precio que había calculado por cero nueve, que es lo mismo que hacerle un diez por ciento de descuento.

Si vos tenías que pagar cien pesos y te multiplica por cero nueve, tenés que pagar noventa pesos y te hizo diez pesos de descuento, que es un diez por ciento. ¿Se entiende? Pero no es eso lo que pedía el enunciado. El enunciado no pedía que muestren el valor del descuento. Entonces, en este caso.

Entonces, en este caso había que hacer. Acá descuento. No tendría que ser precio final, sino que tendría que ser a descuento. Hay que asignarle el precio final por. ¿Por qué?

¿Por cuánto? ¿Eh? Por cero coma uno, porque es el diez por ciento. O sea, el descuento del diez por ciento. Y lo que quiere el enunciado, lo que me pide, es que yo muestre el valor del descuento.

Entonces, tengo que calcular el diez por ciento y mostrarlo. Sí. Pues ya terminamos. ¿Eh? Y acá más abajo.

Y si es mayor a seis, a precio final, acá, de nuevamente, el descuento es el cuatro, entonces yo a descuento. Entonces, yo a descuento le tengo que asignar precio final. Precio final por cero coma cero coma cero cuatro. Es el descuento. Y lo otro no.

Si quiero lo puedo calcular, pero no es lo que se pide. ¿Está? Si la cantidad es mayor a cero, pero es siempre acuento. Siempre acuérdense cómo funciona el segundo. Va a entrar acá solamente si esto fue falso y esto fue falso.

Entonces, va a entrar acá si es entre uno y seis. Entonces, el descuento le asigna, hay que ser cuidadoso con él, le asigna cero. Y otro dice la cantidad no puede ser negativa. Está bien. Está teniendo en cuenta que pueden haber ingresado una cantidad negativa.

¿Está? Y acá, si cantidades mayor a cero, cantidades mayor a cero, cantidades mayor a cero, cantidades de uno para arriba, dice, escribir descuento de, y acá habría que mostrar el valor este del descuento. Claro, exacto. Hay que sacar el porcentaje. Y el precio final que no pide.

Descuento de, descuento. ¿Está? ¿Está bien? La opción. La opción del cero no tiene mucho sentido.

¿De acá? Lo que pasa es que él no le asignó antes ningún valor a descuento. O sea, que lo tiene que asignar en algún lado. Está bien. Pero abajo dice si cantidad mayor a cero.

Claro, porque... Y si no, no muestra nada. Claro, claro. Claro, escribió esto. Es por si él ingresó una cantidad de artículos cero.

No está preguntando por descuento cero. Está preguntando por cantidad. No sé, pero no tiene sentido esa línea. ¿Por qué no? Es por si alguien se...

¿Para qué usas? No le muestra nada nomás. No, igual no entra ahí. ¿Por eso? Si...

Si alguien se le ocurrió poner una cantidad menos cinco. No va a entrar acá. Si es cinco, por ejemplo. Si es cinco, entra. Si es cinco.

No va a entrar si es cero o menos cero. Está bien. Está bien esa validación que hizo. Por ahí es quizá innecesaria. Podríamos haber usado la línea cincuenta y uno nomás.

¿Está? El área cincuenta y uno. ¿Se entiende? Sí. Chicos, a los que les tocó a los que les tocó el 32.

¿Se entiende? La semana que viene no tenemos clase. Así que nos vemos dentro de dos semanas. Por favor, los que hicieron ejercicios esta semana, repítanlo. Los que no hicieron ejercicio, hagan.

Por favor, tienen dos semanas. Así que mínimo dos horas de ejercicio. Hagan todos los ejercicios del trabajo práctico uno. Menos funciones y procedimientos. Que eso vamos a ver en la próxima clase.

Por lo menos participen mirando lo que mandaron. Vamos a ver en la próxima clase. Bueno, vamos a ver en la próxima clase. Vamos a ver en la próxima clase.
