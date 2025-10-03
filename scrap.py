from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re
from typing import Optional

def clean_track_url(url: str) -> str:
    if '?' in url:
        return url.split('?')[0]
    return url

def extract_image_url(html_content: str) -> Optional[str]:
    soup = BeautifulSoup(html_content, 'html.parser')
    TARGET_WRAPPER_CLASS = ".listenArtworkWrapper__artwork"
    
    artwork_wrapper = soup.select_one(TARGET_WRAPPER_CLASS)
    
    if artwork_wrapper:
        span_with_style = artwork_wrapper.find('span', class_=re.compile(r'sc-artwork.*image__full'))

        if span_with_style and 'style' in span_with_style.attrs:
            style_value = span_with_style['style']
            
            match = re.search(r'url\(["\']?(.*?)["\']?\)', style_value)
            
            if match:
                image_url = match.group(1).replace('&quot;', '"').strip('"')
                
                final_url = re.sub(r'-t[\dx]+.jpg', '-t500x500.jpg', image_url)
                return final_url
    
    return None

def get_dynamic_image_url(url: str) -> Optional[str]:
    cleaned_url = clean_track_url(url)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"Load page: {cleaned_url}...")
        
        try:
            page.goto(cleaned_url, wait_until="networkidle")

            TARGET_WRAPPER_CLASS = ".listenArtworkWrapper__artwork"
            print("Wait...")
            page.wait_for_selector(TARGET_WRAPPER_CLASS, timeout=20000)
            
            html_content = page.content()
            
            return extract_image_url(html_content)
            
        except Exception as e:
            print(f"An error occurred while loading or parsing.: {e}")
            return None
            
        finally:
            browser.close()

if __name__ == '__main__':
    test_url = input("Enter link from soundcloud: ")
    result = get_dynamic_image_url(test_url)
    print(f"\nPicture url: {result}")