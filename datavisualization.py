from PIL import Image
import requests
from io import BytesIO
import zipfile
import pathlib 
import random
import os
import warnings
from data_extraction import extract_data


warnings.filterwarnings("ignore")



def visualise_image():
    try:
        url = extract_data()
        url_response = requests.get(url)
        url_response.raise_for_status()  # Raise an error for bad responses
        with zipfile.ZipFile(BytesIO(url_response.content)) as z:
            z.extractall('.')
        print("Data extraction successful.")
    except requests.exceptions.RequestException as e:
        print("Error downloading data:", e)
    except zipfile.BadZipFile:
        print("The downloaded file is not a valid zip file.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    Alaxan_images = os.listdir(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Alaxan/"))
    Bactidol_images = os.listdir(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Bactidol/"))
    Bioflu_images = os.listdir(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Bioflu/"))
    Biogesic_images = os.listdir(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Biogesic/"))
    DayZinc_images = os.listdir(os.path.join(os.getcwd(),"Drug Vision/Data Combined/DayZinc/"))
    Decolgen_images = os.listdir(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Decolgen/"))
    Fish_Oil_images = os.listdir(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Fish Oil/"))
    Kremil_S_images = os.listdir(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Kremil S/"))
    Medicol_images = os.listdir(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Medicol/"))
    Neozep_images = os.listdir(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Neozep/"))
    
    path = pathlib.Path(os.path.join(os.getcwd(),"Drug Vision/Data Combined/"))
    def open_random_image(path):
        # Get a list of all files in the folder
        all_files = os.listdir(path)
        random_image_file = random.choice(all_files)
        image_path = os.path.join(path, random_image_file)
        image = Image.open(image_path)
        return image
    Alaxan_image = open_random_image(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Alaxan"))
    Bactidol_image = open_random_image(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Bactidol/"))
    Bioflu_image = open_random_image(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Bioflu/"))
    Biogesic_image = open_random_image(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Biogesic/"))
    DayZinc_image = open_random_image(os.path.join(os.getcwd(),"Drug Vision/Data Combined/DayZinc/"))
    Decolgen_image = open_random_image(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Decolgen/"))
    Fish_Oil_image = open_random_image(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Fish Oil/"))
    Kremil_S_image = open_random_image(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Kremil S/"))
    Medicol_image = open_random_image(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Medicol/"))
    Neozep_image = open_random_image(os.path.join(os.getcwd(),"Drug Vision/Data Combined/Neozep/"))
    
    
    Alaxan_image.save('Alaxan.jpg')
    Bactidol_image.save('Bactidol.jpg')
    Bioflu_image.save('Bioflu.jpg')
    Biogesic_image.save('Biogesic.jpg')
    DayZinc_image.save('DayZinc.jpg')
    Decolgen_image.save('Decolgen.jpg')
    Fish_Oil_image.save('Fish Oil.jpg')
    Kremil_S_image.save('Kremil S.jpg')
    Medicol_image.save('Medicol.jpg')
    Neozep_image.save('Neozep.jpg')
    return path,Alaxan_images,Bactidol_images,Bioflu_images,Biogesic_images, DayZinc_images, Decolgen_images, Fish_Oil_images, Kremil_S_images, Medicol_images, Neozep_images

visualise_image()


#--------------------------------------------------------

#fig = px.pie(
#    names=class_names,
#    values=class_distribution,
#    width=500,
#    hole=0.2,
#    title="Class Distribution"
#)
#fig.update_layout({'title':{'x':0.5}})
#fig.write_image("class_distribution.jpg")
#
#gen = ImageDataGenerator(rescale=1./255,rotation_range=20,brightness_range=[0.5,0.9],horizontal_flip=True,zoom_range=0.2,validation_split=0.2)
#
## Dataset
#train_data = gen.flow_from_directory(dataset,shuffle=True,batch_size=32,target_size=(256,256),class_mode='binary',subset='training')
#valid_data = gen.flow_from_directory(dataset,shuffle=True,batch_size=32,target_size=(256,256),class_mode='binary',subset='validation')
#
#print("train_data---------",train_data)
#print("valid_data---------", valid_data)

#-----------------------------------------------------------------------------------------
