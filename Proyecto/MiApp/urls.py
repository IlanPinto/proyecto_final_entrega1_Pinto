from django.urls import path
from MiApp.views import buscar_jugador, mostrar_entrenadores, mostrar_jugadores, mostrar_torneos, inicio, mostrar_jugadores_pagina, formulario_jugadores, formulario_entrenadores, formulario_torneos

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('jugadores/', mostrar_jugadores, name='jugadores'),
    path('entrenadores/', mostrar_entrenadores, name='entrenadores'),
    path('torneos/', mostrar_torneos, name='torneos'),
    path('pagina_jugadores/', mostrar_jugadores_pagina, name='Jugadores'),
    path('crear_jugadores/', formulario_jugadores, name='FormularioJugadores'),
    path('crear_entrenadores/', formulario_entrenadores, name='FormularioEntrenadores'),
    path('crear_torneos/', formulario_torneos, name='FormularioTorneos'),
    path('buscar_jugador/', buscar_jugador, name='BuscarJugador'),
]
