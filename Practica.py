class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Miembro(Persona):
    def __init__(self, nombre, edad, miembro_id):
        super().__init__(nombre, edad)
        self.miembro_id = miembro_id
        self.libros_prestados = []

    def tomarP(self, libro):
        self.libros_prestados.append(libro)
        print(f"{self.nombre} ha tomado prestado el libro '{libro.titulo}'.")

    def devolverL(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no tiene el libro '{libro.titulo}' prestado.")
    
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def agregarL(self, libro):
        self.libros.append(libro)
        print(f"'{libro.titulo}' ha sido añadido a la biblioteca")

    def agregarM(self, miembro):
        self.miembros.append(miembro)
        print(f"El miembro {miembro.nombre} ha sido añadido como miembro.")

    def mostrarL(self):
        if self.libros:
            print("Libros disponibles en la biblioteca:")
            for libro in self.libros:
                print(f"- {libro.titulo} por {libro.autor}")
        else:
            print("No hay libros en la biblioteca")

def menu():
    print("\nBienvenido a la Biblioteca")
    print("1. Registrar un nuevo miembro")
    print("2. Añadir un nuevo libro")
    print("3. Mostrar todos los libros disponibles")
    print("4. Tomar prestado un libro")
    print("5. Devolver un libro")
    print("6. Salir")

def main():
    biblioteca = Biblioteca()

    while True:
        menu()
        opcion = input("Ingrese la opción que desee: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del miembro: ")
            edad = int(input("Ingrese la edad del miembro: "))
            miembro_id = int(input("ID del miembro: "))
            nuevo_miembro = Miembro(nombre, edad, miembro_id)
            biblioteca.agregarM(nuevo_miembro)
        elif opcion == "2":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            nuevo_libro = Libro(titulo, autor, isbn)
            biblioteca.agregarL(nuevo_libro)
        elif opcion == "3":
            biblioteca.mostrarL()
        elif opcion == "4":
            miembro_id = int(input("Ingrese el ID del miembro: "))
            miembro = next((m for m in biblioteca.miembros if m.miembro_id == miembro_id), None)
            if miembro:
                libro_titulo = input("Ingrese el título del libro: ")
                libro = next((l for l in biblioteca.libros if l.titulo == libro_titulo), None)
                if libro:
                    miembro.tomarP(libro)
                else:
                    print("No hay libros disponibles con ese título.")
            else:
                print("No se encontró el miembro.")
        elif opcion == "5":
            miembro_id = int(input("Ingrese el ID del miembro: "))
            miembro = next((m for m in biblioteca.miembros if m.miembro_id == miembro_id), None)
            if miembro:
                libro_titulo = input("Ingrese el título del libro: ")
                libro = next((l for l in biblioteca.libros if l.titulo == libro_titulo), None)
                if libro:
                    miembro.devolverL(libro)
                else:
                    print("No hay libros con ese título.")
            else:
                print("No se encontró el miembro.")
        elif opcion == "6":
            print("Gracias por utilizar la biblioteca")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
