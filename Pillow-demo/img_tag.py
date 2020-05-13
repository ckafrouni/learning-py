from PIL import Image, ExifTags

def dict_print(dic):
    for k in dic:
        print(f'{k} --> {dic[k]}')
    print()

def remove_metadata(img):
    with Image.open(img) as image:
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        image_without_exif.save('image_file_without_exif.jpeg')

def get_metadata(img):
    with Image.open(img) as image:
        exif = {
            ExifTags.TAGS[k]: v
            for k, v in image.getexif().items()
            if k in ExifTags.TAGS
        }
    if len(exif) == 0:
        print('Image does not have metadata')
        return None
    return exif
    
def get_gps_info(exif):
    gpsinfo = {}
    for key in exif['GPSInfo'].keys():
        decode = ExifTags.GPSTAGS.get(key,key)
        gpsinfo[decode] = exif['GPSInfo'][key]
    return gpsinfo


img0 = 'example.jpg'
img1 = 'image_file_without_exif.jpeg'
img2 = '/Users/christophekafrouni/Desktop/Images-Sample/00.jpeg'
img3 = '65863425_10156990902193127_3053897630661738496_o.jpg'
img4 = 'me.jpg'
img5 = 'Carlos.jpg'

if __name__ == "__main__":
    img = img5
    exif = get_metadata(img)
    if exif != None:
        dict_print(exif)
        gps_info = get_gps_info(exif)
        dict_print(gps_info)
    