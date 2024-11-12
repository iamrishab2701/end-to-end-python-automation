# Created by rishab at 10/11/24
Feature: Github API Validation

  @github
  Scenario: Session management check
    Given I have github auth credentials
    When I hit getRepo API of github
    Then status code of response should be 200