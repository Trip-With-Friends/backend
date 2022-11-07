from russia_cities_dict import russia_cities_dict as rcd


regions_len_list = []

for region in rcd:
    final_dict = {}

    for region_name, cities_list in region.items():
        final_dict[region_name] = len(cities_list)

        regions_len_list.append(final_dict)

values_list = []

for dict in regions_len_list:
    for key, value in dict.items():
        values_list.append(value)

print(max(values_list))
all_cities = 0

for value in values_list:
    all_cities += value

print(all_cities)
