import requests
from pathlib import Path
from typing import Optional

def setup_download_folder(folder_name: str) -> Optional[Path]:
    download_folder = Path(folder_name)
    
    try:
        download_folder.mkdir(parents=True, exist_ok=True)
        print(f"Folder '{folder_name}' ready.")
        return download_folder
    except Exception as e:
        print(f"Failed to create folder '{folder_name}': {e}")
        return None

def download_image(image_url: str, save_path: Path):
    file_name = image_url.split('/')[-1]

    try:
        print(f"Load file: {file_name}")
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        full_save_path = save_path / file_name

        with open(full_save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Img successfully saved: {full_save_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Image upload error: {e}")

if __name__ == '__main__':
    folder = "Downloads_Folder"
    setup_download_folder(folder)