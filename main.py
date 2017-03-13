import webapp2
from google.appengine.api import urlfetch
from google.appengine.api import images
from google.appengine.ext import ndb

class Photo(ndb.Model):
    image = ndb.BlobProperty()

class ImageHandler(webapp2.RequestHandler):
    def get(self, width, height):
        url = self.request.get('url')
        key = '{}:{}:{}'.format(url, width, height)

        height, width = [int(height), int(width)]

        cached = Photo.get_by_id(key)
        if cached is None:
            img = urlfetch.fetch(url).content
            
            output = images.resize(img, width=width, height=height)

            cache = Photo(id = key, image = output)
            cache.put()
        else:
            output = cached.image
        self.response.headers['Content-Type'] = 'image/jpeg'
        self.response.write(output)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('URL resize @ /img/w:<px>h:<px>url?')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    (r'/img/w:(\d+)h:(\d+)', ImageHandler),
], debug=True)
