from django.shortcuts import render

# Create your views here.

#from car.forms import CarForm, CarDetailForm, CarMainForm
from people.models import Person, Group
from wishes.models import Wish
from events.models import Event

def person_view(request, pk):
    template="person.html"
    context={}
    if request.method == "GET":
        person = Person.objects.get(id=pk)
        #my_wish = Wish.objects.get(author_rel = pk)
        #received_wish = Wish.objects.get(assigned_rel = pk)
        context['person'] = person
        #context['my_wish'] = my_wish
        #context['received_wish'] = received_wish
        return render(request, template, context)