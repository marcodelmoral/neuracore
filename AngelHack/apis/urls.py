# coding=utf-8

from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    url(r'^asana/$', CreateViewAsana.as_view(), name="asana"),
    url(r'^slack/api/$', CreateViewSlack.as_view(), name="slack"),
    url(r'^teamviewer/$', CreateViewTeamViewer.as_view(), name="teamviewer"),
    #url(r'^auth/asana/callback', CreateViewA.as_view(), name="asana_auth"),
    url(r'^auth/group/$', CreateViewAuthGroup.as_view(), name="auth_group"),
    url(r'^auth/group/permission/s$', CreateViewAuthGroupPermissions.as_view(), name="auth_group_permissions"),
    url(r'^auth/permissions/$', CreateViewAuthGroupPermissions.as_view(), name="auth_permissions"),
    url(r'^auth/user/$', CreateViewAuthUser.as_view(), name="auth_user"),
    url(r'^auth/user/groups/$', CreateViewAuthUserGroups.as_view(), name="auth_user_groups"),
    url(r'^auth/user/user/permissions/$', CreateViewAuthUserUserPermissions.as_view(), name="auth_user_user_permissions"),
    url(r'^auth/user/permissions/$', CreateViewAuthUserPermissions.as_view(), name="auth_user_permissions"),
    url(r'^calificaciones/$', CreateViewCalificaciones.as_view(), name="calificaciones"),
    url(r'^clientes/$', CreateViewClientes.as_view(), name="clientes"),
    url(r'^direcciones/clientes/$', CreateViewDireccionesClientes.as_view(), name="direcciones_clientes"),
    url(r'^direcciones/especiales/$', CreateViewDireccionesEspeciales.as_view(), name="direcciones_especiales"),
    url(r'^slack/oauth/$', CreateViewDjangoSlackOauthSlackoauthrequest.as_view(), name="slack_oauth"),
    url(r'^asana/attachment$/', CreateViewDjasanaAttachment.as_view(), name="asana_attachment"),
    url(r'^asana/project/$', CreateViewDjasanaProject.as_view(), name="asana_project"),
    url(r'^asana/project/followers/$', CreateViewDjasanaProjectFollowers.as_view(), name="asana_project_followers"),
    url(r'^asana/story/$', CreateViewDjasanaStory.as_view(), name="asana_story"),
    url(r'^asana/story/hearts/$', CreateViewDjasanaStoryHearts.as_view(), name="asana_story_hearts"),
    url(r'^asana/sync/token/$', CreateViewDjasanaSynctoken.as_view(), name="asana_sync_token"),
    url(r'^asana/task/$', CreateViewDjasanaTask.as_view(), name="asana_task"),
    url(r'^asana/task/followers/$', CreateViewDjasanaTaskFollowers.as_view(), name="asana_task_followers"),
    url(r'^asana/task/projects/$', CreateViewDjasanaTaskProjects.as_view(), name="asana_task_projects"),
    url(r'^asana/task/tag/$', CreateViewDjasanaTaskTags.as_view(), name="asana_task_tag"),
    url(r'^asana/team/$', CreateViewDjasanaTeam.as_view(), name="asana_team"),
    url(r'^asana/user/$', CreateViewDjasanaUser.as_view(), name="asana_user"),
    url(r'^asana/user/workspace/$', CreateViewDjasanaUserWorkspaces.as_view(), name="asana_user_workspace"),
    url(r'^especialistas/$', CreateViewEspecialistas.as_view(), name="especialistas"),
    url(r'^etapas/$', CreateViewEtapas.as_view(), name="etapas"),
    url(r'^etapas/tareas/$', CreateViewEtapasTareas.as_view(), name="etapas_tareas"),
    url(r'^experiencia/$', CreateViewExperiencia.as_view(), name="experiencias"),
    url(r'^grados/$', CreateViewGrados.as_view(), name="grados"),
    url(r'^niveles/$', CreateViewNiveles.as_view(), name="niveles"),
    url(r'^profesiones/$', CreateViewProfesiones.as_view(), name="profesiones"),
    url(r'^proyecto/descripcion/$', CreateViewProyectoDescipcion.as_view(), name="proyectos_descripcion"),
    url(r'^proyectos/$', CreateViewDjasanaProjectMembers.as_view(), name="asana_project_members"),
    url(r'^rol/$', CreateViewRol.as_view(), name="rol"),
    url(r'^servicios/$', CreateViewServicios.as_view(), name="servicios"),
    url(r'^slack/user/$', CreateViewSlackUser.as_view(), name="slack_user"),
    url(r'^status/$', CreateViewStatus.as_view(), name="status"),
    url(r'^status/proyectos/$', CreateViewStatusProyeto.as_view(), name="status_proyecto"),
    url(r'^tareas/$', CreateViewTareas.as_view(), name="tareas"),
    url(r'^tipo/cliente/$', CreateViewTipoCliente.as_view(), name="tipo_cliente"),
    url(r'^cotizacion/$', CreateViewCotizacion.as_view(), name="cotizacion"),
}

urlpatterns = format_suffix_patterns(urlpatterns)