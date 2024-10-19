from django import forms
from .models import Person, Tag, Address, Contact

class ClientForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'lastname', 'date_of_birth', 'place_of_birth', 'passport_number', 'passport_seria', 
                  'issued_by', 'date_of_issue', 'department_code', 'inn_number', 'snils_number', 'tags']

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),  # Теги, которые будут доступны для выбора
        widget=forms.CheckboxSelectMultiple,  # Используем виджет с множественным выбором (чекбоксы)
        required=False  # Необязательное поле
    )

# Форма для модели Address
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'street', 'house_number', 'apartment_number', 'post_index']

# Форма для модели Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'phone_number']

# Формы для тегов остаются без изменений
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
