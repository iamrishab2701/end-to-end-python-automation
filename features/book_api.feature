# Created by rishab at 09/11/24
Feature: Verify if Books are added and deleted using Library API

  @smoke @library
  Scenario: Verify Add Book API Functionality
    Given the book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added

  @regression @library
  Scenario Outline:
    Given the book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
    Examples:
      | aisle | isbn |
      | dsdas | 4535 |
      | sdasd | 3565 |