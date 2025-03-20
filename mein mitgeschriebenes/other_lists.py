# Tupel
mylist = [5,2,1] # listen sind veränderlich
mytupel = (5,2,1) # tupel sind unveränderlich

print (type(mytupel)) # gibt den typ von mytupel aus
print (mytupel)
# mytupel [0] = 10 ist nicht möglich, weil tupel unveränderlich sind

mynewtupel = tuple(mylist) # wandelt die liste in ein tupel um
print (mynewtupel)

# set 
myset = {5,2,1,5,2,1} # set sind veränderlich und enthalten keine doppelten elemente
print (type(myset)) # gibt den typ von myset aus
print (myset)

# dictionary
mydict = {"name": "Max", "alter": 21} # ein dictionary besteht aus key und value
print (type(mydict))
print (mydict)

name = mydict["name"] # gibt den value von dem key "name" aus
print (name)

print (mydict["name"]) # gibt den value von dem key "name" aus
print (mydict["alter"]) # gibt den value von dem key "alter" aus

mydict["name"] = "Moritz" # ändert den value von dem key "name"
print (mydict["name"]) # gibt den value von dem key "name" aus

mydict["geschlecht"] = "männlich" # fügt dem dictionary einen neuen key und value hinzu
print (mydict) # gibt das dictionary aus

mydict.pop("geschlecht") # löscht den key und value von "geschlecht"
print (mydict) # gibt das dictionary aus

mydict_2d = { # ein 2 dimensionales dictionary
    "name" : { 
        "vorname": "Max",
        "nachname": "Mustermann"
    },
    "alter" : {
        "geburtsjahr": 2000,
        "aktuelles_jahr": 2021
    } 
}
print (mydict_2d) # gibt das dictionary aus

print (mydict_2d["name"]["vorname"]) # gibt den value von dem key "vorname" aus dem key "name" aus
print (mydict_2d["alter"]["geburtsjahr"]) # gibt den value von dem key "geburtsjahr" aus dem key "alter" aus

