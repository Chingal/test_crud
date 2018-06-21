from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class PersonaLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100
    max_limit = 10000

class PersonaPageNumberPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000