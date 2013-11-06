request = require 'supertest'
express = require 'express'

chai = require 'chai'
sinon = require 'sinon'
chai.use require 'sinon-chai'

chai.Should()

testRoute = require './test'

env = {}
beforeEach ->
  env = {}

describe 'test route module', ->

  beforeEach ->
    env.app = express()

  describe 'blah blah route', ->

    beforeEach ->
      sinon.spy env.app, 'get'
      testRoute.setup env.app

    it 'should be registered', ->
      env.app.get.should.have.been.calledWith '/blahblah', sinon.match.func

    it 'should return HTTP 200 on GET', (done) ->
      request(env.app)
        .get('/blahblah')
        .expect(200, done)
