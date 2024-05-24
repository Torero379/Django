from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)

user = """
    Имя: Иван <br>
    Отчество: Петрович<br>
    Фамилия: Иванов<br>
    телефон: 8-923-600-01-02<br>
    email: vasya@mail.ru"""

def about(request):
    return HttpResponse(user)

items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
{"id": 10, "name": "Кепка" ,"quantity":124},]


def item1 (request,item):
    count_1 = 0
    for nec_ in items:
        count_1 += 1
        if nec_.get("id") == item:
            return HttpResponse(f'{nec_.get("name")} &nbsp {nec_.get("quantity")} штук')
        if count_1 > len(items): break
    if item == 10:
        for nec_ in items:
            count_1 += 1      
            if nec_.get("id") == 10:
                return HttpResponse(f'{nec_.get("name")} &nbsp {nec_.get("quantity")} штук')
            if nec_.get("id") != 10:
                return HttpResponse("<h1> Товар c id=10 не найден </h1>")
            if count_1 > len(items): break
        



