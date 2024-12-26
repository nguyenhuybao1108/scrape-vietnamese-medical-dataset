from selenium import webdriver
from bs4 import BeautifulSoup

# Set up the browser
driver = webdriver.Chrome()  # Use appropriate WebDriver for your browser
driver.get("https://suckhoedoisong.vn/tra-cuu-benh.htm")

# Wait for JavaScript to load content
import time
time.sleep(5)  # Adjust based on loading time

# Get the rendered HTML
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Now try to find lstDsBenh
lstDsBenh = soup.find('div', id='lstDsBenh')
if lstDsBenh:
    box_items = lstDsBenh.find_all('div', class_='box-item')
    for box in box_items:
        title_element = box.find('div', class_='title').find('span', class_='text')
        title_text = title_element.text if title_element else "No Title"

        print(f"Category: {title_text}")
        link_items = box.find('div', class_='list').find_all('a', class_='item')
        
        for link in link_items:
            href = link.get('href')
            title = link.get('title')
            print(f"  - {title}: {href}")
else:
    print("lstDsBenh is still empty")

driver.quit()
