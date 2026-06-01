from django.db import models

# Create your models here.

# Create your models here.
class Equipment(models.Model):
    name = models.CharField('название техники',max_length=67)
    category = models.CharField('категория техники',max_length=67)
    description = models.TextField('описание')
    price_per_day = models.FloatField('стоимость аренды за сутки')
    serial_number = models.CharField('серийный номер',max_length=30)
    is_available = models.BooleanField('доступность техники')
    created_at = models.CharField('дата добавления',max_length=67)

    def __str__(self):
        return (f" название техники: {self.name}  "
                f"| категория техники: {self.category}  "
                f"| описание: {self.description}  "
                f"| стоимость аренды за сутки: {self.price_per_day}  "
                f"| серийный номер: {self.serial_number}  "
                f"| доступность техники: {self.is_available}  "
                f"| дата добавления: {self.created_at }")

class Customer(models.Model):
    full_name = models.CharField('ФИО клиента', max_length=67)
    phone = models.CharField('телефон', max_length=67)
    email = models.EmailField('электронная почта',max_length=67)

    def __str__(self):
        return (f"ФИО клиента: {self.full_name }  "
                f"| телефон: {self.phone }  "
                f"| электронная почта: {self.email }  ")


class Rental(models.Model):
    name = models.CharField('название техники', max_length=67)
    customer = models.CharField('клиент', max_length=67)
    start_date = models.DateTimeField('дата начала аренды')
    end_date = models.DateTimeField('дата окончания аренды')
    total_price  = models.FloatField('итоговая стоимость')

    class ActiveStatus(models.TextChoices):
        AVAILABLE = 'active', 'Доступна'
        REPAIR = 'finished', 'законченный'
        RENTED = 'cancelled', 'отменен'

    status_active = models.CharField(
        'доступность техники',
        max_length=15,
        choices=ActiveStatus.choices,
        default=ActiveStatus.AVAILABLE
    )
    created_at = models.DateField('дата оформления')
    def __str__(self):
        return (f"название техники: {self.name}  "
                f"| клиент: {self.customer}  "
                f"| дата начала аренды: {self.start_date}  "
                f"| дата окончания аренды: {self.end_date}  "
                f"| итоговая стоимость: {self.total_price }  "
                f"| доступность техники: {self.self.get_status_active_display()}  "
                f"| дата оформления: {self.created_at}")