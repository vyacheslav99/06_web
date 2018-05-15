# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone

class Contractor(models.Model):
    """ Контрагенты: кредитные организации, партнеры ... """

    CONTR_TYPE_CHOICES = (('b', 'Кредитная организация'), ('p', 'Партнер'))

    inn = models.CharField(max_length=12, unique=True)
    contr_name = models.CharField(max_length=256)
    address = models.CharField(max_length=1024)
    contr_type = models.CharField(max_length=1, choices=CONTR_TYPE_CHOICES)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return '{0}: {1}'.format(self.inn, self.contr_name.encode('utf-8'))
        #return '{0}: {1}'.format(self.inn, self.contr_name)

    def __unicode__(self):
        return u'{0}: {1}'.format(self.inn, self.contr_name)

class Proposal(models.Model):
    """ Предложения """

    PROPOSAL_TYPE_CHOICES = (('c', 'Потреб'), ('m', 'Ипотека'), ('a', 'Автокредит'))

    create_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True, null=True)
    start_rotation_date = models.DateTimeField(null=True, blank=True)
    stop_rotation_date = models.DateTimeField(null=True, blank=True)
    proposal_name = models.CharField(max_length=256)
    proposal_type = models.CharField(max_length=1, choices=PROPOSAL_TYPE_CHOICES)
    min_scor_ball = models.PositiveIntegerField(default=1)
    max_scor_ball = models.PositiveIntegerField(default=1)
    credit_contr = models.ForeignKey(Contractor, on_delete=models.PROTECT)

    def __str__(self):
        return '{0}: {1}'.format(self.id, self.proposal_name.encode('utf-8'))
        #return '{0}: {1}'.format(self.id, self.proposal_name)

    def __unicode__(self):
        return u'{0}: {1}'.format(self.id, self.proposal_name)

class ClientProfile(models.Model):
    """ Анкеты клиентов """

    create_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True, null=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    father_name = models.CharField(max_length=128, null=True, blank=True)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=32)
    passport_num = models.CharField(max_length=11, unique=True)
    scor_ball = models.PositiveIntegerField(default=1)
    partner_contr = models.ForeignKey(Contractor, on_delete=models.PROTECT)

    def __str__(self):
        return '{0}: {1} {2} {3}'.format(self.id, self.last_name.encode('utf-8'), self.first_name.encode('utf-8'),
                                         self.father_name.encode('utf-8'))
        #return '{0}: {1} {2} {3}'.format(self.id, self.last_name, self.first_name, self.father_name)

    def __unicode__(self):
        return u'{0}: {1} {2} {3}'.format(self.id, self.last_name, self.first_name, self.father_name)

class Order(models.Model):
    """ Заявки на получение криедита """

    ORDER_STATUS = (('0', 'Новая'), ('1', 'Отправлена'), ('2', 'Получена'), ('3', 'Одобрено'),
        ('4', 'Отказано'), ('5', 'Выдано'))

    create_date = models.DateTimeField(auto_now_add=True)
    post_date = models.DateTimeField(default=django.utils.timezone.now)
    client_profile = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    proposal = models.ForeignKey(Proposal, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default='0')

    def __str__(self):
        return '{0}, from {1}'.format(self.id, self.create_date)

    def __unicode__(self):
        return u'{0}, from {1}'.format(self.id, self.create_date)
