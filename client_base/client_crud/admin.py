# from django.contrib import admin

# from .models import Person,BankAccount,Tag


# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('name', 'surname', 'lastname','phone_number',"inn_number") 
#     list_display_links = ('name',)
#     search_fields = ('name','inn_number',)

# admin.site.register(Person,PersonAdmin)
# admin.site.register(BankAccount)
# admin.site.register(Tag)

from django.contrib import admin
from .models import Person, Tag, BankAccount

class TagInline(admin.TabularInline):
    model = Person.tags.through
    extra = 1  # Количество пустых строк для добавления новых тегов

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'phone_number')
    search_fields = ('name', 'lastname', 'email', 'phone_number')
    inlines = [TagInline]  # Добавляем управление тегами в админку
    filter_horizontal = ('tags',)  # Добавляем виджет для удобного выбора тегов

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'bank_name', 'person')
    search_fields = ('account_number', 'bank_name', 'person__name')

# Если не хотите отображать промежуточную таблицу связи в админке
# admin.site.unregister(Person.tags.through)
