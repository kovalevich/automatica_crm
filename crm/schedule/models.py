from django.db import models
from django.utils.translation import gettext_lazy as _


class Schedule(models.Model):

    class Status(models.IntegerChoices):
        ACTIVE = 0, _('Активно')
        FINISH = 1, _('Выполнено')
        OVERDUE = 2, _('Просрочено')
        ARCHIVED = 3, _('Архив')

    class Type(models.IntegerChoices):
        TO = 0, _('TO')
        CRASH = 1, _('Неисправность')
        CHECK = 2, _('Проверка')
        INSTRUCTION = 3, _('Инструктаж')
        OTHER = 4, _('Другое')

    class Level(models.IntegerChoices):
        SCHEDULE = 0, _('По графику')
        WARNING = 1, _('Важная задача')
        IMMEDIATELY = 2, _('Немедленное исполнение')

    name = models.CharField(max_length=100, verbose_name='Имя задачи',
                            help_text='Введите название задачи',
                            blank=True, null=True)
    date = models.DateField(verbose_name='Дата события')
    type = models.IntegerField(verbose_name='Тип задачи', choices=Type.choices, default=0)
    level = models.IntegerField(verbose_name='Срочность', choices=Level.choices, default=0)
    station = models.ForeignKey('devices.Station',
                                null=True,
                                blank=True,
                                verbose_name='Станция',
                                on_delete=models.SET_NULL,
                                default=3)
    device = models.ForeignKey('devices.Device',
                               null=True,
                               blank=True,
                               verbose_name='Устройство',
                               on_delete=models.SET_NULL)
    description = models.TextField(verbose_name='Заметки', blank=True, null=True)
    status = models.IntegerField(choices=Status.choices, default=0, verbose_name='Статус')

    def __str__(self):
        return f'{self.station if self.station else self.name} {self.Type.labels[self.type]}'
