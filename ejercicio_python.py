# EJERCICIO 1
def contar_caracteres(cadena):
    total = 0
    for c in cadena:
        total += 1
    return total

cadena1 = "¡Hola alumnos! Bienvenidos a clase"
print(contar_caracteres(cadena1))  # 34

cadena2 = 3
# print(contar_caracteres(cadena2))  # Error

# EJERCICIO 2
def calcular_promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

numeros1 = [1, 2, 3, 4, 5]
numeros2 = []

print(calcular_promedio(numeros1))  # 3.0
print(calcular_promedio(numeros2))  # 0

# EJERCICIO 3
def encontrar_duplicado(lista):
    vistos = set()
    for x in lista:
        if x in vistos:
            return x
        vistos.add(x)
    return None

numeros1 = [1,2,3,4,5,6,7,8,9,3]
numeros2 = [1,2,3,4,5,6,7,8,9]

print(encontrar_duplicado(numeros1))  # 3
print(encontrar_duplicado(numeros2))  # None

# EJERCICIO 4
def enmascarado_datos(valor):
    s = str(valor)
    return '#' * (len(s)-4) + s[-4:]

contraseña1 = "Micontraseña1234"
contraseña2 = 123456789

print(enmascarado_datos(contraseña1))  # ############1234
print(enmascarado_datos(contraseña2))  # #####6789

# EJERCICIO 5
def es_anagrama(p1, p2):
    p1 = p1.replace(" ","").lower()
    p2 = p2.replace(" ","").lower()
    return sorted(p1) == sorted(p2)

print(es_anagrama("Roma","lana"))  # False
print(es_anagrama("Roma","amor"))  # True

# EJERCICIO 6
def buscar_nombre():
    lista = ["Jaime","Silvia","Ana"]
    nombre = input("Nombre a buscar: ").strip()
    if nombre in lista:
        print(f"{nombre} encontrado")
    else:
        print(f"{nombre} no encontrado")

# buscar_nombre()

# EJERCICIO 7
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # 55

# EJERCICIO 8
def encontrar_puesto_empleado(nombre_completo, lista):
    try:
        nombre, apellido = nombre_completo.split()
    except:
        return f"{nombre_completo} no trabaja aquí"
    for emp in lista:
        if nombre==emp["nombre"] and apellido==emp["apellido"]:
            return emp["puesto"]
    return f"{nombre_completo} no trabaja aquí"

empleados = [
    {'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
    {'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
    {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}
]

print(encontrar_puesto_empleado("Juan García", empleados))
print(encontrar_puesto_empleado("Alejandro", empleados))

# EJERCICIO 9
cubo_numero = lambda x: x**3
print(cubo_numero(5))

# EJERCICIO 10
resto_division = lambda x,y: x%y
print(resto_division(50,3))

# EJERCICIO 11
lista_numeros = [24,56,2.3,19,-1,0]
numeros_pares = list(filter(lambda x:x%2==0, lista_numeros))
print(numeros_pares)

# EJERCICIO 12
numeros_suma = list(map(lambda x:x+3, lista_numeros))
print(numeros_suma)

# EJERCICIO 13
lista_numeros_1 = [1,4,5,6,7,7]
lista_numeros_2 = [3,11,34,56]
sumar_listas = lambda l1,l2: [x+y for x,y in zip(l1,l2)]
print(sumar_listas(lista_numeros_1,lista_numeros_2))

# EJERCICIO 14
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [r+1 for r in self.ramas]

    def quitar_rama(self, n):
        if 0<n<=len(self.ramas):
            del self.ramas[n-1]

    def info_arbol(self):
        if not self.ramas:
            return f"El árbol tiene tronco {self.tronco} y no tiene ramas"
        return f"El árbol tiene tronco {self.tronco}, {len(self.ramas)} ramas: {', '.join(f'r{i+1}:{v}' for i,v in enumerate(self.ramas))}"

arbol1 = Arbol()
arbol1.crecer_tronco()
arbol1.nueva_rama()
arbol1.crecer_ramas()
arbol1.nueva_rama()
arbol1.nueva_rama()
arbol1.quitar_rama(2)
print(arbol1.info_arbol())

# EJERCICIO 15
class UsuarioBanco:
    def __init__(self,nombre,saldo,corriente=False):
        self.nombre=nombre
        self.saldo=saldo
        self.corriente=corriente

    def retirar_dinero(self,cant):
        if cant>self.saldo: raise ValueError("Saldo insuficiente")
        self.saldo-=cant
        return self.saldo

    def transferir_dinero(self,otro,cant):
        if not otro.corriente or cant>otro.saldo:
            raise ValueError("No se puede transferir")
        self.saldo+=cant
        otro.saldo-=cant
        return self.saldo,otro.saldo

    def agregar_dinero(self,cant):
        self.saldo+=cant
        return self.saldo

# EJERCICIO 16
def contar_palabras(texto):
    c={}
    for w in texto.lower().split():
        c[w]=c.get(w,0)+1
    return c

def reemplazar_palabra(texto,orig,nuevo):
    return ' '.join([nuevo if w==orig else w for w in texto.lower().split()])

def eliminar_palabra(texto,pal):
    return ' '.join([w for w in texto.lower().split() if w!=pal])

def procesar_texto(texto,opcion,*args):
    if opcion=="contar": return contar_palabras(texto)
    if opcion=="remplazar": return reemplazar_palabra(texto,args[0],args[1])
    if opcion=="eliminar": return eliminar_palabra(texto,args[0])
    raise ValueError("Opción inválida")

texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
print(procesar_texto(texto,"contar"))
print(procesar_texto(texto,"remplazar","texto","relato"))
print(procesar_texto(texto,"eliminar","ejemplo"))
