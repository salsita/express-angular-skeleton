angular.module('salsitasoft', [
  'templates-app'
  'templates-common'
  'templates-jade_app'
  'templates-jade_common'

  'ui.router'

  # Add your modules here
  'ngBoilerplate.home'
])

.config ($urlRouterProvider , $locationProvider) ->
  $locationProvider.html5Mode(true)
  $urlRouterProvider.otherwise '/home'


.controller 'AppCtrl', ($scope, $location) ->
  console.log 'AppCtrl'
