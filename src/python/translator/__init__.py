from textblob import TextBlob

class Translator(object):
  def __init__(self):
    self.counter = 0

  def translate(self, message, language):
    self.counter += 1
    return str(self.counter) + ": " + str(TextBlob(message).translate(to=language))
