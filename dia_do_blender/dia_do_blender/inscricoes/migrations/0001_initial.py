# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Participante'
        db.create_table(u'inscricoes_participante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('data_nascimento', self.gf('django.db.models.fields.DateField')()),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cpf', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('rg', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('rg_orgao_expedidor', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('rg_uf', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('rg_data_expedicao', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('logradouro', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('bairro', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('cidade', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('uf', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=140, null=True, blank=True)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('telefone_alternativo', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'inscricoes', ['Participante'])


    def backwards(self, orm):
        # Deleting model 'Participante'
        db.delete_table(u'inscricoes_participante')


    models = {
        u'inscricoes.participante': {
            'Meta': {'ordering': "[u'criacao']", 'object_name': 'Participante'},
            'atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logradouro': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'rg_data_expedicao': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'rg_orgao_expedidor': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'rg_uf': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'telefone_alternativo': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['inscricoes']