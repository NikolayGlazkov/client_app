from django.db import models

# клинты
class Person(models.Model):
    name = models.CharField(max_length=30,verbose_name="Имя")
    surname = models.CharField(max_length=30,verbose_name="Отчество")
    lastname = models.CharField(max_length=30,verbose_name='Фамилия')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    place_of_birth = models.CharField(max_length=30,verbose_name='Место рождения')
    city = models.CharField(max_length=30,verbose_name='город проживания')
    street = models.CharField(max_length=40,verbose_name='Улиа')
    post_index = models.CharField(max_length=8,verbose_name='Почтовый индекс')
    email = models.EmailField(max_length=50,verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=15,verbose_name='Номер телефона')
    pasport_number = models.CharField(max_length=6,verbose_name='Номер паспорта')
    pasport_seria = models.CharField(max_length=4,verbose_name='Серия паспорта')
    issued_by = models.CharField(max_length=100,verbose_name='Место выдачи')
    date_of_issue = models.DateField(verbose_name='Жата выдачи')
    department_code = models.CharField(max_length=7,verbose_name='Код подразделения')
    inn_number = models.CharField(max_length = 12,verbose_name='Номер ИНН')
    snils_number = models.CharField(max_length = 20,verbose_name='Номер СНИЛС')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Теги')
    def __str__ (self) :
       return self.name
    
    class Meta:
        verbose_name_plural = "Клиенты"
        verbose_name = "Клиента"

#теги клиентов (тематика рассылки)
class Tag(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Теги')

    def __str__ (self):
       return self.name

    class Meta:
        verbose_name_plural = 'Тег' 
        verbose_name = 'Тег' 
        ordering = ['name']


#счета клиентов
class BankAccount(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='bank_accounts')
    account_number = models.CharField(max_length=24, verbose_name='Номер счета')
    corr_account = models.CharField(max_length=24, verbose_name='Корр. счет')
    bank_name = models.CharField(max_length=50, verbose_name='Банк получателя')
    bic = models.CharField(max_length=9, verbose_name='БИК')
    inn = models.CharField(max_length=15, verbose_name='ИНН банка')
    kpp = models.CharField(max_length=15, verbose_name='КПП банка')

    class Meta:
        verbose_name_plural = "Банковские счета"
        verbose_name = "Банковский счет"

    def __str__(self):
        return f"Счет {self.account_number} в {self.bank_name}"
    
#теги клиентов
