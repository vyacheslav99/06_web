# -*- coding: utf-8 -*-

from rest_framework import serializers

from credit import models

class ClientProfileSerializer(serializers.HyperlinkedModelSerializer):

    partner_contr = serializers.PrimaryKeyRelatedField(queryset = models.Contractor.objects.filter(contr_type__exact='p'))

    class Meta:
        model = models.ClientProfile
        fields = ('last_name', 'first_name', 'father_name', 'passport_num', 'partner_contr', 'scor_ball',
            'phone_number', 'birthday', 'create_date', 'change_date')

class OrderSerializer(serializers.HyperlinkedModelSerializer):

    client_profile = serializers.PrimaryKeyRelatedField(queryset = models.ClientProfile.objects.all())
    proposal = serializers.PrimaryKeyRelatedField(queryset = models.Proposal.objects.all())

    class Meta:
        model = models.Order
        fields = ('status', 'create_date', 'post_date', 'client_profile', 'proposal')
