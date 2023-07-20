from django.urls import path
from . views import *

urlpatterns = [
    # path('', home, name='home'),
    # path('data/', createData, name='create'),
    # path('update/<int:id>/', update_data, name='update'),
    # path('view/<int:id>/', view_data),
    # path('delete/<int:id>/', delete_data),
    # path('book/<int:id>/', delete_book),
    # path('add/', add_book),
    path('', list_book),
    path('student/', StudentAPI.as_view()),
]