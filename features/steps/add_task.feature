Feature: To-Do List Management - Add a Task

  Scenario Outline: Add a task to the to-do list
    Given the to-do list is empty
    When I add a task with name "<name>" and description "<description>"
    Then the task "<name>" should be in the to-do list

    Examples:
      | name        | description        |
      | Task 1      | Description for 1  |
      | Task 2      | Description for 2  |
