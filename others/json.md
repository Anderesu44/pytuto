# Curso de JSON

## Introducción a JSON

JavaScript Object Notation (JSON) es un formato de datos que se utiliza para transmitir y almacenar información. Es un formato textual que se usa para representar valores y estructuras de datos como listas, diccionarios, etc. JSON es útil para la interacción entre sistemas, ya sea a nivel de cliente-servidor o entre sistemas en diferentes lenguajes de programación.

## JSON básico

Para escribir información en JSON, debes respetar su sintaxis. En un archivo, solo puede existir un objeto de los siguientes tipos:

String, Number, Boolean, Null, Array y Object

- #### String:

  Una string o cadena de texto que se encierra entre comillas dobles.
  - Ejemplo: "Hola Mundo", "Hello World"

- #### Number:

  Un número entero o decimal. Los números pueden ser positivos o negativos y pueden tener decimales.
  - Ejemplos: 10, -5, 3.14

- #### Boolean:

  Un valor booleano que puede ser verdadero (true) o falso (false).
  - Ejemplo: true, false

- #### Null:

  Es un valor especial que representa la ausencia de un valor.
  - Ejemplo: null

- #### Array:

  Una lista ordenada de valores. Los elementos pueden ser de cualquier tipo, incluyendo otros arrays y objetos.
  - Ejemplos: [1, 2, "Hello", true], ["apple", "banana", "cherry"]

- #### Object:

  Un conjunto de pares clave-valor que se separan por comas. Las claves deben ser strings y los valores pueden ser cualquier tipo de datos.
  - Ejemplos: {"name": "John", "age": 30}, {"fruit": "apple", "color": "red"}

## JSON en Python

##### Python tiene una biblioteca llamada `json` que permite trabajar con JSON.

Pero como te habrás dado cuenta, existen más tipos de datos en Python que los que soporta JSON. Esto no es un problema, ya que puedes convertirlos a JSON automáticamente.

### De Python a JSON:

    +-------------------+---------------+
    | Python            | JSON          |
    +===================+===============+
    | dict              | object        |
    +-------------------+---------------+
    | list, tuple       | array         |
    +-------------------+---------------+
    | str               | string        |
    +-------------------+---------------+
    | int, float        | number        |
    +-------------------+---------------+
    | True              | true          |
    +-------------------+---------------+
    | False             | false         |
    +-------------------+---------------+
    | None              | null          |
    +-------------------+---------------+

### De JSON a Python:

    +---------------+-------------------+
    | JSON          | Python            |
    +===============+===================+
    | object        | dict              |
    +---------------+-------------------+
    | array         | list              |
    +---------------+-------------------+
    | string        | str               |
    +---------------+-------------------+
    | number (int)  | int               |
    +---------------+-------------------+
    | number (real) | float             |
    +---------------+-------------------+
    | true          | True              |
    +---------------+-------------------+
    | false         | False             |
    +---------------+-------------------+
    | null          | None              |
    +---------------+-------------------+
