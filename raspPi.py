import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
# import numpy as np
# import tensorflow as tf


class ParkingLot:

    def __init__(self, lot):

        self.lot = lot
        self.lotInfo = lot.to_dict()

        print(self.lotInfo)

        self.name, self.pSpaces, self.tSpaces= self.extractInfo()

    # extracInfo organizes parking lot from firebase a class dictionary
    def extractInfo(self):
        print(self.lotInfo)

        name = self.lot.id
        pSpaces = self.lotInfo['parking_spaces']
        tSpaces = self.lotInfo['taken_spaces']

        return name, pSpaces, tSpaces

    def setTSpaces(self, num):

        if type(num) == int:

            self.tSpaces = num

# Changes the value of the free spaces available based on the parking lot and the number of free spaces passed to the function.
def updateNumOfFreeSpaces(lot, free_spaces):

    tgr_ref = uwi.document(lot.name)

    time.sleep(10)
    print("Sending new info")
    lot.setTSpaces(free_spaces)
    tgr_ref.update({u'taken_spaces' : lot.tSpaces})

    tgr = tgr_ref.get()
    print("Available spaces:", tgr.to_dict())

    # time.sleep(10)
    # print("Sending new info")
    # parkingLots[0].setTSpaces(parkingLots[0].tSpaces - 5)
    # tgr_ref.update({u'taken_spaces' : parkingLots[0].tSpaces})
    # tgr_ref.update({u'parking_spaces': 50})
    #
    # tgr = tgr_ref.get()
    # print("Available spaces:", tgr.to_dict())


cred = credentials.Certificate('UWIParkServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

uwi = db.collection(u'parking_lots')
lots = uwi.get()

x = 0
parkingLots = []
fireLots = []

for lot in lots:
    fireLots.append(lot)
    parkingLots.append(ParkingLot(lot))

print(parkingLots[0].name, parkingLots[0].tSpaces)

updateNumOfFreeSpaces(parkingLots[0], 25)

print(parkingLots[0].name, parkingLots[0].tSpaces)
