from django.shortcuts import render

# Create your views here.

#from car.forms import CarForm, CarDetailForm, CarMainForm
from people.models import Person, Group
from wishes.models import Wish
from events.models import Event


def get_received_wish(pk):
    related_wishes =   Wish.objects.select_related().filter(assigned_to_id = pk)
    if (len(related_wishes)==1):
        return related_wishes[0]
    else:
        return None


def get_my_wish(pk):
    related_wishes =   Wish.objects.select_related('author').filter(author_id=pk)
    if (len(related_wishes)==1):
        return related_wishes[0]
    else:
        return None



def person_view(request, pk):
    template="person.html"
    context={}
    if request.method == "GET":
        person = Person.objects.get(id=pk)
        my_wish = get_my_wish(pk)
        received_wish = get_received_wish(pk)
        context['person'] = person
        context['my_wish'] = my_wish
        context['received_wish'] = received_wish
        return render(request, template, context)





def main_view(request):
    context = {}
    template = "main.html"
    if request.method == 'GET':
        context["people"] = Person.objects.filter(group_id=1).all()
        return render(request, template, context)