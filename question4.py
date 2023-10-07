import queue

class Heapsort:
    def __init__(self):
        self.heap = queue.PriorityQueue()
    
    def ordenar(self, arr):
        for elemento in arr:
            self.heap.put(elemento)
        
        lista_ordenada = []
        while not self.heap.empty():
            lista_ordenada.append(self.heap.get())
        
        return lista_ordenada

if __name__ == "__main__":
    heapsort = Heapsort()
    entrada = input("Ingrese una lista de números separados por espacios: ")
    numeros = [int(x) for x in entrada.split()]
    lista_ordenada = heapsort.ordenar(numeros)
    print("Lista ordenada:", lista_ordenada)
