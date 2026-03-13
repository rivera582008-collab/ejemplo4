Algoritmo Calculadora
	Definir sumando1, sumando2, resultado, edad, respuesta Como Real
	
	Escribir "escriba su fecha de nacimiento"
	Leer respuesta
	edad = 2026 - respuesta
	Escribir "usted tiene:", edad, ":Años"
	si edad >= 16
		Escribir "Seleccione El Número De La Operacón A Realizar 1- Suma 2- Resta 3- Multipicación 4- División 5- Elevar al cuadrado 6- Elevar al cubo" 
		Leer numero
		
		si numero = 1
			Escribir "Escriba un numero para realizar la suma"
			Leer numero1
			Escribir " Escriba un segundo numero para realizar la suma"
			Leer numero2
			resultado = numero1 + numero2	
			Escribir "El resultado de la suma es:", resultado
		FinSi
		
		si numero = 2
			
			Escribir "Escriba un numero para realizar la resta"
			Leer numero1
			Escribir " Escriba un segundo numero para realizar la resta"
			Leer numero2
			resultado = numero1 - numero2	
			Escribir "El resultado de la resta es:", resultado
			
		FinSi
		
		si numero = 3
			
			Escribir "Escriba un numero para realizar la multiplicación"
			Leer numero1
			Escribir " Escriba un segundo numero para realizar la multiplicación"
			Leer numero2
			resultado = numero1 * numero2	
			Escribir "El resultado de la multiplicación es:", resultado
			
		FinSi
		
		si numero = 4
			
			Escribir "Escriba un numero para realizar la división"
			Leer numero1
			Escribir " Escriba un segundo numero para realizar la división"
			Leer numero2
			Escribir "Quiere saber cuanto es el sobrante de su división si o no"
			Leer respuesta1
			
			si respuesta1 es "si"
				
				resultado = numero1 / numero2
				Escribir "El resultado de la división es:", resultado
				resultado2 = numero1 mod numero2
				Escribir "lo sobrante de la división es:" resultado2
				
			SiNo
				resultado = numero1 / numero2	
				Escribir "El resultado de la división es:", resultado	
				
				
				
			FinSi
		FinSi
		
		si numero = 5 
			
			Escribir "Escriba un numero para elevar al cuadrado"
			Leer numero1
			resultado = numero1 ^ 2	
			Escribir "El resultado es:", resultado
		FinSi
		
		si numero = 6
			
			Escribir "Escriba un numero para elevar al cubo"
			Leer numero1
			resultado = numero1 ^ 3	
			Escribir "El resultado es:", resultado
		FinSi
	SiNo
		Escribir "por lo tanto usted no cuenta con suficiente edad para realizar la operación"
		
	FinSi
	
	
	Escribir " numero de dui"
	Leer  numero
	
	Mientras numerodui <> "078338859"
		Escribir "romper bucle infinito 1 si 2 no "
		Leer respuesta1
		si respuesta1 = "no"
		FinSi
		
		si respuesta1 = "si"
			numerodui = "078338859"
		FinSi
	FinMientras
	
	Escribir "final"

FinAlgoritmo