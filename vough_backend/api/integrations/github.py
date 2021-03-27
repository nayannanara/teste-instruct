import os
import requests


class GithubApi:
    API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

    def get_organization(self, login: str):
        """Busca uma organização no Github

        :login: login da organização no Github
        """
        #https://api.github.com/orgs/ministrycentered
        resposta = requests.get(f'https://api.github.com/orgs/{login}')

        resposta.json() if resposta.status_code == 200 else resposta.status_code

    def get_organization_public_members(self, login: str) -> int:
        """Retorna todos os membros públicos de uma organização

        :login: login da organização no Github
        """
        resposta = requests.get(f'https://api.github.com/orgs/{login}/public_members')
        status = resposta.status_code
        qtd = len(resposta.json())

        if status == 200:
            qtd if qtd > 0 else 0
        else:
            return resposta.status_code
