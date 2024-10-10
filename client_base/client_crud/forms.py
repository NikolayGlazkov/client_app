from django import forms
from .models import Person, Tag

class ClientForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'lastname', 'date_of_birth', 'place_of_birth', 'city', 'street', 
                  'post_index', 'email', 'phone_number', 'passport_number', 'passport_seria', 'issued_by', 
                  'date_of_issue', 'department_code', 'inn_number', 'snils_number', 'tags']

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),  # Теги, которые будут доступны для выбора
        widget=forms.CheckboxSelectMultiple,  # Используем виджет с множественным выбором (чекбоксы)
        required=False  # Необязательное поле
    )


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']