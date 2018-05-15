# -*- coding: utf-8 -*-

from django.contrib import admin

import credit.models as models

class ContractorAdmin(admin.ModelAdmin):
    fields = ('inn', 'contr_type', 'contr_name', 'user_id', 'address')
    list_display = ('inn', 'contr_type', 'contr_name', 'user_id', 'address')
    list_filter = ('contr_type', 'user_id')
    search_fields = ('=inn', 'contr_name')
    raw_id_fields = ('user_id',)

class ProposalAdmin(admin.ModelAdmin):
    fields = ('create_date', 'proposal_name', 'proposal_type', 'credit_contr', 'min_scor_ball', 'max_scor_ball',
        'start_rotation_date', 'stop_rotation_date', 'change_date')
    list_display = ('create_date', 'proposal_name', 'proposal_type', 'credit_contr', 'min_scor_ball', 'max_scor_ball',
        'start_rotation_date', 'stop_rotation_date', 'change_date')
    readonly_fields = ('create_date', 'change_date')
    list_filter = ('proposal_type', 'credit_contr', 'create_date', 'start_rotation_date', 'stop_rotation_date')
    search_fields = ('proposal_name',)
    #raw_id_fields = ('credit_contr',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # выпадающие списки контрагентов надо фильтровать: вываливаем только кредитные орг. (тип b)
        if db_field.name == "credit_contr":
            kwargs["queryset"] = models.Contractor.objects.filter(contr_type='b')

        return super(ProposalAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class ClientProfileAdmin(admin.ModelAdmin):
    fields = ('last_name', 'first_name', 'father_name', 'passport_num', 'partner_contr', 'scor_ball',
        'phone_number', 'birthday', 'create_date', 'change_date')
    list_display = ('last_name', 'first_name', 'father_name', 'passport_num', 'partner_contr', 'scor_ball',
        'phone_number', 'birthday', 'create_date', 'change_date')
    readonly_fields = ('create_date', 'change_date')
    list_filter = ('partner_contr',)
    search_fields = ('^last_name', '^first_name', '^father_name', '=passport_num', '=phone_number', '=birthday')
    #raw_id_fields = ('partner_contr',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # выпадающие списки контрагентов надо фильтровать: вываливаем только партнеров (тип p)
        if db_field.name == "partner_contr":
            kwargs["queryset"] = models.Contractor.objects.filter(contr_type='p')

        return super(ClientProfileAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class OrderAdmin(admin.ModelAdmin):
    fields = ('status', 'create_date', 'post_date', 'client_profile', 'proposal')
    list_display = ('status', 'create_date', 'post_date', 'client_profile', 'proposal')
    readonly_fields = ('create_date',)
    list_filter = ('status', 'proposal', 'client_profile')
    search_fields = ('=post_date', '=create_date', '=client_profile')
    raw_id_fields = ('client_profile', 'proposal')

admin.site.register(models.Contractor, ContractorAdmin)
admin.site.register(models.Proposal, ProposalAdmin)
admin.site.register(models.ClientProfile, ClientProfileAdmin)
admin.site.register(models.Order, OrderAdmin)
