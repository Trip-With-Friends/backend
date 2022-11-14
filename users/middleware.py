from django.shortcuts import redirect


class CheckUserLogin:
    def __init__(self, get_request):
        self.get_request = get_request

    def __call__(self, request):
        # print(request)

        # user = 'b'

        # if user is None:
        #     return redirect('register')

        print(request)
