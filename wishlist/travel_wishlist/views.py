from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm


def place_list(request):

    if request.method == 'POST':

        # creates new place from wishlist.html form data (like formatting data to model field,
        # or saving data to a Place template model,
        # or applying data to a table column?)
        form = NewPlaceForm(request.POST)

        # creates (saves) model object from form (formatted) data
        place = form.save()

        # validate against db constraints
        if form.is_valid():
            place.save()    # saves to place db
            return redirect('place_list')   # redirect back to homepage with updated list, skipping this if block

    places = (Place.objects.filter(visited=False).order_by('name'))

    # create empty form for wishlist.html
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {
        'places': places,
        'new_place_form': new_place_form})


def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', { 'visited': visited })


def place_was_visited(request, place_pk):
    if request.method == 'POST':
        # place = Place.objects.get(pk=place_pk)
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True
        place.save()

    return redirect('place_list')


def about(request):
    author = 'Ryan'
    about_app = 'Website to create a travel wishlist'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about_app})

