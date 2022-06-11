# Тестовое задание БО-ЭНЕРГО

### Стек

**python3.10 + fastapi**  

### Запуск

```
docker-compose up -d --build web
```
localhost:8004/docs  

### Тесты

```
docker-compose exec web sh
pytest asyncio-mode=auto
```

### API

#### /equations/quadratic_equation/

**GET**  
Находит корни квадратного уравнения  
Принимает на вход query параметры:  
a - обязательный  
b, c - необязательные  
В случае передачи a = 0 отдает BadRequest  

#### /colored_items/

**GET**  
Принимает на вход число number от 1 до 100  
В случае передачи number < 1 или number > 100 отдает BadRequest  
Отдает рандомный цвет на основе весов (синий - 60, зеленый - 25, красный - 15)  


