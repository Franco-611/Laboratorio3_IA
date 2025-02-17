from reader import Reader 
from modelo import Modelo

reader = Reader('./entrenamiento.txt')
modelo = Modelo(reader.training)


for key in reader.testing:
    for frase in reader.testing[key]:
        print(frase + ' ' + key)
        prueba = Modelo.naiveBayes(modelo, frase)
        print(prueba)
        input()
    
