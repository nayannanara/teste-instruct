from rest_framework import viewsets, status, mixins
from rest_framework.views import Response

from api import models, serializers
from api.integrations.github import GithubApi as git
from api.models import Organization

# TODOS:
# 1 - Buscar organização pelo login através da API do Github
# 2 - Armazenar os dados atualizados da organização no banco
# 3 - Retornar corretamente os dados da organização
# 4 - Retornar os dados de organizações ordenados pelo score na listagem da API


class OrganizationViewSet(
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = models.Organization.objects.all().order_by('-score')
    serializer_class = serializers.OrganizationSerializer
    lookup_field = "login"

    def list(self, request, *args, **kwargs):
        '''
            Retorna todos os dados de uma organização através da API do Github
        '''
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, login=None):
        '''
            Retorna dados de uma organização através da API do Github
            :login: login da organização no Github
        '''
        org = git.get_organization(login)
        org_members = git.get_organization_public_members(login)
        instance, created = Organization.objects.update_or_create(
            login=org['login'],
            name=org['name'],
            score=org['public_repos'] + org_members,
            defaults={'login': login}
            )
        serializer = serializers.OrganizationSerializer(instance)
        return Response(serializer.data)
