from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.defaultfilters import title
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from UG_food_app.forms import UserForm, UserProfileForm, CommentForm, RecipeForm
from datetime import datetime
from UG_food_app.models import Recipe, UserProfile, Comment, Category
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

def index(request):
    context_dict = {}
    context_dict['recipes'] = Recipe.objects.order_by('-likes')
    return render(request, 'UG_food/index.html', context=context_dict)

@login_required
def add_recipe(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect(reverse('UG_food:index'))

    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit = False)
            recipe.user = UserProfile.objects.get(user = request.user)
            recipe.category = category
            recipe.views = 0
            recipe.likes = 0
            recipe.date = datetime.now()
            recipe.save()
            return redirect(reverse('UG_food:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'UG_food/add_recipe.html', context_dict)

def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect(reverse('UG_food:index'))
    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'picture': user_profile.picture,
                            'bio': user_profile.bio})
    if request.method == 'POST':
        if request.user == user:
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save(commit=True)
                return redirect('UG_food:profile', user.username)
            else:
                print(form.errors)

    context_dict = {'user_profile': user_profile,
                    'selected_user': user,
                    'form': form}
    return render(request, 'UG_food/profile.html', context_dict)

@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect(reverse('UG_food:index'))
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'UG_food/profile_registration.html', context=context_dict)

@login_required
def like_recipe(request):
    recipe_id = request.GET["recipe_id"]
    try:
        recipe = Recipe.objects.get(id=int(recipe_id))
    except Recipe.DoesNotExist:
        return HttpResponse(-1)
    except ValueError:
        return HttpResponse(-1)

    recipe.likes = recipe.likes + 1
    recipe.save()
    return HttpResponse(recipe.likes)

@login_required
def like_comment(request):
    comment_id = request.GET["comment_id"]
    try:
        comment = Comment.objects.get(id=int(comment_id))
    except Comment.DoesNotExist:
        return HttpResponse(-1)
    except ValueError:
        return HttpResponse(-1)

    comment.likes = comment.likes + 1
    comment.save()
    return HttpResponse(comment.likes)

def recipe(request, recipe_title):
    context_dict = {}
    try:
        recipe = Recipe.objects.get(title=recipe_title)
        recipe.views += 1
        recipe.save()
        context_dict['recipe'] = recipe
        context_dict['comments'] = Comment.objects.filter(recipe=recipe)
    except Recipe.DoesNotExist:
        recipe = None
        context_dict['recipe'] = None
        context_dict['comments'] = None

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if recipe:
                comment = form.save(commit=False)
                user = UserProfile.objects.get_or_create(user=request.user)[0]
                comment.user = user
                comment.recipe = recipe
                comment.date = datetime.now()
                comment.likes = 0
                comment.save()
                return redirect(reverse('UG_food:recipe', kwargs={'recipe_title': recipe_title}))
            else:
                print(form.errors)
    context_dict['form'] = form
    return render(request, "UG_food/recipe.html", context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        recipes = Recipe.objects.filter(category=category).order_by('-views')
        context_dict['recipes'] = recipes
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['recipes'] = None
        context_dict['category'] = None

    return render(request, 'UG_food/category.html', context=context_dict)
