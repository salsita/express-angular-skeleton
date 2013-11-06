# Server
# ======
# This module is the entry point of the server application. So if you want to
# understand the codebase, it might be a good idea to start here.
#
require 'coffee-script'

path = require 'path'
express = require 'express'
require 'express-namespace'

config = require 'config'

module.exports = app = express()

CLIENT_SECRET = "df237oh3vwoqnmqwuvbn2t732h1"

# Configure the server.
app.configure ->

  app.set 'port', process.env.PORT || 3000

  app.use express.bodyParser()
  app.use express.cookieParser process.env.CLIENT_SECRET or CLIENT_SECRET
  app.use express.methodOverride()

  app.use express.session {
    secret: process.env.CLIENT_SECRET or CLIENT_SECRET
    cookie:
      secure: false
      maxAge: 86400000
  }

  # Gzip the content to save bandwidth.
  app.use express.compress()

  app.use express.favicon()
  app.use '/static/', express.static(config.server.static_root)
  app.use '/static/', (req, res, next) ->
    # We're requesting a non-existent static resource.
    res.send 404

  app.use app.router

  app.set 'views', config.server.views_root
  app.set 'view engine', 'jade'

  process.env.LOG_LEVEL = config.log.level


# Set the development environment.
app.configure 'dev', ->
  app.use express.errorHandler dumpExceptions: true, showStack: true

# Set the development environment.
app.configure 'qa', ->
  app.use express.errorHandler dumpExceptions: true, showStack: true

app.configure 'client', ->
  app.use express.errorHandler()

# Set the production environment too.
app.configure 'prod', ->
  app.use express.errorHandler()

app.namespace '/test', -> require('./routes/test').setup(app)


# Start me up! (If you start me up, I'll never stop.)
app.listen app.get('port'), ->
  console.log "Express server listening on port #{app.get('port')} in " +
    "#{app.settings.env} mode"


app.use (req, res) ->
  console.log 'default route', req.path
  res.sendfile path.join config.server.static_root, 'index.html'


