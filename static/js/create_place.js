const category_selector = document.getElementById('id_category')
const kitchen_type = document.getElementById('id_kitchen_type')

console.log(kitchen_type)
console.log(category_selector)

kitchen_type.style.display = 'none'

document.addEventListener('input', function (event) {
    if (event.target.id == 'id_category') {
        let selected_value = category_selector.options[category_selector.selectedIndex].text

        if (selected_value == 'Кафе и рестораны') {
            kitchen_type.style.display = 'block'

        } else {
            kitchen_type.style.display = 'none'
        }
    }
})
