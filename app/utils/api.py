from flask import jsonify


class Response:
    def success(self, data={}, code=200):
        return jsonify({"data": data}), code

    def failure(self, message, code=500):
        return jsonify({"error": message}), code


res = Response()
