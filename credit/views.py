# -*- coding: utf-8 -*-

from django.core import exceptions
from rest_framework import viewsets

from credit import models
from credit import serializers

class ProfileViewSet(viewsets.ModelViewSet):

    queryset = models.ClientProfile.objects.all()
    serializer_class = serializers.ClientProfileSerializer

    def get_queryset(self):
        order_by = self.request.POST.get('order_by', [])
        filters = self.request.POST.get('filters', {})

        if self.request.user.is_superuser or 'administartors' in self.request.user.groups:
            pass
        elif 'partners' in self.request.user.groups:
            filters.update({'partner_contr__user_id__exact': self.request.user.id})
        else:
            raise exceptions.PermissionDenied()

        if filters:
            queryset = self.queryset.filter(**filters)
        else:
            queryset = self.queryset

        if order_by:
            queryset = queryset.order_by(*order_by)

        return queryset

    def perform_create(self, serializer):
        # добавлять могут только суперпользователи или партнеры
        if self.request.user.is_superuser or 'administartors' in self.request.user.groups or 'partners' in self.request.user.groups:
            super(ProfileViewSet, self).perform_create(serializer)
            self.queryset[0].refresh_from_db()
        else:
            raise exceptions.PermissionDenied()

    def perform_update(self, serializer):
        # редактировать могут только суперпользователи
        if self.request.user.is_superuser or 'administartors' in self.request.user.groups:
            super(ProfileViewSet, self).perform_update(serializer)
            self.queryset.get(id=self.request.POST.get('id')).refresh_from_db()
        else:
            raise exceptions.PermissionDenied()

    def perform_destroy(self, instance):
        # удалять могут только суперпользователи
        if self.request.user.is_superuser or 'administartors' in self.request.user.groups:
            super(ProfileViewSet, self).perform_destroy(instance)
            self.queryset.get(id=self.request.POST.get('id')).refresh_from_db()
        else:
            raise exceptions.PermissionDenied()

class OrderViewSet(viewsets.ModelViewSet):

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        order_by = self.request.POST.get('order_by', [])
        filters = self.request.POST.get('filters', {})

        if self.request.user.is_superuser or 'administartors' in self.request.user.groups:
            pass
        elif 'partners' in self.request.user.groups:
            filters.update({'client_profile__partner_contr__user_id__exact': self.request.user.id})
        elif 'credit_org' in self.request.user.groups:
            filters.update({'proposal__credit_contr__user_id__exact': self.request.user.id})
        else:
            raise exceptions.PermissionDenied()

        if filters:
            queryset = self.queryset.filter(**filters)
        else:
            queryset = self.queryset

        if order_by:
            queryset = queryset.order_by(*order_by)

        return queryset

    def perform_create(self, serializer):
        # добавлять могут только суперпользователи или партнеры
        if self.request.user.is_superuser or 'administartors' in self.request.user.groups or 'partners' in self.request.user.groups:
            super(OrderViewSet, self).perform_create(serializer)
            self.queryset[0].refresh_from_db()
        else:
            raise exceptions.PermissionDenied()

    def perform_update(self, serializer):
        # редактировать могут только суперпользователи, кредитные могут менять статус
        if self.request.user.is_superuser or 'administartors' in self.request.user.groups:
            super(OrderViewSet, self).perform_update(serializer)
            self.queryset.get(id=self.request.POST.get('id')).refresh_from_db()
        elif 'credit_org' in self.request.user.groups:
            #super(OrderViewSet, self).perform_update(serializer)
            serializer.save(update_fields=['status'])
            self.queryset.get(id=self.request.POST.get('id')).refresh_from_db()
        else:
            raise exceptions.PermissionDenied()

    def perform_destroy(self, instance):
        # удалять могут только суперпользователи
        if self.request.user.is_superuser or 'administartors' in self.request.user.groups:
            super(OrderViewSet, self).perform_destroy(instance)
            self.queryset.get(id=self.request.POST.get('id')).refresh_from_db()
        else:
            raise exceptions.PermissionDenied()
