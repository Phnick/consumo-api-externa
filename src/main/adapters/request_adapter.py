from fastapi import Request as RequestFastapi
from typing import Callable


async def request_adapter(request: RequestFastapi, controller: Callable):
    '''FatsApi adapter'''
    body = None
    try:
        body = await request.json()
    except:
        pass
    http_request = {
        'query_params': request.query_params,
        'body': body
    }
    print(http_request)
    http_response = controller(http_request)
    return http_response
