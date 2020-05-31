from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
	path('',views.index,name='index'),
	path('articles/<int:year>/',views.year_archive,name='year'),
	path('articles/<int:year>/<int:month>/',views.month_archive,name='month'),
	path('articles/<int:year>/<int:month>/<int:pk>/',views.article_detail,name='detail'),

]