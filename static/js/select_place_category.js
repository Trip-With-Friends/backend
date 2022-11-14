import { gen_cities_list, reg_full_name } from './regions_and_cities/regions_utils.js'


const city_select_bar = document.getElementById('city-select')
const city_field = document.getElementById('id_city')
const region_select_bar = document.getElementById('id_region')

//liveplace_select_bar.style.display = 'none'
city_field.style.display = 'none'

//generate an option tags for city select
function generate_city_options() {
    let selected_region = region_select_bar.options[region_select_bar.selectedIndex].text

    const cities_list = gen_cities_list(selected_region)

    city_select_bar.innerHTML = ''

    for (const city of cities_list) {
        const option = `<option id="city" value="${city}">${city}</option>`

        city_select_bar.innerHTML += option
    }
}

//detecting a city field changes
document.addEventListener('input', function (event) {
    console.log(event.target.id)

    if (event.target.id == 'id_region') {
        generate_city_options()

        let selected_value = city_select_bar.options[city_select_bar.selectedIndex].value
        city_field.value = selected_value

        console.log(selected_value)

    } else if (event.target.id == 'city-select') {
        let selected_value = city_select_bar.options[city_select_bar.selectedIndex].value

        city_field.value = selected_value

    }
})
