@wallabot
Feature: wallabot 

    @wallabot_launch_browser
    Scenario: wallabot scenario
        Given I access to wallapop site
        And close the window
        Then close the browser

    @wallabot_launch_and_read_all_items
    Scenario: wallabot launch and read all items
        Given I access to wallapop site
        And close the window
        When read all information about screen items
        Then close the browser

    @wallabot_launch_and_save_in_file_all_items
    Scenario: wallabot launch and save in file all items
        Given I access to wallapop site
        And close the window
        When read all information about screen items
        And save the information in file
        Then ∫close the browser