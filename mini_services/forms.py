from django import forms


class CalculatorForm(forms.Form):
    to_city = forms.IntegerField(required=False)
    from_city = forms.IntegerField(required=False)

    flat = forms.IntegerField(required=False)
    live_days = forms.IntegerField(required=False)

    eat = forms.IntegerField(required=False)
    etc_sum = forms.IntegerField(required=False)
    free_sum = forms.IntegerField(required=False)

    insurance = forms.IntegerField(required=False)
    documents = forms.IntegerField(required=False)

    def calculate(self):
        full_sum = 0
        flat_values = []
        cleaned_data = self.cleaned_data

        if cleaned_data.get('flat') and cleaned_data.get('live_days'):
            all_values = [
                value for name, value in cleaned_data.items() if name != 'flat' if name != 'live_days']
            flat_values = [
                value for name, value in cleaned_data.items() if (name == 'flat' or name == 'live_days')]

            for value in all_values:
                try:
                    full_sum += value

                except:
                    print(None)

            try:
                full_sum += (flat_values[0] * flat_values[1])

            except:
                pass

            return full_sum

        else:
            if not cleaned_data.get('flat'):
                self.add_error('flat', 'Не указана цена отеля')

            elif not cleaned_data.get('live_days'):
                self.add_error('live_days', 'Не указано кол-во дней')
