# coffeelint: disable=max_line_length

env = {}
beforeEach ->
  env = {}


describe "app controller", ->

  beforeEach ->
    module 'salsitasoft'

  it 'should have a dummy test', inject ->
    true.should.be.ok

