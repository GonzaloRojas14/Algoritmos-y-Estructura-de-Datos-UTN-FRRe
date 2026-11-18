---
tipo: transcripcion
materia: Algoritmos y Estructura de Datos
clase: 1
tags:
  - AED
  - transcripcion
---

# Clase 1 — Algoritmos y Estructura de Datos

> [!info] Transcripción completa de la clase grabada
> Texto íntegro, sin resumir. Generada con Whisper desde `clase1.wav` y
> depurada con `dedup.py` (colapsa oraciones repetidas consecutivas, que son
> alucinaciones del modelo, no habla real del profesor).
> Video original: `temp_videos/clase1.mp4`

---

Ahí está. Entonces, la programación tiene mucho de contenido teórico, ¿no? Hay muchas cosas que ustedes tienen que saber, pero además de eso, también tiene una parte de arte, de creación, de imaginación de ustedes. Entonces, eso necesitamos que ustedes lo practiquen. Eso, miren, les cuento lo que nos pasaba el año pasado.

Nosotros veníamos, ahora les vamos a explicar cómo es la estructura de las clases, cómo son las estructuras de las clases. Nosotros veníamos, explicábamos el tema, les mostrábamos cómo se resolvía un ejercicio, y después les dábamos otro ejercicio, o dos o tres ejercicios para que resuelvan los estudiantes. ¿Qué hacían algunos? Se levantaban y se iban a la casa porque decían que en la casa estudiaban más tranquilos. Pero en la casa no estamos los profes.

Entonces, la idea es que ustedes hagan acá los ejercicios, ¿sí? Usando la hora de práctica, que está para eso. Que ustedes hagan los ejercicios y que después cualquier cosa que no entiendan, que no les sale, nos muestren a nosotros, nosotros les explicamos, mira, sí, esto hiciste bien, esto no hiciste bien, esto así y esto. Entonces, no la desaprovechen. No hiciste bien, esto hiciste bien, esto hiciste bien, esto hiciste bien, esto hiciste bien.

¿No hiciste bien? No hiciste bien, esto hiciste bien, esto hiciste bien, esto hiciste bien. No, no, no, no. y esto hiciste bien. No, no, no, no.

¿qué significa? no. no, no. no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no. pero eso es lo que está pasando ese papel que le dan cuando ustedes se inscriben es una constancia que están inscritos en una comisión donde realmente sea el horario se trata de mantener eso no cambia pero el aula que finalmente les toca se publica unos pocos días antes de que empiecen las clases y está en la página de la facultad si te vas a links ahí está el horario y también se envió estamos chicos y lo otro que está bueno cuando comparten los ejercicios y los algoritmos que usen un algún editor algún editor de código que le pone en la parte izquierda el número de líneas entonces en el disco en particular cuando yo le tengo que marcar yo le puedo decir que está en tal línea porque si no es un poco engorroso digamos no puedo indicar donde está el error es un detalle que vamos a ir viendo pero le adelanto ¿quién sería la comisión C y D?

Comisión C son los del turno tarde arrancan a las 4 de la tarde hasta las 4 menos 10 hasta las 6 ustedes son comisión D la comisión D o 1.4 D4 que me pareció D4 D4 D4 D4 D4 D4 D4 D4 Por eso hacemos tanto esto así en la práctica. Porque aparte, ustedes van a intentar hacer, la primera vez seguramente no les va a salir bien, pero seguro ese error que cometiste donde vos te equivocaste, lo que agotó y con todo, seguro que ahí vas a aprender. Por eso es tan importante la práctica. Porque por ahí nos dicen, no, profe, le damos los ejercicios, bueno, ¿hicieron algo? No, profe, no.

De una semana para la otra, por ejemplo, no hicieron nada y quieren que nosotros resolvamos en el pizarrón, pero no es que no lo hagamos por mal, aparte que nos lleva mucho tiempo otra vez, ¿está? Entonces generalmente lo que hacemos, agarramos de uno que resolvió y lo mostramos, pero él, el que resolvió, va a aprender, ¿está? A lo mejor si hay alguien, otro que resolvió, va a mirar esa solución, nosotros le vamos a decir lo que está bien y lo que está mal, y él va a corregir lo que él hizo, y esa persona va a aprender, pero los que miran solamente nos van a aprender así. Por eso nosotros le echamos tanto con el práctico. Normalmente cuando hacemos el ejercicio nos puede pasar por el disco ese ejercicio.

Nos puede pasar la solución. Sí, a veces le pasamos, a veces no le pasamos, pero el tema es que ustedes lo hagan. ¿Sí? Que ustedes lo hagan. Muchas veces cuando a ustedes no les sale y lo piensan, y por ahí nos preguntan, o le preguntan a un compañero, y dicen, no, pero mira, fíjate esto acá, ahí lo entienden.

Bueno, como dice ahí, sus profes de práctica vamos a ser nosotros dos, y quizás, si tenemos suerte, vamos a tener algún ayudante más adelante, pero bueno, casi siempre vamos a ser nosotros los profes. El profe Diego, el miércoles, les va a hablar un poco más extenso de las actividades de evaluación que vamos a tener, pero básicamente van a ser tres parciales, cada uno con su recuperatorio, dos laboratorios de lenguaje, uno va a ser del lenguaje Python y otro va a ser del lenguaje C, y después van a tener en el aula, van a tener cinco cuestiones, uno por cada unidad, uno por cada unidad, uno por cada unidad, uno por cada unidad, eso es obligatorio. Si ustedes aprueban todas estas actividades, ustedes tienen aprobación directa de la materia, eso significa que no tienen que rendir final, ya se hace un promedio de todas las actividades que aprobaron, y esa es la nota del final y listo. Ese es el mejor escenario. Y pueden, usar un recuperatorio.

El recuperatorio, más que nada, más que nada, se refiere a los tres parciales, así que sean muy cuidadosos con los cuestionarios del aula y con los laboratorios, porque eso no tienen recuperatorio. Por ahí, todavía estamos viendo si hacemos alguna innovación con el tema de los lenguajes, con el de los laboratorios. Por ahí, si su laboratorio estaba, más o menos, nosotros los llamábamos, más o menos, nosotros los llamábamos, eso se hace en grupo, eso se hace en grupo, entonces los llamábamos al grupo y veíamos y por ahí se lo aprobábamos. Sí, pero, recomendación, prestenle atención a los laboratorios y háganlo bien ya de una. Listo, por eso, no tiene recuperatorio.

Sí, cada parcial tiene un recuperatorio y pueden usar un recuperatorio y si salen bien, promocionan o tienen aprobación directa de la materia. Si salieron mal en un parcial y después salieron mal en un parcial y después salieron mal en un parcial y después salieron mal en otro parcial, todavía siguen en carrera porque pueden regularizar la materia, eso significa que van a, después van a tener que rendir un final para aprobarla y pueden quedar como regulares en la materia teniendo una actividad, una actividad, una actividad evaluativa, una actividad evaluativa, una actividad evaluativa desaprobada. Exacto, pueden regularizar la materia con un parcial, por ejemplo, no aprobada. Y otra cosa, hagan su mayor esfuerzo para presentarse a los parciales porque ahora a fin de año he visto casos de alumnos que no se presentaron en ningún parcial. O sea, si ustedes no se presentan a rendir parcial, igual pueden retirar el recuperatorio.

Porque antes no se presentaron a rendir parcial, porque antes no se presentaron a rendir parcial. Pero vi casos de chicos que no se presentaron a ningún parcial. Y es una oportunidad que ustedes se la están jugando, o sea, dejás pasar esa oportunidad, no, porque después tenés que recuperar los tres parciales y ya ahí sí salís mal. Si salís mal en un parcial te queda todavía la chance en un parcial te queda todavía la chance en el recuperatorio, pero no dejen pasar. Háganme todo el esfuerzo de presentarse.

Acá no hay cuestión de pasar vergüenza. Obviamente, traten de prepararse lo mejor posible, pero igual vengan al parcial. Porque aparte, cuando vienen al parcial van a ver cómo es la dificultad y los ejercicios de parcial. Igual nosotros siempre antes de cada parcial. Si tenemos tiempo, si tenemos tiempo lo hacemos en clase y si no nos da el tiempo le ponemos en el drive algunos ejercicios de parciales anteriores.

Para que ustedes no digan ah, no, los ejercicios de parcial son muchísimo más difíciles que los ejercicios de la guía. A veces sí son. Por eso sí. Dicen hay algunos chicos que traen la notebook y hacen en la notebook. Algunos que hacen en la notebook y que usan Visual Studio.

Hay algunos que también ya saben algún lenguaje de programación. Y está buenísimo eso. Está excelente. Pero el día del parcial ustedes van a rendir en papel. Y en el papel no pueden copiar y pegar.

Entonces les va a llevar tiempo. Entonces acostumbrense a hacer los ejercicios en papel. A inscribir. Sí. Porque hay hijos excelentes.

Algunos que hemos tenido y salían mal porque no. Normalmente tienen dos horas para rendir parciales. Y un ejercicio les lleva más o menos una hora. Y otro ejercicio les debería llevar media hora. Entonces ustedes en una hora y media más o menos deberían terminar el parcial y después les quedaría una media hora para pegar una revisada.

¿Sí? Pero ¿qué pasa? Como muchos no se acostumbran a practicar en papel y les lleva demasiado tiempo. Y capaz sabían pero no les dio tiempo y entregan incompleto. ¿Sí?

Entonces. Acostúmbrense a hacer ejercicios en papel. ¿Sí? Bien. A ver el protocolo que dice acá.

Comenzamos a horario. ¿Sí? Por ahí, bueno. Si no llegan a horario, llegan 10 minutos después, no hay problema. Pero tampoco la idea es que lleguen media hora, 45 minutos después que empezó la clase.

Como dijo la profe Ilse, repasen la teoría. Vengan con el tema fresco. Normalmente vamos a ir a la par. Por ahí puede haber algún desfasaje, pero normalmente vamos a ir a la par con la clase de teoría. Entonces, si el profesor de teoría les dio el lunes una determinada estructura, lo más probable es que el miércoles nosotros en la práctica demos esa estructura.

¿Sí? Así que pendenle una mirada. Que pendenle una mirada. ¿Qué pendenle una mirada. ¿Sí?

Acá están dos vías de contacto. Por favor, escriban ese mail. ¿Sí? Porque después nunca se lo acuerdan y llegamos a noviembre y dicen ¿Cómo era el mail de la cátedra profe? Es cd, porque nosotros somos los profes del C y del D.

¿Sí? cd punto aed, que es algoritmo y estructura de datos, punto frre, o sea facultad regional resistencia, arroba gym. ¿Sí? Sí, sí, sí, sí, sí, sí. No, no, sí, no hay problema, no hay problema.

A ver, nosotros, nosotros siempre preferimos que vengan de manera presencial porque nos parece que acá que acá se entiende más. Tienen más posibilidad de preguntar y todo. Si bien, chicos, ahí los del Zoom ya saben que si quieren preguntar algo pueden habilitar su micrófono y preguntar o escribir en el chat. ¿Sí? Pero me parece más directo, digamos, venir presencial, pero si alguna vez se les complica, sí pueden ponerse al Zoom.

No hay problema con eso. Entonces, anoten, por favor, cd punto aed punto frre. Ese es el correo de la cátedra. Así que cualquier cosa que quieran comunicarse lo pueden hacer por ahí. Si bien también ahora tenemos el tema del Discord que antes no teníamos disponible.

Y también el link tree de la cátedra donde ahí vamos a ir poniendo las diferentes cosas. Diferentes cosas. Ahí normalmente los ejercicios de parciales anteriores los subimos ahí al drive. Sí, para que ustedes lo tengan disponible. Y algunos algunas resoluciones de ejercicio también subimos aquí al drive o algún material que sea útil.

Bueno, con eso ya empezaríamos con el link. ¿En el curso de ingreso dan algo de algoritmo? ¿Qué materia tuvieron en el curso de ingreso? Matemática y física. ¿Ellas tres?

¿Cuál? en la comprensión de textos. Bueno, ahora, bueno, ahora, bueno, bueno, ahora, bueno, ahora, cuando les explicamos el tema de los algoritmos, les vamos a decir que para resolver un algoritmo, bueno, nosotros les vamos a dar una consigna, un problema, y a partir de ahí tienen que escribir un algoritmo que solucione ese problema. Lo primero que hay que hacer es leer esa consigna dos o tres veces para asegurarse de que la entendieron. Una vez que la entendieron, recién se ponen a escribir, porque, ¿qué pasa?

¿Qué pasa? Unas cosas ya de los temas? De los temas. De los temas concretos, digamos. Ahora enseguida vamos a ver.

A ver, esta es la estructura de todos los algoritmos que nosotros vamos a hacer en el año. Vamos a poner la palabra acción. Vamos a ver que hay algunas palabras, como en todos los lenguajes, hay algunas palabras reservadas. En nuestro caso, siempre el algoritmo va a comenzar con la palabra acción. El nombre del algoritmo, que el nombre del algoritmo no debería contener espacios, ni comenzar con un número.

Ahora vamos a, cuando veamos el tema de los nombres de las variables, enseguida, ya vamos a ver. Ahora que él dijo palabras reservadas. ¿Todos saben que hay una palabra reservadas? ¿Alguien no? ¿Sabe?

En un lenguaje existen las palabras que usa ese lenguaje. Por ejemplo, yo te digo, una estructura repetitiva va a decir, mientras, una condición, hacer. Mientras, yo hacer, son palabras que ya el pseudocode está usando. Son palabras reservadas. Son palabras que ya el pseudocode está usando.

Son palabras reservadas. Decíamos, acción, el nombre del algoritmo, la palabra es, y después vamos a tener dos secciones diferenciadas. Una sección que se va a llamar ambiente, donde vamos a definir las variables y las estructuras que vamos a utilizar, y quizás también alguna subacción, un tema que vamos a ver en próximas clases. Y después, otra sección que se va a llamar algoritmo o proceso. Y ahí es donde vamos a escribir las diferentes instrucciones para llegar a nuestro objetivo.

Bien. Tipos de datos elementales. Nosotros en algoritmos vamos a tener estructuras de datos. Y esas estructuras van a usar tipos de datos elementales que son estos. El primer tipo de datos muy usado es el entero.

Son los números, como el nombre indica, los números enteros. Es decir, los números que no tienen decimales. Pueden ser números positivos o negativos o cero, pero siempre, sin decimales. Después tenemos el tipo de datos real, sin decimales. Después tenemos el tipo de datos real, que son los números decimales.

Recordemos que los reales incluyen a los enteros. ¿Se entiende? Si yo defino una variable como real, también va a contener los enteros. Acá tenemos cómo lo vamos a escribir nosotros en el pseudocódigo. Lo vamos a escribir nosotros.

Esas dos maneras. el menos, la coma, el paréntesis. a través de la página web. Les pedimos encarecidamente. A ver.

Estamos cada vez más usando la inteligencia artificial, ¿no? ¿Cierto? ¿Sí o no? Sí. Y ustedes muchas veces para resolver un ejercicio no nos engañemos.

Van a usar la inteligencia artificial. Ahora, lo importante es que ustedes tomen lo que les sirva de la inteligencia artificial, pero no copien y peguen. Muchas veces nos pasa que nosotros les damos un ejercicio y ustedes después nos ponen string. String es cadena de caracteres, pero nosotros en el pseudocódigo no usamos string. Entonces, por más que ChatGPT les diga string, ustedes no lo escriban así.

Cadenas de cadenas de cadenas de cadenas de cadenas de cadenas de cadenas de cadenas de cadenas de cadenas de cadenas de cadenas de caracteres, pero nosotros eso no lo enseñamos. En pseudocódigo no existe. Entonces, si alguno lo sabe hacer en Python, bueno, que entienda que en Python está perfecto, pero acá no. Pero lo que me parece más peligroso es que los que ni siquiera lo saben hacer en Python, sino que le preguntaron a ChatGPT, ChatGPT le dijo que lo haga, porque ChatGPT sí, muchas veces te dan la respuesta en Python y te gusta la concatenación. Y algunos, Ani, eso que le largó ChatGPT, pues lo ponen ahí en la hoja y no.

No. No, no, no, no. No, no, no. No, no, no, no, no. Todo lo, no.

No, no. no, no, no. Bien. Y después tenemos el tipo de dato booleano. Es un tipo de dato que solamente puede tener dos valores.

Verdadero o falso. Después vamos a ver ejemplos de los cuales usamos esos tipos de datos. que son las variables. los dos puntos y el tipo de datos. si yo.

Si yo defino una variable de tipo alfanumérico de 20, alfanumérico entre paréntesis 20, que voy a poder hacer con esa variable. Voy a poder guardar un nombre, un apellido. Voy a poder guardar números. También. Pero que va a pasar con esos números.

no. No. No tiene que superar los 20 caracteres. Exacto. Sí.

Y no se van a poder hacer operaciones matemáticas. Se toman como símbolos. Sí. Porque yo definí que mi alfa, mi variable era de tipo alfanumérico entre paréntesis 20. Si yo hubiera definido que era de 40, no.

No. Vamos a poder superar los 40. ¿Verdad? Todo depende de cómo la defino yo. En el caso de 40.

¿En el caso de 40. En realidad, en el caso de 40. En realidad, en el caso de que se inserte más de 40, ¿se almacena los primeros 40 caracteres o no se almacena los primeros 40 caracteres? En realidad, en realidad, a ver, ahí ya nos vamos a una parte más técnica que depende del lenguaje. ¿Sí?

Normalmente, ¿qué sucedería? Te va a dar un error. Si vos definiste una variable en nombre y le pusiste alfanumérico de 10, si vos querés escribir un nombre que tiene 11 caracteres un nombre que no se puede. Pero nosotros no tenemos ese inconveniente. ¿Por qué?

Porque si vos definiste un nombre como alfanumérico de 10, vamos a asumir que siempre se van a poner nombres de hasta 10 letras. No nos hacemos tanto problema con eso. Lo que sí es importante que seamos cuidadosos al momento de definir una variable. Por ejemplo, si yo tengo una variable que se llama edad, ¿de qué tipo va a ser? Entero.

¿Sí? Si yo tengo una variable que se llama altura, ¿de qué tipo va a ser? Real. Porque la altura de una persona o de un edificio puede tener coma. Si tengo una variable que se llama cantidad de cantidad de estudiantes.

Ahora vamos a ver los nombres de las variables. Pero supongamos que se llama cant. ¿De qué tipo debería ser? Entero. Pues yo no puedo tener 28 estudiantes y medio.

¿Sí? Bueno, así. Si yo tengo una variable peso, sería real. Y así. Bien.

Entonces, si nosotros tenemos una variable que llamamos edad. Como está ahí en el ejemplo. Eso es un espacio de memoria que va a estar definido de tipo entero. Y que va a estar esperando que ahí adentro se guarde un entero. Nosotros a esa variable dentro de las instrucciones que va a tener nuestro alfanumérico y al algoritmo, podemos asignarle un valor.

Ahora después vamos a ver las dos maneras diferentes que tenemos de asignarle un valor. Bien. Supongamos que le asignamos el valor 8. Entonces ahora esa variable, cuando yo use esa variable para algo, esa variable va a valer cuánto? 8.

Correcto. Y después, si yo a esa variable le asigno el valor 6, ¿qué pasó? Ahora la variable 6. Ahora la variable 6 y ya no vale más 8. El 8.

El 8, chau, se perdió. Desapareció. No queda guardado en ningún lado ese 8. Y acá hay un concepto también importante. Antes de que yo le asigne este 8 a la variable, ¿cuánto valía?

¿Qué valor tenía? ¿Qué número tenía la variable? Antes del 8. No sabemos. Entonces, lo que decimos es que esa variable tiene un valor indeterminado.

Que no es lo mismo que decir que no tiene nada y no es lo mismo que decir que tiene cero. ¿Está? ¿Se entiende? Más adelante vamos a ver. Hay algunas variables como la edad, ¿Sí?

Que yo le voy a tener que asignar un valor. Enseguida vamos a ver cómo. Pero más adelante vamos a ver que hay algunas variables que son especiales. Por ejemplo, los contadores. Los contadores me van a servir para que yo, adentro de mi proceso, vaya contando algo.

¿Sí? Vaya contando. Vaya contando, por ejemplo, los estudiantes que aprobaron un examen o vaya contando, no sé, la cantidad de autos que entraron en estacionamiento, cualquier cosa. Y a esa variable contador, yo cada vez que pase por un determinado proceso le voy a tener que ir sumando uno. ¿Está?

Por ejemplo, si le pregunto si el estudiante aprobó, cuento. Si el estudiante no aprobó, no cuento. ¿Está? Y ese contar es sumarle uno y ese contador. Pero hay una acción muy importante.

Pero hay una acción muy importante, fundamental que tengo que hacer con esa variable antes de que tengo que hacer con esa variable antes de empezar a contar. Y es definirla así. Definirla así. Definir todas las variables las tengo que definir. Pero tengo que inicializar la variable.

Yo no puedo empezar a contar estudiantes que aprobaron o autos azules si yo no le puse un valor primero. Entonces yo no le puse un valor primero. Entonces yo lo primero que tengo que hacer con esa variable. Entonces yo lo primero que tengo que hacer con esa variable es asignarle un valor cero para asegurarme que tiene cero y ahí recién empiezo a contar. O no.

O no, bueno. Depende de... Un valor inicial. Exacto. Sí.

En el 99% de los casos se alicia con cero. Puede haber ejercicios donde no. ¿Sí? Está. Pero es importante que ustedes entiendan y siempre recuerden que cuando yo no le asignan y siempre recuerden que cuando yo no le asigné todavía un valor a una variable tiene un valor indeterminado.

No sé qué puede tener ahí adentro. Y si yo quiero usar esa variable para algo me va a dar error. ¿Sí? Porque no tiene valor. Y ahora vamos a ver que nombres correctos puede tener una variable y qué nombres incorrectos puede tener una variable y qué nombres incorrectos puede tener.

Los que están ahí a la izquierda son todos nombres incorrectos. Primero, una variable nunca puede empezar con un número. ¿Sí? Puede tener números después. Yo puedo tener cont 1, con 2, con 3, con 4, con 999, pero no puede iniciar con un número.

Tampoco puede tener espacios. Puede tener guión bajo, puede tener guión medio, pero no espacios. No puede ser una palabra reservada del sistema. Es lo que estábamos diciendo hace un rato. Una variable no puede llamarse acción, no puede llamarse ambiente, no puede llamarse mientras, no puede llamarse leer.

Eso pasa en el rato. Eso pasa en cualquier lenguaje. Y tampoco puede tener símbolos como el arroba o como el signo de exclamación o un signo de pregunta. Solamente letras y números. Pero los números no al principio.

Y ahí vamos a ver que qué nombre sí pueden tener. ¿Qué nombre sí pueden tener? Pueden tener un nombre, por ejemplo, con palabras. ¿Sí? Que se entiende que es un contador de palabras.

O si ustedes quieren, para que sea más claro, le pueden poner un guión bajo. ¿Sí? Lo pueden poner todo junto o con un guión bajo. Es lo mismo para nosotros. Nosotros no vamos a distinguir en segundo código la diferencia entre mayúsculas y minúsculas.

O sea que si ustedes a una variable le ponen bar, para nosotros es la misma variable. No pueden poner una variable con mayúsculas y otra con minúsculas creyendo que son dos distintas. No. Para nosotros es la misma variable. Y otra cosa, que los nombres de las variables sean representativos.

¿Sí? Si yo voy a hacer un algoritmo en el algoritmo en el algoritmo en el algoritmo en el algoritmo en el algoritmo. ¿Sí? No. O sea, la idea es que no sean nombres tampoco tan largos.

No hay problema. no hay una constante que no hay una constante que no hay una constante que se llama pi y ya no hay una constante que se llama pi y ya recibe el valor en el momento de su definición recibe el valor 3, 14 15 92. ¿Sí? Sí. La constante siempre se va a definir en el ambiente igual que la variable.

La diferencia es que la constante va a tener un signo igual. Eso me va a indicar a mí que es una constante y no una variable. Que no se modifica en el momento de ejecución. Y va a recibir un valor. A ver.

La constante, el nombre de la constante tiene que cumplir las mismas reglas que el nombre de la variable. No puede ser una palabra reservada, no puede empezar con número, no puede tener espacios, no puede tener símbolos raros. Exacto, exacto. Así es. El IVA, lo pusieron.

El IVA en otro país. En otro país es mucho más bajo. En un momento hace mucho. En un momento hace mucho lo subieron como una medida excepcional porque el Estado necesitaba recaudar más lo subieron al 21% supuestamente por un tiempito y después prometieron que iba a bajar nunca bajó. Si le preguntan a todos los que son dueños de alguna empresa ruegan que baje algún día el IVA pero no está sucediendo eso.

Ahora, ¿qué pasa? Si nosotros en un momento tenemos que hacer un programa. Si nosotros tenemos que hacer un programa, un algoritmo para un comercio. Por ahí vamos a necesitar tener los precios sin IVA y los precios con IVA. Entonces, si yo escribiera el algoritmo así nomás, tengo el precio sin IVA y después para calcular el IVA agarro ese precio y lo multiplico por 0,21 y ya tengo el IVA y se lo sumo y qué sé yo.

Yo podría tomar una variable y qué sé yo. Yo podría tomar una variable y yo. Yo podría tomar una variable y multiplicarla por 0,21. ¿Puedo hacer eso o no? Sí.

Pero ¿qué problema tengo? ¿Cómo? Si en algún... Supongamos que yo tengo un algoritmo muy largo. Algoritmo que tiene 3.000 líneas.

Y yo en vez de usar una variable y yo en vez de usar una variable y yo en vez de usar una variable y yo en vez de usar una constante para el IVA le puse 0,21 en todos lados. ¿Qué pasa si algún día el IVA cambia y baja al 14%? Voy a tener que recorrer todo mi algoritmo para ver en todo lado donde yo había puesto 0,21 y cambiarle por 0,14. Y ahí corro el riesgo y que se me pasa y se me pasa y se me pasa y se me pasa y se me pasa y se me pasa y se me pasa y se me pasa y se me pasa y se me pasa. Obviamente, obviamente, cuando ya estamos hablando de un lenguaje de programación voy a tener que agarrar el código fuente de mi programa voy a tener que modificar eso voy a tener que compilarlo de nuevo ¿Sí?

¿Por qué? Porque dijimos que no es una variable no la puedo cambiar solamente en el momento de ejecución hay que el momento de compilación va a tener que cambiar ¿Sí? ¿Sí? Pero bueno, esa es la idea. Es muchísimo más fácil hacer eso que estar cambiando uno por uno en todos los lugares donde se usa.

¿Ya? ¿Se entiende? Bien. A ver, vamos a ver esto y ya con esto terminamos. Yo les había dicho que a una variable hay dos maneras de asignarle algún valor.

Una de las maneras de asignarle algún valor. Una de las maneras de hacerlo es usando la acción de asignación que nosotros la representamos con dos puntos igual. Si yo a la variable edad le asigno el número 8, la variable edad que antes tenía un estado indeterminado, ahora pasa un estado indeterminado, ahora pasa un estado indeterminado, ahora pasa un estado indeterminado, ahora pasa a valer 8. Y si unas líneas del algoritmo más abajo, a edad le asigno 6, ¿Qué pasa con eso? Ahora pasa a valer 6 y el 8, chao, se perdió.

Por eso decimos que la asignación es destructiva. Destruye el valor que tenía antes. Ese valor es sobre escrito y el nuevo valor que tenía antes. El valor que tenía antes. ¿Cuánto va a valer edad.

5. ¿Por qué? Porque era el valor que tenía la variable a. Lo que tenía la variable edad se pierde. Y ahora avanzando un poquito con el tema de estos contadores.

Si yo a edad le asigno edad más 1, va a tener 6. Entonces yo a edad le asigno edad. Lo que tenía edad era 5. Más 1, 6. Entonces edad termina 6.

Si yo después en otro momento le vuelvo a hacer edad de edad más 1, va a tener 7 y después 8 y edad. ¿Está? ¿Se entiende? Bien. Y ahora vamos a ver, Jaco, último tema de la clase.

Es la otra acción. El otro verbo. El otro verbo que a mí me permite asignarle el valor a una variable que es leer. Cuando yo utilizo la instrucción leer, lo que le estoy diciendo leer, lo que le estoy diciendo leer entre paréntesis año, lo que estoy diciendo ahí que el usuario tiene que ingresar algo por el teclado y que eso que ingresa va a ir a la variable año. ¿Está?

Siempre, siempre antes de un leer. Siempre antes de un leer tiene que ir un qué. Escribir. ¿Por qué? Porque ustedes imagínense que el leer, el leer para el usuario que está viendo mi programa es un cursor que está titilando ahí.

¿Está? Y él no es adivino, no sabe qué tiene que hacer si yo no le dije antes ingresar tal cosa. Entonces, el escribir a mí me permite, la acción de escribir, la acción de escribir, mostrar por pantalla algún mensaje. Pongo entre comillas lo que yo quiero que aparezca por pantalla y entonces le pongo, por ejemplo, ingrese su año de nacimiento. Va a escribir eso, lo va a mostrar por pantalla y seguido a eso viene una instrucción leer que lo que va a hacer es que lo que el usuario me ingrese por el teclado lo va a guardar en este caso en la variable año.

¿Cuáles son las dos acciones? ¿Cuál es la asignación? Buenísimo. Entonces, después voy a subirle ahí al drive esta presentación. Igual tienen la otra versión vieja.

Y nos vemos. El miércoles. Nos vemos chicos los que están en la casa después les subo la grabación. Chau chau.
