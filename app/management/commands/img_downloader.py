from django.core.management.base import NoArgsCommand, CommandError
from app.models import Album, Band, Review
from multiprocessing import Pool
from PIL import Image, ImageOps
from datetime import datetime

import os
import urllib
import hashlib


def download_and_resize(images):
    urllib.urlretrieve(images['url'], images['path'])
#     im = Image.open(images['path'])
#     method = Image.NEAREST if im.size == (300,300) else Image.ANTIALIAS
#     #thumb = ImageOps.fit(im, (300, 300), method)
#     im.thumbnail((300,300), method)
#     im.save(images['path'].replace("original", "images"))
#     print images['path']
#     print images['path'].replace("original", "images")
    return
            
class Command(NoArgsCommand):
           
    def handle_noargs(self, **options):
   
        images = []
        albums = Album.objects.raw('SELECT `app_album`.`id`, `app_album`.`cover` FROM `app_album` INNER JOIN `app_review` ON `app_review`.`album_id` = `app_album`.`id` WHERE `app_album`.`cover` != "" GROUP BY `app_review`.`album_id` ORDER BY `id` DESC');
        a = datetime.now()
        
        for album in albums:
            print album.id
            try:
                m = hashlib.sha1(str(album.id)).hexdigest()
                path = '/webapps/hme/original/'+m[0]+'/'+m[1]+'/'
#                new_path = '/webapps/hme/images/'+m[0]+'/'+m[1]+'/'
                try:
                    os.makedirs(path)
                except: 
                    pass
#                 try:
#                     os.makedirs(new_path)
#                 except:
#                     pass
                print album.cover
                filename = path + m +".jpg"
                print filename
                images.append({ 'url': album.cover, 'path': filename })
                
            except album.cover == "":
                raise CommandError('Album cover for "%s" does not exists', album.name)
        
        pool = Pool(processes=20)
        result = pool.map(download_and_resize, images)
        
        b = datetime.now()
        c = b - a
        print c.seconds
        return
        


