from channels.routing import route
from notification.notification.consumers import ws_connect, ws_disconnect

notification_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
]

