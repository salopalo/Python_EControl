

class LibroNonAtopado(Exception):
    def __init__(self, titulo, mens="Este libro non se atopa rexistrado."):
        self.titulo = titulo
        self.mens = mens
        super().__init__(self.mens)
        
    def __str__(self):
        return f"{self.titulo} -> {self.mens}"
  

prestamos = {}  



while True:

    
    try:
        print("\n**XESTION DE BIBLIOTECA**")
        print("1 - Préstamo de libro")
        print("2 - Retorno de libro")
        print("3 - Consulta de libro")
        print("4 - Consulta de usuario")
        print("5 - Mostrar a colección de préstamos.")
        print("6 - Fin do programa")
        print("--------------------------")

        try:
            opt = int(input("Introduza a opción: "))
            print(f"Opcion ->{opt}")
        except ValueError as e:
            print("Opción non válida, debe introducir un número entre 1 e 6.")
            opt = None
        
        if opt == 1:
            lib = input("Introduza o titulo do libro.")
            user = input("Introduza o nome do usuario.")
            atopado = False
            for us in prestamos:
                if user.lower() == us.lower():
                    prestamos[us].append(lib)
                    atopado = True
            if not atopado:
                prestamos[user] = [lib]
            print(f"O libro {lib} prestouse ao usuario {user}")
                    
        elif opt == 2:
            lib = input("Introduza o titulo do libro.")
            user = input("Introduza o nome do usuario.")
            atopado_us = False
            atopado_lib = False
            for us, li in prestamos.items():
                if user.lower() == us.lower():
                    atopado_us = True
                    for libro in li:
                        if lib.lower() == libro.lower():
                            prestamos[us].remove(libro)
                            print(f"Retornado o libro {lib} do usuario {user}.")
                            atopado_lib = True
            if not atopado_us:
                print(f"O usuario {user} non ten préstamos.")
            elif not atopado_lib:
                print(f"O usuario {user} non ten a préstamo o libro {lib}. Non se pode proceder á devolución.")
            
        elif opt == 3:
            lib = input("Introduza o titulo do libro: ")
            atopado = False
            for us, li in prestamos.items():
                for libro in li:
                    if lib.lower() == libro.lower():
                        print(f"O libro {lib} prestouse ao usuario {us}.")
                        atopado = True 
            if not atopado:
                raise LibroNonAtopado(lib)
    
        elif opt == 4:
            user = input("Introduza o nome do usuario: ")
            atopado = False
            for us, li in prestamos.items():
                if user.lower() == us.lower():
                    libros = ", ".join(li) if li else "ningun libro"
                    print(f"O usuario {user} ten en préstamo os libros: {libros}")
                    atopado = True 
            if not atopado:
                print("O usuario non existe.")
                
        elif opt == 5:
            if prestamos:
                for us, li in prestamos.items():
                    libros = ", ".join(li) if li else "ningun libro"
                    print(f"Usuario: {us}. Libros a préstamo: {libros}")
            else:
                print("Base de datos vacía.")
                     
        elif opt == 6:
            print("Fin do programa")
            break
        
        else:
            if isinstance(opt, (int, float)) and opt not in (1,2,3,4,5,6):
                raise ValueError ("Opción non válida, teclee unha opción entre 1 e 6.")
            

    except (ValueError, TypeError, LibroNonAtopado) as error:
        print (error)
        
        
    
    
    