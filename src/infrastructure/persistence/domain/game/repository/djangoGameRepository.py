import uuid

from django.core.exceptions import ObjectDoesNotExist

from src.domain.game.exception.gameNotFoundException import GameNotFoundException
from src.domain.game.repository.gameRepository import GameRepository
from src.infrastructure.persistence.domain.game.entity.djangoGame import DjangoGame


class DjangoGameRepository(GameRepository):
    def find_one_by_id(self, game_id: uuid) -> DjangoGame:
        try:
            return DjangoGame.objects.get(pk=game_id)
        except ObjectDoesNotExist:
            raise GameNotFoundException(game_id)

    def save(self, game: DjangoGame):
        game.save()
