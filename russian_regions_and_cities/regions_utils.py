from .sources.russia_cities_dict import russia_cities_dict
from .sources.russia_regions_dict import russia_reg_dict
from django.db.models import Model


def gen_regions_list() -> list:
    """
    Функция генерирует список с названием регионов в формате [(),]
    """
    regions_list = []

    for dict in russia_reg_dict:
        for k, v in dict.items():
            cortage = (v, k)
            regions_list.append(cortage)

    return regions_list


def gen_cities_list(reg_name: str) -> list:
    """
    Функция генерирует список с названиями городов
    """
    cities_list = []
    final_list = []

    for dict in russia_cities_dict:
        for k, v in dict.items():
            if k == reg_name:
                cities_list = v

    for city in cities_list:
        ctg = (city, city)
        final_list.append(ctg)

    return final_list


def get_region_full_name(short_name: str) -> str:
    """
    Функция генерирует полное имя региона
    """
    for dict in russia_reg_dict:
        for k, v in dict.items():
            if v == short_name:
                return k


def valid_liveplace(region: str, city: str) -> bool:
    """
    Функция валидирует выбранный город
    """
    for dict in russia_cities_dict:
        for k, v in dict.items():
            if k == region:
                cities_list = v

                if city in cities_list:
                    return True
                else:
                    return False


def get_all_cities_list() -> list:
    """
    Функция генерирует список со всеми городами
    """
    final_list = []

    for region_dict in russia_cities_dict:
        for region_name, cities_list in region_dict.items():
            for city in cities_list:
                final_list.append(city)

    return final_list


# def write_cities_db(cities_list: list, model: Model):
#     for city in cities_list:
#         model.objects.create(name=city)
#
#     print('done!')
