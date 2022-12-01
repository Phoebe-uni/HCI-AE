import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UG_food.settings')

import django
django.setup()

from UG_food_app.models import Recipe, Category, User, UserProfile, Comment
from datetime import datetime


def add_category(name):
    category = Category.objects.get_or_create(name = name)[0]
    category.save()
    return category

def add_user(username, password, image, bio):
    user = User.objects.get_or_create(username = username)[0]
    user.set_password(password)
    user.save()
    user_profile = UserProfile.objects.get_or_create(user = user, picture = image, bio = bio)[0]
    user_profile.save()
    return user_profile

def add_recipe(category, user, title, views, likes, image, date, text):
    recipe = Recipe.objects.get_or_create(category = category, user = user, title = title, views = views, likes = likes,
                                          img = image, date = date, text = text)[0]
    recipe.save()
    return recipe

def add_comment(user, recipe, text, date, likes):
    comment = Comment.objects.get_or_create(user = user, recipe = recipe, text = text, date = date, likes = likes)[0]
    comment.save()
    return comment

def add_favourites(username):
    try:
        useraccount = User.objects.create_user(username)
        userprofile=UserProfile.objects.get_or_create(UserAccount=useraccount,UserID=useraccount.id)[0]
    except:
        useraccount = User.objects.get(username=username)
        userprofile=UserProfile.objects.get_or_create(UserAccount=useraccount,UserID=useraccount.id)[0]


def populate():

    categories = ['Italian', 'Mexican', 'American', 'French']

    users = [
        {'username': '1234567y',
         'password': 'password8',
         'image': 'profile_images/homer.jpg',
         'bio': "This is student account of University of glasgow."},
        {'username': '2537648m',
         'password': 'password9',
         'image': 'profile_images/bart.jpg',
         'bio': "This is student account of University of glasgow."},
        {'username': '2637482l',
         'password': 'password10',
         'image': 'profile_images/lisa.jpg',
         'bio': "This is student account of University of glasgow."},
        {'username': '2737432w',
         'password': 'password11',
         'image': 'profile_images/marge.jpeg',
         'bio': "This is student account of University of glasgow."},
        {'username': '2735485k',
         'password': 'password12',
         'image': 'profile_images/abe.jpg',
         'bio': "This is student account of University of glasgow."}
    ]

    recipes = [
        {'category': 'curry chicken',
         'user': '1234567y',
         'img': 'recipe_images/las.jfif',
         'text': """taste good ."""},
        


    print("Clearing the database")
    User.objects.all().delete()
    UserProfile.objects.all().delete()
    Category.objects.all().delete()
    Recipe.objects.all().delete()
    Comment.objects.all().delete()

    print("Adding categories")
    for category in categories:
        cat = add_category(category)
        print(f"{cat} category added")

    print("Adding users")
    for user in users:
        u = add_user(user['username'], user['password'], user['image'], user['bio'])
        print(f"User: {u} added")

    print("Adding recipes")
    for recipe in recipes:
        user_profile = UserProfile.objects.get(user__username = recipe['user'])
        category = Category.objects.get(name = recipe['category'])
        r = add_recipe(category, user_profile, recipe['title'], recipe['views'], recipe['likes'], recipe['img'], recipe['date'], recipe['text'])
        print(f"Recipe: {r} added")

    for comment in comments:
        user_profile = UserProfile.objects.get(user__username = comment['user'])
        recipe = Recipe.objects.get(title = comment['recipe_title'])
        com = add_comment(user_profile, recipe, comment['text'], comment['date'], comment['likes'])
        print(f"Comment: '{com}' added")

if __name__ == '__main__':
    print('Starting UG_food population script')
    populate()
