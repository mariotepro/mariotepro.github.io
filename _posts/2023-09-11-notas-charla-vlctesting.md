---
layout: post
title:  "Notas Charla VLC testing"
date:   2023-09-11
hide: true
---

# Charla VLC testing

Fontanería de software: Cómo usar cañerías para parar la fuga.

# Ideas generales
* Shift left testing
* Clean as you code:
  * Cómo utilizar la estrategia
  * Cómo mejora poco a poco nuestro código antiguo, dado que si vamos a tocar, hay que arreglarlo
* Sistemas de CI/CD, cómo parar al desarrollador los pies
  * Resistencia que tienen algunas compañías y algunos desarrolladores a que se les pare un deploy

# Guión o puntos
* Lo primero, presentación 
  * Personal
  * Excentia (qué hacemos)
* Cuando nosotros vamos a crear una nueva pieza de software, se nos plantea la idea de hacerlo de la mayor calidad y con la mayor seguridad posible
* Esto, para un proyecto nuevo, es relativamente sencillo. Nos vamos responsabilizando de no introducir defectos, y todo es maravilloso, fácil y vivimos en el mundo de la piruleta
* Pero pasan dos cosas, normalmente:
  * 1.- No hay tiempo, se introduce un defecto sin querer y ya se arreglará
  * 2.- En un mundo ideal, con vaquillas esféricas, todos los sw que toquemos son nuestros, los hemos iniciado nosotros y controlamos cada mínimo detalle. Pero en el mundo en el que vivimos no es así. Recibimos código que ya está escrito por otros y que está como esté.
    * Aquí tenemos varias opciones:
      * Podemos parar, no desarrollar nada hasta no arreglar lo existente
        * Dedicamos tiempo y recursos a dejarlo todo "como dios manda"
      * Desarrollamos otra vez toda la aplicación desde 0 y lo hacemos "como dios manda"
      * Método Ronaldinho, miramos a la grada: Lo dejamos todo como está, no tomamos ninguna acción y seguimos para adelante mirando a otro lado.
      * O tenemos una opción mejor que es:
        * Seguimos desarrollando y en lo que introduzcamos no metemos absolutamente ninguna incidencia nueva.
        * Dejamos que poco a poco el código antiguo se vaya beneficiando de todos esos cambios nuevos.
          * Si tenemos que arreglar o corregir algo, lo hacemos. Pero no nos centramos en ello.
    * Estrategia Clean as you code:
      * Presentar CAYC propuesto por SonarSource
      * Para los que estamos familiarizados con SonarQube, es fácil conocer estos términos, pero son bastante descriptivos para que no nos perdamos nadie
        * No metemos ningún tipo de bug
        * No metemos vulnerabilidades nuevas.
        * Si hay dudas de seguridad, las chequiamos
        * Todo lo que hagamos nuevo va testiado hasta las muelas.
        * Revisamos que lo que estemos haciendo no esté ya hecho (duplicatis con tomati)
    * Shift left testing:
      * Primero, la responsabilidad de lo que se hace está en el programador. 
        * Un programador no es responsable de lo que han hecho otros en el pasado.
          * Ni sabe cómo lo han hecho. Ni sabe por qué. Y tiene que dedicar mucho esfuerzo a entenderlo y arreglarlo. Incluso lo que ha hecho él mismo hace unos meses supone un esfuerzo porque ya ni se acuerda
          * Pero sí que es responsable de lo que él hace. Y máxime cuando lo está haciendo ahora mismo y es consciente de qué está haciendo y de lo que está metiendo. Si aún así decide hacerlo es cosa suya.
          * Para eso está la estrategia Shift left testing -> Sonarlint. Antes de repositar y mientras nosotros estamos programando, que haya algo que nos diga... eh, jambo, aquí estás metiendo cositas que no deberías. Corregirlo antes de subir.
    * Pero una vez que lo subamos, nos vamos a valer de herramientas como SonarQube para que nos diga lo que estamos introduciendo.
      * Quality gates: Presentar Quality Gates y cómo decidir qué es lo que queremos permitir o no en nuestra aplicación
      * Ese Quality Gate es un pasa/no pasa
      * Si no pasa, sería mejor no mergearlo, sería mejor no dejarlo pasar a nuestras ramas principales de desarrollo.
    * Cómo utilizar en sistemas de CI/CD esos pasa o no pasa para prevenir mergeos. Para impedirlos.
      * Jenkins.
      * Escoger una plataforma sólo (Github, por ejemplo o Gitlab y valernos del caso de Edicom)


"El software no es poner ladrillos"

## Ideas que se pueden hacer:
    * Presentar el gráfico de clean as you code para que vean cómo va a ir mejorando lo anterior


En la ponencia veremos en el mundo real en el que trabajamos, tenemos varios problemas a la hora de codificar en un proyecto como, por ejemplo, trabajar sobre el código de otras personas o código nuestro de hace meses y del que no nos acordamos. Proyectos heredados y antiguos. Eso puede dar lugar a que descuidemos la calidad y la seguridad de nuestro código. 
Siguiendo las estrategias shift left testing y clean as you code, el programador podrá tener la responsabilidad del código que él está haciendo y no del código heredado o antiguo.
Pero siempre se nos puede escapar algo que nosotros mismos no hayamos visto. Para eso existe SonarQube. Para ayudarnos a analizar nuestro código. Y si además, utilizamos nuestro sistema de CI/CD, podemos evitar introducir errores dentro de nuestras ramas de desarrollo valiendonos de los Umbrales de Calidad.



## Guión:
### Presentación:
Buenas tardes a todos, primero dar las gracias al ITI por la oportunidad de exponer en el VLCTesting, a los patrocinadores por hacerlo posible y a vosotros, asistentes, por hacer que sirva para algo. 
Y gracias si no os vais a mitad de charla.

Me presento, soy Mario Bastardo, aunque todo el mundo me conoce como Mariote. Soy Sonar Bug Hunter en excentia.

Empecé mi andadura en el mundo profesional en Renault España. Fabricando coches, literalmente. Allí aprendí mecánica, electrónica, electricidad, automatización y sistemas de mejora contínua como Lean Manufacturing o Kaizen.

Mejora contínua que es el ADN de mi empresa, excentia, donde trabajamos para hacer que nuestros clientes se aseguren de la mejor calidad posible tanto en sus procesos como en su software. Y sean capaces de mejorar en ámbos ámbitos.

Somos partners de Atlassian y de SonarSource, para la parte de procesos y para la parte de software respectivamente.

Como decía, empecé mi andadura profesional en el mundo industrial, posteriormente me pasé al mundo del desarrollo y por deformación profesional he intentado trasladar ese mundo industrial (en el que todo está sistemizado, automatizado, todo está medido, centrado, estudiado al detalle) a mi actividad profesional posterior. 

Para resumir la charla, de automatización del código. De cómo utilizar a nuestro favor los sistemas que pone SonarQube y los diferentes sistemas de CI/CD no sólo para evitar que pueda empeorar la calidad y la seguridad de nuestro código, si no que además, se vaya beneficiando por el simple hecho de no introducir más defectos.

Por poneros también en contexto, mi padre es fontanero y profesor de fontanería, de ahí que quiera utilizar dicho símil, que viene al pelo. Lo que vamos a hacer es dirigir nuestro software por donde nosotros queremos, exactamente igual que hace la fontanería, utilizando pipelines (cañerías en castellano). Además utilizaremos llaves o grifos para evitar que el agua vaya por donde no queremos que vaya. Así evitaremos la fuga de errores introducidos en nuestro código que no deseamos, de lo que no nos damos cuenta.

### Enjundia:
Cuándo nosotros comenzamos una pieza de software nuevo, nadie quiere hacerlo mal, todo el mundo que sea mínimamente responsable va a querer hacerlo de la mejor forma posible, dar una calidad, un desempeño y una seguridad óptimas.

Esto para un desarrollo nuevo es relativamente sencillo. Nosotros como developers nos vamos a responsabilizar de lo que estamos haciendo en ese momento.

Programamos algo, lo hacemos funcionar, luego lo hacemos bien, y luego por fin lo hacemos rápido y seguro. (Make it work, make it right, make it fast).

Todo es maravilloso, todo está bien, el programador es un fenómeno y vivimos en el mundo de la piruleta, en el país de la fantasía, y tenemos una casa justo al lado del árbol que da las fresas de golomina.

Pero vivimos en el mundo real. Y en este punto, suelen ocurrir dos cosas:
  1.- Tenemos que hacer una entrega rápido, o no tenemos tiempo o cualquier otra excusa, y al final, introducimos un defecto y ahí se queda, ya se arreglará más adelante cuando tengamos tiempo y ganas
    * Pista: eso nunca sucede.


  2.- En Matrix, donde las vacas son esféricas, todo el software que tocamos, que hacemos es nuestro, lo hemos diseñado nosotros, lo hemos implementado y conocemos al dedillo todas sus características. Pero bienvenidos al desierto de lo real.

Hay veces (las que más), que recibimos código de otros. Báses de código extensas que no sabemos de dónde vienen, no hay documentación, está fatal. El programador que lo hizo ya ni está en la empresa...

    * Como ejemplo, mi confinamiento en 2020 consistió en mejorar la carga de un fichero que se hacía gracias a un programa alojado en Websphere 7. WebSphere 7 ejecuta JAVA 5.
    * Las responsables del producto, cuando yo entré, no sabían nada del código que había. Decían que lo había estado llevando un chico que se fue. Investigando a través de commits, para mi sorpresa ví que no había estado llevando nada, había estado un par de meses en la empresa y se piró porque no conseguía arreglar aquel desastre.
      
Claro, aquí tenemos varias opciones:

      * Método Villarriba: Paramos el desarrollo del producto. No se realiza ningúna funcionalidad ni se arregla nada hasta que no quede todo limpio y reluciente:
        * Dedicamos todo el tiempo y recursos necesarios hasta dejarlo "como Dios manda"

      * Método Oppenheimer u opción nucelar: Hacemos un cráter donde antes había un software y lo empezamos desde cero otra vez.
        * Eliminar todo lo existente, rediseñarlo y construirlo desde cero

      * La Ronaldinha: Miramos a la grada y seguimos.
        * Hacemos como que nada ha pasado. No tomamos ninguna acción. Seguimos a lo nuestro, desarrollando sin tener ningún tipo de cuidado tampoco

      * Tenemos otra opción:
        * Embrace lo que tenemos. Lo que está está. Pero vamos a continuar desarrollando, esta vez no permitiendo introducir nada más. Todo lo que entre nuevo ha de estar bien. Sin defectos, correctamente testeado y sin duplicados.
        * Y dejamos que poco a poco todo el código que ya teníamos, se vea beneficiado por el código que entra nuevo.
        * ¿Por qué digo que "el código que entra nuevo"? Sencillo:
          * Se calcula que el 20% del código de una empresa es renovado de forma anual. (DISCLAIMER: Ya sabéis que son estudios y medias, que la realidad de nuestra empresa puede ser perfectamente otra. Pero nos hacemos a la idea del point.)
          * Entonces, será acumulativo.
            * El primer año, será un 20%
            * El segundo año, un 35% de todo el código estará "limpio"
            * Al cabo de 5 años, un 50% del código estará limpio.

Conocemos los principios del Clean Code, pero y si Clean as you Code?

Presentamos la estrategia Clean as you Code, de SonarSource. Por comentarlo, esta estrategia anteriormente recibía el nombre de Fix the Leak (tapar la fuga), no me lo he inventado yo, no soy tan ingenioso.

¿En qué se basa? 

    * Dejar el pasado atrás. Vamos a olvidarnos por un momento del código antiguo que tenemos. Vamos a centrarnos en que el código nuevo que introduzcamos sea bueno.
      * El concepto de código nuevo es tanto nuevas funcionalidades que metamos
      * Como código que estamos retocando antiguo.
      * Básicamente es, todo lo que estamos haciendo lo hacemos bien.
    * Para ello, el programador es y ha de ser responsable de lo que hace. Si yo estoy programando algo, soy responsable de aquello que hago hacerlo chachi. Y para ello tengo herramientas para saber si lo estoy haciendo bien.
      * Si hago algo nuevo, lo hago chachi
      * Si toco algo viejo, lo dejo chachi
      * El código que estoy haciendo hoy tiene que ser bueno.
    * Estandaricemos.
      * Como empresa, como organización o equipo, vamos a sentarnos y vamos a decidir las herramientas que usamos. Las métricas y la forma de trabajar que usamos
      * De esa forma sea quien sea, esté en el proyecto que esté, con la tecnología que sea, y trabaje sobre algo nuevo o algo viejo, trabajaremos todos sobre el mismo lienzo y con las mismas pinturas.
    * Remediar la deuda técnica:
      * ¿Oye, qué pasa con el código viejo? ¿Que si tiene una vulnerabilidad no la arreglo?
      * Nope.
        * Como hemos dicho antes, los desarrolladores son responsables de su código y de la calidad del mismo.
        * Pero, ¿quién es el responsable del tiempo y recursos que hay en el proyecto?. Efectivamente los managers. Los managers son los que van a tener esa visión global, para decidir si algo se ha de abordar o no o si se ha de priorizar una tarea sobre otra. Será entonces cuando le asignen a un programador la tarea de limpiar o arreglar X incidencia, error o característica.
        * Pero es que incluso, aunqeu no decidamos ir proactivamente a arreglar, el código antiguo se irá beneficiando de los cambios en el nuevo de forma gradual.
      * Esto tiene una ventaja principal. El código que está limpio es más fácil, barato y mucho menos doloroso de mantener o mejorar en caso de que lo tengamos o lo queramos hacer.

Antes hemos comentado que hay una serie de herramientas para ayudarnos a cumplir esa estandarización. La herramienta principal para ello es lo que llamamos Quality Gate o en la lengua de Cervantes, Umbral de Calidad.

El Umbral de calidad es una serie de métricas que se deben cumplir para considerar que el código es válido o no. La pregunta principal que nos hacemos cuando decidimos cómo son esas métricas es: ¿Está este código preparado para subir a producción? ¿Sería algo que yo subiría a producción?.

Y yo voy a una pregunta más que es... ¿Dejaría que este código fuera introducido, mergeado contra mi rama principal de desarrollo? ¿Dejaría yo que esto pasara a mi rama master?

Bien. Nosotros podemos setear el Quality Gate que queramos o que decidamos, pero llegados a este punto, vamos a ver la estrategia propuesta Clean as you Code por parte de SonarSource. Para mi personalmente y para excentia como organización que también estandarizamos lo que pensamos, creemos firmemente que estas métricas son las mínimas indispensables para asegurar una limpieza de código sin esfuerzo:
  * Decir que los que estemos familiarizados con SonarQube/SonarCloud ya sabremos qué conceptos son pero creo que son descriptivos:
        * No metemos ningún tipo de bug (defecto de código que puede dar lugar a una malfunción)
        * No metemos vulnerabilidades nuevas. (defecto de código que puede dar lugar a una intrusión)
        * Si hay dudas de seguridad, las chequiamos (Security Hotspots)
        * Todo lo que hagamos nuevo va testiado hasta las muelas. (métrica para control de testeo mínimo.)
        * Revisamos que lo que estemos haciendo no esté ya hecho (metrica para los duplicatis con tomati)

  * Que sepáis que, luego además, se pueden meter métricas a mayores. Y se pueden meter tanto para el código nuevo como para el código antiguo. Podemos controlar también el antiguo, que no baje de X calidad o meter una métrica en el quality gate para forzar a llegar a cumplirla. No es el objetivo de hoy, nos centramos en el código antiguo.

Este Quality Gate nos va a dar un resultado una vez que analicemos el código. Es un binario. O bien el código que hemos metido Pasa o No pasa. Si algo inclumple, no pasa. No hay medias tintas, es mecánico. Blanco o negro. Está bien o no está bien.

Claro, esto es una ventaja muy bestia de cara a la automatización del código y al control de qué se hace.
  * Tu código está y va a estar bien. Si no... no pasa.
  * Hemos establecido esto para toda la organización, lo hemos decidido entre todos. Si no está bien, no está bien. Pointball. Punto pelota.

Bien, pues los productos de SonarSource, es decir, SonarCloud y SonarQube nos permiten saber cuál es el estado de nuestro código desde esa estandarización. Nos permiten recoger de forma externa el estado de nuestro quality gate.

Y eso, y unido a los sistemas de CI/CD modernos, nos permiten automatizar el control del código.

Nosotros utilzamos los sistemas de CI/CD para construir nuestra aplicación y hacer una serie de operaciones con él. Imaginad un proyecto donde nosotros lo construyamos, miremos a ver si el código está bien o no y luego, si está bien, hagamos un deploy en un servidor de pruebas.

Pero vayamonos a lo más básico. Vamonos a simplemente, parar el pipeline, parar la cadena de acciones, cuando SonarQube detecte que no se cumplen los parámetros establecidos en la organización. Desde ese "parar el pipeline", ya podremos evitar lo que queramos
  * Que ese código pase a nuestra rama develop (porque está en una rama feature que estamos desarrollando y no permitamos su mergeo)
  * Que ese código pase a un servidor de desarrollo
  * Cualquier cosa.

Vamos a ver mediante Github cómo parar el pipeline y en nuestro ejemplo particular, cómo evitar que se mergee la rama donde estoy desarrollando a cualquier otra rama.

(Demo técnica)
