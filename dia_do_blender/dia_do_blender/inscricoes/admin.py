from django.contrib import admin

from .models import Participante


class InteresseAdmin(admin.ModelAdmin):
    pass


class ParticipanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criacao'
    list_display = ('nome', 'email', 'telefone', 'criacao', 'atualizacao')
    list_filter = ('atualizacao', )
    search_fields = ('nome', 'email', 'cpf', 'rg')


admin.site.register(Participante, ParticipanteAdmin)
