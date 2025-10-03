from scrap import get_dynamic_image_url
from downloader import setup_download_folder, download_image

def main():
    track_url = input("Your link:")
    FOLDER_NAME = "Soundcloud_Artwork"
    
    download_path = setup_download_folder(FOLDER_NAME)
    
    if not download_path:
        print("The program has been stopped because it is impossible to create a folder.")
        return
        
    final_image_url = get_dynamic_image_url(track_url)

    if final_image_url:
        print(f"\nLink: {final_image_url}")
        
        download_image(final_image_url, download_path)
    else:
        print("\nUnable to retrieve image URL. Downloading is not possible.")

if __name__ == '__main__':
    main()