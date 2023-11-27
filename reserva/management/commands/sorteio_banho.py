from django.core.management.base import BaseCommand
from reserva.models import Petshop
import random

#Comandos para que seja gerado um sorteio de um banho gratuito para Clientes.
class Command(BaseCommand):
    def list_petshops(self):
        return Petshop.objects.all().values_list('pk', flat=True)
    
    def escolher_reservas(self, banhos, quantidade):
        banhos_list = list(banhos)
        if quantidade > len(banhos_list):
            quantidade = len(banhos_list)
        
        return random.sample(banhos_list, quantidade)


    def add_arguments(self, parser):
        parser.add_argument(
            'quantidade',
            nargs='?',
            default=5,
            type=int,
            help='Quantas pessoas irão participar do Sorteio'
        )
        parser.add_argument(
            '-petshop',
            required=True,
            type=int,
            choices=self.list_petshops(),
            help='ID do Petshop para o Sorteio'
        )

    def imprimir_info_petshop(self, petshop):
        self.stdout.write(
            self.style.HTTP_INFO(
                'Dados do Petshop que realizou o Sorteio'
            )
        )
        self.stdout.write(f'Nome do Petshop: {petshop.nome}')
        self.stdout.write(
            f'Endereço: {petshop.rua}. {petshop.numero} - {petshop.bairro}'
        )

    def imprimir_reservas_sorteadas(self, reservas):
        self.stdout.write()
        self.stdout.write(
            self.style.HTTP_INFO(
                'Dados das pessoas sorteadas'
            )
        )
        self.stdout.write(
            self.style.HTTP_INFO(
                '=' * 35
            )
        )

        for reserva in reservas:
            self.stdout.write(
                f'Nome: {reserva.nome} - {reserva.email}'
            )
            self.stdout.write(
                self.style.HTTP_INFO(
                    '=' * 35
                )
            )

    def handle(self, *args, **options):
        quantidade = options['quantidade'] #guardando os argumentos passados em variáveis
        id_petshop = options['petshop']

        petshop = Petshop.objects.get(pk=id_petshop)
        reservas = petshop.reservas.all()

        banhos_escolhidos = self.escolher_reservas(reservas, quantidade)
        self.stdout.write(
            self.style.SUCCESS('SORTEIO CONCLUÍDO!')
        )
        self.imprimir_info_petshop(petshop)
        self.imprimir_reservas_sorteadas(banhos_escolhidos)

