from django.shortcuts import render
from web.formularios.formularioPersonal import FormularioPersonal
#IMPORTAR EL FORMULARIO A RENDERIZAR
from web.formularios.formularioPlatos import FormularioPlatos

# Create your views here.
#Las vistas en django son los CONTROLADORES

#Las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def Platos(request):
    formulario=FormularioPlatos()
    datosParaTemplate={
        'formularioRegistro':formulario
    }
    #PREGUNTAR SI EXISTE ALGUNA PETICION DE TIPO POST ASOCIADA A LA VISTA
    if request.method=='POST':
        #Deberiamos capturar los datos del formulario
        datosDelFormulario=FormularioPlatos(request.POST)
        #Verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturamos la data
            datosPlato=datosDelFormulario.cleaned_data
            print(datosDelFormulario)
            print(datosPlato)
    return render(request,'platos.html',datosParaTemplate)

def Personal(request):
    formulario1=FormularioPersonal()
    datosParaTemplates1={
        'formularioPersonal':formulario1
    }
    return render(request,'personal.html',datosParaTemplates1)