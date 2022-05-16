@wallabot
Feature: wallabot 

    @wallabot_launch_browser
    Scenario: wallabot scenario
        Given I acces to wallapop site
        And I close the window
        Then I close the browser

    @wallabot_launch_and_read_all_items
    Scenario: wallabot launch and read all items
        Given I acces to wallapop site
        And I close the window
        When I read all information about screen items
        Then I close the browser

    @wallabot_launch_and_save_in_file_all_items
    Scenario: wallabot launch and save in file all items
        Given I acces to wallapop site
        And I close the window
        When I read all information about screen items
        And I save the information in file
        Then I close the browser