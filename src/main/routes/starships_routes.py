from fastapi import APIRouter, Request as RequestFastApi
from main.adapters.request_adapter import request_adapter
from main.composers.get_starships_composer import get_starships_composer
from main.composers.get_starship_information_composer import get_starships_information_composer
from fastapi.responses import JSONResponse
from presenters.error.error_controller import handler_error
from errors.http_not_found import HttpNotFoundError


router = APIRouter()


@router.get('/api/starships/list')
async def get_starships(request: RequestFastApi):
    # page = request.query_params.get("page")
    controller = get_starships_composer()
    try:
        response = await request_adapter(request, controller.handler)
    except Exception as e:
        response = handler_error(e)
    return JSONResponse(
        status_code=response["status_code"],
        content=response["data"]
    )


@router.post('/api/starships/information')
async def get_id_starships(request: RequestFastApi):
    response = None
    controller = get_starships_information_composer()
    try:
        response = await request_adapter(request, controller.handler)
    except Exception as e:
        response = handler_error(e)
    return JSONResponse(
        status_code=response["status_code"],
        content=response["data"]
    )
