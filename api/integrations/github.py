import os
import requests
from django.http import HttpResponse


class GithubApi:
    API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

    def get_organization(login: str):
        """Busca uma organização no Github

        :login: login da organização no Github
        """
        resposta = requests.get(f'https://api.github.com/orgs/{login}')
        return resposta.json() if resposta.status_code == 200 else resposta.status_code


    def get_organization_public_members(login: str) -> int:
        """Retorna todos os membros públicos de uma organização

        :login: login da organização no Github
        """
        resposta = requests.get(f'https://api.github.com/orgs/{login}/public_members')
        return resposta.json() if resposta.status_code == 200 else resposta.status_code
