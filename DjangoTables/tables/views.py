from django.views.generic import ListView
from .models import Person
from .tables import PersonTable
from django_tables2 import SingleTableView

class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'tables/people.html'