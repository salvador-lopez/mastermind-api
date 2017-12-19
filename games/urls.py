from django.urls import path

from src.infrastructure.presentation.controller import games

urlpatterns = [
    path('', games.post_game, name='post_game'),
    path('<game_id>/feedbacks', games.post_feedback, name='post_feedback'),
    path('<game_id>/historical', games.get_historical, name='get_historical')
]
