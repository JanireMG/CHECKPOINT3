#EJERCICIO 1
string= "This is the Exercise 1"
number=105
list= ["eggs", "potatoes", "olive oil", "bread"]
boolean= True

#EJERCICIO 2
string= "This is the Exercise 1"
string_letters= string[0:3]
print (string_letters)

#EJERCICIO 3
list= ["eggs", "potatoes", "olive oil", "bread"]
list_first_item= list[0]
print(list_first_item)

#EJERCICIO 4
number=105
number_two= (number+10)
print (number_two)

#EJERCICIO 5
list= ["eggs", "potatoes", "olive oil", "bread"]
list_last_item= list[-1]
print(list_last_item)

#EJERCICIO 6
names= "harry,alex,susie,jared,gail,conner"
list_of_names= names.split(",")  
print (list_of_names)

#EJERCICIO 7
string= "This is the Exercise 1"
first_word= string[0:4].upper()
string_two=(first_word + string[4:])
print(string_two)

#EJERCICIO 8
sentence= "Gracias por su compra, el total de su compra es de {0}€".format(number)
print(sentence)

#EJERCICIO 9
greeting= "hello world"#EX9
print(greeting)

#EJERCICO CADENA HOLA
#INDEX
word= "Hola"
query= word.index("Hola")
print(query)

#FIND
word= "Hola"
query= word.find("Hola")
print(query)

#IN
word= "Hola"
query= "Hola" in word
print(query)


#REPLACE
word= "Hola"
word= word.replace("Hola", "Adios")
print(word)
