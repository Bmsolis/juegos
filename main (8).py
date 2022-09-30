#    Solución 1
print("Los aminoácidos esenciales son aquellos que el propio organismo no puede sintetizar por sí mismo.\n")
aminoacidos=["FENILALANINA","FENILALANINA","LEUCINA","LEUCINA","LEUCINA","LEUCINA","LEUCINA","LEUCINA","ISOLEUCINA","ISOLEUCINA","ISOLEUCINA","METIONINA","VALINA","VALINA","VALINA","VALINA","TREONINA","TREONINA","TREONINA","TREONINA","HISTIDINA","HISTIDINA","LISINA","LISINA","stop.","stop.","stop."]
codones=["UUU","UUC","UUA","UUG","CUU","CUC","CUA","CUG","AUU","AUC","AUA","AUG","GUU","GUC","GUA","GUG","ACU","ACC","ACA","ACG","CAU","CAC","AAA","AAG","UGA","UAA","UAG"]

usuario=input("Ingrese la cadena que desea conocer: ")
condicion1= (usuario[:3].startswith("5'-") and usuario[-3:].endswith("-3'")) or (usuario[:3].startswith("3'-") and usuario[-3:].endswith("-5'"))
condicion2= usuario[3:-3].isalpha() and usuario[3:-3].isupper()
condicion3= "AUG" in usuario
condicion4= ( "UGA" in usuario) or ("UAA" in usuario) or ("UAG" in usuario)
cadena=usuario[3:-3]
condicion5= ("A" in cadena )and ("U" in cadena) and ("G" in cadena) and ("C" in cadena)
condiciones= condicion1 and condicion2 and condicion3 and condicion4 and condicion5
while not condiciones:
  print("No se encuentra la información de ese aminoacido")
  usuario=input("Ingrese la cadena que desea conocer: ")
  condicion1= (usuario[:3].startswith("5'-") and usuario[-3:].endswith("-3'")) or (usuario[:3].startswith("3'-") and usuario[-3:].endswith("-5'"))
  condicion2= usuario[3:-3].isalpha() and usuario[3:-3].isupper()
  condicion3= "AUG" in usuario
  condicion4= ( "UGA" in usuario) or ("UAA" in usuario) or ("UAG" in usuario)
  cadena=usuario[3:-3]
  condicion5= ("A" in cadena )and ("U" in cadena) and ("G" in cadena) and ("C" in cadena)
  condiciones= condicion1 and condicion2 and condicion3 and condicion4 and condicion5

numero1,cadena,numero2 = usuario.split("-")
i = cadena.index("AUG")
resultante = cadena[i:] 
tamanio = len(resultante)
recorrido = 0 
nuevoInicio=0 
Lamino = []
bandera=True
while(recorrido<=tamanio) and bandera==True:
  codon = resultante[nuevoInicio:recorrido+3]
  recorrido+=3 
  nuevoInicio=recorrido
  indice=codones.index(codon)
  aminoacido = aminoacidos[indice]
  Lamino.append(aminoacido)
  if aminoacidos[indice] =="stop.":
    bandera= False       
resultado=",".join(Lamino)     
print("Los aminoacidos esenciales de la cadena son: {}".format(resultado)) 

#5'-CUUCAUAUGCAUAAGAUUCACUAGCGCGCG-3'


#    Solución 2 

'''usuario=input("Ingrese la cadena que desea conocer: ")
condicion1= (usuario[:3].startswith("5'-") and usuario[-3:].endswith("-3'")) or (usuario[:3].startswith("3'-") and usuario[-3:].endswith("-5'"))
condicion2= usuario[3:-3].isalpha() and usuario[3:-3].isupper()
condicion3= "AUG" in usuario
condicion4= ( "UGA" in usuario) or ("UAA" in usuario) or ("UAG" in usuario)
cadena=usuario[3:-3]
condicion5= ("A" in cadena )and ("U" in cadena) and ("G" in cadena) and ("C" in cadena)
condiciones= condicion1 and condicion2 and condicion3 and condicion4 and condicion5
while not condiciones:
  print("No se encuentra la información de ese aminoacido")
  usuario=input("Ingrese la cadena que desea conocer: ")
  condicion1= (usuario[:3].startswith("5'-") and usuario[-3:].endswith("-3'")) or (usuario[:3].startswith("3'-") and usuario[-3:].endswith("-5'"))
  condicion2= usuario[3:-3].isalpha() and usuario[3:-3].isupper()
  condicion3= "AUG" in usuario
  condicion4= ( "UGA" in usuario) or ("UAA" in usuario) or ("UAG" in usuario)
  cadena=usuario[3:-3]
  condicion5= ("A" in cadena )and ("U" in cadena) and ("G" in cadena) and ("C" in cadena)
  condiciones= condicion1 and condicion2 and condicion3 and condicion4 and condicion5

indiceInicio=cadena.index("AUG") 
resultante = cadena[indiceInicio:] 
L=[]
bandera=True
while bandera:
  indiceFin=indiceInicio+3  
  elemento=cadena[indiceInicio:indiceFin] 
  indice=codones.index(elemento)
  L.append(aminoacidos[indice])
  indiceFin+=3
  indiceInicio+=3
  if aminoacidos[indice] =="stop.":
    bandera= False   
resultado=",".join(L)    
print("Los aminoacidos esenciales de la cadena son: {}".format(resultado))'''
