# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, unicode_literals

from django.db import models
from localflavor.br.br_states import STATE_CHOICES


GENERO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
)


class Participante(models.Model):
    nome = models.CharField('* Nome', max_length=140)
    data_nascimento = models.DateField('* Data de nascimento')
    sexo = models.CharField(
        '* Sexo',
        max_length=1,
        choices=GENERO_CHOICES
    )
    cpf = models.CharField('* CPF (números)', max_length=11)
    rg = models.CharField('RG - Número', max_length=20, blank=True)
    rg_orgao_expedidor = models.CharField(
        'RG - Órgão expedidor',
        max_length=20,
        blank=True
    )
    rg_uf = models.CharField(
        'RG - UF',
        max_length=2,
        choices=STATE_CHOICES,
        blank=True
    )
    rg_data_expedicao = models.DateField(
        'RG - Data de Expedição',
        blank=True,
        null=True
    )

    logradouro = models.CharField('* Rua / Av./ Edif. / Etc.', max_length=140)
    numero = models.CharField('* Número', max_length=10)
    cep = models.CharField('* CEP (números)', max_length=8)
    bairro = models.CharField('* Bairro', max_length=80)
    cidade = models.CharField('* Cidade', max_length=80)
    uf = models.CharField(
        '* UF',
        max_length=2,
        choices=STATE_CHOICES
    )
    email = models.EmailField('E-mail', max_length=140, blank=True, null=True)

    telefone = models.CharField('Telefone', max_length=20, blank=True)
    telefone_alternativo = models.CharField(
        'Telefone alternativo',
        max_length=20,
        blank=True
    )

    criacao = models.DateTimeField('Data de cadastro', auto_now_add=True)
    atualizacao = models.DateTimeField('Data de atualização', auto_now=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'
        ordering = ['-criacao']
