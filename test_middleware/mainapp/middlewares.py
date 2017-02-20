#-*- coding: utf-8 -*-

from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_request(self, request):
        print("[==>] Proxying request")
        print(request.__dict__)

        #return request #注意しなければならないのは、ここでrequestを返すとこれがresponseとして扱われてしまうこと
                        #responseのオブジェクトではなくWSGIRequestがレスポンスとして返ってしまうので
                        #responseにあるはずのメソッドが無い旨のエラーメッセージが表示される

    def process_response(self, request, response):
        print("[<==] Proxying response")
        print(response.__dict__)

        #print(request.__dict__)

        return response #返してあげないと、Intercept状態のままになるよ！