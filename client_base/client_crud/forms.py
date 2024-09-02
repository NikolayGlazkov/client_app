from django.forms import ModelForm

from .models import Person

class PerForm(ModelForm):
    class Meta:
        model = Person
        fields = (
            'name', 
            'surname', 
            'lastname', 
            'date_of_birth', 
            'place_of_birth', 
            'city', 
            'street', 
            'post_index', 
            'email', 
            'phone_number', 
            'pasport_number', 
            'pasport_seria', 
            'issued_by', 
            'date_of_issue', 
            'department_code', 
            'inn_number', 
            'snils_number',
            "tags"
        )