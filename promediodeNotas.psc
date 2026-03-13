Algoritmo promediodeNotas
	 
		Definir notas Como Real
		Dimension notas[5]
		Definir i Como Entero
		Definir suma, promedio Como Real
		
		
		suma <- 0
		Para i <- 1 Hasta 5 Hacer
			Escribir "Ingrese nota ", i
			Leer notas[i]
			suma <- suma + notas[i]
		FinPara
		
		
		promedio <- suma / 5
		Escribir "Promedio: ", promedio
		
		
		Si promedio > 6 Entonces
			Escribir "Aprobado"
		SiNo
			Escribir "Reprobado"
		finsi
FinAlgoritmo
