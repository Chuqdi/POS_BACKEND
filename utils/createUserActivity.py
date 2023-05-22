import threading
from accounts.models import RecentActivities


def createUserActivity(name, description, user, status="succcess"):
    def creator(name, description, user, status):
        activity = RecentActivities.objects.create(
            name=name, description=description, user=user, status=status
        )
        activity.save()

    t = threading.Thread(target=creator, args=(name, description, user, status))
    t.start()
