#pasar_a_segundos

def pasar_a_segundos(horas,minutos,segundos):
	#horas=0
	#minutos=0
	#segundos=0

	#tiempo=cadena.split(":")
	#horas=int(tiempo[0])
	#minutos=int(tiempo[1])
	#segundos=int(tiempo[2])

	resultado=(((horas*60)+minutos)*60)+segundos

	return(resultado)




#calcular_coste

def calcular_coste(segundos,tarifa):
	coste=(segundos*int(tarifa))

	return(coste)




#convertir_a_euros

def convertir_a_euros(centimos):
	euros=centimos/100

	return(euros)
