from django.db import models

class CompanyInfo(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название компании")
    description = models.TextField(verbose_name="Описание")
    logo = models.ImageField(upload_to='company/', verbose_name="Логотип")
    phone = models.CharField(max_length=50, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Email")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    social_links = models.URLField(verbose_name="Ссылка на соцсети", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Информация о компании"
        verbose_name_plural = "Информация о компании"


class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание услуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='services/', verbose_name="Изображение")

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"