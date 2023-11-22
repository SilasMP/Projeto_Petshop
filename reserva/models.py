from django.db import models

class CamposComuns(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Reserva(CamposComuns):
    TAMANHO_OPCOES = [
        ('pequeno', 'Pequeno'),
        ('medio', 'Médio'),
        ('grande', 'Grande'),
    ]
    TURNO_OPCOES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
    ]
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail')
    data = models.DateField('Data')
    turno = models.CharField('Turno', max_length=10, choices=TURNO_OPCOES)
    tamanho = models.CharField('Tamanho do PET', max_length=10, choices=TAMANHO_OPCOES)
    categoria = models.ForeignKey(
        'Categoria',
        related_name='reservas',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    observacoes = models.TextField('Observações', blank=True)
    petshop = models.ForeignKey(
        'Petshop',
        related_name='reservas',
        on_delete=models.CASCADE,
    )
    
    lido = models.BooleanField('Lido', default=False, blank=True)

    def __str__(self):
        return f'{self.nome}: {self.data} - {self.turno}'
    
    class Meta:
        verbose_name = 'Reserva de Banho'
        verbose_name_plural = 'Reservas de Banho'
        ordering = ['id']

class Petshop(CamposComuns):
    nome = models.CharField('Petshop', max_length=50)
    rua = models.CharField('Endereço', max_length=100)
    numero = models.CharField('Número', max_length=10)
    bairro = models.CharField('Bairro', max_length=50)

    def __str__(self):
        return f'{self.nome} : [{self.bairro}]'
    
    def qtda_reservas(self):
        return self.reservas.count()
    
    class Meta:
        verbose_name = 'Petshop Cadastrado'
        verbose_name_plural = 'Petshops Cadastrados'
        ordering = ['id']

class Categoria(CamposComuns):
    nome = models.CharField('Categoria', max_length=50)

    def __str__(self):
        return self.nome