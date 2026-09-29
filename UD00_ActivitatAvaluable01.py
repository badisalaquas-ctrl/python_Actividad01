"""
UD00 - Activitats Avaluables 01
Sistemes de Gestió Empresarial
"""

# ============================================================
# IMPORTS
# ============================================================

import copy
import hashlib
import random
import sys


# ============================================================
# ACTIVITAT 01
# ============================================================

def actividad_01():
    """
    Activitat 01:
    - Clonar una llista.
    - Diferenciar shallow copy i deep copy.
    - Afegir un element.
    - Llevar un element.
    - Crear una nova llista amb els 4 últims elements.
    - Convertir una cadena en una llista de paraules.
    - Comentaris d'una línia i multilínia.
    """

    print("\n" + "=" * 60)
    print("ACTIVITAT 01")
    print("=" * 60)

    # --------------------------------------------------------
    # 1. Clonar una llista
    # --------------------------------------------------------

    lista_original = [10, 20, 30, 40, 50]

    # Con una lista de valores simples, slicing crea una copia.
    lista_clonada = lista_original[:]

    print("\n1. Clonar una llista:")
    print("Lista original:", lista_original)
    print("Lista clonada: ", lista_clonada)

    # Comprobamos que son dos listas diferentes.
    print("¿Son el mismo objeto?", lista_original is lista_clonada)

    # --------------------------------------------------------
    # 2. Shallow copy y deep copy
    # --------------------------------------------------------

    # Una shallow copy copia la lista exterior, pero los objetos
    # que hay dentro siguen siendo compartidos.
    lista_anidada = [[1, 2], [3, 4]]

    shallow = copy.copy(lista_anidada)
    shallow[0].append(99)

    print("\n2. Shallow copy:")
    print("Lista original:", lista_anidada)
    print("Shallow copy:  ", shallow)

    # En este caso, al modificar una lista interior, el cambio
    # también aparece en la lista original.

    # Deep copy crea una copia independiente también de los
    # objetos que están dentro de la lista.
    lista_anidada_2 = [[1, 2], [3, 4]]

    deep = copy.deepcopy(lista_anidada_2)
    deep[0].append(99)

    print("\nDeep copy:")
    print("Lista original:", lista_anidada_2)
    print("Deep copy:     ", deep)

    # Resumen:
    # shallow -> copia la estructura exterior, pero comparte
    #             los objetos internos.
    # deep    -> copia también los objetos internos.

    # --------------------------------------------------------
    # 3. Añadir un elemento
    # --------------------------------------------------------

    lista = [1, 2, 3]
    lista.append(4)

    print("\n3. Añadir un elemento:")
    print(lista)

    # append() añade un elemento al final de la lista.

    # --------------------------------------------------------
    # 4. Llevar/quitar un elemento
    # --------------------------------------------------------

    lista = [1, 2, 3, 4, 5]
    lista.remove(3)

    print("\n4. Llevar un elemento:")
    print(lista)

    # remove() elimina la primera aparición del valor indicado.

    # --------------------------------------------------------
    # 5. Crear una lista con los 4 últimos elementos
    # --------------------------------------------------------

    lista = [10, 20, 30, 40, 50, 60, 70]

    ultimos_4 = lista[-4:]

    print("\n5. Los 4 últimos elementos:")
    print(ultimos_4)

    # [-4:] significa: desde el cuarto elemento empezando
    # por el final hasta el final de la lista.

    # --------------------------------------------------------
    # 6. Convertir palabras de una cadena en una lista
    # --------------------------------------------------------

    cadena = "Python es un lenguaje de programación"

    palabras = cadena.split()

    print("\n6. Cadena convertida en lista:")
    print(palabras)

    # split() separa la cadena utilizando los espacios como
    # separadores cuando no indicamos otro separador.

    # --------------------------------------------------------
    # 7. Comentarios de una línea y multilínea
    # --------------------------------------------------------

    # Este es un comentario de una sola línea.

    """
    Esto es un comentario multilínea.
    En Python se suele utilizar una cadena de texto
    multilínea para escribir explicaciones de varias líneas.
    """

    print("\n7. Comentarios:")
    print("Se han incluido ejemplos de comentarios de una línea")
    print("y comentarios multilínea en el código.")


# ============================================================
# ACTIVITAT 02
# ============================================================

def sumar_numeros(numero1, numero2):
    """
    Recibe dos números y devuelve su suma.

    Los números son tipos simples, por lo que la función
    trabaja con los valores recibidos y devuelve un resultado.
    """
    return numero1 + numero2


def doblar_lista_en_misma_lista(lista):
    """
    Recibe una lista y modifica ESA MISMA lista.

    No devuelve nada de forma explícita.

    Al trabajar sobre la lista recibida, los cambios se pueden
    observar fuera de la función porque estamos modificando
    el mismo objeto lista.
    """

    for i in range(len(lista)):
        lista[i] = lista[i] * 2


def doblar_lista_copia(lista):
    """
    Recibe una lista, crea una copia y devuelve la copia
    con todos sus valores doblados.

    La lista original no se modifica.
    """

    # Creamos una copia para no modificar la original.
    copia = lista.copy()

    for i in range(len(copia)):
        copia[i] = copia[i] * 2

    return copia


def actividad_02():
    """
    Actividad 02:
    Demuestra el comportamiento solicitado con números
    y listas.
    """

    print("\n" + "=" * 60)
    print("ACTIVIDAD 02")
    print("=" * 60)

    # --------------------------------------------------------
    # 1. Dos números -> suma
    # --------------------------------------------------------

    numero1 = 5
    numero2 = 8

    resultado = sumar_numeros(numero1, numero2)

    print("\n1. Suma de dos números:")
    print(f"{numero1} + {numero2} = {resultado}")

    # --------------------------------------------------------
    # 2. Modificar la misma lista
    # --------------------------------------------------------

    lista_original = [1, 2, 3, 4]

    print("\n2. Modificar la misma lista:")
    print("Antes:", lista_original)

    # La función modifica directamente lista_original.
    doblar_lista_en_misma_lista(lista_original)

    print("Después:", lista_original)

    # --------------------------------------------------------
    # 3. Devolver una copia modificada
    # --------------------------------------------------------

    lista_original = [1, 2, 3, 4]

    print("\n3. Devolver una copia modificada:")
    print("Original antes:", lista_original)

    lista_doblada = doblar_lista_copia(lista_original)

    print("Copia doblada:", lista_doblada)
    print("Original después:", lista_original)

    # Aquí la original permanece igual porque la función
    # trabajó sobre una copia.


# ============================================================
# ACTIVITAT 03
# ============================================================

def hash_contrasena(contrasena):
    """
    Convierte una contraseña en un hash SHA-256.

    El hash no es la contraseña original, sino una representación
    calculada a partir de ella.
    """

    return hashlib.sha256(contrasena.encode("utf-8")).hexdigest()


def buscar_usuario_en_lista(usuarios, nombre_usuario):
    """
    Busca un usuario dentro de una lista de diccionarios.

    Devuelve el usuario encontrado o None si no existe.
    """

    for usuario in usuarios:
        if usuario["usuario"] == nombre_usuario:
            return usuario

    return None


def buscar_usuario_en_diccionario(usuarios, nombre_usuario):
    """
    Busca un usuario directamente en un diccionario utilizando
    su nombre como clave.
    """

    return usuarios.get(nombre_usuario)


def actividad_03():
    """
    Actividad 03:
    Almacena usuarios y contraseñas mediante:
    - Una lista.
    - Un diccionario.

    Las contraseñas se almacenan utilizando SHA-256.
    También se realizan dos consultas.
    """

    print("\n" + "=" * 60)
    print("ACTIVIDAD 03")
    print("=" * 60)

    # --------------------------------------------------------
    # LISTA DE USUARIOS
    # --------------------------------------------------------

    usuarios_lista = []

    datos_usuarios = [
        ("ana", "Ana123"),
        ("juan", "Juan456"),
        ("maria", "Maria789"),
        ("pedro", "Pedro321"),
        ("laura", "Laura654"),
    ]

    for nombre, contrasena in datos_usuarios:
        usuarios_lista.append({
            "usuario": nombre,
            "password_hash": hash_contrasena(contrasena)
        })

    print("\n1. Usuarios almacenados en una lista:")
    for usuario in usuarios_lista:
        print(usuario)

    # Dos consultas.
    consulta1 = buscar_usuario_en_lista(usuarios_lista, "maria")
    consulta2 = buscar_usuario_en_lista(usuarios_lista, "carlos")

    print("\nConsultas en la lista:")
    print("Consulta 'maria':", consulta1)
    print("Consulta 'carlos':", consulta2)

    # --------------------------------------------------------
    # DICCIONARIO DE USUARIOS
    # --------------------------------------------------------

    usuarios_diccionario = {}

    for nombre, contrasena in datos_usuarios:
        usuarios_diccionario[nombre] = hash_contrasena(contrasena)

    print("\n2. Usuarios almacenados en un diccionario:")
    for usuario, password_hash in usuarios_diccionario.items():
        print(usuario, "->", password_hash)

    # Dos consultas.
    consulta3 = buscar_usuario_en_diccionario(
        usuarios_diccionario,
        "juan"
    )

    consulta4 = buscar_usuario_en_diccionario(
        usuarios_diccionario,
        "carlos"
    )

    print("\nConsultas en el diccionario:")
    print("Consulta 'juan':", consulta3)
    print("Consulta 'carlos':", consulta4)

    # IMPORTANTE:
    # No guardamos las contraseñas originales.
    # Guardamos el resultado de aplicar SHA-256.


# ============================================================
# ACTIVITAT 04
# ============================================================

def actividad_04():
    """
    Explicación de los operadores:
    - is
    - not
    - in
    """

    print("\n" + "=" * 60)
    print("ACTIVIDAD 04")
    print("=" * 60)

    # --------------------------------------------------------
    # Operador IS
    # --------------------------------------------------------

    lista_a = [1, 2, 3]
    lista_b = lista_a
    lista_c = [1, 2, 3]

    print("\n1. Operador 'is':")

    # lista_b apunta al MISMO objeto que lista_a.
    print("lista_a is lista_b:", lista_a is lista_b)

    # lista_c tiene el mismo contenido, pero es otro objeto.
    print("lista_a is lista_c:", lista_a is lista_c)

    # 'is' comprueba identidad: si dos variables hacen referencia
    # al mismo objeto.

    # --------------------------------------------------------
    # Operador NOT
    # --------------------------------------------------------

    numero = 10

    print("\n2. Operador 'not':")

    print("numero == 10:", numero == 10)
    print("not(numero == 10):", not (numero == 10))

    # not invierte el resultado lógico:
    # True -> False
    # False -> True

    # --------------------------------------------------------
    # Operador IN
    # --------------------------------------------------------

    colores = ["red", "white", "black"]

    print("\n3. Operador 'in':")

    print("'red' in colores:", "red" in colores)
    print("'blue' in colores:", "blue" in colores)

    # in comprueba si un elemento se encuentra dentro
    # de una colección.


# ============================================================
# ACTIVITAT 05
# ============================================================

def funcion_parametros_variables(*numeros):
    """
    Ejemplo de una función que puede recibir un número
    indefinido de parámetros.

    *numeros recoge todos los argumentos en una tupla.
    """

    return sum(numeros)


def actividad_05():
    """
    Actividad 05:
    - Recibir varios parámetros desde la consola.
    - Mostrar una forma de hacer una sobrecarga de funciones
      en Python mediante parámetros variables.

    Ejemplo de ejecución desde consola:

        python UD00_ActivitatAvaluable01.py 10 20 30

    sys.argv[0] contiene el nombre del programa.
    sys.argv[1:] contiene los parámetros introducidos.
    """

    print("\n" + "=" * 60)
    print("ACTIVIDAD 05")
    print("=" * 60)

    # --------------------------------------------------------
    # 1. Parámetros desde consola
    # --------------------------------------------------------

    parametros = sys.argv[1:]

    print("\n1. Parámetros recibidos desde consola:")

    if parametros:
        print(parametros)

        # Intentamos convertir los parámetros en números.
        try:
            numeros = [float(parametro) for parametro in parametros]

            print("Como números:", numeros)
            print("Suma:", funcion_parametros_variables(*numeros))

        except ValueError:
            print("Algún parámetro no es numérico.")

    else:
        # Si ejecutamos el programa desde el IDE sin parámetros,
        # mostramos un ejemplo para poder comprobar el ejercicio.
        print("No se han recibido parámetros.")
        print("Ejemplo:")
        print("python UD00_ActivitatAvaluable01.py 10 20 30")

    # --------------------------------------------------------
    # 2. "Sobrecarga" de funciones en Python
    # --------------------------------------------------------

    # Python no permite definir dos funciones con el mismo nombre
    # esperando que elija automáticamente según el número de
    # argumentos, como ocurre en otros lenguajes.
    #
    # Una forma habitual de conseguir un comportamiento similar
    # es utilizar *args.

    print("\n2. Ejemplo de parámetros variables:")

    print("Sin parámetros:", funcion_parametros_variables())
    print("Con 2 parámetros:", funcion_parametros_variables(10, 20))
    print(
        "Con 4 parámetros:",
        funcion_parametros_variables(10, 20, 30, 40)
    )


# ============================================================
# ACTIVITAT 06
# ============================================================

def clave_ordenacion(elemento):
    """
    Esta es la KEY FUNCTION.

    Recibe UN elemento de la lista y devuelve la información
    que sorted() utilizará para decidir el orden.

    Cada elemento tiene esta estructura:

        [mida, pes]

    Queremos:
    1. Mayor mida primero.
    2. Si la mida es igual, menor pes primero.

    Para conseguirlo devolvemos:
        (-mida, pes)

    El signo negativo hace que una ordenación ascendente
    coloque las mayores medidas primero.
    """

    mida = elemento[0]
    pes = elemento[1]

    return (-mida, pes)


def actividad_06():
    """
    Actividad 06:
    Ordena una lista de listas [mida, pes] utilizando
    una key function.
    """

    print("\n" + "=" * 60)
    print("ACTIVIDAD 06")
    print("=" * 60)

    lista_medidas_pesos = [
        [170, 70],
        [180, 80],
        [170, 65],
        [160, 60],
        [180, 75],
        [190, 90],
        [160, 55]
    ]

    print("\nLista original:")
    print(lista_medidas_pesos)

    # sorted() devuelve una nueva lista ordenada.
    lista_ordenada = sorted(
        lista_medidas_pesos,
        key=clave_ordenacion
    )

    print("\nLista ordenada:")
    print(lista_ordenada)

    # La key function NO realiza la ordenación por sí sola.
    # Le indica a sorted() qué valor debe utilizar para comparar
    # cada elemento.
    #
    # Como devolvemos (-mida, pes):
    # - Primero se ordena por -mida -> mayor mida primero.
    # - En caso de empate, se ordena por pes -> menor pes primero.


# ============================================================
# ACTIVITAT 07
# ============================================================

class Car:
    """
    Clase Car.

    Atributos solicitados por el ejercicio:
    - matricula
    - color
    """

    def __init__(self, matricula, color):
        """
        Constructor de la clase.

        Se ejecuta cuando creamos una nueva instancia de Car.
        """
        self.matricula = matricula
        self.color = color

    def imprimir(self):
        """
        Método solicitado por el ejercicio.

        Imprime los datos del coche.
        """
        print(
            f"Matrícula: {self.matricula} | "
            f"Color: {self.color}"
        )

    def cambiar_color(self, nuevo_color):
        """
        Segundo método adicional.

        Permite cambiar el color del coche.
        """
        self.color = nuevo_color

    def es_matricula_par(self):
        """
        Tercer método adicional.

        Devuelve True si la matrícula es par
        y False si es impar.
        """
        return self.matricula % 2 == 0


def actividad_07():
    """
    Actividad 07:
    - Define la clase Car.
    - Pide n por teclado.
    - Crea n instancias.
    - Matrículas consecutivas de 1 a n.
    - Color aleatorio de la lista indicada.
    - Imprime como máximo las 10 primeras instancias.
    """

    print("\n" + "=" * 60)
    print("ACTIVIDAD 07")
    print("=" * 60)

    colores = ["red", "white", "black", "pink", "blue"]

    # Pedimos al usuario el número de coches.
    while True:
        try:
            n = int(input("\n¿Cuántos coches quieres crear? "))

            if n < 0:
                print("Introduce un número mayor o igual que 0.")
                continue

            break

        except ValueError:
            print("Debes introducir un número entero.")

    coches = []

    # Creamos n instancias de Car.
    for numero in range(1, n + 1):

        # Elegimos aleatoriamente uno de los colores
        # especificados en el enunciado.
        color_aleatorio = random.choice(colores)

        coche = Car(numero, color_aleatorio)

        coches.append(coche)

    print("\nCoches creados:", len(coches))
    print("Primeras instancias:")

    # El ejercicio pide imprimir las 10 primeras.
    # Si n es menor que 10, range solo recorrerá las que existan.
    limite = min(n, 10)

    for i in range(limite):
        coches[i].imprimir()


# ============================================================
# MAIN
# ============================================================

def main():
    """
    Función principal del programa.

    Desde aquí ejecutamos las 7 actividades.
    """

    print("=" * 60)
    print("UD00 - ACTIVIDADES EVALUABLES 01")
    print("Sistemas de Gestión Empresarial")
    print("=" * 60)

    actividad_01()
    actividad_02()
    actividad_03()
    actividad_04()
    actividad_05()
    actividad_06()
    actividad_07()


# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()
