from django.db import models

# Клиенты
class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя", help_text="Введите Имя")
    surname = models.CharField(max_length=50, verbose_name="Отчество", help_text="Введите Отчество")
    lastname = models.CharField(max_length=50, verbose_name='Фамилия', help_text="Введите Фамилию")
    date_of_birth = models.DateField(verbose_name='Дата рождения', help_text="Введите Дату раждения")
    place_of_birth = models.CharField(max_length=100, verbose_name='Место рождения', help_text="Введите Место рождения")
    city = models.CharField(max_length=50, verbose_name='Город проживания', help_text="Введите Город проживания")
    street = models.CharField(max_length=50, verbose_name='Улица', help_text="Введите Улицу Согласно прописки клиента")
    post_index = models.CharField(max_length=10, verbose_name='Почтовый индекс', help_text="Введите Почтовый индекс")
    email = models.EmailField(max_length=100, verbose_name='Электронная почта', help_text="Введите Электронную почту")
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', help_text="Введите Номер телефона")
    passport_number = models.CharField(max_length=6, verbose_name='Номер паспорта', help_text="Введите Номер паспорта")
    passport_seria = models.CharField(max_length=4, verbose_name='Серия паспорта', help_text="Введите Серию паспорта")
    issued_by = models.CharField(max_length=100, verbose_name='Место выдачи', help_text="Введите Место выдачи паспорта")
    date_of_issue = models.DateField(verbose_name='Дата выдачи', help_text="Введите дату выдочи паспорта")
    department_code = models.CharField(max_length=7, verbose_name='Код подразделения', help_text="Введите код подразделения паспорта")
    inn_number = models.CharField(max_length=12, verbose_name='Номер ИНН', help_text="Введите Номер ИНН", unique=True)
    snils_number = models.CharField(max_length=20, verbose_name='Номер СНИЛС', help_text="Введите Номер СНИЛС")
    # tags = models.ManyToManyField('Tag', blank=True, verbose_name='Теги')
        verbose_name_plural = "Клиенты"
        verbose_name = "Клиент"


# Класс адреса проживания
class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='addresses')
    region = models.CharField(max_length=50, verbose_name="Область")
    city = models.CharField(max_length=50, verbose_name="Город")
    district = models.CharField(max_length=50, verbose_name="Район")
    street = models.CharField(max_length=50, verbose_name="Улица")
    home_number = models.CharField(max_length=10, verbose_name="Номер дома")
    apartment_number = models.CharField(max_length=10, verbose_name="Номер квартиры", blank=True, null=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = 'Адреса'
        verbose_name = 'Адрес'
        ordering = ['city']


# Теги клиентов
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


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
        return f"Счет {self.account_number} в {self.bank_name}"

    class Meta:
        verbose_name_plural = "Банковские счета"
        verbose_name = "Банковский счет"
