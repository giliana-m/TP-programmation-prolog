def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(fibonacci(10))


def is_palindrome(s):
    return s == s[::-1]

#print(is_palindrome("radar"))
print(is_palindrome("hello"))


def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_of_digits(12345))
print(sum_of_digits(9876))



name="frerooooo"
inverse_name=""
for i in range(len(name)-1, -1, -1):
    #print(i,name[i])
    inverse_name += name[i]

#print(name)
#print(inverse_name)   
#print(8, len(name)-1)




def is_palindrome(n):
    ''' 
1- ecrire dans l'ordre
2- ecrire dans le sens inverse
3- parcourir une chaine de caracteres
4- le mot ecrit dans le 
    '''
#mame = str(input(" Le mot ? "))
#for i in range(len(mame)-1, -1, -1):
    #print(i, mame[i])
#   mame += mame[i]

#print(mame  + "\n")
#print(len(mame)-1)





ma_variable = str(12)
ma_string = "hello"
mon_float = 4.5
print(str(ma_variable)+str(3)+str(mon_float))


age = int(input(" Tu as quel âge ?"))
print(age, type(age))


#Conversion Celsius en Fahrenheit
Celsius_fahrenheit = float(input("degré ? "))
Celsius_fahrenheit = Celsius_fahrenheit *9/5+ 32
print(Celsius_fahrenheit)



#mot de passe
mot_de_passe = input("Quel est votre mot de passe ?")

if mot_de_passe == '123456':
    print(" Valide")
else:
    print("Invalide")

print("fin du programme")


#palindrome fonctionne
mot = str (input("quel mot ? "))
inverse = ""
for i in range (len(mot)-1, -1, -1):
    inverse += mot[i]
if mot == inverse:
    print ("ok")
else:
    print("not ok")

#palindrome fonctionne
mot = str (input("quel mot ? "))
inverse = ""
for i in range (len(mot)-1, -1, -1):
    inverse =  inverse + mot[i]
if mot == inverse:
    print ("ok")
else:
    print("not ok")


#exo mention jury
note = float(input ("Veuillez saisir la note : "))

if note > 20:
    print(note, " : invalide ! ")
    note = float(input("veuillez ressaisir une note : "))
if note >= 12 and note <= 13 :
    print(note, ": Bravo ! Mention Assez bien")
elif note >= 14 and note <= 15 :
    print(note, ": Bravo ! Mention Bien")
elif note >= 16 and note <= 17 :
    print(note, ": Bravo ! Mention Très Bien")
elif note >= 18 and note <=20 :
    print(note, ": Bravo ! Félicitations du jury")
elif note >=10 and note <=11 :
    print(note, ": Admis.")


