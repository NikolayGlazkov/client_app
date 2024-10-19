from django.contrib import admin
from .models import Person, Tag, BankAccount, Contact,Address  # Не забудьте импортировать Contact

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

# class TagInline(admin.TabularInline):
#     model = Person.tags.through
#     extra = 1  # Количество пустых строк для добавления новых тегов

# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('name', 'lastname', 'get_email', 'get_phone_number')  # Измените здесь
#     search_fields = ('name', 'lastname')

#     inlines = [TagInline]  # Добавляем управление тегами в админку
#     filter_horizontal = ('tags',)  # Добавляем виджет для удобного выбора тегов

#     # Метод для получения email из связанной модели Contact
#     def get_email(self, obj):
#         return obj.contact.email if obj.contact else '-'
#     get_email.short_description = 'Email'  # Заголовок для столбца

#     # Метод для получения номера телефона из связанной модели Contact
#     def get_phone_number(self, obj):
#         return obj.contact.phone_number if obj.contact else '-'
#     get_phone_number.short_description = 'Номер телефона'  # Заголовок для столбца

# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)

# @admin.register(BankAccount)
# class BankAccountAdmin(admin.ModelAdmin):
#     list_display = ('account_number', 'bank_name', 'person')
#     search_fields = ('account_number', 'bank_name', 'person__name')

# # Если не хотите отображать промежуточную таблицу связи в админке
# # admin.site.unregister(Person.tags.through)
