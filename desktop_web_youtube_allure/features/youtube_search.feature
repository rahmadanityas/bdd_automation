Feature: YouTube Video Search
  Scenario: Open YouTube, search, and play a specific video
    Given the browser is open
    When the user navigates to YouTube
    And the user searches for "IDEMIA MorphoWave touchless fingerprint scanner for access control - high throughput"
    And the user opens the video titled "IDEMIA MorphoWave touchless fingerprint scanner for access control - high throughput"
    And the user skips the ad if present
    Then the video is playing

