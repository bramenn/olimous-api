@acceptanceTest
Feature: Escenarios de pruebas de acceptacion

  Background:
    * url urlBase
    * configure headers = headers
    * def requestPayload = read('request_category_body.json')

    Scenario: Validar el status de category
    Given path '/category'
    When method GET
    Then status 200

    Scenario Outline: Validar el status de category
    Given path '/category/<id>'
    When method GET
    Then status 200
    And match response == {"id": <id>, "name": "#notnull", "alias": "#notnull", "description": "#notnull", "limit_viwers": "#notnull", "limit_participants": "#notnull", "commission": "#notnull", "is_free": "#notnull" }

    Examples:
      | id   |
      | 1    |

    Scenario: Validar el status de category
    Given path '/category'
    And request requestPayload
    When method POST
    Then status 200
    And match response == {"id": "#notnull", "name": "#notnull", "alias": "#notnull", "description": "#notnull", "limit_viwers": "#notnull", "limit_participants": "#notnull", "commission": "#notnull", "is_free": "#notnull" }
