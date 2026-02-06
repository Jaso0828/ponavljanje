serija = ["OK", "NOK", "OK", "NOK", "NOK"]

def zad01_broj_neispravnih(serija: list) -> list:
    '''
    Tema: proizvodnja
    U listi 'serija' su statusi komada: 'ok' ili 'nok'
    Vrati koliko ima 'NOK'
     '''
    

    
    #STUDENT CODE START
    # return serija.count('NOK')

    counter = 0
    for element in serija:
        if element == 'NOK':
            counter += 1
    return counter



    #STUDENT CODE END

assert zad01_broj_neispravnih(["OK", "NOK", "OK", "NOK", "NOK"]) == 3
assert zad01_broj_neispravnih([]) == 0


minute = 1
for element in zastoj_min:
    if element > minute:
        minute = element
return minute