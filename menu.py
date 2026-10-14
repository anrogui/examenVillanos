"""Menú de consola de la aplicación."""

import logging
from gestion import Gestion
from models import CuerpoTecnico, Jugador

logger = logging.getLogger(__name__)


class Menu:
    def __init__(self, gestion: Gestion):
        self.gestion = gestion

    def mostrarMenuVillanos(self) -> None:
        """Muestra el menú principal y procesa las opciones."""
        while True:
            print("\n=== HÉROES Y VILLANOS DEL VIRGEN ===")
            print("1. Crear héroe")
            print("2. Crear villano")
            print("3. Listar personajes")
            print("4. Buscar por atributo")
            print("5. Emparejar héroe y villano")
            print("6. Eliminar personaje")
            print("0. Salir")

            try:
                opcion = input("Elige una opción: ").strip()
                if opcion == "1":
                    self._crear("heroe")
                elif opcion == "2":
                    self._crear("villano")
                elif opcion == "3":
                    self._listar()
                elif opcion == "4":
                    self._buscar()
                elif opcion == "5":
                    self._emparejar()
                elif opcion == "6":
                    self._eliminar()
                elif opcion == "0":
                    logger.info("Aplicación cerrada por el usuario.")
                    print("Hasta luego.")
                    break
                else:
                    print("Opción no válida.")
                    logger.warning("Opción de menú no válida: %s", opcion)
            except (ValueError, TypeError) as exc:
                print(f"Error: {exc}")
                logger.warning("Entrada no válida: %s", exc)
            except (KeyboardInterrupt, EOFError):
                logger.info("Salida solicitada desde teclado.")
                print("\nAplicación finalizada.")
                break
            except Exception:
                logger.exception("Error no controlado en el menú.")
                print("Se ha producido un error. Consulta el archivo aplicacion.log.")

    def _crear(self, tipo: str) -> None:
        nombre = input("Nombre: ").strip()
        apellidos = input("Apellidos: ").strip()
        fecha = input("Fecha de nacimiento (AAAA-MM-DD): ").strip()
        personaje = self.gestion.crear_personaje(tipo, nombre, apellidos, fecha)
        print(f"Personaje creado: {personaje}")

    def _listar(self) -> None:
        tipo = input("¿Qué quieres listar? (heroe/villano/todos): ").strip()
        personajes = self.gestion.listar_personajes(tipo)
        if not personajes:
            print("No hay personajes para mostrar.")
            return
        for personaje in personajes:
            print(personaje)

    def _buscar(self) -> None:
        tipo = input("Tipo (heroe/villano): ").strip()
        print("Atributos: identificador, nombre, apellidos, fecha_nacimiento, edad,")
        print("          puntuacion_total y las cualidades propias de cada tipo.")
        atributo = input("Atributo: ").strip()
        operador = input("Operador (=, !=, >, >=, <, <=, contiene): ").strip()
        valor = input("Valor a buscar: ").strip()
        resultados = self.gestion.buscar_por_atributo(tipo, atributo, operador, valor)
        if not resultados:
            print("No se han encontrado coincidencias.")
        else:
            for personaje in resultados:
                print(personaje)

    def _emparejar(self) -> None:
        heroe, villano, diferencia, valoracion = self.gestion.emparejar_aleatoriamente()
        print(f"Héroe: {heroe}")
        print(f"Villano: {villano}")
        print(f"Diferencia de puntuación: {diferencia}")
        print(valoracion)

    def _eliminar(self) -> None:
        tipo = input("Tipo (heroe/villano): ").strip()
        identificador = int(input("Identificador: "))
        if self.gestion.eliminar_personaje(tipo, identificador):
            print("Personaje eliminado.")
        else:
            print("No existe un personaje con ese identificador.")

    def mostrarMenuPlantilla(self):
        o=0
        while o!=4:
            print("\n================================")
            print("\n     PLANTILLAS DE FÚTBOL     ")
            print("\n================================")
            print("1.Agregar miembro")
            print("2.Listar plantilla")
            print("3.Crear plantilla")
            print("4.Salir")
            try:
                o=int(input("Ingrese una opción: "))
                if o==1:
                    self.menuCrearMiembro()
                elif o==2:
                    self._listar_plantilla()
                elif o==3:
                    #self.gestion.crearPlantilla()
                    print("La opcion 3 está en desarrollo.")
                elif o==4:
                    #print("Saliendo del menú de plantillas...")
                    print("Saliendo del menú de plantillas...")
                    break
                else:
                    print("Opción no válida.")
                    logger.warning("Opción de menú no válida: %s", o)
            except (ValueError, TypeError) as exc:
                print(f"Error: {exc}")
                logger.warning("Entrada no válida: %s", exc)
            except (KeyboardInterrupt, EOFError):
                logger.info("Salida solicitada desde teclado.")
                print("\nAplicación finalizada.")
                break
            except Exception:
                logger.exception("Error no controlado en el menú.")
                print("Se ha producido un error. Consulta el archivo aplicacion.log.")

    def _listar_plantilla(self) -> None:
        miembros = self.gestion.listar_plantilla()
        if not miembros:
            print("La plantilla está vacía.")
            return

        print("========== PLANTILLA DE FÚTBOL ==========")
        for miembro in miembros:
            if type(miembro)==Jugador:
                tipo = "Jugador"
            elif type(miembro)==CuerpoTecnico:
                tipo = "Cuerpo técnico"
            else:
                tipo = "Miembro"

            print(f"\nID: {miembro.identificador}")
            print(f"Tipo: {tipo}")
            print(f"Nombre: {miembro.nombre}")
            print(f"Apellidos: {miembro.apellidos}")
            if isinstance(miembro, Jugador):
                print(f"Posición: {miembro.posicion.capitalize()}")
            elif isinstance(miembro, CuerpoTecnico):
                print(f"Rol: {miembro.rol.capitalize()}")
            print("-----------------------------------------")

    def mostrarMenuPrincipal(self):
        while True:
            print("\n=== MENÚ PRINCIPAL ===")
            print("1. Menú de héroes y villanos")
            print("2. Menú de plantillas de fútbol")
            print("0. Salir")

            try:
                opcion = input("Elige una opción: ").strip()
                if opcion == "1":
                    self.mostrarMenuVillanos()
                elif opcion == "2":
                    self.mostrarMenuPlantilla()
                elif opcion == "0":
                    logger.info("Aplicación cerrada por el usuario.")
                    break
                else:
                    print("Opción no válida.")
                    logger.warning("Opción de menú no válida: %s", opcion)
            except (ValueError, TypeError) as exc:
                print(f"Error: {exc}")
                logger.warning("Entrada no válida: %s", exc)
            except (KeyboardInterrupt, EOFError):
                logger.info("Salida solicitada desde teclado.")
                print("\nAplicación finalizada.")
                break
            except Exception:
                logger.exception("Error no controlado en el menú.")
                print("Se ha producido un error. Consulta el archivo aplicacion.log.")

    def menuCrearMiembro(self):
        print("¿Qué tipo de miembro quieres agregar?")
        print("1.Jugador")
        print("2.Cuerpo técnico")
        tipo = input("Ingrese el tipo (1 o 2): ").strip()
        if tipo == "1":
            nombre = input("Ingrese el nombre del jugador: ").strip()
            apellidos = input("Ingrese los apellidos del jugador: ").strip()
            posicion=input("Ingrese la posicion del jugador: ").strip()
            if posicion != "portero" and posicion != "defensa" and posicion != "centrocampista" and posicion != "delantero":
                print("Posición no válida. Debe ser portero, defensa, centrocampista o delantero.")
                logger.warning("Opción de menú(posición) no válida: %s", tipo)
            else:
                try:
                    self.gestion.agregarJugador(nombre, apellidos,posicion)
                except ValueError as e:
                    print(f"Error al agregar jugador: {e}")
                    logger.warning("Error al agregar jugador: %s", e)

        if tipo=="2":
            nombre = input("Ingrese el nombre del miembro del cuerpo técnico: ").strip()
            apellidos = input("Ingrese los apellidos del miembro del cuerpo técnico: ").strip()
            rol=input("Ingrese el rol del miembro del cuerpo técnico: ").strip()
            if rol != "entrenador" and rol != "preparador físico" and rol != "médico" and rol != "utillero":
                print("Rol no válido. Debe ser entrenador, preparador físico, médico o utillero.")
                logger.warning("Opción de menu (rol) no válida: %s", tipo)
            else:
                try:
                    self.gestion.agregarCuerpoTecnico(nombre, apellidos, rol)
                except ValueError as e:
                    print(f"Error al agregar miembro del cuerpo técnico: {e}")
                    logger.warning("Error al agregar miembro del cuerpo técnico: %s", e)

        else:
            print("Tipo no válido. Debe ser 1 o 2.")
            logger.warning("Opción de menú no válida: %s", tipo)
