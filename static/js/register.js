import { gen_cities_list, reg_full_name } from './regions_and_cities/regions_utils.js'

const city_btn = document.getElementById('btn add-city')
const village_btn = document.getElementById('btn add-village')
const liveplace_select_bar = document.getElementById('liveplace-select')
const liveplace_field = document.getElementById('id_liveplace')
const region_select_bar = document.getElementById('id_region')


//liveplace_select_bar.style.display = 'none'
liveplace_field.style.display = 'none'


//generate an option tags for city select
function generate_city_options() {
    let selected_region = region_select_bar.options[region_select_bar.selectedIndex].text

    const cities_list = gen_cities_list(selected_region)

    liveplace_select_bar.innerHTML = ''

    for (const city of cities_list) {
        const option = `<option id="city" value="${city}">${city}</option>`

        liveplace_select_bar.innerHTML += option
    }
}

//detecting a city field changes
document.addEventListener('input', function (event) {

    if (event.target.id == 'id_region') {
        generate_city_options()

    } else if (event.target.id == 'liveplace-select') {
        let selected_value = liveplace_select_bar.options[liveplace_select_bar.selectedIndex].value

        liveplace_field.value = selected_value
    }
})
