import psutil
import os 
import shutil

"""
Run thiscommand in cmd before using

npm install psutil


"""


avlUsb=[]

def print_directory_contents(path):
    try:
        for child in os.listdir(path):
            child_path = os.path.join(path, child)
            if os.path.isdir(child_path):
                print_directory_contents(child_path)
            else:
                print(child)
    except PermissionError as e:
        print("")
        

def copy_directory_contents(source_path, destination_path):
    try:
        for child in os.listdir(source_path):
            source_child_path = os.path.join(source_path, child)
            destination_child_path = os.path.join(destination_path, child)
            if os.path.isdir(source_child_path):
                os.makedirs(destination_child_path, exist_ok=True)
                copy_directory_contents(source_child_path, destination_child_path)
            else:
                shutil.copy2(source_child_path, destination_child_path)
                print(f"Copied: {source_child_path} to {destination_child_path}")
    except PermissionError as e:
        print(f"PermissionError: {e}")

            
            

def print_connected_usbs():
    partitions = psutil.disk_partitions()
    usb_devices = [partition for partition in partitions if 'removable' in partition.opts]

    if usb_devices:
        print("Connected USB devices:")
        x=0
        for device in usb_devices:
            print(f"({x+1})")
            print(f"Device: {device.device}")
            avlUsb.append(device.device)
            print(f"Mountpoint: {device.mountpoint}")
            print(f"File system type: {device.fstype}")

            try:
                labels = psutil.disk_partitions(all=True)
                for label in labels:
                    if label.device == device.device:
                        print(f"Volume type: {label.opts}")
                        break
                else:
                    print("Volume name: N/A")
            except psutil.NotImplementedError:
                print("Volume name: N/A")

            print("-----------------------------")
    else:
        print("No USB devices found.")


# Replace the destination with your's
destinationPath = 'C:\\Users\\muham\\Desktop\\desto'
while True:
    print("++++++++++++++++++++++++++++++++++++")
    selection = int(input("1) Show Available USB's \n2) Print content of selected drive \n3) COPY Data \n4) Exit\n+++Enter:"))
    if(selection == 1):
        avlUsb.clear()
        print_connected_usbs()
    elif (selection == 2):
        print("*******************************")
        choice = int( input("Enter USB Drive option (#) :"))
        choice = choice-1
        print_directory_contents(avlUsb[choice])
        print("////////////////////////////////////")

    elif (selection == 3):
        choice = int( input("Enter USB Drive option (#) :"))
        choice = choice-1
        copy_directory_contents(avlUsb[choice], destinationPath)
    else:
        break


        
