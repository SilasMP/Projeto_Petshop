from django.contrib import admin
from base.models import Contato
from django.contrib import messages

@admin.action(description='Marcar Formulario(s) de contato como lido(s)')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Formulario de contato marcado(s) como lido(s)', messages.SUCCESS)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'lido','criado_em']
    search_fields = ['nome', 'email']
    list_filter = ['criado_em', 'lido']
    actions = [marcar_como_lido]