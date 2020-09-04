from django.db import models


class Station(models.Model):

    name = models.CharField(max_length=50, verbose_name='Название станции', help_text='Введите название станции')

    def __str__(self):
        return self.name


class System(models.Model):

    """Система привязки устройства - СДРП, ИСС, Телеграф и т.д."""

    name = models.CharField(max_length=100, verbose_name='Наименование системы', help_text='Введите наименование '
                                                                                           'системы или группы '
                                                                                           'устройств')

    station = models.ForeignKey('Station', on_delete=models.SET_NULL, null=True, verbose_name='Станция',
                                help_text='Выберите станцию установки системы')
    type = models.ForeignKey('SystemType', on_delete=models.SET_NULL, null=True, verbose_name='Тип')

    def __str__(self):
        return f'{self.name} - {self.station.name}'


class SystemType(models.Model):

    """Тип системы (СДРП, ИСС, Телеграф и т.д.)"""

    name = models.CharField(max_length=50, verbose_name='Название типа системы', help_text='Введите название системы')

    def __str__(self):
        return self.name


class Type(models.Model):

    """Тип устройства (монитор, принтер, БПМ, и т.д.)"""

    name = models.CharField(max_length=50, verbose_name='Название типа устройств', help_text='Введите название '
                                                                                             'устройств')

    def __str__(self):
        return self.name


STATUS = (('w', 'В работе'),
          ('rs', 'Резерв'),
          ('rp', 'В ремонте'),
          ('?', '?'))


class Device(models.Model):

    name = models.CharField(max_length=50, verbose_name='Название устройства', help_text='Введите название устройства')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    system = models.ForeignKey('System', on_delete=models.SET_NULL, null=True, verbose_name='Система')
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True, verbose_name='Тип')
    status = models.CharField(max_length=3, choices=STATUS, verbose_name='Статус устройства', default='w')
    description = models.TextField(verbose_name='Информация', null=True, blank=True)
    ip = models.CharField(max_length=15, verbose_name='IP', null=True, blank=True, help_text='Введите ip-адрес '
                                                                                             'устройства')
    serial = models.CharField(max_length=50, verbose_name='S/N', help_text='Введите серийный номер'
                                                                           ' устройства', null=True, blank=True)
    inventar_number = models.CharField(max_length=50,
                                       verbose_name='Инвентарный номер',
                                       help_text='Введите инвентарный номер',
                                       null=True,
                                       blank=True)

    def __str__(self):
        return f'{self.name} ({self.system})'
