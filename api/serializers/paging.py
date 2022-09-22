from django.core.paginator import Paginator


class PagingSerializer:
    paginator = None
    serializer_class = None

    def __init__(self, object_paginator: Paginator, serializer_class):
        self.paginator = object_paginator
        self.serializer_class = serializer_class

    def data(self, num_page):
        return {
            "data": self.serializer_class(self.paginator.page(num_page).object_list, many=True).data,
            "paging": {
                "totalDataCount": self.paginator.count,
                "dataPerPage": self.paginator.per_page,
                "currentPage": num_page,
                "hasPrev": self.paginator.page(num_page).has_previous(),
                "hasNext": self.paginator.page(num_page).has_next(),
                "totalPage": self.paginator.num_pages
            }
        }
