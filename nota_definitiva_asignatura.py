#programa para saber las definitavas de una asignatura

#input

nc = int(input ("digite el valor de nc: " ))
np = int(input ("digite el valor de np: " ))
na = int(input ("digite el valor de na: " ))
au = int(input ("digite el valor de au: " ))
bi = int(input ("digite el valor de bi: " ))

#processig
nd = (0.3*nc) + (0.3*np) + (0.1*na) + (0.1*au) + (0.2*bi)

#output
print("la nota definitiva es de: " + str(nd))