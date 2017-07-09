# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from AngelHack import difusa
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class LoginView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': (u'request.user'),  # `django.contrib.auth.User` instance.
            'auth': (u'request.auth'),  # None
        }
        return Response(content)


class CreateViewAsana(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ApisAsana.objects.all()
    serializer_class = AsanaSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()


class CreateViewTeamViewer(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ApisTeamviewer.objects.all()
    serializer_class = TeamViewerSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()


class CreateViewSlack(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ApisSlack.objects.all()
    serializer_class = SlackSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewAuthGroup(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest ap3i."""
    queryset = AuthGroup.objects.all()
    serializer_class = AuthGroupSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewAuthGroupPermissions(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = AuthGroupPermissions.objects.all()
    serializer_class = AuthGroupPermissionsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewAuthPermission(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = AuthPermission.objects.all()
    serializer_class = AuthPermissionSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewAuthUser(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()
class CreateViewAuthUserGroups(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = AuthUserGroups.objects.all()
    serializer_class = AuthUserGroupsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewAuthUserUserPermissions(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = AuthUserUserPermissions.objects.all()
    serializer_class = AuthUserUserPermissionsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewAuthUserPermissions(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = AuthUserUserPermissions.objects.all()
    serializer_class = AuthUserUserPermissionsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewCalificaciones(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Calificaciones.objects.all()
    serializer_class = Calificaciones

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewClientes(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDireccionesClientes(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Direccionclientes.objects.all()
    serializer_class = DireccionclientesSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDireccionesEspeciales(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Direccionespecialistas.objects.all()
    serializer_class = DireccionEspecialistasSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjangoAdminLog(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjangoAdminLog.objects.all()
    serializer_class = DjangoAdminLogSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()


class CreateViewDjangoContentType(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjangoContentType.objects.all()
    serializer_class = DjangoContentTypeSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()


class CreateViewDjangoSlackOauthSlackoauthrequest(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjangoSlackOauthSlackoauthrequest.objects.all()
    serializer_class = DjangoSlackOauthSlackoauthrequestSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()


class CreateViewDjasanaAttachment(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaAttachment.objects.all()
    serializer_class = DjasanaAttachmentSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjasanaProject(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaProject.objects.all()
    serializer_class = DjasanaProjectSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjasanaProjectFollowers(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaProjectFollowers.objects.all()
    serializer_class = DjasanaProjectFollowersSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjasanaProjectMembers(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaProjectMembers.objects.all()
    serializer_class = DjasanaProjectMembersSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjasanaStory(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaStory.objects.all()
    serializer_class = DjasanaStorySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjasanaStoryHearts(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaStoryHearts.objects.all()
    serializer_class = DjasanaStoryHeartsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjasanaSynctoken(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaSynctoken.objects.all()
    serializer_class = DjasanaSynctokenSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjasanaTask(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaTask.objects.all()
    serializer_class = DjasanaTaskSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjasanaTaskFollowers(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaTaskFollowers.objects.all()
    serializer_class = DjasanaTaskFollowersSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjasanaTaskProjects(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaTaskProjects.objects.all()
    serializer_class = DjasanaTaskProjectsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjasanaTaskTags(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaTask.objects.all()
    serializer_class = DjasanaTaskTags

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjasanaTeam(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaTeam.objects.all()
    serializer_class = DjasanaTeamSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjasanaUser(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaUser.objects.all()
    serializer_class = DjasanaUserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewDjasanaUserWorkspaces(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DjasanaUserWorkspaces.objects.all()
    serializer_class = DjasanaUserWorkspacesSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewEspecialistas(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Especialistas.objects.all()
    serializer_class = EspecialistasSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewEtapas(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Etapas.objects.all()
    serializer_class = EtapasSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewEtapasTareas(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Etapastareas.objects.all()
    serializer_class = EtapasTareasSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewExperiencia(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewGrados(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Grados.objects.all()
    serializer_class = GradosSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewNiveles(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Niveles.objects.all()
    serializer_class = NivelesSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewProfesiones(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Profesiones.objects.all()
    serializer_class = ProfesionesSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewProyectoDescipcion(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Proyectodescripcion.objects.all()
    serializer_class = ProyectoDescripcionSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewProyetos(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewRol(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewServicios(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewSlackUser(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = SlackUser.objects.all()
    serializer_class = SlackUserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewStatus(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewStatusProyeto(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Statusproyecto.objects.all()
    serializer_class = StatusProyectoSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewTareas(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewTipoCliente(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Tipocliente.objects.all()
    serializer_class = TipoClienteSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

class CreateViewCotizacion(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    cot = Cotizacion
    cotizacion = difusa.fuzzy()
    cotizacion = difusa.cotizacion(difusa.calcula(100, 15, 3, cotizacion), 10, 3, 5, 6, 8, 6, 4)
    cot.cotizacion = cotizacion
    # cot.save()
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer


    def perform_create(self, serializer):
        """Save the post data when creating a new neuracore."""
        serializer.save()

