
import os, sys 
def cd_to_folder(path=None):
  if(path==None):   
    # Get user input for the folder path
    path = input("Enter the folder path: ")
  # Change the current working directory to the specified folder
  os.chdir(path)
  # Verify the new current working directory
  print("Current working directory:", os.getcwd())

  current_directory = os.getcwd()
  print(current_directory)
  print(os.listdir()) 
  
def pwd(): 
  current_directory = os.getcwd()
  print("pwd: ", current_directory)
  print("ls: ", os.listdir()) 
  
import shutil
def rm_file(path=None, folder=False): 
  if(path==None): 
    path = input("Enter the direction: ")

  if os.path.exists(path):
      if(folder): shutil.rmtree(path)
      else: os.remove(path)
      print(f"File '{path}' has been removed.")
  else:
      print(f"File '{path}' does not exist.")

def cat_file(path=None): 
  if(path==None): 
    path = input("Enter the file path: ")

  read_file = open(path, "r")
  content = read_file.read() 
  read_file.close()
  return content 

def replace_file(): 
  file_path = input("Enter the file path: ")
  content_path = input("Enter the CONTENT path: ")
  new_content = cat_file(content_path)
  
  write_file = open(file_path, "w")
  write_file.write(new_content)
  write_file.close() 
  print("Content of File Changed!\n")
  print(new_content)

