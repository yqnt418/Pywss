from pywss import AsyncPyws, AsyncRadioMiddleware

ws = AsyncPyws(__name__)


class Radio(AsyncRadioMiddleware):
    RADIO_TIME = 0.5

    def process_data(self):
        return "you can also use async here"


@ws.route('/test/example/4')
def example_4(request, data):
    """There Nothing To Do"""


if __name__ == '__main__':
    ws.add_middleware(Radio)
    ws.serve_forever()

"""
/* Client Code */
ws = new WebSocket("ws://127.0.0.1:8866/test/example/4");
ws.onmessage = function (ev) {
    console.log(JSON.parse(ev.data));
}
ws.onclose = function (ev) {
    console.log('Connect Closed')
}
ws.onopen = function() {
    if (ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify({'name': 'example4'}))  // you will get enter the AuthenticationMiddleware first
    }
}
"""
