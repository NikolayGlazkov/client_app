from django.db import models
from django.core.validators import RegexValidator

# контакты клиента 
class Contact(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='contacts')  # Связь с клиентом
    email = models.EmailField(max_length=100, verbose_name='Электронная почта', help_text="Введите Электронную почту",blank=True,null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', help_text="Введите Номер телефона",blank=True,null=True)

    class Meta:
        verbose_name_plural = "Контакты"
        verbose_name = "Контакт"

    def __str__(self):
        return f"{self.person} телефон {self.phone_number} Электронная почта {self.email}"

# Класс адреса проживания
class Address(models.Model):
    city = models.CharField(max_length=50, verbose_name='Город проживания', help_text="Введите Город проживания")
    street = models.CharField(max_length=50, verbose_name='Улица', help_text="Введите Улицу", blank=True, null=True)
    house_number = models.CharField(max_length=10, verbose_name='Номер дома', help_text="Введите Номер дома")
    apartment_number = models.CharField(max_length=10, verbose_name='Номер квартиры', help_text="Введите Номер квартиры (если есть)", blank=True, null=True)
    post_index = models.CharField(max_length=10, verbose_name='Почтовый индекс', help_text="Введите Почтовый индекс",
                                  validators=[RegexValidator(regex=r'^\d{6}$', message='Индекс должен содержать 6 цифр')])
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='address')  # Связь с клиентом

    class Meta:
        verbose_name_plural = "Адреса"
        verbose_name = "Адрес"

    def __str__(self):
        # Формирование строки адреса с учётом возможных пропусков данных
        address = f"{self.post_index}, {self.city}"
        if self.street:
            address += f", {self.street}"
        if self.house_number:
            address += f", дом {self.house_number}"
        if self.apartment_number:
            address += f", кв. {self.apartment_number}"
        return address

# Теги клиентов
class Tag(models.Model):
    name = models.CharField(max_length=200, help_text="Введите тег для клиента")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Теги"
        verbose_name = "Тег"
        
class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя", help_text="Введите Имя")
    surname = models.CharField(max_length=50, verbose_name="Отчество", help_text="Введите Отчество")
    lastname = models.CharField(max_length=50, verbose_name='Фамилия', help_text="Введите Фамилию")
    date_of_birth = models.DateField(verbose_name='Дата рождения', help_text="Введите Дату рождения")
    place_of_birth = models.CharField(max_length=100, verbose_name='Место рождения', help_text="Введите Место рождения")
    
    passport_number = models.CharField(max_length=6, verbose_name='Номер паспорта', help_text="Введите Номер паспорта",
                                       validators=[RegexValidator(regex=r'^\d{6}$', message='Номер паспорта содержит 6 цифр')])
    passport_seria = models.CharField(max_length=4, verbose_name='Серия паспорта', help_text="Введите Серию паспорта",
                                      validators=[RegexValidator(regex=r'^\d{4}$', message='Серия паспорта содержит 4 цифры')])
    issued_by = models.CharField(max_length=100, verbose_name='Место выдачи', help_text="Введите Место выдачи паспорта")
    date_of_issue = models.DateField(verbose_name='Дата выдачи', help_text="Введите дату выдачи паспорта")
    department_code = models.CharField(max_length=7, verbose_name='Код подразделения', help_text="Введите код подразделения паспорта",
                                       validators=[RegexValidator(regex=r'^\d{3}-\d{3}$', message='Код подразделения имеет формат 000-000')])
    inn_number = models.CharField(max_length=12, verbose_name='Номер ИНН', help_text="Введите Номер ИНН", unique=True,
                                  validators=[RegexValidator(regex=r'^\d{12}$', message='ИНН должен состоять из 12 цифр')])
    snils_number = models.CharField(max_length=20, verbose_name='Номер СНИЛС', help_text="Введите Номер СНИЛС")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Теги',help_text="Выберете соответсвующий тег")

    class Meta:
        verbose_name_plural = "Клиенты"
        verbose_name = "Клиента"

    def __str__(self):
        return f"{self.name} {self.lastname} {self.surname}"


# Счета клиентов
class BankAccount(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='bank_accounts')
    account_number = models.CharField(max_length=24, verbose_name='Номер счета')
    corr_account = models.CharField(max_length=24, verbose_name='Корр. счет')
    bank_name = models.CharField(max_length=100, verbose_name='Банк получателя')
    bic = models.CharField(max_length=9, verbose_name='БИК')
    inn = models.CharField(max_length=15, verbose_name='ИНН банка')
    kpp = models.CharField(max_length=15, verbose_name='КПП банка')

    def __str__(self):
        return f"Счет {self.person} в {self.bank_name}"

    class Meta:
        verbose_name_plural = "Банковские счета"
        verbose_name = "Банковский счет"
