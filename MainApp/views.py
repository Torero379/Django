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
{"id": 8, "name": "Кепка" ,"quantity":124},]

def item1 (request,item):
    
    for i in range(10):
        if items[item+1].get("id")==item:
           item2 = [items[item].get("name" ), items[item].get( "quantity")] 
    
    
    
    
    

    
    return HttpResponse(item2)






