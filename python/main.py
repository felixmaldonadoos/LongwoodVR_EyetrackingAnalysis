    
import os
import glob
import pandas as pd

class Analysis(): 
    def __init__(self) -> None:
        self.path_dir = None
        self.path_data = dict()
        self.data = None
        self.df = pd.DataFrame()
        pass
    
    def read_single_file(self):
        if self.path_dir is None:
            current_file_path = os.path.abspath(__file__)
            current_dir = os.path.dirname(current_file_path)
            self.path_dir = os.path.dirname(current_dir)
            self.path_dir = os.path.join(self.path_dir, 'data')
            self.path_dir = glob.glob(os.path.join(self.path_dir, '*.tsv'))
        
        file = self.path_dir[0]
        self.df = pd.read_csv(self.path_dir[0],sep="\t",header=8)
        print(self.df.head())
        # self.data = pd.read_table(glob.glob(os.path.join(self.path_dir, '*.tsv')))
        
    def __get_file_from_ext__(self, path_dir:str, ext:str)->str:
       return glob.glob(os.path.join(path_dir, '*.txt'))
       
    def read_data(self)->None:
        if self.path_dir is None:
            current_file_path = os.path.abspath(__file__)
            current_dir = os.path.dirname(current_file_path)
            self.path_dir = os.path.dirname(current_dir)
            self.path_dir = os.path.join(self.path_dir, 'data')
            
        # Iterate over all items in self.path_dir
        for item in os.listdir(self.path_dir):
            # Construct the full path to the item
            item_path = os.path.join(self.path_dir, item)
            self.path_data[item] = pd.DataFrame()

            # Check if the item is a directory
            if os.path.isdir(item_path):
                # Find all .txt files in the directory
                txt_files = glob.glob(os.path.join(item_path, '*.txt'))
                # Iterate over each file
                for file_path in txt_files:
                    self.path_data[item] = pd.read_csv(file_path)
            else:
                print(f"{item_path} is not a directory")
Analysis().read_single_file()