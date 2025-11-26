def get_client_ip(request):
    x_fwd = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_fwd:
        ip = x_fwd.split(",")[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
