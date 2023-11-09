from django.db import models

class Contato(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail')
    mensagem = models.TextField('Mensagem')
    criado_em = models.DateTimeField('data', auto_now_add=True)
    lido = models.BooleanField('Lido', default=False, blank=True)

    def __str__(self):
        return f'{self.nome} [{self.email}]'
    class Meta:
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contatos'
        ordering = ['-criado_em']

