from boletin81 import pasar_a_segundos, calcular_coste, convertir_a_euros

coste=[]
Lllamadas=[]
total=[]
duracion2=[]
contador=0

try:
	with open("comunicaciones.txt","r") as f:

		comu=f.read()
		comu2=comu.split("\n")
		llamadas=len(comu2)

		for linea in comu2:
			if "Tarifa" in linea:
				tarifa=linea.split()
				if tarifa[0] == "Tarifa":
					tarifa=tarifa[1]
			else:
				duracion=linea.split(":")
				if len(duracion) == 3:
					duracion2.append(duracion)

		numero=(int(llamadas)-1) #error bucle por dos for
		
		for i in duracion2:
			if numero == 0:
				print("Error debe existir al menos una llamada.")
			else:
				if numero == 1:
					horas=int(i[0])
					minutos=int(i[1])
					segundos=int(i[2])
					csegundos=pasar_a_segundos(horas,minutos,segundos)
					centimos=calcular_coste(csegundos,tarifa)
					euros=convertir_a_euros(centimos)
					contador=contador+1
					coste.append(contador)
					coste.append(euros)
					Lllamadas.append(coste)
					total.append(euros)
					coste=[]
				else:
					horas=int(i[0])
					minutos=int(i[1])
					segundos=int(i[2])
					csegundos=pasar_a_segundos(horas,minutos,segundos)
					centimos=calcular_coste(csegundos,tarifa)
					euros=convertir_a_euros(centimos)
					contador=contador+1
					coste.append(contador)
					coste.append(euros)
					Lllamadas.append(coste)
					total.append(euros)
					coste=[]

except NameError:
	print("Error al introducir datos.")

except ValueError:
	print("Error al introducir datos.")

for i in range(len(Lllamadas)):
	lista=Lllamadas[i]
	if len(Lllamadas) == 1:
		print("La llamada cuesta: %.2f Euros" % (lista[1]))
	else:
		print("La llamada %d cuesta: %.2f Euros" % (lista[0],lista[1]))

print("Total: %.2f Euros" % (sum(total)))

#3 3 25
#1650.75 Euros
