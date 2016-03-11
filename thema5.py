
key = raw_input("dose imerominia")
date = key.split("/")
print date
dd = date[0]
mm = date[1]
yy = date[2]
day = int(dd)
month = int(mm)
year = int(yy)
kodikos_aiona=[6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2] #edo grafo tous kodikous ton eonon
code1=[0,1,4,4,0,2,5,0,3,6,1,4,6] #edo einai oi kodiki ton minon
imeres = ["savato","kiriaki","deftera","triti","terarti","pemti","paraskeui"] #edo einai oi kodiki ton imeron
y = (year / 100) #ipologizi poios eonas einai
x= (year % 100) # ipologizi ta 2 teleftea psifia tou year
code_aiona = kodikos_aiona[y]
kodikos_xronou = (code_aiona + x + (x / 4))%7 #ipologi ton kodiko xronou
kodikos_mina = code1[month]
meres = (kodikos_xronou + kodikos_mina + day)%7 #ipologizi tin mera
print "h hmera einai", imeres[meres]
raw_input()
#epidi otan prospathisa na to kano me diko mou algorithmo den doulepse vrika apo ton internet auton ton algoritmo kai ton ilopiisa se python http://theorhma.blogspot.gr/2011/04/blog-post.html
