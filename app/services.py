from .models import Conductor, Vehiculo, Direccion

def crear_conductor(rut,nombre,apellido,fecha_nac):
    conductor = Conductor(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        fecha_nac=fecha_nac
    )
    conductor.save()
    return conductor


def agregar_direccion_a_conductor(calle, numero, dpto, comuna, ciudad, region, conductor_id):
    conductor = Conductor.objects.get(id_conductor=conductor_id)
    # Crear la nueva dirección asignando la instancia del conductor
    direccion = Direccion(
        calle=calle,
        numero=numero,
        dpto=dpto,
        comuna=comuna,
        ciudad=ciudad,
        region=region,
        id_conductor=conductor  # Aquí debes asignar la instancia del conductor
    )
    direccion.save()
    return direccion

def agregar_un_vehiculo(patente,marca,modelo,anio,conductor_id):
    conductor = Conductor.objects.get(id_conductor=conductor_id)
    vehiculo = Vehiculo(
        patente=patente,
        marca=marca,
        modelo=modelo,
        anio=anio,
        id_conductor=conductor
    )
    vehiculo.save()
    return vehiculo

def eliminar_vehiculo(id_vehiculo):
    vehiculo = Vehiculo.objects.get(id_vehiculo=id_vehiculo)
    vehiculo.delete()
    return  vehiculo

def eliminar_conductor(id_conductor):
    conductor = Conductor.objects.get(id_conductor=id_conductor)
    conductor.delete()
    return conductor

