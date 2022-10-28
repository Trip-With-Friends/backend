from .py.russia_cities_dict import russia_cities_dict as rcd
from .py.russia_regions_array import russia_reg_array as rra


def gen_regions_list() -> list:
    regions_list = []

    for dict in rra:
        for k, v in dict.items():
            ctg = (v, k)
            regions_list.append(ctg)

    return regions_list


def gen_cities_list(reg_code: str) -> list:
    city_full_name = ''
    cities_list = []
    final_list = []

    if len(str(reg_code)) < 4:
        for dict in rra:
            for k, v in dict.items():
                if v == reg_code:
                    city_full_name = k

    else:
        city_full_name = reg_code

    for dict in rcd:
        for k, v in dict.items():
            if k == city_full_name:
                cities_list = v

    for city in cities_list:
        ctg = (city, city)
        final_list.append(ctg)

    return final_list


def get_region_full_name(short_name: str) -> str:
    for dict in rra:
        for k, v in dict.items():
            if v == short_name:
                return k
