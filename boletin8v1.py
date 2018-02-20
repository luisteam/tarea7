from boletin81 import pasar_a_segundos, calcular_coste, convertir_a_euros

coste=[]
Lllamadas=[]
total=[]

try:

	tarifa=int(input("Tarifa centimos por segundo: "))
	llamadas=input("Numero de llamadas:" )

	for i in range(int(llamadas)):
		if llamadas == "0":
			print("Error debe existir al menos una llamada.")
		else:	
			if llamadas == "1":
				horas=int(input("Horas llamada: "))
				minutos=int(input("Minutos llamada: "))
				segundos=int(input("Segundos llamada: "))
				csegundos=pasar_a_segundos(horas,minutos,segundos)
				centimos=calcular_coste(csegundos,tarifa)
				euros=convertir_a_euros(centimos)
				coste.append(i+1)
				coste.append(euros)
				Lllamadas.append(coste)
				total.append(euros)
				coste=[]
			else:
				horas=int(input("Horas llamada %d: " % (i+1)))
				minutos=int(input("Minutos llamada %d: " % (i+1)))
				segundos=int(input("Segundos llamada %d: " % (i+1)))
				csegundos=pasar_a_segundos(horas,minutos,segundos)
				centimos=calcular_coste(csegundos,tarifa)
				euros=convertir_a_euros(centimos)
				coste.append(i+1)
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
