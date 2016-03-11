import urllib2
read=raw_input("dose sintetagmenes (x,y)")
pin = read.split(",")
x= pin[0]
y= pin[1]
k = "http://api.openweathermap.org/data/2.5/weather?lat="+x+"&lon="+y+"&appid=44db6a862fba0b067b1930da0d769e98"
url=k
request = urllib2.Request(url)
handle= urllib2.urlopen(request)
kimeno = handle.read()
firstsplit=kimeno.split("weather") #kanw ena split oles tis plirofories pou perno apo to openweathermap se 2 komatia
secondsplit1=firstsplit[1].split('stations","main"')
secondsplit=firstsplit[1].split("main") # 3ana kanw pali split
z=secondsplit[1].split(":")
w=secondsplit1[1].split(":")
finalsplit1=z[1].split(",") #auti periexi to an vrexi i oxi
finalsplit2=w[2].split(",") # auti periexi tin thrmokrasia
print finalsplit1[0],finalsplit2[0]
R = finalsplit1[0]#periexi to an vrexi i oxi
C = float(finalsplit2[0]) # periexi tin thermokrasia

C-=273 #metatrepo kelvin se kelsiou
if R=='"Rain"'or R=='"rain"':
    print "im singing in the rain"
elif C > 20 :
    print "nice!!"
elif C <5 :
    print "mprrrr!"
else:
    print"paleuete"
raw_input()
