import django_tables2 as tables
from .models import Person

class PersonTable(tables.Table):
    class Meta:
        models = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", )