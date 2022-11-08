import statistics

class Pelicula():
    def __init__(self, Nombre, Genero,fecha):
        self.valoraciones = []
        
        self.nombre = Nombre
        self.genero = Genero
        self.fecha = fecha
        self.valoracion = 0
        
    def __str__(self):
        if len(self.valoraciones) == 0:
            return f"Nombre: {self.nombre}\nFecha: {self.fecha}\nGenero: {self.genero}\n\nLa Pelicula no tiene Valoraciones"
        else:
            return f"Nombre: {self.nombre}\nFecha: {self.fecha}\nGenero: {self.genero}\nValoracione: {self.valoracion}"
    def agregarValoraciones(self, n):
        self.valoraciones.append(n)
        self.valoracion = statistics.mean(self.valoraciones)
        
    def getNombre(self):
        return self.nombre
    
    def getFecha(self):
        return self.fecha
    
    def getValoracion(self):
        return self.getValoracion
    
    def getValoraciones(self):
        return self.valoraciones
    
    def getGenero(self):
        return self.genero
    
    
    
Peliculas = []


activo = True

while(activo):
    print("1. Agregar Pelicula")
    print("2. Listar Pelicula")
    print("3. Eliminar Pelicula")
    print("4. Agregar Valoracion")
    print("0. Salir")
    
    opcion = int(input("Seleccione opcion : "))
    
    if opcion == 0:
        activo = False
        
    if opcion == 1:
        nombre = str(input("Digite el Nombre de la Pelicula : "))
        genero = str(input("Digite el Genero de la Pelicula : "))
        fecha = int(input("Digite el fecha de la Pelicula : "))
        
        p = Pelicula(nombre, genero, fecha)
        Peliculas.append(p)
        
    if opcion == 2:
        print("\n")
        if len(Peliculas) != 0:
            for p in Peliculas:
                print(p)
                print("\n")
        else:
            print("No hay peliculas")
            
    if opcion == 3:
        indice = int(input("Digite el indice de la pelicula : "))
        Peliculas.pop(indice - 1)
        
    if opcion == 4:
        indice = int(input("Digite el indice de la pelicula : "))
        valoracion = int(input("Digite la valoracion : "))
        Peliculas[indice - 1].agregarValoraciones(valoracion)
        



        