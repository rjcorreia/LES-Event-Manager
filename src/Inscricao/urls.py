from django.urls import path

import Inscricao.views
from .views import CriarInscricao, PartConsultarInscricoes, PartInscricaoCancelar,\
    PropAlterarEstadoInscricao, PropConsultarInscricoes, PropRemoverInscricao,  PartInscricaoCheckin,\
    PartAlterarInscricao,  returnCurrentEstado, updateEstado, PropConsultarCheckIns, doCheckin, PropAlterarInscricao, consultarInscricaoProp, consultarInscricaoPart, create_csv_certificates

app_name = 'Inscricao'

urlpatterns = [



    # URL'S para os participantes
    path('create/<int:eventoid>/', CriarInscricao, name='create_inscricao'),
    path('', PartConsultarInscricoes.as_view(), name='part_list_inscricao'),
    path('evento/<int:eventoid>', PropConsultarInscricoes.as_view(), name='prop_list_inscricao'),
    path('delete/<int:inscricaoid>/', PartInscricaoCancelar, name='part_delete_inscricao'),
    path('evento/delete/<int:inscricaoid>/', PropRemoverInscricao, name='prop_delete_inscricao'),
    path('evento/update/<int:id>/', PropAlterarEstadoInscricao, name='prop_update_inscricao'),
    path('update/<int:id>/', PartInscricaoCheckin, name='part_update_inscricao'),
    path('alterar/<int:id>', PartAlterarInscricao, name='part_alterar_inscricao'),
    path('getInsEstado/<int:id>', returnCurrentEstado, name='get_ins_estado'),
    path('updateEstado/<int:id>', updateEstado ),
    path('checkIns/<int:eventoid>', PropConsultarCheckIns.as_view(), name='consultar_checkins' ),
    path('doCheckin/<int:id>', doCheckin),
    path('alterarProp/<int:id>', PropAlterarInscricao, name='prop_alterar_inscricao'),
    path('certificados/<int:evento_id>', create_csv_certificates, name='certificates_csv'),

    #URL'S para os proponentes


    #URL's para ambos
    path('consultar/<int:inscricaoid>', consultarInscricaoPart, name='consultar_inscricao_part'),
    path('consulta/<int:inscricaoid>', consultarInscricaoProp, name='consultar_inscricao_prop'),

]
