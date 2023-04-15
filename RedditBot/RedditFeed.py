import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..Feed import Feed
from typing import Iterator, Any

class RedditFeed(Feed):
    def __init__(self, driver):
        super().__init__('Reddit Feed')
        # Store the WebDriver instance
        self.driver = driver
        self.driver.get('https://www.reddit.com/')

        # Find the div[data-scroller-first] element
        self.first_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-scroller-first]'))
        )
        print(self.first_element)

    def __iter__(self) -> Iterator[Any]:
      # Check if there are no more siblings
        if not self.first_element:
            raise StopIteration

        # Scroll the first element into view with random scroll position
        self.scroll_element_into_view(self.first_element, random.uniform(0.2, 0.8))

        # Get the parent element of the first_element
        parent_element = self.first_element.find_element(By.XPATH, '..')

        # Get all the child elements (siblings) of the parent_element
        siblings = parent_element.find_elements(By.XPATH, '*')

        # Iterate over the siblings and yield their text
        for sibling in siblings:
            # Scroll each sibling element into view with random scroll position
            self.scroll_element_into_view(sibling, random.uniform(0.2, 0.8))  # Add random scroll position between 0.2 and 0.8
            yield sibling.text

        # Set the first_element to None to mark the end of iteration
        self.first_element = None

    def __next__(self) -> Any:
        # Check if there are no more siblings
        if not self.first_element:
            raise StopIteration

        # Scroll the first element into view with random scroll position
        self.scroll_element_into_view(self.first_element, random.uniform(0.2, 0.8))

        # Get the parent element of the first_element
        parent_element = self.first_element.find_element(By.XPATH, '..')

        # Get all the child elements (siblings) of the parent_element
        siblings = parent_element.find_elements(By.XPATH, '*')

        # Iterate over the siblings and yield their text
        for sibling in siblings:
            # Scroll each sibling element into view with random scroll position
            self.scroll_element_into_view(sibling, random.uniform(0.2, 0.8))  # Add random scroll position between 0.2 and 0.8
            yield sibling.text

        # Set the first_element to None to mark the end of iteration
        self.first_element = None

    def scroll_element_into_view(self, element, scroll_position=0.5):
        # Get the element's height
        element_height = element.size['height']

        # Calculate the target scroll position based on the element's height and the given scroll position
        target_scroll_position = element.location['y'] + element_height * scroll_position

        # Scroll the page to the target scroll position using JavaScript
        self.driver.execute_script("window.scrollTo(0, arguments[0]);", target_scroll_position)

    def close(self):
        # Close the WebDriver instance
        self.driver.quit()