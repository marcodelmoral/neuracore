# coding=utf-8

from __future__ import unicode_literals
from rest_framework import serializers
from .models import *

class AsanaSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ApisAsana
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class TeamViewerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ApisTeamviewer
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class SlackSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ApisSlack
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class AuthGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthGroup
        fields = ('name',)

class AuthGroupPermissionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthGroupPermissions
        fields = ('group',)
        read_only_fields = ('permission',)

class AuthPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthPermission
        fields = ('name',)
        read_only_fields = ('content_type', 'codename')

class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('password', 'first_name', 'last_name', 'username',
                  'email')
        read_only_fields = ('last_login', 'is_superuser', 'is_staff',
                            'is_active', 'date_joined')

class AuthUserGroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUserGroups
        fields = ('user', 'group')

class AuthUserUserPermissionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUserUserPermissions
        fields = ('user',)
        read_only_fields = ('permission',)

class CalificacionesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calificaciones
        read_only_fields = ('calificacionesid', 'calificacionesnombre')

class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientes
        fields = ('clientespass', 'clienteslogin', 'clientesnombre', 'clientedireccion', 'clientescorreo',
                  'clientestelefono', 'clientestipo', 'clientesrfc', 'clientesnacimiento')
        read_only_fields = ('clientesid', )

class DireccionclientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direccionclientes
        fields = ('calles', 'numerointerior', 'numeroexterior', 'zip', 'colonia', 'ciudad', 'estado', 'pais')
        read_only_fields = ('direccionclientesid', )

class DireccionEspecialistasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direccionclientes
        fields = ('calles', 'numerointerior', 'numeroexterior', 'zip', 'colonia', 'ciudad', 'estado', 'pais')
        read_only_fields = ('direccionespecialistasid', )

class DjangoAdminLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjangoAdminLog
        read_only_fields = ('action_time', 'object_id', 'object_repr', 'action_flag', 'change_message', 'content_type'
                            'user')

class DjangoContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjangoContentType
        read_only_fields = ('app_label', 'model')

class DjangoSlackOauthSlackoauthrequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjangoSlackOauthSlackoauthrequest
        read_only_fields = ('access_token', 'extras','ip', 'created', 'modified', 'associated_user')

class DjasanaAttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaAttachment
        fields = ('name', 'download_url', 'host', 'view_url', 'parent', 'permanent_url')
        read_only_fields = ('remote_id', 'created_at')

class DjasanaProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaProject
        fields = ('name', 'archived', 'color', 'current_status', 'layout', 'notes', 'public', 'owner', 'team'
                  'workspace')
        read_only_fields =('remote_id', 'created_at', 'due_date', 'modified_at')

class DjasanaProjectFollowersSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaProjectFollowers
        fields = ('project', 'user')

class DjasanaProjectMembersSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaProjectMembers
        fields = ('project', 'user')

class DjasanaStorySerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaStory
        fields = ('name', 'hearted', 'num_hearts', 'target', 'source', 'text', 'type')
        read_only_fields = ('remote_id', 'created_at', 'created_by')

class DjasanaStoryHeartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaStoryHearts
        fields = ('story', 'user')

class DjasanaSynctokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaSynctoken
        fields = ('sync', 'project')

class DjasanaTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaTag
        fields = ('name', )
        remote_id = ('remote_id', )

class DjasanaTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaTask
        fields = ('name', 'hearted', 'num_hearts', 'assignee_status', 'completed', 'notes', 'assignee', 'parent')
        read_only_fields = ('remote_id', 'completed_at', 'created_at', 'due_at', 'due_on', 'modified_at')

class DjasanaTaskFollowersSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaTaskFollowers
        fields = ('task', 'user')

class DjasanaTaskHeartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaTaskHearts
        fields = ('task', 'user')

class DjasanaTaskProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaTaskProjects
        fields = ('task', 'project')

class DjasanaTaskTagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaTaskTags
        fields = ('task', 'tag')

class DjasanaTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaTeam
        fields = ('name', 'organization_name')
        read_only_fields = ('remote_id', 'organization_id')

class DjasanaUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaUser
        fields = ('name', 'email', 'photo')
        read_only_fields = ('remote_id',)

class DjasanaUserWorkspacesSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaUserWorkspaces
        read_only_fields = ('user', 'workspace')

class DjasanaWebhookSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaWebhook
        read_only_fields = ('secret', 'project')

class DjasanaWorkspaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjasanaWorkspace
        fields = ('name', )
        read_only_fields = ('remote_id', 'is_organization')


class EspecialistasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Especialistas
        fields = ('especialistaslogin', 'especialistaspass', 'especialistasnombre',
                  'especialistasnacimiento','especialistasprofesion', 'especialistasexperiencia',
                  'especialistasnivel', 'especialistasnivel', 'especialisrasdireccion','especialistasdireccion',
                  'especialistasgrado','especialistastelefono','especialistasrol')
        read_only_fields = ('especialistasid', )

class EtapasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Etapas
        fields = ('etapasnombre', 'etapasduracion')
        read_only_fields = ('etapasid', )

class EtapasTareasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Etapastareas
        fields = ('tareasespecialista', 'tareasstatus', 'tareascalificacion')
        read_only_fields = ('etapastareasid', 'tareasetapasid')

class ExperienciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experiencia
        fields = ('experienciaarango', )
        read_only_fields = ('experienciaid', )

class GradosSerializer(serializers.ModelSerializer):

    class Meta:
        managed = False
        fields = ('grado', )
        read_only_fields = ('gradosid', )

class NivelesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Niveles
        fields = ('nivelnombre', )
        read_only_fields = ('nivelesid', )

class ProfesionesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profesiones
        fields = ('profesion', )
        read_only_fields = ('profesionesod', )

class ProyectoDescripcionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proyectodescripcion
        fields = ('etapaproyecto', 'etapaespecialista', 'etapastatus', 'etapacalificacion')
        read_only_fields = ('proyectoid', )

class ProyectosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proyectos
        fields = ('proyectonombre', 'proyectodescripcions','proyectoservicio','proyectoduracion','proyectoespecialista'
                  'proyectocliente','proyectostatus','proyetocalificacion','proyectoinicio','proyectofinal')
        read_only_fields = ('proyectoid', )

class RolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rol
        fields = ('roldescripcion', )
        read_only_fields = ('rolid', )

class ServiciosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servicios
        fields = ('serviciosnombre', 'serviciosdescripcion')
        read_only_fields = ('serviciosid', )

class SlackUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SlackUser
        read_only_fields = ('slacker', 'access_token', 'extras')

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('statusnombre', )
        read_only_fields = ('statusid', )

class StatusProyectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statusproyecto
        fields = ('statusproyecto', )
        read_only_fields = ('statusproyectoid', )

class TareasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tareas
        fields = ('tareasnombre', 'tareasduracion', )
        read_only_fields = ('tareasid', )

class TipoClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tipocliente
        fields = ('tipo', )
        read_only_fields = ('tipoclienteid', )

class CotizacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cotizacion
        fields = ('cotizacion', )
