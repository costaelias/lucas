lista_materiales = [{'material':'hierro 6', 'cantidad':10, 'OC':702, 'producto':'x' },
                    {'material':'hierro 6', 'cantidad':15, 'OC':503, 'producto':'y' },
                    {'material':'hierro 5', 'cantidad':10, 'OC':504, 'producto':'yx'},
                    {'material':'hierro 5', 'cantidad':55, 'OC':505, 'producto':'wz'},
                    {'material':'Madera', 'cantidad':5, 'OC':505, 'producto':'m'},
                    {'material':'Madera 1', 'cantidad':55, 'OC':702, 'producto':'m1'},
                    {'material':'Madera 1', 'cantidad':55, 'OC':703, 'producto':'m2'},
                    {'material':'Madera', 'cantidad':5, 'OC':504, 'producto':'mm'},
                    {'material':'caucho', 'cantidad':5, 'OC':504, 'producto':'c'},
                    {'material':'caucho 2', 'cantidad':5, 'OC':504, 'producto':'cc'}]

lista_materiales_parseada=[]
#Elementos auxiliares para limpiar parsear la lista vieja en una nueva lista con los OC y productos joineados
cantidades = 0
lista_oc = []
lista_prod = []
material_aux = {'material':'', 'cantidad':0, 'OC':lista_oc, 'producto':lista_prod}

for material in lista_materiales:
    '''
        Recorro la lista original de materiales, separandola entre material que quiero meter en la nueva lista
        con los otros materiales
    '''
    list_aux = list(filter(lambda mat: mat['material'] == material['material'],lista_materiales))
    lista_materiales = list(filter(lambda mat: mat['material'] != material['material'],lista_materiales))
    '''
        recorro la lista auxiliar que tiene un unico material para rellenar las listas con los OC y producto.
        una vez que termine de llenar esas listas, lo agrego en material_aux para agregarlo en la lista parseada
    '''
    for elem in list_aux:
        cantidades += elem['cantidad']
        lista_oc.append(elem['OC'])
        lista_prod.append(elem['producto'])
    material_aux = {'material':elem['material'], 'cantidad':cantidades, 'OC':lista_oc, 'producto':lista_prod}
    '''
        aplico este if porque estaba falopa y me agregaba algo asi "material_aux = {'material':'hierro 6', 'cantidad':0, 'OC':[], 'producto':[]}" por cada material,
    '''
    if material_aux['cantidad'] > 0:
        lista_materiales_parseada.append(material_aux)

    '''
        limpio las variables auxiliares para el proximo material
    '''
    cantidades = 0
    lista_oc = []
    lista_prod = []

'''
    este print muestra la nueva lista:
        [{'material': 'hierro 6', 'cantidad': 25, 'OC': [702, 503], 'producto': ['x', 'y']}, 
         {'material': 'hierro 5', 'cantidad': 65, 'OC': [504, 505], 'producto': ['yx', 'wz']}, 
         {'material': 'Madera', 'cantidad': 10, 'OC': [505, 504], 'producto': ['m', 'mm']}, 
         {'material': 'Madera 1', 'cantidad': 110, 'OC': [702, 703], 'producto': ['m1', 'm2']}, 
         {'material': 'caucho', 'cantidad': 5, 'OC': [504], 'producto': ['c']}, 
         {'material': 'caucho 2', 'cantidad': 5, 'OC': [504], 'producto': ['cc']}]
'''
print(lista_materiales_parseada)
