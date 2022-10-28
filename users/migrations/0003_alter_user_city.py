# Generated by Django 4.0.3 on 2022-10-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, choices=[('Москва', 'Москва'), ('Абрамцево', 'Абрамцево'), ('Алабино', 'Алабино'), ('Апрелевка', 'Апрелевка'), ('Архангельское', 'Архангельское'), ('Ашитково', 'Ашитково'), ('Байконур', 'Байконур'), ('Бакшеево', 'Бакшеево'), ('Балашиха', 'Балашиха'), ('Барыбино', 'Барыбино'), ('Белоомут', 'Белоомут'), ('Белые Столбы', 'Белые Столбы'), ('Бородино', 'Бородино'), ('Бронницы', 'Бронницы'), ('Быково', 'Быково'), ('Валуево', 'Валуево'), ('Вербилки', 'Вербилки'), ('Верея', 'Верея'), ('Видное', 'Видное'), ('Внуково', 'Внуково'), ('Вождь Пролетариата', 'Вождь Пролетариата'), ('Волоколамск', 'Волоколамск'), ('Вороново', 'Вороново'), ('Воскресенск', 'Воскресенск'), ('Восточный', 'Восточный'), ('Востряково', 'Востряково'), ('Высоковск', 'Высоковск'), ('Голицино', 'Голицино'), ('Деденево', 'Деденево'), ('Дедовск', 'Дедовск'), ('Джержинский', 'Джержинский'), ('Дмитров', 'Дмитров'), ('Долгопрудный', 'Долгопрудный'), ('Домодедово', 'Домодедово'), ('Дорохово', 'Дорохово'), ('Дрезна', 'Дрезна'), ('Дубки', 'Дубки'), ('Дубна', 'Дубна'), ('Егорьевск', 'Егорьевск'), ('Железнодорожный', 'Железнодорожный'), ('Жилево', 'Жилево'), ('Жуковский', 'Жуковский'), ('Загорск', 'Загорск'), ('Загорянский', 'Загорянский'), ('Запрудная', 'Запрудная'), ('Зарайск', 'Зарайск'), ('Звенигород', 'Звенигород'), ('Зеленоград', 'Зеленоград'), ('Ивантеевка', 'Ивантеевка'), ('Икша', 'Икша'), ('Ильинский', 'Ильинский'), ('Истра', 'Истра'), ('Калининград', 'Калининград'), ('Кашира', 'Кашира'), ('Керва', 'Керва'), ('Климовск', 'Климовск'), ('Клин', 'Клин'), ('Клязьма', 'Клязьма'), ('Кожино', 'Кожино'), ('Кокошкино', 'Кокошкино'), ('Коломна', 'Коломна'), ('Колюбакино', 'Колюбакино'), ('Королев', 'Королев'), ('Косино', 'Косино'), ('Котельники', 'Котельники'), ('Красково', 'Красково'), ('Красноармейск', 'Красноармейск'), ('Красногорск', 'Красногорск'), ('Краснозаводск', 'Краснозаводск'), ('Краснознаменск', 'Краснознаменск'), ('Красный Ткач', 'Красный Ткач'), ('Крюково', 'Крюково'), ('Кубинка', 'Кубинка'), ('Купавна', 'Купавна'), ('Куровское', 'Куровское'), ('Лесной Городок', 'Лесной Городок'), ('Ликино-Дулево', 'Ликино-Дулево'), ('Лобня', 'Лобня'), ('Лопатинский', 'Лопатинский'), ('Лосино-Петровский', 'Лосино-Петровский'), ('Лотошино', 'Лотошино'), ('Лукино', 'Лукино'), ('Луховицы', 'Луховицы'), ('Лыткарино', 'Лыткарино'), ('Львовский', 'Львовский'), ('Люберцы', 'Люберцы'), ('Малаховка', 'Малаховка'), ('Михайловское', 'Михайловское'), ('Михнево', 'Михнево'), ('Можайск', 'Можайск'), ('Монино', 'Монино'), ('Муханово', 'Муханово'), ('Мытищи', 'Мытищи'), ('Нарофоминск', 'Нарофоминск'), ('Нахабино', 'Нахабино'), ('Некрасовка', 'Некрасовка'), ('Немчиновка', 'Немчиновка'), ('Новобратцевский', 'Новобратцевский'), ('Новоподрезково', 'Новоподрезково'), ('Ногинск', 'Ногинск'), ('Обухово', 'Обухово'), ('Одинцово', 'Одинцово'), ('Ожерелье', 'Ожерелье'), ('Озеры', 'Озеры'), ('Октябрьский', 'Октябрьский'), ('Опалиха', 'Опалиха'), ('Орехово-Зуево', 'Орехово-Зуево'), ('Павловский Посад', 'Павловский Посад'), ('Первомайский', 'Первомайский'), ('Пески', 'Пески'), ('Пироговский', 'Пироговский'), ('Подольск', 'Подольск'), ('Полушкино', 'Полушкино'), ('Правдинский', 'Правдинский'), ('Привокзальный', 'Привокзальный'), ('Пролетарский', 'Пролетарский'), ('Протвино', 'Протвино'), ('Пушкино', 'Пушкино'), ('Пущино', 'Пущино'), ('Радовицкий', 'Радовицкий'), ('Раменское', 'Раменское'), ('Реутов', 'Реутов'), ('Решетниково', 'Решетниково'), ('Родники', 'Родники'), ('Рошаль', 'Рошаль'), ('Рублево', 'Рублево'), ('Руза', 'Руза'), ('Салтыковка', 'Салтыковка'), ('Северный', 'Северный'), ('Сергиев Посад', 'Сергиев Посад'), ('Серебряные Пруды', 'Серебряные Пруды'), ('Серпухов', 'Серпухов'), ('Солнечногорск', 'Солнечногорск'), ('Солнцево', 'Солнцево'), ('Софрино', 'Софрино'), ('Старая Купавна', 'Старая Купавна'), ('Старбеево', 'Старбеево'), ('Ступино', 'Ступино'), ('Сходня', 'Сходня'), ('Талдом', 'Талдом'), ('Текстильщик', 'Текстильщик'), ('Темпы', 'Темпы'), ('Тишково', 'Тишково'), ('Томилино', 'Томилино'), ('Троицк', 'Троицк'), ('Туголесский Бор', 'Туголесский Бор'), ('Тучково', 'Тучково'), ('Уваровка', 'Уваровка'), ('Удельная', 'Удельная'), ('Успенское', 'Успенское'), ('Фирсановка', 'Фирсановка'), ('Фосфоритный', 'Фосфоритный'), ('Фрязино', 'Фрязино'), ('Фряново', 'Фряново'), ('Химки', 'Химки'), ('Хорлово', 'Хорлово'), ('Хотьково', 'Хотьково'), ('Черкизово', 'Черкизово'), ('Черноголовка', 'Черноголовка'), ('Черусти', 'Черусти'), ('Чехов', 'Чехов'), ('Шарапово', 'Шарапово'), ('Шатура', 'Шатура'), ('Шатурторф', 'Шатурторф'), ('Шаховская', 'Шаховская'), ('Шереметьевский', 'Шереметьевский'), ('Щелково', 'Щелково'), ('Щербинка', 'Щербинка'), ('Электрогорск', 'Электрогорск'), ('Электросталь', 'Электросталь'), ('Электроугли', 'Электроугли'), ('Яхрома', 'Яхрома')], default='', max_length=50, null=True),
        ),
    ]