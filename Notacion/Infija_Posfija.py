# Hacer un programa que convierta una expresion matematica en notación infija a notación posfija 
# y luego evalúe el resultado.

# Convertir expresion infija a posfija
def infija_posfija(expresion):
	operadores = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
	output = []
	pila = []
	num = ''
	
	for char in expresion:
		
        # Manejar números incluyendo decimales
		if char.isdigit() or char == '.':
			num += char
			
		else:
			# Si encontramos un operador, primero añadimos el número anterior
			if num:
				output.append(num)
				num = ''

            # Manejar operadores y parentesis	
			if char in operadores:
				while (pila and pila[-1] != '(' and operadores.get(pila[-1], 0) >= operadores[char]):
					output.append(pila.pop())
					
				pila.append(char)
				
			elif char == '(': 
				pila.append(char)
				
			elif char == ')':
				while pila and pila[-1] != '(': 
					output.append(pila.pop())
					
				pila.pop()  
			
	if num:
		output.append(num)

    # Vaciar la pila y añadir al output	
	while pila:
		output.append(pila.pop())
		
	return output


# Evaluar expresión posfija
def solve_posfija(expresion):
	pila = []
	
    # Recorrer cada dato en la expresión posfija
	for dato in expresion:
		
		# Si es un número, convertir a float y añadir a la pila
		if dato.replace('.', '', 1).isdigit():
			pila.append(float(dato))
			
		else:
			b = pila.pop()
			a = pila.pop()
			
            # Hacer la operación segun el operador
			if dato == '+':
				pila.append(a + b)
				
			elif dato == '-':
				pila.append(a - b)
				
			elif dato == '*':
				pila.append(a * b)
				
			elif dato == '/':
				pila.append(a / b)
				
			elif dato == '^':
				pila.append(a ** b)
				
	return pila[0] # Resultado final


# Uso de ejemplo:
expr = input("Ingrese una expresion matematica en notación infija: ")
posfija = infija_posfija(expr)
resultado = solve_posfija(posfija)
print("Notacion posfija:", ' '.join(posfija))
print("Resultado:", resultado)