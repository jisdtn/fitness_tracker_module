### Один из первых и самых простых проектов - модуль фитнес-трекера.

Программный модуль для фитнес-трекера с использованием парадигмы ООП. Модуль рассчитывает и отображает результаты тренировки.

```commandline
Модуль обрабатывает данные для трёх видов тренировок: бега, спортивной ходьбы и плавания. 
Модуль выполняет следующие функции:
- принимает от блока датчиков информацию о прошедшей тренировке,
- определяет вид тренировки,
- рассчитывает результаты тренировки,
- выводит информационное сообщение о результатах тренировки.
```
### Запуск проекта в dev-режиме:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/jisdtn/fitness_tracker_module
```

```
cd fitness_tracker_module
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

В корневой директории выполнить команду:

```
python3 homework.py
```

