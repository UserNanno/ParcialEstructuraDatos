class EvaluadorExpresion:
    def __init__(self, expresion):
        self.expresion = expresion

    def es_operador(self, char):
        return char in "+-*/^"

    def precedencia(self, operador):
        if operador in ('+', '-'):
            return 1
        if operador in ('*', '/'):
            return 2
        if operador == '^':
            return 3
        return 0

    def infija_a_prefija(self):
        salida = []
        pila = []
        for char in reversed(self.expresion):
            if char.isalnum():  # Operand
                salida.append(char)
            elif char == ')':
                pila.append(char)
            elif char == '(':
                while pila and pila[-1] != ')':
                    salida.append(pila.pop())
                if not pila:
                    raise ValueError("Error en la expresión: paréntesis no balanceados")
                pila.pop()  # Desapilar el '('
            elif self.es_operador(char):
                while pila and pila[-1] != ')' and self.precedencia(pila[-1]) >= self.precedencia(char):
                    salida.append(pila.pop())
                pila.append(char)
        
        while pila:
            salida.append(pila.pop())

        return ''.join(reversed(salida))

    def evaluar_prefija(self, expresion):
        pila = []
        for char in reversed(expresion):
            if char.isalnum():
                pila.append(int(char))
            elif self.es_operador(char):
                if len(pila) < 2:
                    raise ValueError("Error en la expresión: operadores insuficientes")
                operando1 = pila.pop()
                operando2 = pila.pop()
                if char == '+':
                    pila.append(operando1 + operando2)
                elif char == '-':
                    pila.append(operando1 - operando2)
                elif char == '*':
                    pila.append(operando1 * operando2)
                elif char == '/':
                    if operando2 == 0:
                        raise ValueError("Error en la expresión: división por cero")
                    pila.append(operando1 / operando2)
                elif char == '^':
                    if operando1 == 0 and operando2 < 0:
                        raise ValueError("Error en la expresión: potenciación de 0^negativo")
                    pila.append(operando1 ** operando2)
        if len(pila) != 1:
            raise ValueError("Error en la expresión: operandos sobrantes")
        return pila[0]

    def evaluar(self):
        self.mostrar_prefija()
        expresion_prefija = self.infija_a_prefija()
        try:
            resultado = self.evaluar_prefija(expresion_prefija)
            return resultado
        except ValueError as error:
            return str(error)

    def mostrar_prefija(self):
        expresion_prefija = self.infija_a_prefija()
        print("Expresión en notación prefija:", expresion_prefija)

if __name__ == "__main__":
    expresion_infija = input("Ingrese una expresión algebraica infija: ")
    evaluador = EvaluadorExpresion(expresion_infija)
    resultado = evaluador.evaluar()
    print("Resultado de la expresión:", resultado)
