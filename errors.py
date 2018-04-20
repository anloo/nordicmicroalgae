
class NotFound(Exception):
    status_code = 404

    def __init__(self, message = None, payload = None):
        Exception.__init__(self)
        self.message = message
        self.payload = payload

    def to_dict(self):
        error_dict = dict(self.payload or ())
        error_dict['message'] = self.message
        return error_dict
