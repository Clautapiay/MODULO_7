from .models import Tarea, SubTarea
"""
a. recupera_tareas_y_sub_tareas
b. crear_nueva_tarea
c. crear_sub_tarea
d. elimina_tarea
e. elimina_sub_tarea
f. imprimir_en_pantalla
"""

#A. recuperar tarear y sub tareas
def recuperar_tareas_y_subtareas():
    tareas = Tarea.objects.filter(eliminada=False) #filter, para que no muestre todo
    todas_las_tareas = []
    for tarea in tareas:
        item = {
            'tarea': tarea,
            'sub_tareas' : tarea.subtarea_set.filter(eliminada=False)
        }
        todas_las_tareas.append(item)
    return todas_las_tareas

#B. crear nueva tarea
def crear_nueva_tarea(descripcion=''): #se necesita texto vacío
    tarea = Tarea(descripcion=descripcion, eliminado=False)
    tarea.save()
    return recuperar_tareas_y_subtareas()

#C. crear subtarea    
def crear_subtarea(tarea_padre_id, descripcion=''):
    #Primero necesitamos el objeto padre para crear una subtar
    tarea = Tarea.objects.get(id=tarea_padre_id) #Nos traemos el objeto especifico que se necesita
    sub_tarea = SubTarea(descripcion=descripcion, eliminada=False, tarea_id=tarea)
    sub_tarea.save()
    return recuperar_tareas_y_subtareas()

    
#D. eliminar tarea
def elimina_tarea(tarea_id):
    tarea_elim = Tarea.objects.filter(tarea_id)
    tarea_elim.delete()
    return tarea_elim

#E. elimina subtarea
def elimina_subtarea(subtarea_id):
    subtarea_elim = SubTarea.objects.filter(subtarea_id)
    subtarea_elim.delete()
    return subtarea_elim

#F. imprimir en la pantalla
def imprimir_en_pantalla(tarea_con_subtareas):
    if not tarea_con_subtareas:
        print("No hay tareas ni subtareas para mostrar")
    else:
        #i enumera tareas principales y j enumera subtareas asociadas
        for i, (tarea, subtareas) in enumerate(tarea_con_subtareas, start=1):
            print(f'[{i}] {tarea.descripcion}')
            for j, sub_tarea in enumerate(subtareas, start=1):
                print(f'.... [{i}].[{j}] {sub_tarea.descripcion}')