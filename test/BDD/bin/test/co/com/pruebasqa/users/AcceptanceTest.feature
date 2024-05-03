@acceptanceTest
Feature: Escenarios de pruebas de acceptacion

  Background:
    * url urlBase
    * configure headers = headers

    Scenario: Hola Mundo
    Given path '/users/2'
    When method GET
    Then status 201
