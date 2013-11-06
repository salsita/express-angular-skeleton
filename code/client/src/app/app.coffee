angular.module('salsitasoft', [
  'templates-app'
  'templates-common'
  'templates-jade_app'
  'templates-jade_common'

  'ui.router'

  # Add your modules here
])

.config ($urlRouterProvider , $locationProvider) ->
  $locationProvider.html5Mode(true)
  $urlRouterProvider.otherwise '/home'
