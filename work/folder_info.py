import os

def list_folders_with_item_count(directory):
    """
    Lists all folders in the given directory and the total number of items in each folder.

    :param directory: The path of the main directory to inspect.
    """
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        
        # Check if it's a folder
        if os.path.isdir(folder_path):
            items = os.listdir(folder_path)  # Get items in the folder
            item_count = len(items)  # Count items
            print(f"{folder_name}")


# Example usage
main_directory = "fruit_dataset\Test"  # Replace with the path of your folder
list_folders_with_item_count(main_directory)



# import pandas as pd

# # List of fruit names
# fruit_names = [
#     "ackee", "apple", "apricot", "avocado", "banana", "bell pepper", "betel nut", "bitter gourd", 
#     "black cherry", "black mulberry", "blueberry", "bottle gourd", "brazil nut", "burdekin plum", 
#     "caimito", "cantaloupe", "carambola", "cardon", "cashew", "cherry", "chico", "cocoa bean", 
#     "coconut", "corn kernel", "custard apple", "date", "dragonfruit", "eggplant", "grape", 
#     "grapefruit", "guava", "jackfruit", "jambul", "kiwi", "lablab", "lemon", "lime", "lychee", 
#     "macadamia", "mango", "midyim", "olive", "orange", "papaya", "pea", "peanut", "pear", 
#     "persimmon", "pineapple", "pomegranate", "pumpkin", "raspberry", "ridged gourd", "strawberry", 
#     "tomato", "vanilla", "watermelon", "zucchini"
# ]

# # Convert the list to a DataFrame
# df = pd.DataFrame(fruit_names, columns=["Fruit Name"])

# # Save to an Excel file
# df.to_excel("Book1.xlsx", index=False)

# print("Fruit names saved to fruit_names.xlsx!")
