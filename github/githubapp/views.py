from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



class Home(TemplateView):
    template_name = "home.html"

import requests


def github_trending_repos(self,requests):
    response = requests.get(
        url='https://api.github.com/search/repositories',
        # params={
        #     'q': f'created:>{from_date}',
        #     'sort': sort_by,
        #     'order': order_by
        # }
    )
    return Response(response.status_code)
    return Response(response.json())


# if __name__ == '__main__':
#     github_trending_repos('2022-08-30')
#     github_trending_repos('2022-08-29')


    

    