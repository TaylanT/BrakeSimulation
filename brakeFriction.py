#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from scipy import integrate

pi=math.pi

#erste Ideen für Temperaturverteilung in Bremse

#parameter

#drehzahl u/min
n=2000
Pmotor=7.5 #[kW]

#bremszeit [s]
bremszeit=10

#Anpresskraft [N]
#Fn=10000 
#Anpressdruck [Pa]
pAnpress=10e5

#Dimension Scheibe [m] 
rBrake=0.1
bBrake=8e-3

#position klotz
rInnen=50e-3

#Klotz Reibfläche
radKlotz=38e-3
tanKlotz=80e-3
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
	#Auf zwei Seiten der Scheibe in Kontakt
	Fn=2*p*Anpressflaeche
	return Fn*Reibwert

def CrossCheck(Pmotor,Drehzahl,bremszeit):

	Mbr=(Pmotor*20000.0)/Drehzahl
	
	#laut Handbuch Fbr=Mbr/0.5Dsmax
	

	return (Drehzahl*Mbr*bremszeit)/(1.91e4),Mbr



#n=linearAbnahme(2900,10,0)


W=Reibkraft(pAnpress,AKlotz,nu)*friction_length(rInnen+radKlotz/2,n,bremszeit)
m=masse(rInnen,radKlotz,bBrake)
T=W/(m*cScheibe)+StartTemperaturScheibe

Wcross=CrossCheck(Pmotor,n,bremszeit)
print(T,W,Wcross[0]*1e3)
#Vergleich Anpresskräfte
print(2*pAnpress*AKlotz,Wcross[1]/rBrake)








