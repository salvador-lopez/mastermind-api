import uuid

from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from src.domain.game.exception.gameNotFoundException import GameNotFoundException
from src.infrastructure.dependencyInjection.staticFactories.requestDataTransformers import \
    DjangoHttpRequestToCreateGameRequestStaticFactory, DjangoHttpRequestToCreateFeedbackByCodeGuessRequestStaticFactory
from src.infrastructure.dependencyInjection.staticFactories.useCases import \
    CreateFeedbackByCodeGuessColorsUseCaseStaticFactory, GetHistoricByGameIdUseCaseStaticFactory
from src.infrastructure.dependencyInjection.clients.useCase.createGame.clientCreateGameUseCase import ClientCreateGameUseCase
from src.useCase.getHistoric.getHistoricByGameIdRequest import GetHistoricByGameIdRequest

STATUS_OK = 200
STATUS_CREATED = 201
STATUS_BAD_REQUEST = 400
STATUS_NOT_FOUND = 404


@require_POST
@csrf_exempt
def post_game(request: HttpRequest):
    create_game_request = DjangoHttpRequestToCreateGameRequestStaticFactory.create().transform(request)

    create_game_use_case = ClientCreateGameUseCase()

    return _build_json_response(create_game_use_case.execute(create_game_request), STATUS_CREATED)


@require_POST
@csrf_exempt
def post_feedback(request: HttpRequest, game_id: uuid):
    try:
        get_feedback_by_code_guess_request = \
            DjangoHttpRequestToCreateFeedbackByCodeGuessRequestStaticFactory.create().transform(game_id, request)

        get_feedback_by_code_guess_use_case = CreateFeedbackByCodeGuessColorsUseCaseStaticFactory.create()

        return _build_json_response(
            get_feedback_by_code_guess_use_case.execute(get_feedback_by_code_guess_request),
            STATUS_OK
        )
    except ValueError as e:
        return _build_json_response({'code': STATUS_BAD_REQUEST, "detail": str(e)}, STATUS_BAD_REQUEST)
    except GameNotFoundException as e:
        return _build_json_response({'code': STATUS_NOT_FOUND, "detail": str(e.message)}, STATUS_NOT_FOUND)
    except Exception:
        return _build_json_response({'code': STATUS_BAD_REQUEST, "detail": 'Invalid request'}, STATUS_BAD_REQUEST)


@require_GET
def get_historical(request: HttpRequest, game_id: uuid):
    try:
        get_historic_by_game_id_request = GetHistoricByGameIdRequest(game_id)

        get_historic_by_game_id_use_case = GetHistoricByGameIdUseCaseStaticFactory.create()

        return _build_json_response(get_historic_by_game_id_use_case.execute(get_historic_by_game_id_request),
                                    STATUS_OK)
    except GameNotFoundException as e:
        return _build_json_response({'code': STATUS_NOT_FOUND, "detail": str(e.message)}, STATUS_NOT_FOUND)


def _build_json_response(data: dict, status: int) -> JsonResponse:
    return JsonResponse(data=data, status=status)
