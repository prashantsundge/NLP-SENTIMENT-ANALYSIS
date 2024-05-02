import os
def create_folder():
    folders = ['app' , 'data', 'models', 'notebooks']

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Folder {folder} created successfully")
        else:
            print(f"Folder {folder} already exists")


if __name__ == "__main__":
    create_folder()