Feature: Typing in Word

  Scenario: Open Word and type a message
    Given I click the start menu
    When I search for "Word"
    And I open Word
    Then I type "Hi I'm Here :]"
