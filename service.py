# -*- coding: utf-8 -*-
import xbmcaddon

# Import the common settings
from resources.lib.settings import log
from resources.lib.database import EbooksDB


ADDON = xbmcaddon.Addon(id='script.ebooks')


#########################
# Main
#########################
if __name__ == '__main__':
    log("eBookService: Checking eBooks database version (version %s)" % ADDON.getAddonInfo('version'))

    ebooksDB = EbooksDB()
    ebooksDB.createOrUpdateDB()
    del ebooksDB
