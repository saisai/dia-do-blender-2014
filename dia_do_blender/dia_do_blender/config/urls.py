from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

from ..inscricoes.views import CadastrarParticipante, ListarParticipantes

urlpatterns = patterns(
    '',
    url(r'^$', CadastrarParticipante.as_view(),
        name='inscricoes-cadastrar-participante'),
    url(r'^lista-de-participantes/', ListarParticipantes.as_view(),
        name='inscricoes-listar-participantes'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
