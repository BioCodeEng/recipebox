#[V1/2] importing render, HttpResponseRedirect, reverse
#[Auth] imported login, logout, auth, login_required, User, LoginForm, SignForm
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

#[V1/2] importing recipe, author, AddRecipeForm, AddAuthorForm
#[Auth] added LoginForm, SignForm
from recipe_app.models import Recipe, Author
from recipe_app.forms import AddRecipeForm, AddAuthorForm, LoginForm, SignupForm
# Create your views here.

def index(request):
    data = Recipe.objects.all()
    return render(request, "index.html", {'data': data})


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe_detail.html", {"recipe": recipe})


def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    data = Recipe.objects.filter(author=author)
    favorite_recipe = author.favorites.all()
    return render(request, "author_detail.html",
                  {"author": author, "data": data, 'favorites': favorite_recipe})

#[Auth] added login_required decorator
@login_required
def addrecipe_view(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                author=data.get('author'),
                description=data.get('description'),
                time_required=data.get('time_required'),
                instructions=data.get('instructions')
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddRecipeForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
def editrecipe_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.user.author.id == recipe.author.id or request.user.is_staff:
        data = {
            'title': recipe.title,
            'author': recipe.author,
            'description': recipe.description,
            'time_required': recipe.time_required,
            'instructions': recipe.instructions,
        }
        if request.method == 'POST':
            form = AddRecipeForm(request.POST, initial=data)
            if form.is_valid():
                data=form.cleaned_data
                recipe.title = data['title']
                recipe.author = data['author']
                recipe.description = data['description']
                recipe.time_required = data['time_required']
                recipe.instructions = data['instructions']
                recipe.save()
            return HttpResponseRedirect(reverse('recipe_detail', args=[recipe.id]))
    
        form = AddRecipeForm(initial=data)
        return render(request, 'generic_form.html', {'form': form})

    return HttpResponseForbidden("You are not authorized to access this page!")


#[Auth] added login_required decorator
@login_required
def addauthor_view(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AddAuthorForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
def favorites_view(request, favorites_id):
    current_user = request.user
    favorite = Recipe.objects.filter(id=favorites_id).first()
    current_user.author.favorites.add(favorite)
    
    return HttpResponseRedirect(request.META.get('favorites', '/'))


#[Auth] added signup_view
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})

#[Auth] added login_view
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
            # return HttpResponseRedirect(reverse("homepage"))
                return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

#[Auth] added logout_view
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
