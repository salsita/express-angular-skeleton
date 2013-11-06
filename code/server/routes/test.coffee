exports.setup = (app) ->

  app.get '/blahblah', (req, res) ->
    res.send 'blah blah!'
