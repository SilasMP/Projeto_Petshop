from django.contrib import admin
from reserva.models import Reserva
from django.contrib import messages

@admin.action(description='Marcar Reserva(s) como lida(s)')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Reserva(s) marcada(s) como lida(s)', messages.SUCCESS)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'lido','data', 'turno']
    search_fields = ['nome', 'tamanho']
    list_filter = ['data', 'turno', 'lido']
    actions = [marcar_como_lido]