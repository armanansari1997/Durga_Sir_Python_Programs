class TooYoungException(BaseException):
    def __init__(self, msg):
        self.msg = msg


class TooOldException(BaseException):
    def __init__(self, msg):
        self.msg = msg


age = int(input('Enter your age'))
if age > 60:
    raise TooYoungException('You are too young now...')
elif age < 18:
    raise TooOldException('You are too old now...')
else:
    print('Matched found, we will contact you by mail...')
