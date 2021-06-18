import json


def get_request_data(request):
    """
	Retrieves the request data irrespective of the method and type it was send.
	@param request: The Django HttpRequest.
	@type request: WSGIRequest
	@return: The data from the request as a dict
	@rtype: dict
	"""
    data = None
    if request is not None:
        request_meta = getattr(request, 'META', {})
        request_method = getattr(request, 'method', None)
        if str(request_meta.get('CONTENT_TYPE', '')).startswith('multipart/form-data;'):  # Special handling for
            # Form Data?
            data = request.POST.copy()
            data = data.dict()
        elif request_method == 'GET':
            data = request.GET.copy()
            data = data.dict()
        elif request_method == 'POST':
            data = request.POST.copy()
            data = data.dict()
        elif request_method == 'PUT':
            data = request.POST.copy()
            print(data)
            data = data.dict()
        elif request_meta.get('CONTENT_TYPE', '') == 'application/json':
            data = json.loads(request.body)
        if not data:
            request_body = getattr(request, 'body', None)
            if request_body:
                data = json.loads(request_body)
            else:
                data = dict()
        return data
