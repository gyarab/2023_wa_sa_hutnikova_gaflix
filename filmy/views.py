from django.shortcuts import render
from django.db.models import Q

from filmy.models import Movie,Actor,Director
# Create your views here.

def movies(request):
    movies = Movie.objects.all().order_by('name')
    search = request.GET.get('search')
    if search:
        movies = movies.filter(Q(name__icontains=search)|Q(description__icontains=search)) 

    context = {
        'movies': movies,
        "search": search,
    }
    return render (request, 'filmy/movies.html', context)

def movie(request, id):
    context = {
        'movie': Movie.objects.get(id=id)
    }
    return render (request, 'filmy/movie.html', context)

def actors(request):
    actors = Actor.objects.all().order_by('name')
    search = request.GET.get('search')
    if search:
        actors = actors.filter(name__icontains=search)

    context = {
        'actors': actors,
        "search": search,
    }
    return render (request, 'filmy/actors.html', context)

def actor(request, id):
    actor = Actor.objects.get(id=id)

    context = {
        'actor': actor,
        'movies': Movie.objects.filter(actors=actor),
    }
    return render(request, 'filmy/actor.html', context)

def directors(request):
    directors = Director.objects.all().order_by('name')
    search = request.GET.get('search')
    if search:
        directors = directors.filter(name__icontains=search)
    
    context = {
        'directors': directors,
        'search': search
    }
    return render(request, 'filmy/directors.html', context)


def director(request, id):
    director = Director.objects.get(id=id)

    context = {
        'director': director,
        'movies': Movie.objects.filter(director=director)
    }
    return render(request, 'filmy/director.html', context)