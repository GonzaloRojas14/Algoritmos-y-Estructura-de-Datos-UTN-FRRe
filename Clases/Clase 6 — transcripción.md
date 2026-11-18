---
tipo: transcripcion
materia: Algoritmos y Estructura de Datos
clase: 6
tags:
  - AED
  - transcripcion
---

# Clase 6 — Algoritmos y Estructura de Datos

> [!info] Transcripción completa de la clase grabada
> Texto íntegro, sin resumir. Generada con Whisper desde `clase6.wav` y
> depurada con `dedup.py` (colapsa oraciones repetidas consecutivas, que son
> alucinaciones del modelo, no habla real del profesor).
> Video original: `temp_videos/clase6.mp4`

---

Ahí estamos grabando. Bueno, les explicamos cómo iban a hacer la nota de los parciales este año. Creo que sí, estoy casi seguro que sí, pero bueno, repasemos ese tema. Este año va a ser así. Ustedes, como siempre, van a tener que rendir primero la parte teórica.

Pero la parte teórica no va a tener nota, va a ser tipo aprobó o no aprobó. Aprueban la parte teórica y pasan a la práctica. Si no aprueban la teoría, ni siquiera rinden la práctica, ya tienen un 1 ahí. O la nota que hayan sacado en teoría. Si aprueban teoría, ahí pasan a la práctica y ahí les corregimos el parcial práctico.

Y la nota que van a tener en el parcial es la del práctico. O sea, no importa si sacaron un 10 en teoría, si en el práctico sacaron 6, van a tener un 6. Si en el práctico sacaron un 5, no se aprobaron. No importa si sacaron un 10 en teoría. O sea, tienen que estudiar teoría, pero tienen que tener mucha práctica, porque la nota que vale finalmente es la de práctica.

¿Ok? El ejercicio de, todavía no estoy 100% seguro, pero casi 99, el ejercicio de secuencia va a valer 6 puntos. Y el otro ejercicio va a valer 4 puntos. O sea, que el de secuencia va a ser más difícil. Así todo, si hacen perfecto el ejercicio de secuencia, pero no hicieron nada del otro, también salen mal.

Porque tienen que tener los dos hechos. Por eso yo siempre les digo, practiquen. Porque la práctica en esta materia es fundamental. Probablemente lo pasemos una semana. Si nos da, mira, si nos da el tiempo, si nos da el tiempo, vamos a dedicar una clase entera para practicar para el parcial.

Pero, ustedes tienen que, ustedes tienen que comprometerse a hacer el ejercicio, porque muchas veces nos pasa que le damos un ejercicio y le decimos, miren, así va a ser el parcial y se ponen a pabear, se ponen a mirar otra cosa o algunos se van. Entonces, no tiene gracia. ¿Está? Nosotros les vamos a dar ejercicios de parciales anteriores o simulacros de parcial. Ustedes tienen que hacerlo.

¿Sí? ¿Por qué? ¿Por qué es importante que hagan esos ejercicios de parciales? Porque los ejercicios de parciales siempre son más difíciles que los ejercicios de parciales siempre son más difíciles que los ejercicios que hacemos en clase. Por eso nosotros se los damos para que ustedes vean cuál es la complejidad que tomamos en el parcial.

¿Está? ¿Sí? Bien. ¿Alguna duda con respecto a los temas que venimos dando. Bueno, a ver, vamos a hacer un muy breve repaso de la parte de funciones y procedimientos.

Y después vamos a hacer algunos ejercicios de parciales. Funciones y procedimientos. ¿Sí? Y en la segunda mitad de la clase vamos a arrancar con el tema de secuencias de datos elementales. ¿Ok?

Bueno. Supongamos. Yo empiezo un ejercicio, ¿no? Le pongo acción, ejercicio, modelo, es. ¿Qué es lo primero que tengo que poner?

Perfecto. Ambiente. Constantes. Constantes, variables, funciones y procedimientos. ¿Cómo?

¿En qué orden lo defino? Bien. Primero defino las constantes. Y las constantes se definen con un igual. ¿Sí?

Después, ¿qué defino? Variables. Voy, voy, voy. Ahí está. Variables que defino con dos puntos.

Y después vienen funciones y procedimientos que pueden ser indistinto el orden o no. ¿Yo puedo tener un procedimiento que llame a funciones? Sí. ¿En qué orden tengo que definirlos? Primero las funciones y después el procedimiento.

No sería lógico que yo en un procedimiento llame a una función que todavía no está definida. ¿Sí? Lo mismo que una función puede llamar a otra función? Sí. ¿Cómo tengo que definirlas?

En el orden inverso. O sea, la función que llama a la otra tiene que definirse después que la otra. ¿Sí? Entonces, supongamos que yo tengo una función que yo tengo una función que yo tengo una función que se llama que se llama que no sé calcular y va a recibir qué cosa. Parámetros.

Un parámetro uno. Un parámetro dos. Supongamos que fueran los dos enteros o los dos reales. ¿Está? Si yo, además de eso, si yo, además de eso, fuera a, además, si fuera a recibir un parámetro que es alfanumérico o un carácter, tendría que poner acá, por ejemplo, puedo poner carácter o puedo poner alfanumérico de uno.

¿Está bien? Y después, ¿qué pongo? El tipo de datos. El tipo de datos que va a devolver mi función. ¿Una función puede devolver más de un dato?

Seguro, ¿eh? ¿Cuántos respondieron? Tres. ¿Y los otros? ¿Puede devolver más de un dato?

No. Por eso, lo que vamos a poner acá, después de dos puntos, es el tipo de dato que va a devolver la función. Me va a devolver un solo dato la función. ¿Está? Vuelvo un dato.

Después puedo hacer varias cosas dentro dentro de la función dentro de la función dentro de la función dentro de la función dentro de la función dentro de la función. No es llamar, es asignarle el valor a la función. Yo tengo que a la función calcular en algún momento de mi función le tengo que asignar algo. ¿Sí? Y ese algo, en este caso, en este ejemplo, en este ejemplo, ¿de qué tipo de datos estamos hablando?

Real. ¿Por qué? Porque yo definí que mi función es real. ¿Y eso puede hacer un carácter? ¿Este?

No, eso es algo que viene de afuera. Es un parámetro que va a recibir la función. La función va a recibir, supongamos que va a recibir dos enteros, vamos a ponerle para, va a recibir dos enteros y un carácter. O sea, ¿cuántos parámetros tiene mi función? Tres.

Par uno, par dos y car. Se supone que acá adentro tiene que hacer algo con par uno, par dos y car. ¿No? Sí, exacto. Los parámetros trabajan como variables locales.

¿Está? Hacemos algo con par uno, par dos y car. Y después en algún momento a calcular le asignamos algo que es de tipo real. ¿Está? Y termina mi función.

Fin función. Bueno, supongamos que después tengo otro procedimiento. Un procedimiento. Procedimiento que se va a llamar ¿Cómo le llamamos? ¿Eh?

Descalcular. Y el procedimiento. Sí, porque no nos llegaba a mi cal. ¿Por qué el procedimiento recibe parámetros? Puede ser que sí, puede ser que no.

¿Sí? Pero muchas veces recibe parámetros. ¿Sí? Vamos a ponerle par tres de tipo real. ¿Sí?

Y acá tengo que ponerle dos puntos y un tipo de datos. ¿Por qué no? Exacto. Porque el procedimiento no devuelve un valor. Es la diferencia que hay entre los procedimientos y las funciones.

¿Está? Bueno, entonces acá pasan cosas y vamos a ponerle dos puntos. Bueno, entonces acá vamos a ponerle dos puntos. Bien, entonces acá vamos a ponerle dos puntos. ¿Por qué no?

Entonces acá vamos a ponerle dos puntos. Y aquí vamos a ponerle dos puntos. Y yo voy a ponerle dos puntos. Y después podría tener un leer opción. Y después con esos tres parámetros.

Y después con esos tres parámetros puedo llamar a mi función calcular. ¿Sí? Porque necesito dos enteros y un alfanumérico. ¿Sí? Bien.

Y estaría bien que yo haga esto. Claro. N1, A ver. N2, opción. ¿Podría hacer esto?

¿Por qué no? Necesito una variable global para poder asignarle el valor. Necesito una variable global a la cual asignarle el valor. Yo no puedo llamar a una función así suelta. Entonces yo lo que podría hacer es a una función, no sé, result, asignarle el valor que devuelva la función.

¿Eso está bien? Bien. Perfecto, eso está bien. Y después yo podría preguntar si result es menor que 100, entonces. ¿Está bien?

¿Se puede hacer eso? Bien. ¿Cuál sería una alternativa. ¿Cuál sería una alternativa si yo quiero llamar a la función y preguntar si ese valor es menor a 100? ¿Cómo?

Poner en el condicional. Exacto. Llamar a la función en el condicional. Eso sí se puede hacer. Yo puedo preguntar si calcular es menor a 100 entonces.

¿Sí? Esto sí se puede hacer. ¿Se entiende? Bien. Entonces se puede hacer esto.

Va a hacer esto. Y se puede hacer esto también. ¿Ok? Y después. Supongamos que hago acá leer N3.

¿Está bien esto? ¿Sí o no? Levante la mano quien dice que sí. Levante la mano quien dice que no. Bueno, muchos dicen que no.

¿Quién dice que sí? No. Está mal. El procedimiento no devuelve un valor. Entonces no tenés nada que asignarle a esta variable, ¿entendés?

Así como acá en el procedimiento no pusimos dos puntos y un tipo de dato. ¿Por qué? Porque no devuelve un valor el procedimiento. Entonces no tengo ningún valor para asignárselo a nada. ¿Se entiende?

Sí o no. A ver, sería correcto. ¿Esto sería correcto. Esto sería correcto. Sí.

Llamo al procedimiento. Al procedimiento sí lo puedo llamar. Así suelto. Sí. Acá.

No. Exacto. Si vos haces esto. No haces esto. Es como que esta acción acá reemplaza a las dos.

Obviamente que vas a hacer esto si no necesitas este resultado para otra cosa. Si vos vas a usar ese resultado en dos, tres, cuatro acciones, te conviene calcularlo y guardarlo en una variable. Pero si solamente lo vas a guardar para, si lo vas a calcular para ese condicional, te conviene hacerlo así. ¿Sí? Bien.

Ahora tenemos una, tenemos tarea para ustedes. La profe Ilse les mandó en el Discord, no sé quiénes leyeron un aviso. ¿Leyeron o no leyeron? A ver, en el Discord, no sé quiénes leyeron un aviso. En el Discord, no sé quiénes leyeron un aviso.

Así que bueno. Ahí en el Discord tienen el link para entrar. Igual les muestro acá. Hasta esta fila. Hasta la cuarta.

Van a hacer el ejercicio cuatro. Después. Sí. Acá van a hacer uno, dos, tres, cuatro. Hasta la nueve.

Van a hacer ejercicio cinco. A ver. No. Ustedes van a hacer el diez. Ustedes van a hacer el diez al medio.

Y las últimas cuatro van a hacer el ejercicio cinco. Vamos. Rápidamente. Ejercicio cuatro. Primero, ¿se acuerdan que les dijimos varias veces?

Varias veces. Lean los enunciados más de una vez. Y lean los enunciados más de una vez. Entiendan bien lo que se les está pidiendo y recién después pónganse a pensar la solución. ¿Está bien?

Entonces, ejercicio cuatro. Tienen que hacer una función que calcule el total de una factura después de aplicarle el IVA. La función tiene que recibir como parámetro la cantidad sin IVA, el precio sin IVA y el porcentaje de IVA que hay que aplicar. Y tiene que devolver el total de la factura con el IVA de aplicado. Si se invoca la función sin pasarle el porcentaje y el IVA con el IVA.

Y tiene que aplicarle un 21%. ¿Está bien? Bastante fácil. Vamos allá con las últimas cuatro. Ustedes tienen que hacer el ejercicio cinco.

Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función. ¿Quién sabe la fórmula del círculo? ¿Quién sabe la fórmula del área del círculo? Googleen, si parece que tiene celular todo. ¿Fuerte?

¿Sabes que el profe está medio sordo? Pi por radio al cuadrado. Bien. Entonces, ustedes tienen que hacer una función que pida... ¿Cuántos datos tienen que pedir?

Solo el radio. Solo el radio, porque pi ya conocen. Solamente necesitan el radio. Piden el radio. Piden el radio, ¿Sí?

En el algoritmo principal piden el radio y con ese radio llaman a la función y ahí hacen la fórmula y devuelven el área del círculo. Bien. Ahora, ¿Cómo se calcula el volumen de un cilindro? ¿Qué forma tiene? ¿Cómo se calcula el volumen de un cilindro?

Pi por radio al cuadrado por altura. O sea, básicamente es el área del cilindro que está en la base multiplicado por la altura del círculo. El área del círculo que está en la base multiplicado por la altura del cilindro. ¿Sí? Entonces, ustedes tienen que calcular ese volumen pero usando la función de área que definieron antes.

¿Ok? Listo. Ahora vamos al 10 que es el fácil. Escribir una función que convierta un número decimal en binario Escribir otra función que convierta un número binario en decimal. Escribir otra función que convierta un número binario en decimal.

Ese es fácil. No. Nada. ¿Qué? Claro.

Qué buena idea. A ver. Vayan. Miren. Miren, miren, miren.

Como quieran. Hagamos. Hagamos un ejemplo. Hablando el resto. ¿Sí?

Bien. Entonces, fíjense. Hacemos una división entera de 15 dividido dos. Me da siete. ¿Y el resto?

Uno. ¿Ok? Ahora. Al siete lo vuelvo a dividir por dos. ¿Cuál toda la división entera?

Tres. ¿Y el resto? Uno. Bien. Ahora.

Este uno. Esto yo lo tengo que ir. Este uno. Este uno va a ser mi último número binario. Este uno.

¿Cuánto vale? Digamos. Si yo tuviera que ir sumando todo esto. Una unidad. Entonces es uno.

Este uno. ¿Vale uno? ¿Cuánto vale? Diez. Este uno.

Yo lo tengo que sumar pero me tiene que quedar en la tercera posición. Entonces, ¿cuánto vale? Cien. Y esto lo vuelvo a dividir por dos. ¿Cuánto me da?

Cien. Y esto lo vuelvo a dividir por dos. ¿Cuánto me da? Cien. Cero.

Cien. . C. Cien. C.

. C. . C. .

C. . C. . C.

. C. . C. .

C. . C. . C.

. C. . C. .

C. . C. B. C.

B. C. que es BINDEC. Ahora veamos. Esto sería de decimal a binario.

Ambiente local, no se pone local, se pone ambiente y proceso. A DECBIN le asigno cero y al contador le asigno cero. Acá, al contador, dos puntos, no me enteró la asignación. Repetir. DECBIN más NMod2 por 10 elevado al contador.

Al contador, contador más 1 y a N, NDIP2. ¿Se entiende esto? Más o menos. Es lo que estábamos diciendo allá. Al número, al número BIN, que va a ser finalmente mi número convertido a binario, le voy a asignar lo que tiene.

¿Cuánto es lo que tiene originalmente cuando entra acá? ¿La primera vez? Cero. Si acá le asigné cero, la primera vez que venga acá, ¿cuánto vale esto? Cero.

¿Sí? Cero. Multiplicando por 10. Claro. Sí, le asignaba uno, después le multiplicaba por 10, te da 10, la próxima vez te da 100, la próxima vez te da 1000.

También es otra manera de hacerlo. ¿Están? ¿Se entiende? ¿Se entiende esta parte del algoritmo? ¿O no?

Bien. Y la otra función de binario a decimal. Tenemos un contador entero. A BINDEC le asigna cero. Y repetir BINDEC.

No, esto está mal. Esta línea es NMod10 por 2 elevado al contador. Pero después pasa de binario decimal. Por eso. Cuando vos pasas de binario decimal.

Supongamos que vos tenés 1. Y este lo tenés que multiplicar por 2 elevado al 1. Es 2. A este lo tenés que multiplicar por 2 elevado al cuadrado, que es 4. Y a este lo tenés que multiplicar por 2 elevado al cubo, que es 8.

¿Sí? Pero no es 10. Es 2. Acá en este 10. Acá.

En este 10. Va un 2. ¿Sí? Básicamente la idea es la misma. Hay otro chico que creo que lo había pensado como hacer un mientras primero para ver cuál es la cantidad de dígitos que tiene ese número binario.

Y después sabiendo la cantidad de dígitos empieza por el dígito más significativo y va calculando hacia el número menos significativo. Otra manera de hacerlo, pero esta es más corta y más simple. Bueno. Todo tuyo. Un pequeño repaso entonces lo que vieron con el profe Diego.

De secuencias. Que es una secuencia de un conjunto de datos relacionado entre sí. Por ejemplo, dice 1, 2, 3 hasta el número N y tiene una marca de fin de secuencia. F de F de S. Lo que están sacando fotos es porque no vieron para nada el drive porque esta presentación ya está subida en el drive.

O sea que la pueden leer nomás. Eso en el drive. Eso en caso de que sea numérico. Y si es carácter o es algoritmo. Y el último es algoritmo y el último es una marca especial.

Bien. Secuencias tiene cuatro características. La primera característica es un primer elemento distintivo que nos permite trabajar con la secuencia. Es el acceso para poder poder empezar a trabajar con la secuencia. La segunda característica.

La segunda característica es que todos los elementos están relacionados de alguna manera. Entonces hay una relación de sucesión. Salvo el primero que inicia y salvo el último que cierra no tiene relación. Son elementos distintivos. La tercera característica es que es finita.

Existe una secuencia infinita porque justamente va con la siguiente característica que tiene un indicador que tiene un indicador de fin de secuencia. Y el fin de secuencia. Y el fin de secuencia es un elemento distintivo que nos indica que está terminando esta secuencia. Hasta ahí termina. ¿Sí?

Bien. ¿Cómo se clasifican las secuencias? Hay dos maneras. Uno es en base al contenido y otro en base a cómo se va a procesar la secuencia. Según el contenido lo que vamos a procesar la secuencia.

Y lo que vamos a procesar la secuencia. Lo que vamos a procesar la secuencia. Y lo que vamos a procesar la secuencia. Y lo que vamos a ver ahora es datos elementales. Números o caracteres.

Y registro. Que eso vamos a ver la clase que viene. Más adelante. Después que terminemos todo lo del tema de secuencia. Otra manera de clasificarlo es según cómo se procesa.

Y tenemos dos maneras. Definidas. Y ya sabemos de antemano cuántos elementos vamos a trabajar. Y las indefinidas. Las definidas.

Es ya sé cuántos elementos tiene mi secuencia. Por ejemplo, si tengo 12 elementos y cada elemento me determina el mes, el estado de cuenta de un mes, entonces tengo un ciclo de un para de i, de 1 a 12, y sé que cada elemento es un mes del año. ¿Está? Entonces, de esa manera controlo ese tipo de secuencia. Es un tipo de secuencia.

Es el ejercicio le dice, específicamente tiene un elemento distintivo que no pertenece a la secuencia. Es para marcarme el fin. ¿Cuáles son las operaciones con que vamos a contar para trabajar con ese tipo de datos? Estructura de datos. Uno es arrancar la secuencia.

Que lo que hace es, estamos empezando, está diciendo al algoritmo, que estamos por empezar a trabajar con esa secuencia. En este caso, ARR seco. Y la siguiente es avanzar. Y la siguiente es avanzar secuencia y B de ventana. O sea que vamos a trabajar ese elemento de esa secuencia.

Entonces, uno inicializamos y el otro vamos a ir recorriendo los elementos. Esto es para lectura. Siempre hay una secuencia que ya existe. Y después tenemos cuando vamos a crear una secuencia. B contiene el valor B contiene el valor B contiene el valor B contiene el valor B contiene el valor B contiene el valor B contiene el valor B.

¿Sí? ¿Estamos ahí? ¿Sí? Bueno, acá tenemos una estructura que corresponde indefinida pura. Indefinida pura.

Indefinida impura. Y tenemos la condición. De un lado tenemos el pseudocódigo y del otro lado tenemos el diagrama de flujo. ¿Sí? Cuando arrancamos la secuencia.

¿No? No. Es como posicionar la secuencia. No. Es como posicionar la secuencia para empezar a trabajar.

Siempre tenés que arrancar una secuencia existente para poder trabajar. No, no. Es como posicionar la secuencia existente para poder trabajar. No, no. Es como posicionar la secuencia para empezar a trabajar.

Siempre tenés que arrancar una secuencia existente para poder trabajar. No, no. Es como posicionar la secuencia existente para poder trabajar. No, no. Es como posicionar la secuencia existente para poder trabajar.

No, no. Es como posicionar la secuencia existente para poder trabajar. No, no. Es como posicionar la secuencia existente para poder trabajar. Sí, está mal.

Está mal. Prepara antes del primer elemento. Sí, está mal. Y cuento el elemento. Sí, está mal.

¿Cómo? No, no. No existe. Sí, exacto. Está contando la cantidad de elementos.

Este algoritmo lo que hace es contar la cantidad de elementos que tiene una secuencia. Una observación. Ahí fíjense que en el mientras dice mientras no fin de secuencia y el nombre de la secuencia. Esa es una función que hasta ahora no la habíamos visto. Simplemente lo que hace la función.

La función en realidad se llama fin de secuencia. Y lo que hace es analizar si está parado en el elemento final de la secuencia. Esa función va a devolver verdadero si está parado en ese elemento final. Y va a devolver falso si está parado en cualquier otro elemento que no sea el último. Ahora, el mientras entra por el verdadero o por el falso.

Por el verdadero. Y yo quiero entrar cuando es fin de secuencia. Cuando está parado en el final. Yo tengo que negarla. Tengo que negarla.

Tengo que decir no fin de secuencia para que entre al mientras. ¿Entiende? Ahora cuando vemos un ejercicio. Ahora vamos a ver un ejercicio y ahí lo van a entender. Lo van a entender.

¿Eh? Bueno. Operadores lógicos. ¿Se acuerdan de los operadores lógicos? ¿Cuáles eran los operadores lógicos?

No, no, no, no. Bandera es un tipo de datos lógicos. Dale. Operaciones. Operaciones como que, por ejemplo.

No, no, es lógico. Porque la suma es una operación. No, no. Es lógico. La suma es una operación matemática.

Está bien, pero él pregunta, por ejemplo, si A más B es menor a 100. ¿Así? ¿Sí? ¿Se puede? No, no, no, no, no.

Ahora si yo digo. Ahora si yo digo A más B es mayor que 100 es una expresión lógica. Eso puedo negar, pero no la suma. Hay que repasar todo eso en las primeras clases. Así que repasen.

Operadores lógicos, matemáticos. ¿Sí? Bien. Continuamos. Ahora vamos a ver cómo se trata la indefinida pura.

¿Sí? Tenemos diagrama de flujo y un pseudocódico. Entonces, en acción inicializamos, arrancamos la secuencia y los contadores que vamos a utilizar. Y ahí utilizamos la estructura repetir. Se avanza el elemento, secuencia, ventana, y contamos.

Un elemento, dos elementos, hasta que lleguemos al fin de secuencia, el fin de secuencia de la secuencia. Entonces en el diagrama del flujo sería acción, inicializar, y preguntamos. ¿Sí? Finalizamos. Y por último, escribimos el valor del contador.

¿Sí? Bien. Veamos entonces el primer ejercicio. No, está grabando. Sigue, sigue.

Bueno, ejercicio. Ejercicio 2.1.1 dice. Dada una secuencia de letras del alfabeto que finaliza con una marca, asterisco. Contar cuánta letra A hay en la secuencia. ¿Sí?

Si el último carácter tiene que ser tratado como un elemento más de la secuencia o no. ¿Se entiende? ¿El asterisco es una letra? No. Entonces impura.

Entonces, comenzamos. Acción. Ejercicio 2.1.1 es. ¿Qué defino? En el ambiente lo que voy a utilizar.

S. Secuencia de carácter B, que es el tipo carácter. Y un contador que es el tipo entero. ¿Sí? Proceso.

Y acá comenzamos. Arrancar S, secuencia. Inicializo mi contador. Y avanzo el primer elemento de la secuencia. Entonces comienzo.

Y pregunto. Mientras ventana o B sea distinto de asterisco, hacer. ¿Sí? Ese sería el reemplazo a No fin de secuencia. Tiene pregunta.

Si B es igual a A. Entonces, cuento. Si B es igual a A. Entonces, cuento. Si el elemento que tengo en la ventana es igual a A, cuento.

Si no, paso de largo, sigo. Y avanzo en secuencia de ventana. Vuelvo otra vez al mientras y pregunto. Acá tengo una pequeña prueba. Prueba de escritorio.

Ponerle el asterisco en la secuencia. Para ganar el asterisco. A ver, asterisco. Bien. Entonces.

Entonces tenemos. Para. Está. Entonces. Vamos a poner que tenemos esa secuencia.

Hola. Y al final tenemos. El asterisco que es el elemento distintivo. ¿Sí? Comenzamos entonces.

Arrancamos S. Inicializamos el contador en cero. Y avanzamos. En el primer elemento. Y ahí preguntamos.

Mientras B. Mientras B es distinto de marca. B. ¿Cuánto vale? H.

Pregunto. H es igual a A. Entonces mi contador sigue en cero. ¿Sí? Avanzo al siguiente elemento.

En la secuencia. Y ahora viene a. ¿A cuál viene? A O. Pregunto.

Avanso al siguiente elemento. Después viene A. ¿Sí? Y ahí pregunta. B es igual a A.

Sí. Entonces entra y a contador le sumo 1. ¿Sí? Avanzo al siguiente elemento. Siguiente elemento es Asterisco.

Y pregunto. B es distinto de asterisco. No. Entonces sale. No.

Entonces sale. El delfín mientras y escribo. La cantidad de letras A son contador. ¿Sí? ¿Alguna duda?

No. Vamos entonces ahora con el siguiente ejercicio. Ejercicio 2. 1. 2.

Dice. Dada una secuencia de letras del alfabeto que finaliza con la letra Z. Contar cuántas consonantes hay en la secuencia. ¿Entienden? ¿Comprenden?

¿Sí? ¿No? ¿Cómo es la secuencia? ¿Pura o impura? ¿Cómo?

Pura. ¿Por qué es pura? Porque tengo que tratar el último elemento. Entonces comienzo. Acción.

Acción ejercicio 2. 1. 2. 1. 2.

S. Y defino mi ambiente. Defino S. Una secuencia de carácter. B.

El tipo carácter. Contador del tipo entero. Y defino un conjunto que llamo vocal. Y ahí defino A, E, I, O, U. ¿Sí?

Pregunto. Este igual. ¿Está bien ahí? ¿Sí? Porque estoy definiendo vocal como un conjunto de datos que contiene A, E, I, O, U.

¿Sí? Me es más fácil definir vocal y preguntar si no es vocal que definir A, A, E, B, C. Así. ¿Sí? Entonces, ahí comenzamos.

Procesos. Arranco la secuencia S. Y contador. La secuencia S. Y contador.

La secuencia S. Y comenzamos. Repetir. Avanzo el primer elemento. Y pregunto.

Si B no en vocal, entonces. Si no en vocal, si es verdadero, entro, cuento uno y salgo. Y pregunto. Y pregunto al final. Si B.

El elemento que está en esa variable B. Es igual a Z. ¿Sí? Y comienza la estructura. La estructura repetitiva.

Acá muestro. No. ¿Se acuerdan que en la primera clase dijimos que no íbamos a diferenciar mayúscula de minúscula? O sea que para nosotros la A minúscula la mayúscula lo mismo. Bien.

Acá hacemos una pequeña pruebita de escritorio y comenzamos. Bien. Comenzamos entonces. Arrancamos la secuencia. El contador en cero.

¿Sí? Y avanzamos. Avanzamos secuencia ventana. Entonces ahora ventana o B tiene la letra H. ¿Sí?

Y vengo y pregunto. Si B no en vocal. B no es vocal. ¿Sí? ¿No?

Entonces si no es vocal. ¿Tengo que contarlo? ¿Sí o no? Por eso vengo acá y al contador. ¿Sí?

Después pregunto. B es igual a Z. No. Entonces vuelvo otra vez. Subo acá.

Avanzo al siguiente elemento. Secuencia de ventana. Ahora tiene O. ¿Sí? B no en vocal.

Entonces. ¿Cuento o no? No. No, no contamos. Bien.

Venimos acá y preguntamos otra vez. B es igual a Z. No. Bien. Vuelvo a la estructura repetir.

Voy a repetir. Y avanza al siguiente elemento. Siguiente elemento es. El siguiente elemento es. L.

Y pregunto. B en. Si B no en vocal. Sumo. Sumo o no?

Sí. Ahora entonces vale. Y pregunto. B es igual a Z. Entonces.

B es igual a Z. Entonces. Avanzo. Secuencia de ventana. Y ahora tengo A.

¿Sí? Y pregunto otra vez. B no en vocal. Estoy preguntando por el contrario. Digamos la negación.

¿Sí? Entonces. No entro. B es igual a Z. No.

Avanzo. Y estoy. En el último elemento. Z. Vengo acá.

B no en vocal. Entonces. Lo sumo uno. Tres. Y pregunto.

B es igual a Z. Entonces. Salgo de repetir. Y escribo. La cantidad de letras consonantes son.

Y ahí terminó. El algoritmo. Fíjense. Fíjense que. Cuando usamos un pre-test.

Nosotros tenemos que avanzar. Antes de entrar. A la estructura. Y al final. ¿Sí?

Antes del fin mientras. Y en cambio. Cuando usamos un post-test. El avanzar está. Al principio.

Pero no está afuera. ¿Ven? ¿No está afuera. No está afuera. No.

No está afuera. No afuera. afuera. No afuera. afuera.

af. af af af
