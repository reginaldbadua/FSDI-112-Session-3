from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Movie, Genre

# Create your views here.


def index(request):
    # Movie.objects.all()  read all the table
    # Movie.objects.filter(release_year = 2004)
    # Movie.objects.get(id=1)

    catalog = Movie.objects.all()
    return render(request, 'views/index.html',
                  {'catalog': catalog, 'title': 'This is the page title'})


# /movie/detail/1
# find the object with id = 1
def detail(request, movie_id):
    try:
        the_movie = Movie.objects.get(id=movie_id)
        return render(request, 'views/detail.html', {'movie': the_movie})
    except Movie.DoesNotExist:
        # raise a 404 error
        raise Http404()


def test(request):
    return HttpResponse("<h1>I'm a test</h1>")


def contact(request):
    return HttpResponse("<h1>Page under construction</h1>")


def genres(request):
    all = Genre.objects.all()
    print(all)
    return render(request, "views/genres.html", {"genres": all})

def history(request):
    return render(request, 'views/history.html')

def order(request):
    return render(request, 'views/order.html')

# /movies/genres
# display the list of generes

# need:
#   register the path /url
#   register the view function
#   create the html file (generes.html)
