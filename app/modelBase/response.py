from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

class ResponseData():
    def Response(error, code, message, data, codeHttp):
        response =  Response(
                                { 
                                    "error":error,
                                    "codeError":code,
                                    'message': message, 
                                    'data':data
                                },
                                status=codeHttp
                            )

        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        
        return response