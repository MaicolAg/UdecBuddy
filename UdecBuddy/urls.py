from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from home.views import *

urlpatterns = [
    path("", include("home.urls")),
    path('admin/', admin.site.urls),
    path('archivos/', ArchivosPageView.as_view(), name='archivos'),
    path('registro/', RegistroPageView.as_view(), name='registro'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    
    #Usuarios 
    path('editar_usuario/<int:usuario_id>/', EditarUsuarioView.as_view(), name='editar_usuario'),
    path('editar_contrasena_usuario/<int:usuario_id>/', EditarContrasenaUsuarioView.as_view(), name='editar_contrasena_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', EliminarUsuarioView.as_view(), name='eliminar_usuario'),
    
    #Archivos DIrectivo
    path('eliminar_archivo_directivo/', EliminarArchivoDirectivoView.as_view(), name='eliminar_archivo_directivo'),
    path('guardar_texto_directivo/', GuardarTextoDirectivoView.as_view(), name='guardar_texto_directivo'),
    path('subir_archivos_directivo/', SubirArchivosDirectivoView.as_view(), name='subir_archivos_directivo'),
    path('eliminar_archivos_directivo/', EliminarArchivosDIrectivoView.as_view(), name='eliminar_archivos_directivo'),

    #Archivos 
    path('eliminar_archivo/', EliminarArchivoView.as_view(), name='eliminar_archivo'),
    path('guardar_texto/', GuardarTextoView.as_view(), name='guardar_texto'),
    path('subir_archivos/', SubirArchivosView.as_view(), name='subir_archivos'),
    path('eliminar_archivos/', EliminarArchivosView.as_view(), name='eliminar_archivos'),
    
    #Administrador
    path('archivos/', ArchivosPageView.as_view(), name='archivos'),
    path('chatAdministrador', ChatAdministradorPageView.as_view(), name='chatAdministrador'),
    path('chat/message/', ChatMessageView.as_view(), name='chat_message'),
    path('datos/', DatosAdministrativoPageView.as_view(), name='datos'),
    path('perfil/', PerfilAdministradorView.as_view(), name='profileAdministrador'),
    path('registronuevo/', RegistronnuevoView.as_view(), name='registronuevo'),
    path('table/', TableAdministrativoPageView.as_view(), name='table'),    
    path('cambiar_contrasena/', CambiarContrasenaAdminView.as_view(), name='cambiar_contrasena'),
    
    #Directivo
    path('archivosDIrectivo/', ArchivosDirectivoPageView.as_view(), name='archivosDirectivo'),
    path('chatDirectivo', ChatDirectivoPageView.as_view(), name='chatDirectivo'),
    path('chat/message/directivo/', ChatDirectivoMessageView.as_view(), name='chat_message_directivo'),
    path('perfilDirectivo/', PerfilDirectivoView.as_view(), name='profileDirectivo'),
    path('tableDirectivo/', TableDirectivoPageView.as_view(), name='tableDirectivo'),
    path('cambiar_contrasena_dire/', CambiarContrasenaDireView.as_view(), name='cambiar_contrasena_dire'),
    
    #Estudiante
    path('chatEstudiante', ChatEstudiantePageView.as_view(), name='chatEstudiante'),
    path('chat/message/estudiante/', ChatEstudianteMessageView.as_view(), name='chat_message_estudiante'),
    path('perfilEstudiante/', PerfilEstudiantePageView.as_view(), name='profileEstudiante'),
    path('cambiar_contrasena_estu/', CambiarContrasenaEstuView.as_view(), name='cambiar_contrasena_estu'),
    
    #Estadisticas
    path('estadisticas/', EstadisticasPageView.as_view(), name='estadisticas'),
    path('calificar_respuesta/', calificar_respuesta, name='calificar_respuesta'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
