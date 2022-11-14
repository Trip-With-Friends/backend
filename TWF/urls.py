from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from users import views as users_views
from where_to_go import views as where_to_go_views
from mini_services import views as mini_services_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', users_views.register, name='register'),
    path('register2', users_views.user_append, name='append_user'),
    path('cabinet', users_views.cabinet, name='cabinet'),
    path('login_select', users_views.login_select, name='login_select'),
    path('login/<login_method>', users_views.login, name='login'),
    path('logout', users_views.logout, name='logout'),
    path('delete_user', users_views.delete_user, name='delete_user'),

    path('', where_to_go_views.city_selector,
         name='city_selector_no_city', kwargs={
             'region_short_name': None,
             'city_name': None
         }),
    path('<region_short_name>/<city_name>', where_to_go_views.city_selector,
         name='city_selector'),
    path('cat_viewer/<region_short_name>/<city_name>/<category>', where_to_go_views.category_viewer,
         name='cat_viewer'),
    path('add_place/<region_short_name>/<city_name>', where_to_go_views.create_place,
         name='add_place'),

    path('menu', mini_services_views.menu,
         name='menu'),
    path('calculator', mini_services_views.calculator,
         name='calculator_no_city'),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
