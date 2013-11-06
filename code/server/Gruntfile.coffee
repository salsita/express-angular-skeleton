path = require 'path'

module.exports = (grunt) ->

  grunt.initConfig

    express:
      options:
        cmd: 'coffee'
        delay: 50
      dev:
        options:
          script: path.join __dirname, 'app.coffee'
          node_env: 'dev'

    coffeelint:
      files: ['**/*.coffee', '!node_modules/**']

    mochaTest:
      options:
        compilers: 'coffee-script'

      test:
        options:
          reporter: 'dot'
        src: ['!node_modules/**', '**/*.spec.coffee']

      jenkins:
        options:
          reporter: 'xunit-file'
        src: ['!node_modules/**', '**/*.spec.coffee']


    watch:
      express:
        options:
          nospawn: true
        files: ['**/*.coffee']
        tasks: ['express:dev']
      test:
        options:
          nospawn: false
        files: ['**/*.coffee']
        tasks: ['test']

    env:
      jenkins:
        # We need to set this so that Jenkins gets his test-results*.xml file
        # and doesn't complain about missing tests.
        XUNIT_FILE: 'test-results-server.xml'

  grunt.loadNpmTasks 'grunt-express-server'
  grunt.loadNpmTasks 'grunt-contrib-watch'
  grunt.loadNpmTasks 'grunt-mocha-test'
  grunt.loadNpmTasks 'grunt-coffeelint'
  grunt.loadNpmTasks 'grunt-env'

  grunt.registerTask 'test', ['coffeelint', 'mochaTest:test']
  grunt.registerTask 'test:jenkins', ['env:jenkins', 'mochaTest:jenkins']
  grunt.registerTask 'dev', ['test', 'express:dev', 'watch']
  grunt.registerTask 'default', ['dev']

