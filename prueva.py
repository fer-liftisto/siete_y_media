##  https: // tutz.tv/python/copiar-lista ##
def cambiar(lis):
    print('1',lis)
    li_nu = lis.copy()
    li_nu.append('fer')
    print('2',lis)

lista = [(4,'r'),(5,'d')]
cambiar(lista)
print(lista)

li_nu = lista.copy()
cambiar(li_nu)
print(lista)

lista.remove((4,'r'))
#print(lista)