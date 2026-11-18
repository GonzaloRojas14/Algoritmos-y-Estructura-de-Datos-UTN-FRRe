---
tipo: transcripcion
materia: Algoritmos y Estructura de Datos
clase: 3
tags:
  - AED
  - transcripcion
---

# Clase 3 — Algoritmos y Estructura de Datos

> [!info] Transcripción completa de la clase grabada
> Texto íntegro, sin resumir. Generada con Whisper desde `clase3.wav` y
> depurada con `dedup.py` (colapsa oraciones repetidas consecutivas, que son
> alucinaciones del modelo, no habla real del profesor).
> Video original: `temp_videos/clase3.mp4`

---

Ahora sí. Bien, arrancamos. Ahí puse a grabar. Bien, vamos a hacer un breve repaso. En primer lugar, ¿hicieron ejercicios?

¿Sí? Bien. ¿Les resultaron fáciles o difíciles? ¿Sí o no? Bueno, los que no, les recomiendo que se unan.

¿Sí? En el link tree está el enlace de invitación. Así que, únanse al servidor de Discord. No sé si vieron que hay un canal en el Discord. Discord del D.

Hay un canal que se llama Control de Ejercicios. ¿Vieron? Bien. En ese canal de Control de Ejercicios hay algunos compañeros que ya estuvieron compartiendo ejercicios y otros compañeros que estuvieron opinando, dándole sus observaciones. ¿Vieron eso o no?

Bien. ¿Y vieron los ejercicios que compartieron los compañeros o no? ¿No? Pues la idea es que cuando alguien manda un ejercicio, ustedes no les cuesta nada, descárguenselo, mírenlo, ¿sí? Fíjense si lo entienden.

Y bueno, si ustedes quieren pueden opinar o si no, si alguien más opina sobre el ejercicio, revisan a ver si... ¿Aprétan los ventiladores, por favor? Revisan... Ah, ok. Voy a avisar.

Dale. Entonces, eh... Les... Así también ustedes se van ayudando entre ustedes, ¿sí? Bien.

Ok. En la primera clase, habíamos visto lo que eran las variables, lo que eran las constantes, cómo era la estructura de un algoritmo, y habíamos visto acciones secuenciales, ¿se acuerdan? Que era una acción debajo de otra, donde podemos asignar, escribir, leer, hacer algunas operaciones. Y la clase pasada vimos ya algunas acciones que son complejas. No es una acción simple como un leer, sino que eran unas acciones que estaban compuestas por más de una, más de un renglón, ¿sí?

Y a esas acciones las llamamos estructuras, ¿sí? ¿Qué estructuras vimos la clase pasada? ¿Cómo se llaman? Estructuras condicionales. ¿Por qué se llaman condicionales?

Porque hay una condición, ¿sí? Y al resultado de esa condición, se hace una acción o se hace otra. ¿Está? Bien. ¿Cómo se llama?

¿Cuántos condicionales vimos? ¿Cuántos? Tres. El condicional simple, ¿el condicional simple qué característica tiene? Exacto.

Que solamente hay, en realidad, siempre va a haber una sola condición en cada condicional. Después tenemos condicionales anidados, donde podemos tener un sí adentro de otro sí. Pero en cada sí, en cada estructura condicional, siempre vamos a tener una condición. Esa condición puede ser una condición simple, como A mayor que B, o puede ser una condición compuesta, donde preguntamos si A mayor que B, B mayor que C. Pero siempre la condición es una.

El tema es que en el condicional simple solamente tenemos acciones por el verdadero. Solamente si la condición es verdadera se hacen acciones y si no, no se hace nada. Después vimos el condicional alternativo, que ¿qué agrega? ¿Qué agrega al condicional simple? Agrega acciones por el falso, que es el si no.

Tenemos si, una determinada condición. Entonces, si esa condición es verdadera, tenemos unas acciones y después tenemos si no. Y en el si no tenemos otras acciones. Tenemos acciones tanto por verdadero como por falso. Bien.

Y después tenemos el último condicional que vimos. ¿Cómo se llama? El nombre? El nombre, el según vendría a ser el apodo. Condicional múltiple.

Condicional múltiple, que por ahí lo llamamos según, familiarmente. ¿Sí? El condicional múltiple, ¿qué características tenía? ¿No evalúa una condición. O sea, sí, siempre es una condición, pero acuérdense cómo escribimos el según?

¿Qué es lo que evalúa? Varias opciones, pero de una sola variable. Acuérdense esas dos cosas que tiene que cumplir el caso para poder usar el condicional múltiple. ¿Está? ¿Se acuerdan que el condicional múltiple?

La estructura del condicional múltiple es según el condicional múltiple es según el nombre de la variable. ¿Sí? Ser? Y después acá lo lo lo ideal, digamos, sería que tengamos el valor el valor de la variable. El primer valor que puede tener la variable, y acá tenemos una acción o un conjunto de acciones.

¿Sí? Después otro valor y otras acciones. Otro valor y otras acciones. Y después teníamos el otro que es para el valor y tenemos un valor por descarte, digamos, si no es, no tiene valor 1, 2, 3, hacemos otra cosa. ¿Sí?

Y después fin, según. ¿Sí? ¿Puedo hacer una pregunta? Por ejemplo, yo sí tengo un según y tengo las diferentes opciones. Yo no puedo, por ejemplo, en evaluar A mayor que B o tiene que ser sí o sí una sola variable.

Así es. Exacto. Acá nunca pueden tener A mayor que B. No. Si ustedes van a comparar dos variables.

Si ustedes van a comparar dos variables tienen que ir por el condicional simple o alternativo. El según solamente se usa cuando queremos evaluar los distintos valores que puede tener una sola variable. Entonces dijimos, esta es la estructura del según. Si esto, si nosotros no ponemos nada acá delante, significa que es igual al valor 1, igual al valor 2, igual al valor 3. Otra cosa que podemos hacer en el según es poner, por ejemplo, acá, menor o igual a valor 1, menor o igual a valor 2, menor o igual a valor 3.

¿Sí? Siempre nos estamos refiriendo a esa variable que está allá arriba y que es la que estamos analizando. Si esta variable es menor o igual a este valor, entra acá. Si es menor o igual a este valor, va a entrar acá y es menor o igual a este valor. Ahora, supongamos que yo pongo...

Pará, pará. Yo compartí la pantalla. ¿Y qué está ahí? Pero qué barbaridad. Variable, no sé, variable, no sé, variable, no sé, variable, no sé, variable, no sé, variable, no sé, variable, no sé, variable, no sé, variable edad o cantidad de algo, que es menor o igual a 13, menor o igual a 18, y menor o igual a 45, y otro.

¿Qué pasa si yo acá arriba tengo un leer edad? ¿Sí? Yo le digo a una persona ingresa su edad, me ingresa la edad, y supongamos que la edad es 17. Y supongamos que la edad es 17. ¿A dónde va a entrar?

Acá, acá o acá o acá? En la segunda opción. ¿Sí? ¿Por qué va a entrar en esa segunda opción? Pregunto, 17 es menor a 45?

Entonces, ¿esto es verdadero? ¿O no? ¿Y por qué no entra acá? ¿Por qué entra acá? ¿Por qué no entra acá en la opción en la opción?

Solamente va a entrar acá en la opción. Sí. Un según, exacto. Un según también puede hacerse con condicionales anidados, ¿no? O sea, yo esto mismo lo podría hacer como si edad es menor o igual a 13, tal cosa.

Si no, pregunto, si edad es menor o igual a 18, acciones 2. Y si no, acciones 4. ¿Está? ¿Se entiende eso, chicos? Sí.

Entonces, si yo tengo condicionales anidados, esos son varios, y siempre evalúo una sola variable, puedo usar un condicional alternativo. ¿Está? ¿Todos de acuerdo? Bien. Dijimos hace un ratito y preguntó el compañero que está en el Zoom.

Si tengo dos variables que tengo que comparar entre ellas, ya no uso más condicional alternativo. Condicional múltiple, perdón. Condicional múltiple. Bueno. Si eso está total, pero totalmente comprendido, vamos a seguir avanzando.

Sí, puede ser. ¿Qué están preguntando aquí? Bien. Levanten la mano quienes hicieron ejercicio en la casa en la semana. Uno, dos, tres, cuatro.

Felicitaciones a todos los que hicieron ejercicios, pero son menos de la mitad. ¿Sí? Capaz, esto no debería suceder, pero hasta diciembre le vamos a volver a ser acordada de la faula de la liebre y la tortuga. Los que no hacen ejercicio se están comportando como la liebre, se están confiando porque estos temas son fáciles, pero hagan que haganse el háganse el hábito de hacer ejercicio. Ustedes dicen, bueno, el miércoles tengo clase de práctica de algoritmo, el martes a la noche me dedico una o dos horas a hacer ejercicio.

Pónganse como hábito el martes a la noche, el miércoles a la mañana, no sé, pero pónganse como hábito, digan, bueno, no sé, todos los miércoles de ocho a nueve de la noche me voy a poner a hacer ejercicio. Tómenlo como hábito porque le va a venir bien cuando los ejercicios se empiecen a complicar. ¿Sí? Es más, si pueden hacer ejercicio. Es más, si pueden hacerse un grupito de tres o cuatro y juntarse y hacer ejercicio juntos, mejor todavía.

Porque entonces no le sale a uno y el otro le ayuda y ahí va saliendo más rápido. ¿Sí? Pero les doy como consejo, pónganse un horario, decir, bueno, no sé, los martes a la noche me voy a poner una hora de hacer ejercicio de algoritmo. Hice antes de arrancar la clase, dice Valentina. Sí, a ver, mejor que nada es, pero digamos, si haces justo antes de arrancar la clase, como que está muy, ¿eh?

Sí, está con la mente fresca, pero antes de empezar la clase de la facu. Bueno, a ver, entonces, la clase pasada vimos condicional simple, condicional alternativo y condicional múltiple. Ahora, y llegamos hasta este ejercicio de las inundaciones, ¿se acuerdan? Bueno, ahora, todas estas acciones que venimos haciendo hasta ahora se ejecutan una sola vez. Entonces, para eso necesitamos otras estructuras.

Estructuras que, ¿cómo se llaman? ¿Eh? No solamente esa, más, esa es una de las que vamos a ver. Exacto, estructuras repetitivas o iterativas o cíclicas, ¿sí? Me permite tener eso, repeticiones o ciclos.

Y es la condición que se va a evaluar si el conjunto de acciones que están adentro se vuelve a ejecutar o no, ¿cierto? Y de ahí se desprende algo también fundamental. Y es que, supongamos, si yo controlo si A es mayor que B, y eso lo tengo que hacer varias veces, ¿qué tiene que suceder adentro de mi estructuras? Con A o con B o con B o con B o con B o con las dos? La comparación se da en el momento de la condición, que ahora vamos a ver que puede ser arriba o abajo, ¿sí?

Pero adentro de las acciones que se van a hacer en la estructura, las variables tienen que ser modificadas. ¿Sí? ¿Por qué? Porque si no se modifican las variables, yo no puedo salir nunca de ese ciclo. Supongamos que yo digo, ahora vamos a ver la estructura, pero supongamos que yo digo, mientras A sea menor que 100, y a A yo le asigné un valor, no sé, 95.

Pero yo adentro de las acciones, yo no modifico el valor de A. Yo no modifico el valor de A. ¿Va a salir algún día? ¿Y eso qué va a ser? Un error.

Eso se llama un bucle infinito y es un error. ¿Sí? Entonces, siempre que tengamos una estructura repetitiva, tenemos que asegurarnos que las variables que intervienen en la condición se modifiquen de alguna manera. ¿Está? Bien.

Vamos a ver tres estructuras repetitivas. Una se va a llamar ciclo pretest. Esta presentación ya está subida en el drive, así que hace falta que saquen foto. La estructura, entonces, que vamos a ver, se llama pretest. La segunda se llama posttest.

Y la última se llama manejada por contador. A ver, si ustedes escuchan la palabra pretest, ¿qué les viene a la mente? Una prueba previa. Exacto. Entonces, el pretest, como el nombre lo indica, la pregunta o la condición, se realiza antes del conjunto de acciones.

Entonces, ¿cómo es la estructura? ¿Cómo es la sintaxis de este? La sintaxis de este ciclo pretest es así. Mientras, viene una condición, ¿sí? Esa condición puede ser mientras A menor que 100, mientras A mayor que B, B mayor que C, B mayor que C.

¿Sí? Hacer, adentro vienen todas las acciones. Y esto es lo que yo les decía. Es muy importante que haya una acción que modifique esa variable. Si no, no voy a salir nunca.

Fíjense el dibujito. Fíjense el dibujito que tenemos acá a la derecha. ¿Cuándo entra a la estructura repetitiva? ¿Cuándo la condición es cómo? Cuando la condición es verdadera.

¿Y qué pasa cuando la condición es falsa? No entra a la estructura, no ejecuta las acciones. Entonces, basado en esto que dijimos recién, ¿cuál es la cantidad mínima de veces que pueden ejecutarse las acciones de ahí adentro? ¿Cuál es la cantidad mínima de veces que pueden ejecutarse las acciones de ahí adentro? ¿Sí?

A ver. ¿Por qué? Porque si la condición no se cumple, no va a ejecutar las acciones que están ahí adentro. Y eso está bien. Por ejemplo, eso se puede usar cuando yo quiero controlar el valor que ingresa de una variable.

Miren. ¿Quién está jugando? Fíjense. Perdón, toqué sin crear ese tipo. No hay problema.

Fíjense una cosa. Supongamos que yo le pido a alguien que me ingrese una edad, ¿no? Que ingrese su edad. Obviamente, la edad de una persona, ¿cómo debería ser? Entera, bien.

Y después, positiva. ¿Y qué pasa si me ingresa una edad negativa? Entonces, yo podría hacer esto. Leer edad, ¿sí? Y mientras edad menor que cero, hacer, y ahí le reto primero y después le pido que me ingrese de nuevo.

Le digo, escribir, la edad debe ser positiva. Ingrese de nuevo y no sea pago. ¿Entendés bien la edad. ¿Entendés? O sea, si algún vivo me pone menos 15, se le voy a decir, no, ponerme bien.

¿Entendés? O sea, porque se supone que si yo te estoy preguntando cuántos años tenés, bueno, me va a poner menos 15 porque no tenés menos 15 años. Esperen, esperen. Escuchen lo que dice acá, compañero. ¿Cómo es tu nombre?

Tiago. Tiago dice que este escribir es el que me hace modificar la variable. ¿Están de acuerdo? ¿Sí o no? ¿Cuál es la acción que me hace modificar la variable?

El leer es, profe. El leer. Porque acuérdate, o sea, yo la variable que estoy evaluando es edad. Y yo tengo un nuevo valor para edad cuando hago el leer. Fíjense.

Vamos a... Fíjense. Vamos a... A ver, escucha. Vos lo que me estás diciendo es si vamos a hacer validación de errores.

Depende. A veces sí, a veces no. Depende de lo que me pida el ejercicio. Nosotros, por ejemplo, nosotros podríamos haber puesto que edad sea una variable que puede tomar desde cero hasta 150 años. Si yo lo defino así en el ambiente, ya no hace falta que yo valide.

Ya no hace falta que yo valide. ¿Por qué? Porque cuando él quiera ingresar un negativo no va a poder. Pero si yo definí a la edad como entero, ahí sí tengo que contemplar porque entero puede ser positivo o negativo. ¿Se entiende?

O sea, nosotros por ahí lo que tenemos es que en el ambiente ya podemos decir los valores que puede tomar son estos y entonces ya no hacemos validación de errores. Pero todo depende del enunciado. Lo vamos a ir. Bien. Miren.

Fíjense. Yo voy acá, voy a escribir. Ingrese su edad. Ingrese de nuevo. ingrese su edad.

Ingrese su edad. ingrese su edad. Ingrese su edad. Ingrese. Ingres su edad.

Ingres. edad. nrl. n. n.n.

n. No importa lo que ingrese, acordate. El IS no puede ser ingresado. El I va a ir desde mi valor inicial hasta mi valor final. Pero si yo defino I como real, después del 1, ¿qué número viene?

1,000000 y allá un 1 al final. No, no funciona. El ciclo manejado por contador tiene que ser manejado entera. ¿Se entiende? Ahora, fíjense.

No se puede modificar el valor del contador adentro del ciclo. O sea, yo no puedo hacer esto. Ahí asignarle uno más. No. O supongamos que yo uso una condición ahí adentro y digo, si pasa tal cosa, ahí le asigno 10 para que salga directamente.

No. Eso no se puede hacer. Yo uso el para si sé cuántas veces se va a ejecutar y no, eso no va a cambiar. Ojo, esa cantidad de veces puede ser fija o puede depender de otra variable. Supongamos que yo quiero hacer una determinada acción o conjunto de acciones y le pregunto al usuario cuántas veces quiere que se haga.

Cantidad de alumnos, por ejemplo. Supongamos que él tiene que cargar una X cantidad de notas. Entonces yo lo que podría hacer es decirle, cuántas notas. Cuántas notas o cuántos estudiantes tiene. Él me ingresa en una variable un número y yo hago un para que va desde uno hasta ese número.

¿Sí? Claro. Así es. No. Ah, vos querés que vos querés, bueno, vos mostrarías solamente en el, modificarías en el escribir, pero ojo, ojo, ojo, conceptualmente, vos no estás modificando la variable.

Vos estás modificando lo que mostrás nomás, pero no modificás la variable. Exacto. Ah, porque vos no hacés una asignación de algo ahí. ¿Entendés? Fíjense.

Vamos a ver cómo sería ese ejemplo. Supongamos que yo quiero cargar ciertas notas de mis estudiantes. Entonces yo lo primero que voy a hacer es escribir ingrese cantidad de estudiantes. Y leer es esto. Y después hago un para.

Que va para ahí que va de uno hasta cantidad de estudiantes. Y ahí pongo escribir ingrese la nota del estudiante. Y acá voy a poner coma y voy a mostrar la variable y. Entonces, ¿qué va a mostrar la primera vez? El número uno.

¿Sí? Porque y arrancó en uno. Acá. Y entonces va a leer notas. ¿Sí?

Y acá hago fin para. Después tengo que hacer algo con esa nota. ¿Sí? Entonces fíjense. Tengo can.

Estud. Comentero. Y supongamos que la nota podría ser con decimales. Definir nota como real. ¿Sí?

Y tengo. Aquí no le gustó a él. Qué sábado que es. Sí, era el flechita. No me acuerdo cómo se hacía.

Ah, con el menor y el guión, sí. Menor y guión. Fíjense. Le puse ingrese la cantidad de estudiantes. Me dice cuántos estudiantes.

O sea, cuántas notas va a cargar. Y yo hago un para que va desde uno hasta esa cantidad de notas. ¿Sí? Bien. Entonces.

Fíjense. Supongamos que yo le digo. Me dice ingrese cantidad de estudiantes. Le digo, bueno, tengo cinco estudiantes. Vamos a hacerlo cortito para que si no.

Entonces, variable no definida. Ah, claro. Está bien. Fíjense. Yo les dije que y o contador o como quiera que nosotros le llamemos es una variable.

Y como es una variable la tengo que definir. Y yo que hice ahí arriba no la definí. Entonces. Tengo que definir. Y cantidad de estudiantes como entero.

Entonces. Si yo escribo y igual a uno. Tengo que hacer. Y no puedo hacer. Y sobre todo.

Si vos querés que el valor de eso vaya cambiando. Tiene que ser una variable. No puede ser una constante. ¿Está? Y si es una variable.

No le puedo asignar un valor en el ambiente. ¿Está? Cantibilidad de estudiantes 5. Dijimos. Entonces.

Ingrese la nota del estudiante 1. Bueno, se sacó un 10. Ingrese la nota del estudiante 2. Se sacó un 5. El estudiante 3.

Se sacó un 6. El estudiante 4. Se sacó un 8. Y el último estudiante se sacó un 8. Y el último estudiante se sacó un 1.

Y termina. Fíjense una cosa. Yo le dije que son 5 estudiantes. Y entonces me hizo para ahí que va de 1 hasta 5. El 5 inclusive.

¿Está? Entonces si yo hago algo para ahí que va de 1 a 10. El 10 también va a ser que entre. ¿Está? Bueno, podría haber hecho otras cosas, digamos, con esas notas, pero por ahora.

¿Se entendió? Entonces, siempre que ustedes sepan la cantidad de veces que se va a ejecutar en su ciclo, cuando no sepan la cantidad de veces que se va a ejecutar, cuando no sepan la cantidad de veces que se va a ejecutar, cuando no sepan la cantidad de veces que se va a ejecutar. Cuando no sepan, usan un mientras o un repetido. ¿Sí? El 90% de las veces vamos a usar un mientras.

¿Sí? Es como que casi siempre es más fácil controlar por ahí. Pero, bueno, también tenemos la opción de usar un repetido. No, a ver. Si vos tenés que hacer una triquiñuela para que funcione es porque no conviene.

¿Está? Vos solamente tenés que usar un repetir. Si vos estás seguro que sí o sí o sí, tenés que ejecutar por lo menos una vez las acciones. ¿Ah? Si, por ejemplo, miren.

En este ejemplo acá. En este ejemplo de acá. ¿Qué es más óptimo? ¿Usar el mientras o el repetir? ¿Cuál es más corto?

¿Seguro? Uno, dos, tres, cuatro, cinco. Acá tiene cinco líneas mi código y acá tiene cuatro. Y acá, acá yo tenía, es más, tengo un seis porque acá tengo que escribir también ahí arriba. Acá tengo un escribir y un leer afuera y acá tengo un escribir y un leer adentro.

Acá tengo que hacer dos veces y acá tengo una sola. Acá, si yo sí o sí necesito leer la edad. O sea, yo seguro que lo mínimo una vez lo voy a tener que hacer. Entonces, en este caso me conviene usar un repetir. Porque yo sí o sí una vez voy a necesitar que entre.

¿Sí? ¿Se entiende? Ahora, si yo quiero controlar otra cosa y puede ser que no entre nunca, me conviene usar un miento. ¿Ah? ¿Se entiende?

Bien. A ver, hoy le habíamos mostrado algún ejercicio a los chicos o no? El de los edificios. A ver. Fíjense, vamos a hacer el ejercicio 15.

Dice, hacer un algoritmo que calcule la altura aproximada de un edificio en pies. Ingresando como dato la cantidad de piso del mismo y la altura promedio de cada piso en metros. O sea, yo le tengo que pedir al usuario que me ingrese cuántos pisos tiene su edificio y cuánto mide cada piso en metros. Y después, ¿qué le tengo que devolver? La altura del edificio.

¿En qué unidad? Empieza. Bien. Bueno. Entonces, vamos a hacerlo por acá.

El ejercicio ese, dijimos, el 1.15. Entonces, vamos a hacer acción. Ejercicio 1.15 es ambiente. ¿Qué variables de entrada vamos a tener? Bien.

Cantidad de pisos. ¿Qué va a ser de qué tipo? Entero. Porque yo no puedo tener tres pisos y medio. ¿Está?

¿Y qué más voy a tener? Altura promedio que va a ser como? Real. Altura promedio. Que va a ser real.

¿Y qué más? A ver. Podría ponerlo como constante, pero puedo multiplicar directamente. ¿Por qué? Así como el número pi.

El número pi, por ejemplo, vale siempre los mismos. No va a cambiar. Y que un metro son 3,28 pies. Aparentemente no debería cambiar nunca. En este caso, podría poner directamente el valor.

O podría definirlo como una constante. ¿Sí? Las dos opciones. Bien. ¿Y qué otra variable necesito?

La altura en metro. La altura en metro es la altura promedio. Es la altura de cada piso. ¿Y qué más necesito? Hasta ahora todas las variables están vacías.

Una variable, dicen del zoom, una variable para guardar el resultado final, que sería altura de qué? ¿Altura aproximada en pies? Sí, o podría ponerle directamente altura del edificio. ¿Sí? Porque me van a dar la altura en metros de cada piso y yo le tengo que devolver en pies la altura de todo el edificio.

Entonces le puedo llamar altura del edificio. ¿Está bien? Bueno, creo que por ahí andamos. Vamos al proceso. ¿Qué voy a escribir?

Ingrese. Ingrese cantidad de pistos. En metros. ¿Está bien? ¿Y qué leo?

Alt. ¿Qué voy a escribir? Díganme. Dos puntos igual. Exacto.

Dos puntos igual. La acción de asignación. ¿Qué le asigno? Altura prom por cantidad de pisos. Exacto.

Y después qué hago. Mostrar. ¿Cómo muestro? Escribir. ¿Y qué escribo?

La altura del edificio en pies es los puntos coma alt edificio. Fin. Acción. ¿Está bien? Le hago la cantidad de pisos.

Le hago la altura promedio. Hago la multiplicación. Y le digo la altura del edificio es tal. Bien. ¿Todos de acuerdo?

¿Alguien tiene alguna duda? Sí. ¿Cómo? Bien. Tenemos dos opciones en ese caso.

Uno es que ya acá arriba le pongamos qué cantidad de pisos va desde uno hasta, no sé, exageremos, le ponemos 200 pisos. No sé. Ahí ya listo. Si hacemos eso, ya no tenemos que validar nada. ¿Por qué?

Porque si él quiere ingresar cero, ya no le va a dejar. Lo otro, si fuera entero, nosotros tendríamos que poner acá un repetir, ingrese cantidad de pisos y leer can P hasta que can P sea mayor que cero. Entonces, si ingresa cualquier verdura, no le va a dejar. Esas validaciones por ahora, no las vamos a hacer. No las vamos a hacer.

Vamos a asumir que el usuario es medianamente inteligente y vamos a hacer. El día de mañana cuando ustedes programen sí van a tener que controlar porque los usuarios ya lo van a ver. Pueden cometer muchísimos más errores de lo que a ustedes se les puede ocurrir. Le digo por experiencia. Pueden poner cualquier cosa.

Lo que vos le digas, no ponga esto, él va a ir a poner. Serio. Tengo que hacerlo muchas veces significa que tengo que usar alguna estructura repetitiva. ¿Sé cuántas veces tengo que ejecutar las acciones? Sí.

¿Qué voy a usar? Un para, manejado por contador. ¿Y dónde voy a meter el para? ¿En qué hasta? Sí, pero ¿dónde pongo el para?

Díganme en qué línea pongo el para. ¿Y dónde pongo el para? ¿Dónde pongo el para? ¿Dónde pongo el para. Y?

Entonces, ¿Dónde pongo el para? Y entonces, ¿Dónde pongo el para? ¿Dónde pongo el para? ¿Sí? Fíjense, yo puse la altura del edificio, abro la comilla y cierro la comilla, coma, pongo una variable, coma, abro la comilla, cierro la comilla y pongo otra variable.

¿Lo ven? La altura del edificio y en pies es acá. ¿Y qué me está faltando? Chicos, ¿Qué me está faltando acá? Exacto.

Fin para. ¿Ah? Bueno. Esto va a funcionar. Va a funcionar.

Esto va a funcionar. Ahora, vamos a hacer el punto C. Dice, modifique el algoritmo para que permita calcular la altura de una cantidad indeterminada de edificios. O sea, no sé cuántos edificios. Lo puedo hacer con un mientras o lo puedo hacer con un repetir.

Entonces. Está bien, pero a ver, suponete que la persona que está cargando no sabe cuántos edificios tiene. ¿Por qué? Ponele. Ponele que vos no sabés, pero él tiene, no sé, hoy tiene 10 carpetas, mañana tiene 12, después tiene 15 y vos le podés preguntar cuántos edificios querés cargar.

¿Está? Pero ponele que tiene una pila así y no se va a poner a contar uno por uno. Entonces lo que vos tenés que hacer en ese caso es ponerle una opción que le pregunte, si le pregunte a continuar sí o no. Entonces que le pregunte a continuar sí o no. Entonces que él te ponga sí o no.

Si te dice que sí, vuelve a entrar y si te dice que no, salga. ¿Está? Bien. A ver. Vamos a hacerlo con, a ver, ¿con cuál le parece más fácil?

¿Con el mientras o con el mientras o con el repetir? Bueno. ¿Cómo va a hacer con el mientras? Y de tarea le va a quedar con el repetir a usted. ¿Sí?

Ahí. Bueno. Entonces. Si no vamos a tener un contador como i, no hace falta que lo definamos. ¿Sí?

No vamos a tener ni para ni fin para. Y tampoco vamos a tener este i. Ni este i. Entonces. Lo que sí vamos a tener es una variable que se llame.

¿Eh? ¿No? Eso es lo que le acabo de contestar acá al compañero. El usuario no sabe cuántos edificios va. Y el usuario no sabe cuántos edificios va.

Va a ser una variable de tipo carácter. Pero, pero, ¿se acuerdan allá en la primera clase cuando hablamos de la variable de tipo carácter? Eh, ¿qué valores podía tener? No. No es booleano.

Alfanumérico, pero carácter es un alfanumérico de uno. ¿Sí? O sea que, ¿qué valores puede tener? ¿Qué valores puede tener? ¿Cómo?

No te escucho. Sí, pero muchos símbolos y muchos números. Por eso, yo defino la variable de tipo carácter. Carácter es lo mismo que alfanumérico de uno. Entonces, ¿qué valores puede tener?

Una sola letra, un solo símbolo. Yo puedo acotar más eso y puedo definirlo así. Una S o una S o una N. Y entonces, ¿está? Y entonces me evito el tema de la validación.

Entonces, lo que voy a hacer acá es escribir. Dijimos que yo voy a usar un pretest. ¿No es cierto? Entonces, ¿cuál va a ser mi condición de fin? Que la variable esa continúa sea N.

Entonces, entonces, ¿qué es lo primero que tengo que hacer? Si quiero que ingrese, si quiero que ingrese, tiene que ser sí. Pero, para no serlo tan arbitrario, vamos a preguntarle a él. Entonces vamos a poner, desea comenzar a calcular y se igual a la altura. y después, ya le pongo que ingresar.

de la estructura. Tengo que hacer que la variable. Tengo que hacer que la variable tome otro valor. Para ver si va a terminar o no. Entonces acá le pongo.

Se terminó. Desea continuar. Y le pongo sí o no. Y leo nuevamente la variable. Y esta acción de la línea 47 es la que me permite que este bucle no sea infinito.

Porque en algún momento él se va a cansar y me va a poner una N y eso va a hacer que salga. Fíjense una cosa. Si yo no hubiera definido esta variable como SN, si no la hubiera definido como carácter, ¿Qué cambia? ¿Qué cambia? Chiste.

A ver, a ver, a ver. Debatamos. ¿Tengo definido qué me hace salir o qué me hace entrar al mientras? Sí o no? ¿Qué va a ser un carácter cualquiera?

Va a hacer que salga. Dimas, acá en el Zoom dice, con cualquier carácter que no sea S se va a cortar el ciclo. Y también sirve, digamos. Si él pone una X, pone una Ñ, pone una T, una Z, va a salir. El único carácter que va a hacer que entre va a ser la S.

Claro. Exacto. Poner S si desea continuar. Y si no, poner lo que quiera. ¿Está bien?

A ver, qué otra variante podemos tener. Yo podría hacer que continúa sea un booleano. ¿Sí? Y entonces, cuando le pregunto, desea comenzar a calcular, le pongo verdadero o falso. Y él me va a tener que poner verdadero o falso.

Y entonces, ¿qué tendría yo que cambiar acá? La condición, ¿cómo la cambio? Cuando una variable es Juliana, se pregunta solamente por la variable. No tengo que preguntar si la variable es igual a verdadero. Porque la variable ya es verdadero o falso.

Entonces, cuando yo uso una variable booleana, pregunto, ¿mientras? La variable no. Mientras continúa, hacer. Y acá, desea continuar, verdadero o falso. Leo continúa.

Leo un booleano, que solamente puede valer verdadero o falso. Y viene acá arriba. Eso depende de cada lenguaje. ¿Sí? ¿Cómo?

No. Mira. Vamos a hacerlo en PC. Vamos a probar. Me quedó mi oculi.

A ver. Vamos a probar. Proceso. Vamos a probar. Mientras continuo.

Vamos a probar. Sí, la verdadero. 3,2 metros. a ver, a ver, le pongo B. .

a ver. a. a ver. a. a ver.

B. Y acá haces. A resultado. Te asignas. Resultado más A.

¿Por qué? Porque esta instrucción de contador-contador más uno la está acá. O sea, esto está bien. Funciona. Pero esto es 2P.

Siempre, cuando ustedes hagan el mientras y se dan cuenta de que el mientras está manejado por un contador, puede ser reemplazado por un parámetro. ¿El nombre lo indica? ¿Manejado por contador? ¿Está? Súper.

Buenísimo. ¿Alguien más hizo? Ocho y cuatro. Al Discord. Vamos al Discord.

Discord. Guido, vos mismo pediste que le llamemos control de ejercicio. ¿Por qué no manda el control de ejercicio? El canal se llama control de ejercicio. Mandate al general.

No, todo ejercicio son ejercicio. Bueno. Miren, ¿se alcanza a ver o no? Bueno, igual lo agrandamos ahora. Chicos, silencio, por fa.

Ahí Guido mandó el ejercicio 18. Que dice, elabora un algoritmo que calcule el cociente de dos enteros y el resto de la operación empleando solo las operaciones suma y diferencia. Entonces tenemos acción, cociente restando es ambiente A, B y Kant. Y si B igual a cero, entonces escribe, no se puede vivir por cero, no se puede vivir por cero. Ahí hace un control del divisor.

Y si B no es cero, Kant le asigna cero, inicializa Kant. Mientras A mayor o igual que B, hacer A A le asigna A menos B. Y a Kant le asigna Kant más uno. ¿Qué sería el A menos B que él hace? A ver, veamos cómo funciona una división.

Supongamos que tengo 11 dividido 4. ¿Cuánto es esto? ¿Eh? 2. ¿Y qué resto tiene?

3. ¿Cómo funciona esto? A 11 le resto 4. ¿Le resto este número? 4.

¿Cuánto me queda? 7. Entonces acá lo resté una vez. Acá le resto de nuevo. 4.

O sea que le resté 2 veces. ¿Y cuánto me queda acá? 3. ¿Le puedo volver a restar? No.

Entonces significa que este es mi resto. Y este es mi cociente. La cantidad de veces que pude restar. ¿Lo ven? Y si dice A, que a A le asigno A menos B.

Lo que va haciendo es finalmente le va a dar el resto. Y el Kant le va a dar el cociente. ¿Sí? ¿Alguien puede comentar algo ahí? La verdad porque me parece que estaría bien.

A ver. ¿Cómo? No, eso no. No. Si B es mayor a A, B es mayor a A, B es cero y resto A.

No va a entrar nunca. Si B es mayor a A, nunca va a entrar al mientras y el Kant te queda en cero y el resto te queda igual a A. No, funciona. Funciona. Porque este es un caso en el que no va a entrar acá.

El resultado es un caso en el caso en el caso en el caso en el caso en el caso. ¿Qué dice A. El cociente entre A y B. ¿Qué dice A? El cociente entre A y B.

¿Y A qué valor tiene A? No. A no tiene el cociente. ¿Qué tiene A? El resto.

Si voy a querer mostrar los valores originales de A y B, al principio tendría que descansar A. Tendría que resguardar A o asignarle el valor de A a una variable que se llame RESTO y hacer toda la operación con RESTO. ¿Se entiende? ¿No te va a complicar? ¿Por qué te complica la vida?

¿Por qué? Cuando ustedes A ver, piénsenlo. Piensen y acuérdense de esto. Cuando ustedes ven que se están complicando demasiado, es porque están errando. ¿Sí?

Siempre tienen que buscar la solución más simple. ¿Está? Entonces fíjense, ahí como decía Guido recién, para mostrar el cual era el A original, multiplico A por B y le sumo no sé qué. Más vale, en ese caso resguarden esa A del principio y recuérdense la A en una variable que estamos dividiendo. O en todo caso, en una variable que estamos dividiendo.

Ya vimos 17, ya vimos 17, ya vimos el 18, ahora nos faltan el 28. El 28. El tipo con control lograste lograste dilucidar. Lograste dilucidar. Está mejorados.

Bueno. Sí. Acá alguien mandó. No, no. Algo me mandaron, pero no sé qué.

Chicos, presten atención. No, no sé qué. No sé qué. qué. qué es lo que cambia.

y no sé qué. los dos. y varía. de los dos. no.

y no. I was. . I was. was.
