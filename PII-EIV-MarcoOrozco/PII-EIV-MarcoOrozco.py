global lista
lista = list()

from io import open

archivo_texto=open('archiv.txt','w')

archivo_texto.write('BIENVENIDO AL RESULTADO DEL CONTROL \n')
archivo_texto.close()

file=open('archiv2.txt','w')
file.write('BIENVENIDO AL RESULTADO DE PRODUCTO MÁS COSTOSO Y EL MÁS ECONÓMICO \n')
file.close()


class producto:
    código = ''
    nombre = ''
    descripción = ''
    categoría = ''
    precio = 0
    cantidad = 0

class dolar:
    preciodeldia=200

class importante:
    
    
    maseconomico=0
    totalventa=0
    totalbolivares=0

def dolardeldia():
    
    print('////////////////////////')
    print('1-Precio del dolar del día')
    print('2-Actualizar valor del dolar')
    opc=input('Escoja un opción: ')
    opc=int(opc)
    print('')

    if opc == 1:
        
        print('El precio del dolar actual es de ',dolar.preciodeldia,' Bolivares soberanos')
    else:
        print('Actualice')
        dolar.preciodeldia=input('Ingrese el nuevo valor del dolar en BS')
        print('')
        print('El precio del dolar actualizado al dia es de',dolar.preciodeldia,'Bolivares soberanos')

def registrarproducto():
    print('Registrar nuevo producto')
    print('/////////////////////////')
    print('')
    a=producto()

    a.código=input('Ingrese el código: ')
    a.nombre=input('Ingrese el nombre: ')
    a.descripción =input('Ingrese una breve descripción del producto: ')
    a.categoría = input('Ingrese a que categoría pertenece: ')
    a.precio=input('Ingrese el precio en Dolares Américanos: ')
    a.precio=int(a.precio)
    a.cantidad=input('Ingrese la cantidad que hay: ')
    a.cantidad=int(a.cantidad)

    lista.append(a)

   #append() Este método nos permite agregar nuevos elementos a una lista.


def controldesalida():
    print('Bienvenido al control de salida')
    print('///////////////////////////////')
    
    
    filtro=input('Por favor ingrese el nombre o el código del producto que saldrá:')
      

    for a in lista:
        
        if a.código == filtro or a.nombre == filtro:
            print('Código: ',a.código,'--Nombre:',a.nombre,'-- Categoría: ',a.categoría,'-- Precio: ',a.precio,'$ --')
            print('Hay una cantidad disponible de ',a.cantidad,' Unidades')
            print('')
            print('Descripción del producto:')
            print(a.descripción)
            print('////////////////////////////////')
            print('')
            opc1=input('¿Desea vender el producto? s/n: ')
        
            

            if opc1 == 's':
                vendido=input('Ingrese la cantidad a vender: ')
                vendido=int(vendido)

                if vendido <= a.cantidad:
                    
                    precio1=vendido*a.precio
                    precio1=int(precio1)

                    importante.totalventa=int(importante.totalventa)

                    importante.totalventa=importante.totalventa+precio1

                    


                    
                    
                    a.cantidad=a.cantidad-vendido
                    print('has vendido: ',vendido,' Unidades')
                
                

                    preciot=dolar.preciodeldia*a.precio

                    importante.totalbolivares=importante.totalbolivares+preciot
     

                    
            
                    print('por un precio de ',precio1,' $ y en moneda local ',preciot,' Bolivares soberanos')
                    print('te quedan: ',a.cantidad,' Unidades de ',a.nombre)

                    
            
                

                else:
                    print('No hay suficiente de este producto disponible')
                    print('Hay disponible: ',a.cantidad,' Unidades')

            
                

            else:
                print('Aún quedan: ',a.cantidad,' Unidades de ',a.nombre)
                print('Saldrás al menú')



def Modificar():
    
    print('Modificar información del producto')
    print('//////////////////////////////////')

    filtro=input('Por favor ingrese el nombre o el código del producto que modificará:')

    for a in lista:
        if a.código == filtro or a.nombre == filtro:
            print('Código: ',a.código,'--Nombre: ',a.nombre,'-- Categoría: ',a.categoría,'-- Precio: ',a.precio,'$ --')
            print('')
            print('Ingrese la nueva información del producto')
            a.código=input('Ingrese el código: ')
            a.nombre=input('Ingrese el nombre: ')
            a.descripción =input('Ingrese una breve descripción del producto: ')
            a.categoría = input('Ingrese a que categoría pertenece: ')
            a.precio=input('Ingrese el precio en Dolares Américanos: ')
            a.precio=int(a.precio)
            a.cantidad=input('Ingrese la cantidad que hay: ')
            a.cantidad=int(a.cantidad)
            print('')
            print('Los datos se han actualizado correctamente')
            print('')
            print('Los nuevos datos son: ')
            print('Código: ',a.código,'--',a.nombre,'-- Categoría: ',a.categoría,'-- Precio: ',a.precio,'$ --')
            print('Cantidad: ',a.cantidad)





def consultardatos():
    print('Consultar los datos')
    print('////////////////////////////////////////////')
    print('')

    for a in lista:
        print('Código: ',a.código,'--Nombre: ',a.nombre,'-- Categoría: ',a.categoría,'-- Precio: ',a.precio,'$ --')
        print('Unidades disponibles: ',a.cantidad)
        print('Breve descripción del producto:')
        print(a.descripción)
        print('///////////////////////////////////////////////')
        
    
def totaldeventas():
    print('Total de ventas')
    print('///////////////////////////////////')

    archivo_texto=open('archiv.txt','a')
    
    print('El total de las ventas del día es de: ',importante.totalventa,' $')
    print('y en Bolivares Soberanos son: ',importante.totalbolivares,'BS.S')
    print('')

    archivo_texto.write('\n//////////////Total de ventas actualizadas////////////////////////\n')
    archivo_texto.write('\nEl total actualizado de las ventas  es de\n $ % s'%importante.totalventa)
    archivo_texto.write('\n En moneda local \n BS.s %s'%importante.totalbolivares)
    archivo_texto.write('\n//////////////////////////////////////////////////////////////////\n')

    archivo_texto.close()



def productoagotado():
    print('Productos agotados')
    print('///////////////////////////////////')
    print('')
    

    for a in lista:
        if a.cantidad<=0:
            
            
            print('El producto ',a.nombre,' está agotado')
            print('')
            a.nombre=str(a.nombre)
    
      

            archivo_texto=open('archiv.txt','a')
            archivo_texto.write=('\n \n////////Productos agotados actualizados///////////////////////////\n')
            archivo_texto.write=('\n \n Está agotado el producto \n',a.nombre,' ')
            
            archivo_texto.close()
            



def productocostoso():
    print('Producto más costoso')
    print('///////////////////////////////////')
    print('')
    mayor=0

    for a in lista:
        if a.precio>mayor:
            mayor=a.precio
            x=a.nombre


    print('El producto más costoso es',x,'Con un precio de: ',mayor,' $')
    print('')
    print('////////////////////////////////')

    file=open('archiv2.txt','a')
    file.write=('\n \n////////Productos más costoso actualizado///////////////////////////\n')
    file.write=('El producto más costoso es',x,'Con un precio de:$ % s'%mayor)

    file.close()

    menor=0

    menor=mayor

    for a in lista:
        if menor>a.precio:
            menor=a.precio
        

            print('El producto más económico es',a.nombre,'Con un precio de: ',menor,' $')

            file=open('archiv2.txt','a')
            file.write=('\n \n////////Productos más económico actualizado///////////////////////////\n')
            file.write=('El producto más económico es',a.nombre,'Con un precio de:$ % s '%menor)

            file.close()
            
    



def salir():
    print('Muchas gracias por utilizar el programa vuelva pronto')
    exit


def menu():
    op= 0
    

    while op!= 9:
        #mostrar menu
        print('/////////////////////////////////////////////////////')
        print('//                FLACCO Y ASOCIADOS C.A.          //')
        print('//Control v-1.0//////////////////////////////////////')

        print('Menú')
        print('1-Precio del $ del día')
        print('2-Registro de productos')
        print('3-Control de salida')
        print('4-Modificar')
        print('5-Consultar datos')
        print('6-Ventas')
        print('7-Productos agotados')
        print('8-Producto más costoso y producto más económico')
        print('9-SALIR')
      
        op=input('Digite opción: ')
        op=int(op)
        print('')


        if op==1:
            dolardeldia()
        elif op==2:
            registrarproducto()
        elif op==3:
            controldesalida()
        elif op==4:
            Modificar()
        elif op==5:
            consultardatos()
        elif op==6:
            totaldeventas()
        elif op==7:
            productoagotado()
        elif op== 8:
            productocostoso()
        elif op== 9:
            salir()
        
             #son funciones hay que crear

        print('')

menu()
