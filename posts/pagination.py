from rest_framework.pagination import PageNumberPagination

class CustomFeedPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'  # allow client to override ?page_size=10
    max_page_size = 50
