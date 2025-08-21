from datetime import datetime


def myproject(request):
    return {
        # "user": request.user
        "now": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
