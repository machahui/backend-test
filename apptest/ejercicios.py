import requests
import random
import sys
# class Ejecicios():

def ejercicio3():
    listTextPalindromo = []
    text = 'stencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood'
    index = 2
    while index <= len(text):
        textOrigin = text[0:index]
        lenTextAnalize = len(textOrigin)
        indexY = 0
        while lenTextAnalize > 2:
            textAnalize = textOrigin[indexY:]
            textAnalizeInverse = textAnalize[::-1]
            if (textAnalize == textAnalizeInverse):
                listTextPalindromo.append(textAnalize)
            lenTextAnalize -= 1
            indexY += 1

        index += 1
    print(listTextPalindromo)
    return listTextPalindromo

def ejercicio4():
    try:
        url = 'https://schema.getpostman.com/json/collection/v2.1.0/collection.json'
        postResponse = requests.get(url)
        response = postResponse.json()
        print(response)
    except Exception as e:
        print(e)

def recur_fibo(n):
    if n <= 1:
        return n
    return (recur_fibo(n - 1) + recur_fibo(n - 2))

def ejercicio5():
    index = 1
    firsNumberDivisores = False
    while not firsNumberDivisores:
        numberEvaluate = recur_fibo(index)
        lisDivisores = []

        accumulated = 2
        if numberEvaluate % 2 == 0:
            accumulated = 1
        for value in range(1,numberEvaluate+1,accumulated):
            if numberEvaluate % value == 0:
                lisDivisores.append(value)

        if len(lisDivisores) >= 1000:
            break
        index += 1
    response = [lisDivisores,numberEvaluate]
    print(response)
    return response

def ejercicio6():
    rangoN = 20
    listRango = []
    for value in range(1,rangoN+1):
        if value == 1:
            listRango.append({'distancia':100*value,'dias':0})
        elif value in [2,3]:
            listRango.append({'distancia':100*value, 'dias':1})
        else:
            dia = listRango[value-2]['dias'] + listRango[value-3]['dias']
            listRango.append({'distancia':100*value, 'dias': dia})

    lengthDistancia = random.randrange(2000)

    index = 0
    while index <= len(listRango):
        if (lengthDistancia < listRango[index]['distancia'] and index == 0) or (lengthDistancia < listRango[index]['distancia'] and lengthDistancia >= listRango[index-1]['distancia']):
            timeEntrega = listRango[index]['dias']
            break
        index +=1

    response = {'distancia':lengthDistancia,'tiempoEntrega':'{} dias'.format(timeEntrega)}
    print(response)
    return response


def ejercicio7():
    query = """
                update employees a,
                join countries b on a.country_id = b.id
                join continents c on b.continent_id = c.id
                set a.salary = c.anual_adjustment
                where a.salary <= 5000;
    """
    print(query)

if __name__ == '__main__':
    globals()[sys.argv[1]]()