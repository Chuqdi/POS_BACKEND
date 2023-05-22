from django.http import JsonResponse
from rest_framework import status


class ResponseHandler:
    @staticmethod
    def error_response(msg, status=status.HTTP_400_BAD_REQUEST):
        return JsonResponse({"msg": msg}, status=status)

    def success_response(msg, status=status.HTTP_200_OK):
        return JsonResponse({"msg": msg}, status=status)
