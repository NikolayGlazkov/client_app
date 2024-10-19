# from django.contrib import admin

<<<<<<< HEAD
# from .models import Person,BankAccount,Tag
=======
# admin.site.register(Person)
# admin.site.register(Tag)
# admin.site.register(BankAccount)
# admin.site.register(Contact)
# admin.site.register(Address)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('lastname','name','surname')
    # fields = ['lastname',('name','surname')]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    pass  

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Address)
class AddressAdminn(admin.ModelAdmin):
    pass
>>>>>>> b9ff6aa (Last_fix in main, go to temp_branch)


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
