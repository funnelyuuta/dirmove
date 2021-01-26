import shutil
import os
import click

@click.command()
@click.argument('imgdir', type=click.Path(exists=True))


def main(imgdir):
    allow_suffix_list = ['jpg', 'jpeg', 'png', 'svg']
    for folder, subfolders, files in os.walk(imgdir):
        for num, file in enumerate(files):    
            image_suffix = file.split('.')[-1]
            if image_suffix not in allow_suffix_list:
                continue
            move_path = folder + "/"+ file
            non_forder = folder.replace(".","")
            save_foles_name = non_forder.replace("/","")+ "["+str(num)+"]."+image_suffix
            save_path = "./copy/"+ save_foles_name
            save(move_path, save_path)

def save(move_path, save_path):
    shutil.copy(move_path, save_path)
    print(move_path)
