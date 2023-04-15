# código del libro
# título del libro
# apellido del autor 
# nombre del autor 
# Área de Conocimiento 
# editorial 
# Cantidad de páginas
import sqlite3 as sql
from colorama import init, Fore, Back, Style

def ver():
    print("")
    print("***************************************************************************************************")
    print("")
    print(Fore.GREEN+f"(#,"+Fore.RESET+Fore.BLUE+f"  Nombre  ,"+Fore.RESET+Fore.WHITE+f"  Apellido  ,"+Fore.RESET+Fore.RED+f"     Título    ,"+Fore.RESET+Fore.CYAN+f"        Area       ,"+Fore.RESET+Fore.MAGENTA+f"          Editorial         ,"+Fore.RESET+Fore.YELLOW+f"  Pg  )"+Fore.RESET)
    conectar_bd =sql.connect("almacen.db")
    cursor = conectar_bd.cursor()
    instructioncode =f"SELECT codigo FROM libros"
    cursor.execute(instructioncode)
    datos = cursor.fetchall()
    for col in datos:
            i=col[0]
            #este es el campo a mostrar
            cursorn = conectar_bd.cursor()
            instructionnombre =f"SELECT name_autor FROM libros where codigo = '{i}'"
            cursorn.execute(instructionnombre)
            nombrea = cursorn.fetchone()
            cursora = conectar_bd.cursor()
            instructionapellido =f"SELECT apellido_autor FROM libros where codigo='{i}'"
            cursora.execute(instructionapellido)
            apellidoa = cursora.fetchone()
            cursort = conectar_bd.cursor()
            instructiontitulo =f"SELECT titulo FROM libros where codigo='{i}'"
            cursort.execute(instructiontitulo)
            tit = cursort.fetchone()
            cursorar = conectar_bd.cursor()
            instructionarea =f"SELECT area FROM libros where codigo='{i}'"
            cursorar.execute(instructionarea)
            are = cursorar.fetchone()
            cursore = conectar_bd.cursor()
            instructioneditorial =f"SELECT editorial FROM libros where codigo='{i}'"
            cursore.execute(instructioneditorial)
            edi = cursore.fetchone()
            cursorp = conectar_bd.cursor()
            instructionpg =f"SELECT cantidad FROM libros where codigo='{i}'"
            cursorp.execute(instructionpg)
            pg = cursorp.fetchone()           
            print(Fore.GREEN+f"{col}"+Fore.RESET+Fore.BLUE+f"{nombrea}"+Fore.RESET+Fore.WHITE+f"{apellidoa}"+Fore.RESET+Fore.RED+f"{tit}"+Fore.RESET+Fore.CYAN+f"{are}"+Fore.RESET+Fore.MAGENTA+f"{edi}"+Fore.RESET+Fore.YELLOW+f"{pg}"+Fore.RESET)
    conectar_bd.commit()
    conectar_bd.close()
    print("")
    print("***************************************************************************************************")
    print("")

def guardar():
    print("")
    print("***************************************************************************************************")
    print("")
    print("Ingrese el Nombre del autor:")
    name=input()
    print("Ingrese el Apellido del autor:")
    apellido=input()
    print("Ingrese el Título del libro:")
    titulo=input()
    print("Ingrese el Área de Conocimiento:")
    area=input()
    print("Ingrese el Editorial del libro:")
    editorial=input()
    print("Ingrese la Cantidad de páginas que tiene el libro:")
    cantidad=int(input())
    print("")
    print("***************************************************************************************************")
    print("")
    #insertando el registro
    conectar_bd =sql.connect("almacen.db")
    cursor = conectar_bd.cursor()
    instruction =f"INSERT INTO libros VALUES ( NULL,'{name}','{apellido}','{titulo}','{area}','{editorial}',{cantidad})"
    cursor.execute(instruction)
    conectar_bd.commit()
    conectar_bd.close()
    print("")
    print("Se Agrego el nuevo libro")
    print("")
    print("***************************************************************************************************")
    print("")

def borrar():
    print("")
    print("***************************************************************************************************")
    print("")
    print("Ingrese el codigo del libro que quiera Borrar:")
    code=input()
    print("")
    print("***************************************************************************************************")
    print("")
    #ver si es el registro que quiere borrar
    conectar_bd =sql.connect("almacen.db")
    cursor = conectar_bd.cursor()
    instruction =f"SELECT codigo FROM libros where codigo='{code}'"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    print(Fore.GREEN+f"(#,"+Fore.RESET+Fore.BLUE+f"  Nombre  ,"+Fore.RESET+Fore.WHITE+f"  Apellido  ,"+Fore.RESET+Fore.RED+f"     Título    ,"+Fore.RESET+Fore.CYAN+f"        Area       ,"+Fore.RESET+Fore.MAGENTA+f"          Editorial         ,"+Fore.RESET+Fore.YELLOW+f"  Pg  )"+Fore.RESET)
    for col in datos:
            i=col[0]
            #este es el campo a mostrar
            cursorn = conectar_bd.cursor()
            instructionnombre =f"SELECT name_autor FROM libros where codigo = '{i}'"
            cursorn.execute(instructionnombre)
            nombrea = cursorn.fetchone()
            cursora = conectar_bd.cursor()
            instructionapellido =f"SELECT apellido_autor FROM libros where codigo='{i}'"
            cursora.execute(instructionapellido)
            apellidoa = cursora.fetchone()
            cursort = conectar_bd.cursor()
            instructiontitulo =f"SELECT titulo FROM libros where codigo='{i}'"
            cursort.execute(instructiontitulo)
            tit = cursort.fetchone()
            cursorar = conectar_bd.cursor()
            instructionarea =f"SELECT area FROM libros where codigo='{i}'"
            cursorar.execute(instructionarea)
            are = cursorar.fetchone()
            cursore = conectar_bd.cursor()
            instructioneditorial =f"SELECT editorial FROM libros where codigo='{i}'"
            cursore.execute(instructioneditorial)
            edi = cursore.fetchone()
            cursorp = conectar_bd.cursor()
            instructionpg =f"SELECT cantidad FROM libros where codigo='{i}'"
            cursorp.execute(instructionpg)
            pg = cursorp.fetchone()  
            print(Fore.GREEN+f"{col}"+Fore.RESET+Fore.BLUE+f"{nombrea}"+Fore.RESET+Fore.WHITE+f"{apellidoa}"+Fore.RESET+Fore.RED+f"{tit}"+Fore.RESET+Fore.CYAN+f"{are}"+Fore.RESET+Fore.MAGENTA+f"{edi}"+Fore.RESET+Fore.YELLOW+f"{pg}"+Fore.RESET)
    conectar_bd.commit()
    conectar_bd.close()
    #borrar registro
    #delete from usuarios where nombre='Marcelo';
    print("")
    print("Esta seguro de borrar este libro: si/no")
    elec = input()
    match elec:
            case "si":
                conectar_bd =sql.connect("almacen.db")
                cursor = conectar_bd.cursor()
                instruction =f"delete from libros where codigo='{code}'"
                cursor.execute(instruction)
                conectar_bd.commit()
                conectar_bd.close()
                print("Se elimino el libro")
            case "no":
                print("No se eliminara el libro")
            case _:
                print("ingrase la opcion correcta")
    print("")
    print("***************************************************************************************************")
    print("")

def modificar():
    print("")
    print("***************************************************************************************************")
    print("")
    print("Ingrese el codigo del libro que quiera modificar:")
    code=input()
    print("")
    print("***************************************************************************************************")
    print("")
    #ver si es el registro que quiere modificar
    conectar_bd =sql.connect("almacen.db")
    cursor = conectar_bd.cursor()
    instruction =f"SELECT codigo FROM libros where codigo='{code}'"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    print(Fore.GREEN+f"(#,"+Fore.RESET+Fore.BLUE+f"  Nombre  ,"+Fore.RESET+Fore.WHITE+f"  Apellido  ,"+Fore.RESET+Fore.RED+f"     Título    ,"+Fore.RESET+Fore.CYAN+f"        Area       ,"+Fore.RESET+Fore.MAGENTA+f"          Editorial         ,"+Fore.RESET+Fore.YELLOW+f"  Pg  )"+Fore.RESET)
    for col in datos:
            i=col[0]
            #este es el campo a mostrar
            cursorn = conectar_bd.cursor()
            instructionnombre =f"SELECT name_autor FROM libros where codigo = '{i}'"
            cursorn.execute(instructionnombre)
            nombrea = cursorn.fetchone()
            cursora = conectar_bd.cursor()
            instructionapellido =f"SELECT apellido_autor FROM libros where codigo='{i}'"
            cursora.execute(instructionapellido)
            apellidoa = cursora.fetchone()
            cursort = conectar_bd.cursor()
            instructiontitulo =f"SELECT titulo FROM libros where codigo='{i}'"
            cursort.execute(instructiontitulo)
            tit = cursort.fetchone()
            cursorar = conectar_bd.cursor()
            instructionarea =f"SELECT area FROM libros where codigo='{i}'"
            cursorar.execute(instructionarea)
            are = cursorar.fetchone()
            cursore = conectar_bd.cursor()
            instructioneditorial =f"SELECT editorial FROM libros where codigo='{i}'"
            cursore.execute(instructioneditorial)
            edi = cursore.fetchone()
            cursorp = conectar_bd.cursor()
            instructionpg =f"SELECT cantidad FROM libros where codigo='{i}'"
            cursorp.execute(instructionpg)
            pg = cursorp.fetchone()  
            print(Fore.GREEN+f"{col}"+Fore.RESET+Fore.BLUE+f"{nombrea}"+Fore.RESET+Fore.WHITE+f"{apellidoa}"+Fore.RESET+Fore.RED+f"{tit}"+Fore.RESET+Fore.CYAN+f"{are}"+Fore.RESET+Fore.MAGENTA+f"{edi}"+Fore.RESET+Fore.YELLOW+f"{pg}"+Fore.RESET)
    conectar_bd.commit()
    conectar_bd.close()
    #modificar
    #update usuarios set nombre='Marceloduarte', clave='Marce'
    #where nombre='Marcelo';
    print("")
    print("Esta seguro de modificar este libro: si/no")
    elec = input()
    match elec:
            case "si":
                print("")
                print("***************************************************************************************************")
                print("")
                print("Ingrese el nuevo Nombre del autor:")
                name=input()
                print("Ingrese el nuevo Apellido del autor:")
                apellido=input()
                print("Ingrese el nuevo Título del libro:")
                titulo=input()
                print("Ingrese la nueva Área de Conocimiento:")
                area=input()
                print("Ingrese el nuevo Editorial del libro:")
                editorial=input()
                print("Ingrese la nuevo Cantidad de páginas que tiene el libro:")
                cantidad=int(input())
                print("")
                print("***************************************************************************************************")
                print("")
                conectar_bd =sql.connect("almacen.db")
                cursor = conectar_bd.cursor()
                instruction =f"update libros set name_autor = '{name}', apellido_autor = '{apellido}', titulo = '{titulo}', area = '{area}', editorial = '{editorial}', cantidad = {cantidad} where codigo='{code}'"
                cursor.execute(instruction)
                conectar_bd.commit()
                conectar_bd.close()
                print("Se modifico el libro")
            case "no":
                print("No se modificara el libro")
            case _:
                print("ingrase la opcion correcta")
    print("")
    print("***************************************************************************************************")
    print("")

def buscar():
    print("")
    print("***************************************************************************************************")
    print("")
    print("Ingrese el codigo del libro que quiera Buscar:")
    code = input()
    print("")
    print("***************************************************************************************************")
    print("")
    #ver el registro
    conectar_bd =sql.connect("almacen.db")
    cursor = conectar_bd.cursor()
    instruction =f"SELECT codigo FROM libros where codigo='{code}'"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    print(Fore.GREEN+f"(#,"+Fore.RESET+Fore.BLUE+f"  Nombre  ,"+Fore.RESET+Fore.WHITE+f"  Apellido  ,"+Fore.RESET+Fore.RED+f"     Título    ,"+Fore.RESET+Fore.CYAN+f"        Area       ,"+Fore.RESET+Fore.MAGENTA+f"          Editorial         ,"+Fore.RESET+Fore.YELLOW+f"  Pg  )"+Fore.RESET)
    for col in datos:
            i=col[0]
            #este es el campo a mostrar
            cursorn = conectar_bd.cursor()
            instructionnombre =f"SELECT name_autor FROM libros where codigo = '{i}'"
            cursorn.execute(instructionnombre)
            nombrea = cursorn.fetchone()
            cursora = conectar_bd.cursor()
            instructionapellido =f"SELECT apellido_autor FROM libros where codigo='{i}'"
            cursora.execute(instructionapellido)
            apellidoa = cursora.fetchone()
            cursort = conectar_bd.cursor()
            instructiontitulo =f"SELECT titulo FROM libros where codigo='{i}'"
            cursort.execute(instructiontitulo)
            tit = cursort.fetchone()
            cursorar = conectar_bd.cursor()
            instructionarea =f"SELECT area FROM libros where codigo='{i}'"
            cursorar.execute(instructionarea)
            are = cursorar.fetchone()
            cursore = conectar_bd.cursor()
            instructioneditorial =f"SELECT editorial FROM libros where codigo='{i}'"
            cursore.execute(instructioneditorial)
            edi = cursore.fetchone()
            cursorp = conectar_bd.cursor()
            instructionpg =f"SELECT cantidad FROM libros where codigo='{i}'"
            cursorp.execute(instructionpg)
            pg = cursorp.fetchone()  
            print(Fore.GREEN+f"{col}"+Fore.RESET+Fore.BLUE+f"{nombrea}"+Fore.RESET+Fore.WHITE+f"{apellidoa}"+Fore.RESET+Fore.RED+f"{tit}"+Fore.RESET+Fore.CYAN+f"{are}"+Fore.RESET+Fore.MAGENTA+f"{edi}"+Fore.RESET+Fore.YELLOW+f"{pg}"+Fore.RESET)
    conectar_bd.commit()
    conectar_bd.close()
    print("")
    print("***************************************************************************************************")
    print("")

def inicio():
    while True:
        print(Back.LIGHTGREEN_EX+"********************************************BIENVENIDOS********************************************")
        print("")
        print("***************************************************************************************************")
        print("(1) Ver libros ")
        print("(2) Guardar libro nuevo ")
        print("(3) Borrar un libro ")
        print("(4) Modificar un libro ")
        print("(5) Buscar un libro por su codigo")
        print("(6) Salir")
        print("***************************************************************************************************")
        print("")
        print("Ingrse el numero de la opcion a utilizar"+Back.RESET)
        eleccion = input()
        match eleccion:
            case "1":
                ver()
            case "2":
                guardar()
            case "3":
                borrar()
            case "4":
                modificar()
            case "5":
                buscar()
            case "6":
                break
            case _:
                print("ingrase la opcion correcta")