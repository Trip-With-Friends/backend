import { russia_cities_dict } from "./sources/russia_cities_dict.js"
import { russia_reg_array } from "./sources/russia_regions_array.js"


export function gen_cities_list(region_name) {
    // Функция генерирует список с городами региона
    for (const all_regions of russia_cities_dict) {
        for (const region in all_regions) {
            if (region == region_name) {
                return all_regions[region]
            }
        }
    }
}


export function reg_full_name(short_name) {
    // Функция генерирует полное имя региона
    for (const region of russia_reg_array) {
        for (let key in region) {
            if (region[key] == short_name) {
                return key
            }
        }
    }
}
