from datetime import datetime


def get_local_time(request):

    today = datetime.now()
    return {'time': today}
