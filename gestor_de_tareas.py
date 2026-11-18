tareas = []

def menu_principal(lista_tareas: list[dict]) -> None:
    while True:
        print("Gestor de Tareas")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Buscar tarea")
        print("4. Completar tarea")
        print("5. Eliminar tarea")
        print("6. Editar tarea") 
        print("7. Consultar tareas pendientes") # Added option to edit a task
        print("8. Salir")

        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            registrar_tarea(lista_tareas)
        elif opcion == "2":
            consultar_tareas(lista_tareas)
        elif opcion == "3":
            buscar_tarea(lista_tareas)
        elif opcion == "4":
            completar_tarea(lista_tareas)
        elif opcion == "5":
            eliminar_tarea(lista_tareas)
        elif opcion == "6":
            editar_tarea(lista_tareas)
        elif opcion== "7":
            consultar_pendientes(lista_tareas)
        elif opcion == "8":
            print("Cerrando el programa.")
            break
        else:
            print("Error: Opción no válida. Selecciona un número del 1 al 7.\n")



def generar_id(lista_tareas: list[dict]) -> int:
    if not lista_tareas:
        return 1
    return max(tarea["id"] for tarea in lista_tareas) + 1


def registrar_tarea(lista_tareas: list[dict]) -> dict:
    while True:
        titulo = input("Título de la tarea: ").strip()
        if titulo:
            break
        print("Error: El título no puede estar vacío.")

    opciones_prioridad = {
        "1": "alta",
        "2": "media",
        "3": "baja",
    }

    while True:
        print("Prioridad: 1. Alta | 2. Media | 3. Baja")
        opcion = input("Selecciona una opción (1-3): ").strip()
        if opcion in opciones_prioridad:
            prioridad = opciones_prioridad[opcion]
            break
        print("Error: Opción no válida. Ingresa 1, 2 o 3.")

    nueva_tarea = {
        "id": generar_id(lista_tareas),
        "titulo": titulo,
        "prioridad": prioridad,
        "completada": False,
    }

    lista_tareas.append(nueva_tarea)
    print(f"Tarea registrada correctamente con ID {nueva_tarea['id']}.\n")
    return nueva_tarea


def consultar_tareas(lista_tareas: list[dict]) -> None:
    if not lista_tareas:
        print("No hay tareas registradas.\n")
        return

    print("\nLISTA DE TAREAS REGISTRADAS")
    for tarea in lista_tareas:
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(
            f"ID: {tarea['id']} | "
            f"Título: {tarea['titulo']} | "
            f"Prioridad: {tarea['prioridad']} | "
            f"Estado: {estado}"
        )
    print("\n")

def buscar_tarea(lista_tareas: list[dict]) -> None:
    entrada = input("Ingresa el ID de la tarea a buscar: ").strip()
    if not entrada.isdigit():
        print("Error: El ID debe ser un número entero positivo.\n")
        return

    tarea_id = int(entrada)

    for tarea in lista_tareas:
        if tarea["id"] == tarea_id:
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print("\nTarea encontrada")
            print(
                f"ID: {tarea['id']} | "
                f"Título: {tarea['titulo']} | "
                f"Prioridad: {tarea['prioridad']} | "
                f"Estado: {estado}\n"
            )
            return

    print(f"No existe ninguna tarea con el ID {tarea_id}.\n")

def completar_tarea(lista_tareas: list[dict]) -> None:
    if not lista_tareas:
        print("No hay tareas registradas para completar.\n")
        return

    consultar_tareas(lista_tareas)

    entrada = input("Ingresa el ID de la tarea a completar: ").strip()
    if not entrada.isdigit():
        print("Error: El ID debe ser un número entero positivo.\n")
        return

    tarea_id = int(entrada)

    for tarea in lista_tareas:
        if tarea["id"] == tarea_id:
            if tarea["completada"]:
                print(f"La tarea '{tarea['titulo']}' (ID {tarea_id}) ya estaba completada.\n")
            else:
                tarea["completada"] = True
                print(f"Tarea '{tarea['titulo']}' (ID {tarea_id}) marcada como completada.\n")
            return

    print(f"No existe ninguna tarea con el ID {tarea_id}.\n")

def eliminar_tarea(lista_tareas: list[dict]) -> None:
    if not lista_tareas:
        print("No hay tareas registradas para eliminar.\n")
        return

    consultar_tareas(lista_tareas)

    entrada = input("Ingresa el ID de la tarea a eliminar: ").strip()
    if not entrada.isdigit():
        print("Error: El ID debe ser un número entero positivo.\n")
        return

    tarea_id = int(entrada)

    for indice, tarea in enumerate(lista_tareas):
        if tarea["id"] == tarea_id:
            titulo_eliminado = tarea["titulo"]
            lista_tareas.pop(indice)

            for tarea_siguiente in lista_tareas[indice:]:
                tarea_siguiente["id"] -= 1

            print(f"Tarea '{titulo_eliminado}' eliminada correctamente.\n")
            return

    print(f"No existe ninguna tarea con el ID {tarea_id}.\n")

def editar_tarea(lista_tareas: list[dict]) -> None:
    if not lista_tareas:
        print("No hay tareas registradas para editar.\n")
        return

    consultar_tareas(lista_tareas)

    entrada = input("Ingresa el ID de la tarea a editar: ").strip()
    if not entrada.isdigit():
        print("Error: El ID debe ser un número entero positivo.\n")
        return

    tarea_id = int(entrada)

    for tarea in lista_tareas:
        if tarea["id"] == tarea_id:
            nuevo_titulo = input(f"Nuevo título (actual: {tarea['titulo']}): ").strip()

            if nuevo_titulo:
                tarea["titulo"] = nuevo_titulo
                print(f"Tarea con ID {tarea_id} actualizada correctamente.\n")
            else:
                print("Error: El título no puede estar vacío. No se realizaron cambios.\n")
        
            nueva_prioridad = input(f"Nueva prioridad (actual: {tarea['prioridad']}): ").strip().lower()
            if nueva_prioridad in ["alta", "media", "baja"]:
                tarea["prioridad"] = nueva_prioridad
                print(f"Tarea con ID {tarea_id} actualizada correctamente.\n")  
            else:
                print("Error: Prioridad no válida. No se realizaron cambios.\n")
            return


    print(f"No existe ninguna tarea con el ID {tarea_id}.\n")

def consultar_pendientes(lista_tareas: list[dict]) -> None:
    if not lista_tareas:
        print("No hay tareas registradas.\n")
        return
    for tarea in lista_tareas:
        estado = "Completada" if tarea["completada"] else "Pendiente"
        if estado == "Pendiente":
            print(
                f"ID: {tarea['id']} | "
                f"Título: {tarea['titulo']} | "
                f"Prioridad: {tarea['prioridad']} | "
                f"Estado: {estado}"
            )     
        print("\n")


if __name__ == "__main__":
    menu_principal(tareas)