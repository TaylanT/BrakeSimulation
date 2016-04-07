#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from scipy import integrate

pi=math.pi

#erste Ideen für Temperaturverteilung in Bremse

#parameter

#drehzahl u/min
n=2000

#bremszeit [s]
bremszeit=5

#Anpresskraft [N]
#Fn=10000 
#Anpressdruck [Pa]
pAnpress=10e5

#Dimension Scheibe [m] 
rBrake=0.3
bBrake=0.02

#position klotz
rInnen=0.1

#Klotz Reibfläche
radKlotz=0.1
tanKlotz=0.1
AKlotz=radKlotz*tanKlotz

#Stoffwerte [J/kgK]
cScheibe=500
#cKlotz=

#Reibwert
nu=0.3

StartTemperaturScheibe=20

#Funktion zur Bestimmen der Ringmasse auf dem der Klotz sitzt
def masse(rInnen,radKlotz,bBrake):
	#dichte 7.2 [g/cm3]
	dichteBrake=1000*7.2
	#Fläche Kreisring
	ARing=pi*((rInnen+radKlotz)**2-rInnen**2)
	#Volumen Kreisring
	VolRing=ARing*bBrake
	mRing=VolRing*dichteBrake
	return mRing

#Ansatz über geleistete Arbeit W=Fr*s = mcdT
def friction_length(rMittelpunkt,Drehzahl,bremszeit):
	#Ansatz über Kreisumfang und Anzahl der Umdrehungen innerhalb der Bremszeit
	Umfang=2*pi*rMittelpunkt
	#umrechung in U/s
	b=Drehzahl/60.0

	#linear Abhängigkeit Drehzahl
	m=-b/bremszeit
	y=lambda x:m*x+b
	u=integrate.quad(y,0,bremszeit)
	s=Umfang*u[0]
	
	return s

def Reibkraft(p,Anpressflaeche,Reibwert):
	Fn=p*Anpressflaeche
	return Fn*Reibwert


#n=linearAbnahme(2900,10,0)


W=Reibkraft(pAnpress,AKlotz,nu)*friction_length(rInnen+radKlotz/2,n,5)
m=masse(rInnen,radKlotz,bBrake)
T=W/(m*cScheibe)+StartTemperaturScheibe
print(T)








