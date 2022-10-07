import pickle

class Vehiculo():
  print("oh soy una clase vehiculo")
  marca=''
  color=''

  def __init__(self,color,tipo):
    self.tipo=tipo
    self.color=color

  def getMarca(self):
    return self.tipo

newVehiculo= Vehiculo('Honda','rojo')


#print(newVehiculo.getMarca())

#Los de abajo creo el binario
#f = open('datos.bin','wb')
#pickle.dump(newVehiculo,f)
#f.close()

f = open('datos.bin','rb')

reloadnewVehiculo = pickle.load(f)

f.close()

print(reloadnewVehiculo.getMarca())
