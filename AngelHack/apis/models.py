# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class ApisAsana(models.Model):
    name = models.CharField(unique=True, max_length=255)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'apis_asana'


class ApisSlack(models.Model):
    name = models.CharField(unique=True, max_length=255)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'apis_slack'


class ApisTeamviewer(models.Model):
    name = models.CharField(unique=True, max_length=255)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'apis_teamviewer'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Calificaciones(models.Model):
    calificacionesid = models.AutoField(primary_key=True)
    calificacionesnombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calificaciones'


class Clientes(models.Model):
    clientesid = models.AutoField(primary_key=True)
    clienteslogin = models.CharField(max_length=50, blank=True, null=True)
    clientespass = models.CharField(max_length=50, blank=True, null=True)
    clientesnombre = models.CharField(max_length=50, blank=True, null=True)
    clientedireccion = models.ForeignKey('Direccionclientes', models.DO_NOTHING, db_column='clientedireccion', blank=True, null=True)
    clientescorreo = models.CharField(max_length=30, blank=True, null=True)
    clientestelefono = models.CharField(max_length=30, blank=True, null=True)
    clientestipo = models.ForeignKey('Tipocliente', models.DO_NOTHING, db_column='clientestipo', blank=True, null=True)
    clientesrfc = models.CharField(max_length=13, blank=True, null=True)
    clientesnacimiento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class Direccionclientes(models.Model):
    direccionclientesid = models.AutoField(primary_key=True)
    calles = models.CharField(max_length=60, blank=True, null=True)
    numerointerior = models.CharField(max_length=10, blank=True, null=True)
    numeroexterior = models.CharField(max_length=10, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    colonia = models.CharField(max_length=30, blank=True, null=True)
    ciudad = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    pais = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccionclientes'


class Direccionespecialistas(models.Model):
    direccionespecialistasid = models.AutoField(primary_key=True)
    calles = models.CharField(max_length=60, blank=True, null=True)
    numerointerior = models.CharField(max_length=10, blank=True, null=True)
    numeroexterior = models.CharField(max_length=10, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    colonia = models.CharField(max_length=30, blank=True, null=True)
    ciudad = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    pais = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccionespecialistas'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSlackOauthSlackoauthrequest(models.Model):
    access_token = models.CharField(max_length=128, blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    associated_user = models.OneToOneField(AuthUser, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_slack_oauth_slackoauthrequest'


class DjasanaAttachment(models.Model):
    remote_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=1024)
    created_at = models.DateTimeField()
    download_url = models.CharField(max_length=1024)
    host = models.CharField(max_length=24)
    permanent_url = models.CharField(max_length=1024)
    view_url = models.CharField(max_length=1024)
    parent = models.ForeignKey('DjasanaTask', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djasana_attachment'


class DjasanaProject(models.Model):
    remote_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=1024)
    archived = models.BooleanField()
    color = models.CharField(max_length=16, blank=True, null=True)
    created_at = models.DateTimeField()
    current_status = models.CharField(max_length=16, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    layout = models.CharField(max_length=16)
    modified_at = models.DateTimeField()
    notes = models.TextField()
    public = models.BooleanField()
    owner = models.ForeignKey('DjasanaUser', models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey('DjasanaTeam', models.DO_NOTHING)
    workspace = models.ForeignKey('DjasanaWorkspace', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djasana_project'


class DjasanaProjectFollowers(models.Model):
    project = models.ForeignKey(DjasanaProject, models.DO_NOTHING)
    user = models.ForeignKey('DjasanaUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djasana_project_followers'
        unique_together = (('project', 'user'),)


class DjasanaProjectMembers(models.Model):
    project = models.ForeignKey(DjasanaProject, models.DO_NOTHING)
    user = models.ForeignKey('DjasanaUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djasana_project_members'
        unique_together = (('project', 'user'),)


class DjasanaStory(models.Model):
    remote_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=1024)
    hearted = models.BooleanField()
    num_hearts = models.SmallIntegerField()
    created_at = models.DateTimeField()
    target = models.BigIntegerField()
    source = models.CharField(max_length=16)
    text = models.CharField(max_length=1024)
    type = models.CharField(max_length=16)
    created_by = models.ForeignKey('DjasanaUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djasana_story'


class DjasanaStoryHearts(models.Model):
    story = models.ForeignKey(DjasanaStory, models.DO_NOTHING)
    user = models.ForeignKey('DjasanaUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djasana_story_hearts'
        unique_together = (('story', 'user'),)


class DjasanaSynctoken(models.Model):
    sync = models.CharField(max_length=36)
    project = models.ForeignKey(DjasanaProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djasana_synctoken'


class DjasanaTag(models.Model):
    remote_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'djasana_tag'


class DjasanaTask(models.Model):
    remote_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=1024)
    hearted = models.BooleanField()
    num_hearts = models.SmallIntegerField()
    assignee_status = models.CharField(max_length=16)
    completed = models.BooleanField()
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    due_at = models.DateTimeField(blank=True, null=True)
    due_on = models.DateField(blank=True, null=True)
    modified_at = models.DateTimeField()
    notes = models.TextField()
    assignee = models.ForeignKey('DjasanaUser', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djasana_task'


class DjasanaTaskFollowers(models.Model):
    task = models.ForeignKey(DjasanaTask, models.DO_NOTHING)
    user = models.ForeignKey('DjasanaUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djasana_task_followers'
        unique_together = (('task', 'user'),)


class DjasanaTaskHearts(models.Model):
    task = models.ForeignKey(DjasanaTask, models.DO_NOTHING)
    user = models.ForeignKey('DjasanaUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djasana_task_hearts'
        unique_together = (('task', 'user'),)


class DjasanaTaskProjects(models.Model):
    task = models.ForeignKey(DjasanaTask, models.DO_NOTHING)
    project = models.ForeignKey(DjasanaProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djasana_task_projects'
        unique_together = (('task', 'project'),)


class DjasanaTaskTags(models.Model):
    task = models.ForeignKey(DjasanaTask, models.DO_NOTHING)
    tag = models.ForeignKey(DjasanaTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djasana_task_tags'
        unique_together = (('task', 'tag'),)


class DjasanaTeam(models.Model):
    remote_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=1024)
    organization_id = models.BigIntegerField(blank=True, null=True)
    organization_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'djasana_team'


class DjasanaUser(models.Model):
    remote_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=1024)
    email = models.CharField(max_length=254)
    photo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djasana_user'


class DjasanaUserWorkspaces(models.Model):
    user = models.ForeignKey(DjasanaUser, models.DO_NOTHING)
    workspace = models.ForeignKey('DjasanaWorkspace', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djasana_user_workspaces'
        unique_together = (('user', 'workspace'),)


class DjasanaWebhook(models.Model):
    secret = models.CharField(max_length=64)
    project = models.ForeignKey(DjasanaProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djasana_webhook'


class DjasanaWorkspace(models.Model):
    remote_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=1024)
    is_organization = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'djasana_workspace'


class Especialistas(models.Model):
    especialistasid = models.AutoField(primary_key=True)
    especialistaslogin = models.CharField(max_length=50, blank=True, null=True)
    especialistaspass = models.CharField(max_length=50, blank=True, null=True)
    especialistasnombre = models.CharField(max_length=50, blank=True, null=True)
    especialistasnacimiento = models.DateField(blank=True, null=True)
    especialistasprofesion = models.ForeignKey('Profesiones', models.DO_NOTHING, db_column='especialistasprofesion', blank=True, null=True)
    especialistasexperiencia = models.ForeignKey('Experiencia', models.DO_NOTHING, db_column='especialistasexperiencia', blank=True, null=True)
    especialistasnivel = models.ForeignKey('Niveles', models.DO_NOTHING, db_column='especialistasnivel', blank=True, null=True)
    especialistasdireccion = models.ForeignKey(Direccionespecialistas, models.DO_NOTHING, db_column='especialistasdireccion', blank=True, null=True)
    especialistasgrado = models.ForeignKey('Grados', models.DO_NOTHING, db_column='especialistasgrado', blank=True, null=True)
    especialistastelefono = models.CharField(max_length=30, blank=True, null=True)
    especialistasrol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='especialistasrol', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialistas'


class Etapas(models.Model):
    etapasid = models.AutoField(primary_key=True)
    etapasnombre = models.CharField(max_length=40, blank=True, null=True)
    etapasduracion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etapas'


class Etapastareas(models.Model):
    etapastareasid = models.OneToOneField(Etapas, models.DO_NOTHING, db_column='etapastareasid', primary_key=True)
    tareasetapasid = models.OneToOneField('Tareas', models.DO_NOTHING, db_column='tareasetapasid')
    tareasespecialista = models.OneToOneField(Especialistas, models.DO_NOTHING, db_column='tareasespecialista', blank=True, null=True)
    tareasstatus = models.OneToOneField('Status', models.DO_NOTHING, db_column='tareasstatus', blank=True, null=True)
    tareascalificacion = models.OneToOneField(Calificaciones, models.DO_NOTHING, db_column='tareascalificacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etapastareas'
        unique_together = (('etapastareasid', 'tareasetapasid'),)


class Experiencia(models.Model):
    experienciaid = models.AutoField(primary_key=True)
    experienciarango = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiencia'


class Grados(models.Model):
    gradosid = models.AutoField(primary_key=True)
    grado = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grados'


class Niveles(models.Model):
    nivelesid = models.AutoField(primary_key=True)
    nivelnombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'niveles'


class Profesiones(models.Model):
    profesionesid = models.AutoField(primary_key=True)
    profesion = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesiones'


class Proyectodescripcion(models.Model):
    proyectoid = models.OneToOneField('Proyectos', models.DO_NOTHING, db_column='proyectoid', primary_key=True)
    etapaproyecto = models.OneToOneField(Etapas, models.DO_NOTHING, db_column='etapaproyecto', blank=True, null=True)
    etapaespecialista = models.OneToOneField(Especialistas, models.DO_NOTHING, db_column='etapaespecialista', blank=True, null=True)
    etapastatus = models.OneToOneField('Status', models.DO_NOTHING, db_column='etapastatus', blank=True, null=True)
    etapacalificacion = models.OneToOneField(Calificaciones, models.DO_NOTHING, db_column='etapacalificacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyectodescripcion'


class Proyectos(models.Model):
    proyectoid = models.AutoField(primary_key=True)
    proyectonombre = models.CharField(max_length=40, blank=True, null=True)
    proyectodescripcions = models.CharField(max_length=150, blank=True, null=True)
    proyectoservicio = models.OneToOneField('Servicios', models.DO_NOTHING, db_column='proyectoservicio', blank=True, null=True)
    proyectoduracion = models.IntegerField(blank=True, null=True)
    proyectoespecialista = models.OneToOneField(Especialistas, models.DO_NOTHING, db_column='proyectoespecialista', blank=True, null=True)
    proyectocliente = models.OneToOneField(Clientes, models.DO_NOTHING, db_column='proyectocliente', blank=True, null=True)
    proyectostatus = models.OneToOneField('Statusproyecto', models.DO_NOTHING, db_column='proyectostatus', blank=True, null=True)
    proyectocalificacion = models.OneToOneField(Calificaciones, models.DO_NOTHING, db_column='proyectocalificacion', blank=True, null=True)
    proyectoinicio = models.DateField(blank=True, null=True)
    proyectofinal = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyectos'


class Rol(models.Model):
    rolid = models.AutoField(primary_key=True)
    roldescripcion = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class Servicios(models.Model):
    serviciosid = models.AutoField(primary_key=True)
    serviciosnombre = models.CharField(max_length=50, blank=True, null=True)
    serviciosdescripcion = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios'


class SlackUser(models.Model):
    slacker = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    access_token = models.CharField(max_length=128, blank=True, null=True)
    extras = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'slack_user'


class Status(models.Model):
    statusid = models.AutoField(primary_key=True)
    statusnombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'


class Statusproyecto(models.Model):
    statusproyectoid = models.AutoField(primary_key=True)
    statusproyecto = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statusproyecto'


class Tareas(models.Model):
    tareasid = models.AutoField(primary_key=True)
    tareasnombre = models.CharField(max_length=40, blank=True, null=True)
    tareasduracion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tareas'


class Tipocliente(models.Model):
    tipoclienteid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipocliente'


class Cotizacion(models.Model):
    cotizacionid = models.AutoField(primary_key=True)
    cotizacion = models.IntegerField( blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cotizaciones'

