import shutil
import os
import click

@click.command()
@click.option('-i',
        '--importdir',)
@click.option('-s',
        '--savedir',
        default='./copy')
@click.option('-n',
            '--savename',
            default='image')


def main(importdir, savedir, savename):
    print(importdir)
    print(savedir)
    print(savename)
    save_images = []
    move_images = []
    allow_suffixs = []
    allow_suffix_list = ['jpg', 'jpeg', 'png', 'svg']
    for folder, subfolders, files in os.walk(importdir):
        for file in files:    
            image_suffix = file.split('.')[-1]
            if image_suffix not in allow_suffix_list:
                continue
            move_path = folder + "/"+ file
            image_path = savedir+ "/"+savename
            move_images.append(move_path)
            save_images.append(image_path)
            allow_suffixs.append(image_suffix)
    if not os.path.exists(savedir):
        os.mkdir(savedir)
    save(move_images, save_images, allow_suffixs)

def save(move_images, save_images, allow_suffixs):
    for num, save_path in enumerate(save_images):
        save_image_path = save_path+"["+str(num)+"]."+allow_suffixs[num]
        shutil.copy(move_images[num], save_image_path)
        print(save_image_path)
