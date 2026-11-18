---
tipo: transcripcion
materia: Algoritmos y Estructura de Datos
clase: 5
tags:
  - AED
  - transcripcion
---

# Clase 5 — Algoritmos y Estructura de Datos

> [!info] Transcripción completa de la clase grabada
> Texto íntegro, sin resumir. Generada con Whisper desde `clase5.wav` y
> depurada con `dedup.py` (colapsa oraciones repetidas consecutivas, que son
> alucinaciones del modelo, no habla real del profesor).
> Video original: `temp_videos/clase5.mp4`

---

Listo, ahí estoy grabando la clase, así que después la van a poder ver si quieren. Bueno, hoy vamos a ver, la clase de hoy vamos a ver subacciones. ¿Se acuerdan que en la clase pasada hicimos algunos ejercicios de funciones, procedimientos, pero le dijimos vamos a hacerlo sin funciones y sin procedimientos? ¿Se acuerdan de eso? ¿O no?

¿Por qué hay varios que me miran como diciendo de qué estás hablando? Bueno, a ver, el concepto de subacciones, el concepto en el que se basan las subacciones es este que está acá, la modularidad. ¿Qué significa eso? Que las subacciones son pequeños trozos de código, que yo los escribo una sola vez y después los puedo llamar varias veces. Y después lo puedo llamar desde mi proceso principal.

La estrategia es divide y vencerás. Entonces, tomamos un problema grande, lo dividimos en pequeños problemas, inclusive si estuviéramos haciendo un ejercicio entre varios compañeros, y el caso del día de mañana que ustedes programen, podría darse el caso que ustedes programen con otros compañeros. Entonces podrían decir, vos encárgate de esta partecita, vos encárgate de esta parte y yo me encargo de esta otra. Y después juntamos. Y cada uno construye un módulo específico para hacer algo concreto.

Por eso dice acá que es un módulo específico que sirve para hacer algo concreto. Tareas concretas que se puede reutilizar. O sea, lo puedo llamar varias veces dentro de mi proceso principal. Y estas subacciones se definen en el ambiente. ¿Cómo vendría a ser la cosa en el momento de la ejecución?

Fíjense acá cuando dice la línea principal significa que se viene en ejecución la ejecución del algoritmo principal. Y cuando dice la línea principal, que se viene en ejecución de la línea principal. siempre le tengo que dar determinados parámetros para que esa función pueda hacer lo que yo necesito que haga. y entonces vamos a los ejemplos. Quédense con esto.

Las subacciones son funciones y procedimientos. En el 90% de los casos vamos a usar funciones. Así que concentrémonos más en funciones que en procedimientos. Y ahora vamos a ver cuál es la diferencia entre los dos. Pero piensen más en funciones.

Una función necesita un nombre. No puede ser una palabra reservada. No puede ser, por ejemplo, leer. No puede ser escribir. Porque ya existen funciones que tienen ese nombre.

No le podemos poner sí. No le podemos poner según. No le podemos poner mientras. Porque esas palabras ya se usan para otra cosa. Bien.

Y después parámetros. Y después parámetros que son variables que yo voy a necesitar que entren a la función para poder hacer lo que tenga que hacer. Las funciones normalmente van a tener uno, dos, tres, cuatro parámetros. Esos parámetros. Cuando yo defino mi función se llaman parámetros formales.

Y cuando llamo a la función adentro de mi algoritmo. Esos parámetros son reemplazados por los argumentos. ¿Sí? Ay, los estoy mareando mucho. Bueno.

Les prometo que enseguida va un ejemplo. Entonces, funciones. La función es una subacción. Es un conjunto de acciones que tienen un nombre que recibe una cierta cantidad de parámetros de entrada, los procesa y devuelve un único resultado. ¿Está?

Hay algunas funciones que ya están predefinidas. Por ejemplo, leer. Por ejemplo, escribir. Esas son funciones. ¿Sí?

Y el parámetro de esa función. Normalmente vieron que cuando nosotros hacemos leer y le ponemos el nombre de una variable. Bueno, ese sería el parámetro. Y cuando usamos un escribir y ponemos que queremos escribir un texto o el valor de una variable o lo que sea. Bueno, esos son los parámetros de esa función.

Y después vamos a tener las funciones que creamos nosotros. Que son funciones que no existen. Y que son funciones que no existen. Y que es lo que no existen. ¿Sí?

Bien. Después vienen todas las acciones que yo quiera. Que pueden ser poquitas, muchas, no importa. Y en algún momento antes de que termine mi función, a este nombre de la función yo le tengo que asignar algo. Siempre una función me va a devolver un valor.

¿De qué tipo? Del valor que yo haya definido acá. Un entero. Si mi función era de tipo lógico, ¿qué le tengo que asignar acá? Verdadero o falso.

Que son los dos únicos valores lógicos que puede haber. ¿Está? ¿Se entiende? Lo importante es que yo siempre adentro de mi función, en algún lado, tengo que tener una acción de este tipo. Al nombre de mi función, le tengo que asignar un valor.

Cuando sale un valor. Cuando sale la función tiene que salir con un valor sí o sí. Fíjense. Miren, acá hay un ejemplo. Supongamos que yo tengo una función que se llama mayor de tres.

Esta función me puede servir para lo que sea. Para comparar cualquier número. Cualquier trío de números existen y me va a devolver cuál es el más grande. Acá lo que hace esta función es estos son los parámetros formales A, B y C dos puntos enteros. Siempre a los parámetros le tengo que poner de qué tipo son.

Acá se da el caso de que A, B y C son enteros. Pero si yo tuviera dos enteros y un real, yo podría tener que poner A, B dos enteros y un real. ¿Está? Cada variable así como se define en el ambiente básicamente. Y después pongo dos puntos enteros para indicar que esta función mayor de tres me va a devolver un valor entero.

¿Ok? Sí. Suponete que A y B son enteros. Y C es real. Entonces pones A, B dos puntos enteros, coma C dos puntos reales.

¿Está? O sea, los enteros los definís por un lado, los reales por otro lado. Suponete que tenés otra variable que se llame bandera que es de tipo lógico. Pones A, B dos puntos enteros, coma C dos puntos real, coma bandera dos puntos lógicos. Cada variable con su tipo de datos.

Y después acá ponen el tipo de datos que va a devolver la función. Entonces acá dice, si A mayor que B y A mayor que C, entonces A mayor de tres, que es el mismo nombre que la función, le asigno A. Y después sigue, ¿no? Si le pongo si no, y ahí empiezo a ver si B es el mayor o si C es el mayor o que sea. ¿Ok?

Lo importante es que yo tengo que tener por lo menos una de estas acciones de asignación. Cuando sale de esta función. Cuando sale de esta función mayor de tres tiene que valer algo. ¿Ok? Ahora vamos acá a mi proceso principal.

Supongamos que yo digo, de los tres hijos que yo tengo, quiero saber cuál es el más grande. Entonces leo las tres edades, leo edad uno, edad dos, edad tres, y después a una variable mayor, le voy a asignar el más grande. Le voy a asignar el más grande. Le voy a asignar el resultado de la función mayor de tres. Y los argumentos van a ser edad uno, edad dos y edad tres.

Fíjense que acá tengo lo que se llaman parámetros reales. Acá la flechita se me chingó ahí. No es mayor de tres, sino edad uno, edad dos y edad tres son los parámetros reales o argumentos. ¿Se entiende? Porque lo importante.

Porque lo importante es que cuando yo llaman parámetros. Porque lo importante es que cuando yo llame a la función no va a ir edad uno como texto. Va a ir lo que tiene edad uno que es un número. ¿Un número de qué tipo? Entero.

¿Por qué yo sé que es entero? Porque acá está definido como entero. Si yo en mi ambiente principal hubiera definido una de estas edades como real, está malo. ¿Está? Yo no puedo definir como que las tres son enteras y después le pasa un real.

Es un error. ¿Está? Y otra cosa importante también es que el orden es fundamental. Si edad uno yo lo puse primero, cuando vaya a la función edad uno, ¿a dónde va a ir a parar? A A.

Edad dos, A B. Y edad tres, A C. El orden es muy importante también. Entonces. Importante también.

Yo no puedo llamar a una función suelta. No puedo llamar sin poner esta primera parte. No puedo decir mayor de tres edad uno, edad dos y tres. Porque es como que va, calcula eso y ¿dónde queda después? Queda en el aire.

¿Está? Hay una salvedad. A ver, ¿quién me puede decir dónde yo podría llamar a una función sin guardarlo en una variable. ¿Eh? ¿En qué acción?

¿Qué acción yo podría tener acá que como parámetro de la acción yo tenga mayor de tres edad uno, edad dos, edad tres? No. ¿Sabes? No. ¿Eh?

La función ya tiene un nombre. Se llama mayor de tres. En el único lugar donde yo podría llamar a una función así suelta es en un escribir. ¿Por qué? Porque se acuerdan que yo en el escribir puedo hacer una operación y lo que va a hacer es me resuelve la operación y me lo muestra por pantalla.

Bueno, acá sería lo mismo. Como hago con cualquier variable como hago con cualquier variable. ¿Está? ¿Se entiende? Bien.

Ahora les prometo que vamos a un ejemplo enseguida. O a ver, vamos a ver, vamos a ver, vamos a ver, vamos a ver, vamos a ver. Bueno, vamos a ver un ejemplo. Antes de ir a, antes de ir a procedimientos, que procedimientos no me gustan. Yo tenía por aquí.

Tuki. ¿No? ¿Por qué no? Qué maldad. Bueno, ahí va.

Pará. Pará, vamos a compartir. Puedo compartir y comparto de nuevo. Ahí. Entonces, para los que están en el Zoom, vamos a hacer el ejercicio del 1, 2, 1.

Realice una función que dado un número devuelva su cuadrado. Entonces, sería acción ejercicio 1.2.1 es. Está bien si yo pongo así. Exacto. Bien.

Vamos, entonces. Vamos a tener ambiente. Y le vamos a poner el cuadrado. Y le vamos a poner de tipo real. Cosa que vamos a hacer los cuadrados de...

A ver, normalmente, normalmente, que cuando hacemos funciones o procedimientos, la idea es hacer primero, o lo que yo hago y lo que yo aconsejo es hagan primero el procedimiento general. Después me ocupo de la función. ¿Por qué? Porque de eso se trata el divide y vencerás. Pienso primero en el problema general y después me encargo del chiquitito.

Yo sé que va a haber una función. Yo sé que va a haber una función que yo le voy a dar un número y me va a devolver el cuadrado. Punto. ¿Cómo lo voy a hacer? No sé.

Eso se encarga mi compañero. ¿Verdad? Entonces, vamos al proceso general. ¿Sí? Vamos a poner escribir ingrese un número.

¿Está? Y leer, ¿qué cosa? Genero. Perfecto. Y después.

Después. Puedo hacerlo de dos maneras. Como dije. A cuadrado. Le voy a asignar.

No, no pues. Y no, pues si no, no tendría mi función. Tengo que... Bueno, pero dijimos, el ejercicio me está pidiendo que yo haga una función que devuelva al cuadrado. Entonces, yo voy a tener una función acá una función acá que se va a llamar cuadrado.

Que va a tener unos parámetros y que va a tener unos parámetros y que va a ser de tipo... ¿De qué tipo va a ser? Real. ¿Por qué? Porque si el número que entró era con coma, cuando haga el cuadrado me va a quedar con coma.

¿Está? Y voy a tener un... Por acá voy a tener un fin función. Y adentro no sé. Entonces, a cuadrado, ¿qué le voy a asignar?

Le asigno cuadrado. ¿Y qué? ¿Qué va ahí? El argumento. ¿Y cuál sería mi argumento?

El número. ¿Está bien? Y después voy a poner. Escribir. El cuadrado.

NRO. Es. ¿Cuál es el cuadrado? Cuadro. ¿Ah?

Podría yo haberme ahorrado esta línea y directamente esto lo escribí acá. Es lo que dije recién. ¿Se entiende? ¿Sí? ¿Se entendió, Tay?

Habrá que hacer la función. ¿Cuántos argumentos, cuántos parámetros va a tener mi función? Uno. ¿Y cómo se tiene que llamar? ¿Se tiene que llamar NRO?

No. ¿Cómo se va a llamar? N, por ejemplo. ¿Y de qué tipo va a ser? Real.

¿Ah? ¿Por qué? Porque este número que se ingresó acá y que me pasan acá es real. ¿Y acá qué voy a hacer? ¿Ah?

¿Así nomás? ¿N por N? ¿Así le hago? ¿N por N? Ah.

A cuadrado, que es el nombre de mi función, le asigno N por N. ¿Está? Y listo. Terminó. Vamos a complicarlo un poquito.

Vamos a hacer lo siguiente. Vamos a hacer que si el número es par, haga el cuadrado y si el número es impar, haga el cubo. ¿Está bien? Vamos a poner el nombre de mi función. Le voy a poner result.

¿Está bien? Y entonces acá le voy a tener que poner result. Y acá le voy a poner el resultado nomás. Para no explicarle demasiado. ¿Está?

Y entonces ahora, ¿qué tendría que hacer? Le voy a poner... Ahora vamos a poner el res. Para. Acá le voy a poner res.

Bien. ¿Cómo sé si el número es par? ¿Sí? Ah. Si N mod 2.

No me digan si mod 2 nomás. Si N mod 2. ¿Qué pasa? Es igual a 0. Entonces, ¿Qué?

Ah, a result. Que es mi función. A result le asigno N por N. ¿Y si no? N por N.

Por N. ¿Está. Y después? Fin sí. ¿Está?

Entonces, si el número es par, le asigno el cuadrado. Y si es impar, le asigno el cubo. ¿Está bien? Perfecto. Ingreso el número, entonces a res le asigno result número.

Y digo, el resultado es tal. ¿Se entendió? ¿Sí? Bien. Siempre pensemos en lo siguiente.

Pensemos que lo que va acá dentro de la función tiene que ser más largo de lo que sería escribirnos más acá. Porque si yo acá en... No tiene ni gracia. Pero cuando la función tiene un conjunto de acciones y sobre todo si yo a esa función la voy a poder llamar más de una vez en mi algoritmo principal, ahí la defino. ¿Se entiende?

Fíjense que la función está definida en el ambiente. ¿Está? ¿Se entendió? Bien. Volvamos entonces acá.

Ahora ya no me miran con tanta cara de perdido como recién. ¿Vieron que no era tan difícil? Bien. Vamos a los procedimientos. Los procedimientos son subacciones también diseñados con un fin específico.

Que no devuelve ningún valor. El procedimiento lo que hace es escribir. Leer, escribir, qué sé yo. Dentro de un procedimiento se pueden modificar los valores de variables globales. Variables que estén definidas en mi algoritmo principal.

¿Está? Pero no devuelve ningún valor. ¿Está? Puede un procedimiento puede recibir parámetros o puede no recibir parámetros también. El procedimiento en eso es como más flexible.

Puede recibir o no. Y no retorna un valor. ¿Está? ¿Se entiende? ¿Cómo se hace?

¿Cómo es un ejemplo de un procedimiento? Así, miren. Supongamos que hay un procedimiento que yo llamo login. Que lo que va a hacer es validar si el password que ingresó una persona es válido o no. Entonces el procedimiento se llama login y los parámetros que va a recibir son usu, pass y valid, que son alfanuméricos.

En realidad, en realidad, en realidad, en realidad, en realidad, en realidad, en realidad, en realidad, en realidad, en realidad, para que esto esté bien, debería ser alfanumérico y en realidad, en realidad, en realidad, para que esto esté bien, debería ser alfanumérico y entre paréntesis la longitud del alfanumérico. ¿Sí? Acuérdense siempre que cuando definimos una variable de tipo alfanumérico es alfanumérico y de 10, de 20, de 30, de 50, pero tengo que definirle la longitud. Entonces, dentro del procedimiento pregunto si pass es igual a valid, que son dos parámetros que yo tengo acá. Si pass es igual a valid, que son dos parámetros que yo tengo acá.

Si pass es igual a valid, entonces escribo acceso autorizado a usu, que es otro parámetro. Y si no son iguales, escribo login inválido para usu. Y los procedimientos sí pueden ser llamados como una única acción en una línea de mi algoritmo principal. No tengo que asignarlo a nada. ¿Sí?

Fíjense, si yo tengo acá, si yo llamo dentro de mi algoritmo principal a este procedimiento login y los argumentos que le doy son Tom, Goku y Vegeta. ¿Qué me va a escribir? Tom, Goku y Vegeta. ¿Qué escribe por pantalla? Login inválido porque Goku y Vegeta no coinciden.

¿Sí? Ahora, si yo llamo y los argumentos son Tom, Goku y Goku. ¿Qué me va a escribir? Acceso autorizado. ¿Está?

Fíjense, fíjense que cuando defino el procedimiento no le pongo acá dos puntos y un tipo de datos porque el procedimiento no me devuelve un valor. ¿Se dan cuenta de eso? Y fíjense, por la misma razón, acá adentro de las acciones del procedimiento, al procedimiento no se le asigna nada. ¿Se entiende? ¿Sí o no?

Bien. Veamos entonces las diferencias que tienen los dos tipos de subacciones. Las funciones tienen como objetivo calcular y devolver un dato. ¿Sí? Ese cálculo puede ser un cálculo matemático o puede ser un condicional.

¿Está? Pero el tema es que siempre la función tiene que devolver un dato. Y el procedimiento tiene como objetivo ejecutar determinadas acciones. Nada más. La función devolver un resultado.

Un único resultado que va a ser del tipo de dato que usé en la definición de la función. Y el procedimiento no va a devolver ningún valor. Aunque, como dije recién, el procedimiento puede modificar variables globales. Eso sí. Especifica el tipo de datos que devolver.

Y en el procedimiento no. Y en la invocación, en la invocación, en la llamada a la función. En la llamada a la función, yo no puedo llamar a la función suelta. Tengo que llamarla o dentro de un escribir o asignándose, asignándole la función a otra variable. En cambio, el procedimiento sí se puede llamar como una acción independiente.

Acá está el tema del ámbito de las variables. Hay variables locales y que solamente pueden ser usadas adentro de una función o de un procedimiento. Y hay otras variables que son globales y pueden ser usadas en todo el... Fíjense, esta variable número es una variable local para esta función. Yo no puedo usar en mi algoritmo principal número.

Fíjense. Entonces, lo que sí se puede hacer es esto. Yo tengo acá mi variable local y tengo una variable global y tengo una variable global. Y la variable global puede ser usada dentro de mi función. ¿Lo ven?

Este es dibujito. ¿Está? Vamos a ver un ejemplo de para qué se usaría un procedimiento. Acá el ejercicio 1, 2, 11 dice, diseñe un algoritmo que muestre un menú con las opciones sumar, restar, multiplicar y dividir. El algoritmo solicitará una opción y realizará la tarea elegida.

Se debe usar un procedimiento para mostrar el menú, pedir los datos en el algoritmo principal y después usar funciones para realizar los cálculos. ¿Se entiende más o menos? ¿Sí? Tengo que usar un procedimiento para mostrar el menú. Después tengo que leer la opción que elige el...

Usuario. Y después las operaciones suma, suma, resta, amplificación y división. Las tengo que hacer en diferentes funciones. Bien. Vamos a hacerlo juntos.

Acción. Ejercicio. Uno. Dos, once. Ambiente.

¿Qué voy a tener? Exacto. ¿Un número? ¿Cuántos números tengo que ingresar? Dos.

Número uno. Número dos. ¿De qué tipo van a ser esos números? Podría ser entero. Podría ser real.

Vamos a suponer que voy a hacer operaciones con entero en principio. ¿Está? ¿Y después? Variables suma, resta. Puedo tener esas variables o puedo no tenerlas.

Ahora... ¿Y ese resultado cómo va a ser? Bueno, vamos a tener un resultado que va a ser real. Dice acá el compañero. ¿Por qué?

Ajá. Si yo sumo dos enteros, ¿qué tengo? Si yo resto dos enteros. Si multiplico dos enteros. ¿Y si divido?

No. Dividí cinco, no. Divido dos. No entero. Entonces, si yo, si yo, si yo, si la, si el usuario, si la, si el usuario elige división, puede ser que no sea entero.

Entonces, el resultado tiene que ser real. ¿Se entiende? Bueno. ¿Y después? ¿Algo más o no?

¿Eh? Exacto. ¿Y esa opción cómo tiene que ser? ¿Cómo? Podría ser numérica de 1 a 4.

Podría ser numérica de 1 a 4 porque tengo suma, resta, multiplicación, división. O podría ser de tipo carácter. ¿Sí? Opción de tipo carácter. Podría ser o no.

Y que ese carácter sea el más, el menos, el asterisco o la barrita de división. O alguna otra cosa. También. Ahora vamos a ver. Bueno.

Lo primero que vamos a tener acá es el procedimiento menú. Dijimos. ¿Debe crear una línea entre mis variables y cuando un procedimiento una función? No. No necesariamente para mayor claridad.

Si podés dejar el renglón, la línea, mejor. Más claro. Pero no es obligatorio. Voy a tener mi procedimiento que ahora lo vamos a explicar. Sin procedimiento.

Y después voy a tener mis funciones. Y después voy a tener mis funciones para la suma, para la resta, la multiplicación y la división. ¿Sí? Suma. Y después vamos a hacer el...

Proceso. Entonces. ¿Qué es lo primero que voy a hacer en mi algoritmo? ¿Qué voy a escribir? Bueno.

Dale. Escribir. Comilla. Ingresa. Los dos.

Dos. O.P.T.A. Do. T.S. Y leer.

Bien. Número uno. Número dos. Y después. ¿Cómo se llama mi procedimiento?

Menú. Y el procedimiento. Dijimos. Puede ser invocado así. Como una acción sola.

Menú. Esa acción. Lo que va a hacer. Es mostrar un menú por pantalla. Y después.

¿Qué tengo que hacer? Yo les muestro. Vamos a escribir el procedimiento. Porque si no nos vamos a perder. Este procedimiento lo que va a hacer es escribir.

Ingresa la operación a realizar. Y acá le vamos a poner más. Y acá le vamos a poner más para suma. Y así todo. Después.

Menos para resta. Asterisco para muro. Multiplicación. Después. Y eso es todo.

El procedimiento lo único que va a hacer es mostrar esto por pantalla. Listo. Y después de haber llamado al menú. ¿Qué tengo que hacer? Leer.

¿Qué le habíamos puesto? Opción. Leer. Opción. ¿Sí?

¿Por qué escribo este menú? Acá arriba como un procedimiento. Por un lado. Para tener un algoritmo modular. El módulo del menú.

El módulo del menú lo tengo separado. Y por otro lado. ¿Qué sería lo ideal? Que yo a este menú lo pueda llamar varias veces adentro de mi algoritmo. Entonces para no escribir todas las veces todos estos renglones de código de algoritmo.

Lo pongo una sola vez allá. ¿Se entiende? Eso sería lo ideal. Leer opción. Y ahora.

¿Qué tengo que hacer? Definir la función. Sí, pero fíjate. Mirá. Vamos a la función.

Supongamos que tenemos la suma que es... ¿Está bien si yo le pongo número uno y número dos ahí? Sí o no. ¿Está bien? No.

Cuando yo defino una función. Yo, acordate, las variables globales las puedo usar dentro de la función. Pero no las puedo definir como parámetros. No, no puedo tener una variable global que se llame igual que un parámetro. ¿Está bien?

Entonces, n1, n2, que son los parámetros que va a recibir. Y después, ¿qué me está faltando acá? El tipo de dato que va a devolver. ¿Sí? Y suma, si yo sumo dos enteros, ¿de qué tipo va a ser?

Entero. ¿Y qué hago acá adentro? Asuma, le asigno N1 más N1. Perfecto. ¿Está?

Sí, exacto. Está. Muy bien. Yo pongo el tipo de dato de los parámetros y el tipo de dato que va a devolver la función. La resta va a ser igual.

La multiplicación va a ser igual. ¿Y la división? ¿Va a ser igual o no? ¿Cómo? No se llama...

Sí. Esa va a ser una diferencia. Esa va a ser igual. Esa va a ser una diferencia. ¿Cuánto.

¿Cuánto son? Tres. Tengo tres tipos de condicionales. Simple, alternativo y múltiple. ¿Ah?

¿Cuándo uso el simple? Siempre en un... Voy a tener una sola condición en un condicional. Una condición simple, una condición compuesta, pero siempre hace una sola condición. ¿Cómo?

No. En el condicional simple solamente, o sea, uso condicional simple cuando solamente me importa el valor verdadero. Cuando voy a tener un solo camino. O ninguno, digamos. Porque cuando por el sino no hago nada.

¿Está? Cuando tengo un condicional simple. Cuando me importa el verdadero y cuando me importa el falso, voy a tener un alternativo. Y cuando tengo una sola variable a evaluar y tengo tres valores o más, ¿cuál uso? ¿Cuál tengo que usar acá?

¿Cuál es la variable que yo tengo que evaluar? Opción. ¿La tengo que comparar con otra variable? No. Listo.

La primera condición se cumple. ¿Cuántos valores puede tener opción? Cinco. Porque dije que está definida como carácter. Entonces podría ser más, menos, asterisco, la barra, o cualquier otra cosa.

Son cinco valores. Entonces, el ejemplo justo para usar un condicional múltiples en el condicional múltiples en el condicional múltiples en el condicional múltiples en el condicional múltiples en el condicional múltiple. Entonces, ¿cómo se escribe el condicional múltiple? Segundo. Opción.

Bien. ¿Y acá qué pongo? Yo sabía que alguien iba a caer. No se pone el igual en el condicional múltiple. Nunca se pone el igual.

Se puede poner menor, se puede poner mayor, pero no se puede poner igual. Ahí, sí, caíste. No se puede poner el condicional múltiples en el condicional múltiples en el condicional múltiple. Y ahí estoy llamando la función, mira. Ah, yo no puedo llamar a una función así suelta.

O sea, la llamada a la función sería suma número 1, número 2. Cuando yo, cuando va adentro de la función, este número 1 pasa a ser tomar el lugar de n1 y este número 2 pasa a tomar el lugar de n2. ¿Está bien? No, no, no, no, no, no, no, no, no, no, no, no. Claro, si pongo escribir no usaría la variable result.

Directamente le pondría la suma de los dos números es y llamo a la función. Bueno, ¿qué pasa si eligió el menos? A Resul le asigno resta. Espera. No, no, no.

A ver, acá a Resul le asigno. Multiplicación. Sí. Y acá. ¿Qué hago?

Le asigno de la división? Resul, ¿cómo está definido Resul? ¿Qué pasa si el número 2 es 0? Entonces, ¿qué tengo que hacer? A ver, ¿qué pasa si el número 2 es 0?

Nadie dijo. Pusieron cara, pero da error. Me va a dar un error si yo le pongo la división así. Entonces, ¿qué hago? Sí, ¿qué?

Ah, si el número 2 es distinto de 0. Ah, si el número 2 es distinto de 0, entonces, ¿qué? Entonces, ¿qué? A Resul le asigno división. Número 1, número 2.

Fincínoma. Si no, ¿qué hago si no? ¿Escribo algo? No, no. Porque si no, no.

Si yo no hago nada, si yo no hago nada, si yo no hago nada, el algoritmo termina y el usuario dice, ¿y qué pasó? No hizo nada. ¿Entendés? Entonces, si el número 2 era igual a 0, escribo, no se puede dividir y le escribir. ¿Entendés?

Y acá recién va el fincínoma. ¿Está? Lo hicimos porque es lo que nos pedía el ejercicio. En realidad, el ejercicio no me pedía que yo lo haga varias veces. Después de poner el menú, cada vez que nos pongo un menú en el presento, ¿no?

¿Cómo se puede hacer eso? Espera. Sí, pero fíjate que lean bien la consigna. El algoritmo solicitará una opción y realizará la tarea elegida, te dice. Entonces, ya te está diciendo que vos no tenés que hacer adentro del procedimiento adentro del procedimiento la suma, la suma, la resta, la multiplicación, la división.

¿Entendés? Y aparte, en ningún lado te dice que lo tenés que hacer varias veces. Te dice un algoritmo que muestre un menú que solicite la opción, que solicite los números y que haga las funciones y que devuelva el resultado. Una sola vez. Ajá.

Elegir la opción. Elegir la opción, no el procedimiento. Según la opción, vos elegís la función. Podría estar adentro del procedimiento, sí. ¿Está?

¿Se entiende, chicos, lo que preguntó el compañero? Bueno. Y haga, ¿Qué? ¿Termina? ¿Qué?

¿Termina? ¿Fin según? Nos va entre comillas. El otro no va entre comillas. Otro es cualquier otro valor.

¿Qué pasa si escribió otro valor? Podríamos hacer que retorne al menú, pero como no usamos ninguna estructura repetitiva, le va a volver a mostrar el menú, pero no va a poder volver. ¿Entendés? Ahora, así como está planteado, simplemente lo que tendríamos que hacer acá es escribir, no sea pavo, no sea pavo, no sea pavo, no sea pavo, no sea pavo. El resultado de la operación deseada es coma resulta.

Va a dar un error esto. A ver quién se da cuenta. O sea, hay un caso en el que va a dar error. ¿Qué pasa? Fíjense.

¿Qué pasa si vino? Esto tiene que ver con prueba de escritorio. ¿Qué pasa si la persona me ingresó un 5 acá y un 0 acá? 5 y 0. Y la opción es división.

¿Qué pasa? Me va a escribir, no se puede vivir por cero. ¿Y qué le asigna a Resul? Ah, y qué va a pasar cuando llegue acá. Va a dar un error porque Resul no tiene valor.

¿Está? Entonces, yo lo que podría hacer acá es, no sé, ponerle a Resul ponerle algo. Sí, o podría escribir. Podría escribir directamente acá y ya me evito esto, escribir acá. ¿Se entiende?

¿Y qué va a hacer? ¿Va a poner acá procedimiento tanto y para eso puede usar no escribir? Es lo mismo, ¿entendés? Usted, dense cuenta de esto. Si usted escribe en un procedimiento acá que solamente tiene un escribir, no lo hagan.

Pongan el escribir en el algoritmo principal porque es lo mismo. No es la idea. La idea. La idea es que la función te calcule algo y te devuelva un valor. Si no sería procedimiento.

¿Te entiende? Se puede poner dentro del procedimiento, pero no es lo que te pide la consigna. La consigna específicamente te dice que el algoritmo. El algoritmo principal. El algoritmo principal te va a pedir la opción.

Entonces, ya te está diciendo no pidas la opción adentro del procedimiento. ¿Está? Sean siempre muy cuidadosos con lo que le dice la consigna. La consigna te va a decir si la consigna no te dice vos podés elegir la pido adentro del procedimiento, pido adentro del procedimiento, pido adentro del procedimiento. ¿Está?

Cuando tengan dudas sobre todo en el parcial, pregunten. No se queden con la duda y no supongan nada. Porque por ahí lo que ustedes suponen está bien, perfecto, pero por ahí lo que suponen está recontra mal y van a hacer todo un ejercicio y van a gastar 45 minutos el parcial haciendo algo que está mal. Entonces, no se queden con la duda. Si ustedes tienen una duda como esa, si ustedes tengo que hacer adentro o afuera, pregunten.

Si ustedes tienen una duda como esa tengo que hacer adentro o afuera, pregunten. Bueno, tenemos una hora. Bueno, ahora que vimos procedimientos y funciones, vamos a hacer ejercicios. Bueno, vamos a hacer ejercicios. Dos de funciones y dos de procedimientos.

Atacadas hasta la mitad, hagan el 1, 2, 3. ¿Sí? Diseñen una función que permite ingresar tres números y devuelva el mínimo valor. El programa principal debe permitir que este proceso se repita todas las cantidades de veces que el usuario desee. Y de acá para allá hagan el 1, 2, 5.

Escribe una función que verifique su carácter inclusivo. Y también háganlo repetitivo, hagan lo que pueda hacer varias veces hasta que el usuario diga, no quiero seguir jugando. Sí. La función te tiene que volver el más chico. Así es.

Y los que están en la casa hagan. Los dos ejercicios. Bueno, acá una compañera está haciendo el 1, 2, 3. Porrado. ¿Alguien puede sacar una foto y mandar al Discord eso, por favor?

Para los chicos que están en Zoom. No sé, no se desesperen. A ver. Si alguien podría sacar una foto a eso y mandar al Discord para los chicos que están en el Zoom. Y después vemos.

en la función que se desesperen. en el nombre de la función. N2. Y si no, N3. N3.

O sea, no hace falta preguntar por otro número. ¿Se entiende? ¿Sí? ¿Qué pasaría si algunos son iguales? ¿Qué pasa si N1, por ejemplo, N1 y N3 son iguales?

N3. N2 vale 2. N1. N2. N3.

N2. No importa ya. Con uno que sea falso ya sale. ¿N2 es menor que N3? Sí.

¿Entonces cuál es menor? N2. ¿Está bien? Anda. ¿N1 es menor que N2?

Sí. ¿N1 es menor que N3? Sí. ¿Cuál es menor? N1.

Anda. Sí, anda. Sí, prójalo. Yo lo probé muchas veces. Bueno.

Ah, y ahora dice, me están preguntando en el chat cuál sería el proceso. Entonces tenemos, fíjense, lo que me pide el enunciado, lo que pide el enunciado es que podamos hacer esto varias veces hasta que el usuario diga que nos quiere seguir. Si yo, chicos, chicos, presten atención. Si yo sé que por lo menos una vez lo tengo que hacer, ¿qué estructura uso? ¿Mientras o repetir?

Repetir. Porque dijimos que el mientras, ¿lo puedo hacer con un mientras? Sí, lo puedo hacer con un mientras, pero voy a tener que forzar que entre al mientras. ¿Sí? Yo a esta opción, supongamos que yo digo mientras, opción sea igual a S, que haga esta opción sea igual a S que haga esta cosa.

¿Qué le voy a tener que asignar antes para que entre sí o sí? Una S. Eso se llama forzar una estructura repetitiva. Y eso no es óptimo. Lo óptimo es que si vos querés que sí o sí entre una B, use un repetitivo.

¿Se entiende? Bien. Salvo que yo le pusiera desea comenzar sí o no. Si él me dice no. Digo, ¿para qué ejecutaste mi programa?

Entonces yo digo, ¿entendés? Entonces digo, desea comenzar sí o no. Bueno, leo y ahí hago un mientras. Pero si yo sí o sí la primera vez quiero que entre, hago un repetitivo. Ingrese tres valores.

Leer número uno, número dos, número tres y escribir. El menor es y ahí sin necesidad de usar otra variable, llamo a la función menor de tres y le doy los argumentos. Num uno, num dos y num tres que leí recién. Esos argumentos cuando viene acá, num uno pasa a ocupar el lugar de n uno, num dos pasa a ocupar el lugar de n dos y num tres pasa a ocupar el lugar de n tres. Entra acá, hace su magia y sale con el más chiquito.

Y entonces está. Desea continuar S o N. Y ahí leo opción. Opción está definido como S o N. Entonces los únicos valores que va a poder ingresar el usuario es S o N.

Entonces, y le digo hasta qué opción sea igual a N. ¿Se entiende? ¿Sí? ¿Está bien? ¿Le gustó o no le gustó?

Bueno. A ver. A ver, Guido. ¿Qué mandó Guido. El otro ejercicio.

El uno, dos, cinco. Dice, escribir una función que verifique si un carácter introducido es un dígito o no. ¿Por qué hiciste? ¿Por qué tan así? ¿Por qué?

¿Con qué necesidad? Definía un conjunto y si estaba en el conjunto es más fácil. Pero ¿Cómo? Bueno. A ver.

Acción. Verificar caracteres. Ambiente. Carácter. Un alfanumérico de uno.

Alfanumérico de uno. O sea, acá. Acá hay algo que está mal. Carácter no se puede llamar a variable porque es una palabra reservada porque es un tipo de dato. De última ponele carac o per.

Pero no le pongas carácter. Y alfanumérico de uno. Y alfanumérico de uno no se pone carácter. Continuar lógico. Función control.

Car. Alfanumérico de uno. Lógico. Según carácter. 0.1.

A control le pone verdadero. Repetir. Ingresa un carácter para evaluarse un dígito. Leer carácter. Si control.

Fíjense que ahí él está preguntando. Control es una función que es de tipo lógico. ¿Está bien? Entonces, está bien que pregunte si control no más porque control es verdadero o falso. Entonces, el carácter es un dígito y si no, el carácter no es un dígito.

Escribir. Desea terminar verdadero o falso. Leer continuar hasta que continuar. ¿Está bien? Él le dice si desea terminar.

Entonces, la persona le va a poner verdadero cuando quiera terminar. ¿Se entiende? Entonces, es raro, es raro el nombre de tu variable porque para terminar le pusiste continuar. Es que originalmente le pregunté si desea continuar y después iba a tener que poner hasta que no continuar. Claro.

Y sí. Exacto. Pero ¿se entiende la idea? ¿Sí? Funcionar funciona.

¿Es óptimo? No tanto. A ver. ¿Qué decía? Acá está lo que yo les decía.

Y lo ponemos por ahí. Copiar. Y lo pegamos en un blog de notas. Por aquí. ¿Cómo?

No entiendo. ¿Cómo? No entiendo. Sí. Y él le pone en 10.

Sí, por eso no es óptimo. Pero funciona. Vamos a ver este. Dice. Ejercicio 5.

Ac lo define como carácter y después define una variable que se llama dígitos. Esto es un conjunto. Está bien, ¿no? Entre llaves. Y no es igual.

Ah, bien. Esto es un conjunto de datos. Se pone con igual. ¿Está bien? Y lo ponemos entre paréntesis.

Entre. Ahí. Fíjense, chicos. Esto es algo. Esto creo que no dimos hasta ahora.

Esto no lo dimos. Así que esto es una primicia. Presten atención. Acá, a dígitos, el compañero lo definió como un conjunto de datos. ¿Sí?

¿Para qué me sirve definir un conjunto de datos? Porque yo puedo preguntar si una variable como esta, D, está dentro de ese conjunto. Si tiene un valor que está dentro de ese conjunto. Pero para poder hacerlo así. Pero para poder hacerlo así le tengo que poner igual.

No dos puntos. ¿No está? ¿Se entiende? Claro, dos puntos. ¿Se dan cuenta la diferencia.

¿Se dan cuenta la diferencia? El concepto. ¿Está? la funciones dígito. ¿Se dan cuenta?

Puedo preguntar esto. Bueno. ¿Se animan a hacer el 1-2-7 y el 1-2-8? Sí, rápidamente, en 5 minutos. Por eso, por eso, por eso, fíjate una cosa.

Fíjate que acá le dice ingrese un carácter. Y lee C. Que C está definido de tipo carácter. Podría ser una letra, podría ser un más, podría ser un punto, podría ser un arroba, lo que sea. Y acá dice, si D en dígitos, lo que está preguntando es si ese carácter que vino está dentro de estos valores.

Y no, no, no, no, no, no, no. Puedes funcionar. si puede funcionar. No, no, no, no. se entiende.

porque en todo. no, no, no, no. No, no. No, no, no, no. no, no, no, no, no.

no, no, no. No, no, no, no. no. No, no, no, no, no. , no, no, no, no, no.

no, no, no, no, no, no, no, no. , no, no, no, no, no, no, no, no. no, no, no. , no, no, no, no, no, no, no, no, no, no, no, no. no, no, no, no.

no, no, no, no, no, no, no, no, no, no, no.
