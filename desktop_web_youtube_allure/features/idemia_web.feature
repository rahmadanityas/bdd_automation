Feature: IDEMIA News Access

  Scenario: Open news article using organization account in Edge
    Given the Edge browser is open
    When the user opens the IDEMIA Line homepage
    And the user navigates to the Global News Center
    And the user searches for the IST news article
    And the user applies the search filter
    And the user opens the article
    Then the news article is displayed
