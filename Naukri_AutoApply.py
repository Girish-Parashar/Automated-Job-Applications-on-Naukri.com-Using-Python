from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace these with your Naukri login details
email = "0000"  # Enter your email
password = "0000"  # Enter your password

# Step 1: Initialize WebDriver
driver = webdriver.Chrome()

# Step 2: Navigate to Naukri login page
driver.get("https://www.naukri.com/nlogin/login")

# Step 3: Log in to Naukri
time.sleep(2)  # Wait for the page to load
driver.find_element(By.ID, "usernameField").send_keys(email)  # Enter email
driver.find_element(By.ID, "passwordField").send_keys(password)  # Enter password
driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Click login button

# Step 4: Wait for login to complete and page to load
time.sleep(5)

# Step 5: Navigate directly to the "Data Analyst" job search results page
driver.get("https://www.naukri.com/data-analyst-jobs?k=data%20analyst&nignbevent_src=jobsearchDeskGNB")

# Step 6: Wait for the page to load completely
time.sleep(5)

# Print a success message
print("Logged in and navigated to 'Data Analyst' job search page successfully.")

# Step 8: Wait for the page to load completely
time.sleep(2)

# Step 9: Find all job links on the page
job_links = driver.find_elements(By.XPATH, "//a[contains(@class, 'title') and contains(@href, '/job-listings-')]")

# Step 10: Iterate over each job link and apply the steps for each job
for job_link in job_links:
    job_url = job_link.get_attribute("href")

    if job_url:
        # Open the job link in a new tab
        driver.execute_script(f"window.open('{job_url}', '_blank');")
        time.sleep(3)  # Wait for the new tab to open
        
        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])

        # Step 11: Check for "Apply" buttons and only apply directly on Naukri, not on external sites
        try:
            # Check for "Apply on Company Site" button and skip if present
            apply_on_company_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply on company site')]")
            print("Apply on Company Site button found. Skipping this job.")
            time.sleep(1)
            
        except NoSuchElementException:
            # If "Apply on Company Site" button is not found, check for the direct "Apply" button
            try:
                apply_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]")
                apply_button.click()
                print("Applied to the job successfully on Naukri.")
                time.sleep(2)
                
                # Step 12: Handle questions if they appear after applying
                try:
                    # Wait for questions to appear (adjust the time accordingly)
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='question-container']")))
                    print("Questions detected. Answering them...")

                    # Find all questions and answer them
                    questions = driver.find_elements(By.XPATH, "//div[@class='question-container']")
                    for question in questions:
                        try:
                            # Text input question handling
                            text_input = question.find_element(By.XPATH, ".//input[@type='text']")
                            if text_input:
                                text_input.send_keys("Predefined answer")  # Enter predefined answer
                                print("Answered text input question.")
                        
                        except NoSuchElementException:
                            pass  # No text input field

                        try:
                            # Radio button or dropdown handling
                            options = question.find_elements(By.XPATH, ".//input[@type='radio']")
                            if options:
                                options[0].click()  # Select the first option (you can customize this logic)
                                print("Selected radio button option.")

                            dropdown = question.find_element(By.XPATH, ".//select")
                            if dropdown:
                                select = dropdown.find_element(By.XPATH, ".//option[2]")  # Example: select 2nd option
                                select.click()
                                print("Selected dropdown option.")
                            
                        except NoSuchElementException:
                            pass  # No radio button or dropdown

                    # Submit the answers (if needed)
                    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
                    submit_button.click()
                    print("Answers submitted.")

                except NoSuchElementException:
                    print("No questions appeared after applying.")

            except NoSuchElementException:
                print("No Apply button found or job already applied. Skipping this job.")

        # Step 12: Close the current tab and switch back to the original tab
        driver.close()
        
        # Step 13: Switch back to the main job listing tab
        driver.switch_to.window(driver.window_handles[0])

        # Step 14: Close any additional tabs that may have opened
        while len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
            print("Closed an unintended tab opened by 'Apply on Company Site'.")
        
        # Switch back to the main job listing tab to continue with the next job
        driver.switch_to.window(driver.window_handles[0])
        print("Returned to the main job listing page.")

        # Wait a bit before moving to the next job link
        time.sleep(2)

# Print completion message
print("Processed all jobs on the page.")

# Code execution will pause here for the next steps.

# You can close the browser after the script completes its actions
# driver.quit()
