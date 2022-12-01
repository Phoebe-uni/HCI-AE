from django import forms
from django.contrib.auth.models import User
from UG_food_app.models import Recipe, Comment, UserProfile

class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the recipe.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    img = forms.ImageField()
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Recipe
        fields = ('title', 'img', 'text',)

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ('text',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'bio',)