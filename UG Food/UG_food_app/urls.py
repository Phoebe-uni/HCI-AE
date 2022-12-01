from django.urls import path
from UG_food_app import views

app_name = 'UG_food'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>/', views.profile, name='profile'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('like_recipe/', views.like_recipe, name='like_recipe'),
    path('like_comment/', views.like_comment, name='like_comment'),
    path('categories/', views.categories, name='categories'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('<recipe_title>/', views.recipe, name='recipe'),
    path('category/<slug:category_name_slug>/add_recipe/', views.add_recipe, name='add_recipe'),
]


