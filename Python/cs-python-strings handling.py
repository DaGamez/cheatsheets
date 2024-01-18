sample_string="Hello World"


sample_string[1] #strings are arrays

#loop through letters in string
for x in sample_string:
  print(x)
  
print(len(sample_string)) #length of a string

print("Hello" in sample_string) #check substring is in string

print("Hello" not in sample_string) #check substring is not in string

#Get the characters from position 2 to position 5 (not included)
print(sample_string[2:5]) 

#Get the characters from the start to position 5 (not included)
print(sample_string[:5]) 

#Get the characters from position 2, and all the way to the end:
print(sample_string[2:])


print(sample_string[-5:-2])

print(sample_string.upper()) #poner todo en mayusculas

print(sample_string.lower()) #poner todo en minusculas

print(sample_string.strip()) #quitar espacios en blanco al inicio o final

print(sample_string.replace("H", "J")) #reemplaza

print(sample_string.split(" ")) #parte el string por el substring

print("Hello " + "World") #concatenate string

#combinar strings y numeros usando format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#un ejemplo mas complejo de format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#se pueden usar numeros como indices de los argumentos en format
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



#f strings
key = 'my_var'
value = 1.234
formatted = f'{key} = {value}'
print(formatted)

formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)


#Escape characters
print("\'") #prints '
print("\\") #prints \
print("\n") #prints new line
print("\r") #prints carriage return
print("\t") #prints tab
print("\b") #prints backspace
print("\f") #prints form feed
print("\ooo") #prints octal value
print("\x48") #prints hexal value

sample_string="hello World"
print(sample_string.capitalize()) #capitalice first word

sample_string="HELLO World"
print(sample_string.casefold()) #lower case, more robust than lower() method

print(sample_string.center(20)) #string de longitud 20 con el string de ref en centro

sample_string="hello World"
print(sample_string.count("l")) #cuenta las ocurrencias del substring

sample_string="Hélloú Mundö"
print(sample_string.encode()) #version codificada del string, tip UTF-8

sample_string="hello World"
print(sample_string.endswith("World"))  #verifica si el string termina con

sample_string = "H\te\tl\tl\to"
sample_string=sample_string.expandtabs(5) #expande los tabs en el string con el esp ind
print(sample_string)

sample_string="hello World"
print(sample_string.find("World")) #devuelve la posicion del substring, no encuentra arroja -1
print(sample_string.index("World")) #devuelve la posicion del substring, no encuentra arroja error

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49)) #formato de numero en string


print(sample_string.isalpha()) #all characters are in the alphabet
print("123123".isdecimal())
print("123123".isdigit())
print("Demo0_10".isidentifier()) #string es un identificador de python valido

print(sample_string.islower()) #revisa si todos los caracteres son lower

print("21323".isnumeric()) #revisa si todos los caracteres son numericos

print("Hello".isprintable()) #True si todos son imprimibles, \n no es impr

print("    ".isspace()) #true si todos los caracteres son espacios

print("Hello Word".istitle()) # true si es titulo

print("Hello Word".isupper()) # true si todos los caracteres son Mayus

print("".join(["Hello ","World"])) #une string con iterable


print("Hello ".ljust(20,"-")) #justificar a la izquierda con llenado de -

print("HELLO".lower()) #pasar a minuscula

print("      HELLO".lstrip()) #strip por la izquierda

#hacer tablas de traducciones
mytable = str.maketrans("S", "P")
txt = "Hello Sam!"
print(txt.translate(mytable))


print("I could eat bananas all day".partition("bananas")) #parte en tres 
print("I could eat bananas all day".rpartition("bananas")) #parte en tres buscando por derecha


print("Hello World".replace("H", "P")) #reemplazar

print("llo".rfind("l")) #indice del ultimo lugar del substring
print("llo".rindex("l")) #indice del ultimo lugar del substring

print("Hello World Again!".rsplit(" ")) #parte el string por el substring


print("Hello   ".rstrip()) #strip por la derecha

print("Thank you \n again".splitlines()) #parte string a vector por lineas

print("Hello Worlds".startswith("Hello")) #true si comienza por 

print("  Hello Worlds".strip()) #quita espacios en blanco al inicio

print("Hello Worlds".swapcase()) #intercambia mayus y minus

print("hello word".title()) #convierte la primera letra cada palab a mayus

print("hello word".zfill(20)) #pone 0s al inicio


