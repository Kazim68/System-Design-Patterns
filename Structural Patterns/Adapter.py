class UsbCable:
    def __init__(self):
        self.isPlugged = False
    
    def plugUsb(self):
        self.isPlugged = True
        print("USB Cable is plugged in")

class UsbPort:
    def __init__(self):
        self.isPortAvailable = True

    def plug(self, usb):
        usb.plugUsb()
        self.isPortAvailable = False
        print("USB plugged in successfully")
    
# UsbCables can directly plug into Usb ports
usbCable = UsbCable()
usbPort1 = UsbPort()
usbPort1.plug(usbCable)


class MicroUsbCable:
    def __init__(self):
        self.isPlugged = False

    def plugMicroUsb(self):
        self.isPlugged = True
    

class MicroToUsbAdapter(UsbCable):
    def __init__(self, microUsbCable):
        self.microUsbCable = microUsbCable
        self.microUsbCable.plugMicroUsb()
    
    # can override UsbCable.plugUsb() if needed


# microUsbCables can plug into usbPorts via adapter
microToUsbAdapter = MicroToUsbAdapter(MicroUsbCable())
usbPort2 = UsbPort()
usbPort2.plug(microToUsbAdapter)