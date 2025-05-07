def create_post(request):
    title = request.data.get('title') 
    content = request.data.get('content')

    return Response()