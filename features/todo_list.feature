
Feature: To-Do List Management

  Scenario Outline: Add a task to the to-do list
    Given the to-do list is empty
    When I add a task with name "<name>" and description "<description>"
    Then the task "<name>" should be in the to-do list

    Examples:
      | name        | description        |
      | Task 1      | Description for 1  |
      | Task 2      | Description for 2  |

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | name        | description        | status     |
      | Task 1      | Description for 1  | Incomplete |
      | Task 2      | Description for 2  | Incomplete |
    When I list all tasks
    Then I should see the following tasks:
      | name        | description        | status     |
      | Task 1      | Description for 1  | Incomplete |
      | Task 2      | Description for 2  | Incomplete |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | name        | description        | status     |
      | Task 1      | Description for 1  | Incomplete |
      | Task 2      | Description for 2  | Incomplete |
    When I mark the task "<task_name>" as completed
    Then the task "<task_name>" should be marked as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | name        | description        | status     |
      | Task 1      | Description for 1  | Incomplete |
      | Task 2      | Description for 2  | Incomplete |
    When I clear the entire to-do list
    Then the to-do list should be empty

  Scenario Outline: Edit a task in the to-do list
    Given the to-do list contains tasks:
      | name        | description        | status     |
      | Task 1      | Description for 1  | Incomplete |
      | Task 2      | Description for 2  | Incomplete |
    When I edit the task "<old_task_name>" with new name "<new_name>", new description "<new_description>", and new status "<new_status>"
    Then the task "<new_name>" should be in the to-do list with description "<new_description>" and status "<new_status>"

    Examples:
      | old_task_name   | new_name      | new_description        | new_status |
      | Task 1          | New Task 1    | New Description for 1  | Complete   |
      | Task 2          | New Task 2    | New Description for 2  | Incomplete |

  Scenario: Delete a specific task from the to-do list
    Given the to-do list contains tasks:
      | name        | description        | status     |
      | Task 1      | Description for 1  | Incomplete |
      | Task 2      | Description for 2  | Incomplete |
    When I delete the task "<task_name>"
    Then the task "<task_name>" should not be in the to-do list
