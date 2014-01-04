# Returns a generic server-side initialized JavaScript



application = webapp2.WSGIApplication([
    ('/js/generic', MainPage)
], debug=True)