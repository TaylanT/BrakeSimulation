import math

pi=math.pi()

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
bBrake=0.05

#position klotz
rInnen=0.1

#Klotz Reibfläche
radKlotz=0.1
tanKlotz=0.1
AKlotz=bKlotz*lKlotz

#Stoffwerte [J/kgK]
cScheibe=500
#cKlotz=

#Reibwert
nu=0.3

#Funktion zur Bestimmen der Ringmasse auf dem der Klotz sitzt
def masse(rInnen,radKlotz,bBrake):
	#dichte 7.2 [g/cm3]
	dichteBrake=1000*7.2
	ARing=pi*((rInnen+radKlotz)**2-rInnen**2)
	VolRing=ARing*bBrake
	m=VolRing*dichteBrake
	return m






