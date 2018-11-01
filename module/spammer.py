#!/usr/bin/python

# - Spammer v3.0
# | Description: spams a phone number by sending it a lot of sms by using Grab API
# | Spam: Grab
# | Date: 01/11/2018
# | Disclaimer: For Fun Purpose Only
# | What's New?
# | - Added coloring
# | - Added support multiple proxies (BETA)
# | - Added feature to create a new separate thread for each proxy in order to increase spam speed (BETA)
# | - Added support for phone number with +xxxxxx format 
# | - And another fixes

import spammer_class
spammer = spammer_class.Spammer()
spammer.tema = "Grab Spam"
try:
    spammer.main()
except KeyboardInterrupt:
    print spammer_class.color.FAIL+spammer_class.color.REVERSE+"\r[!][except] KeyboardInterrupt detected! Exiting . . ."+spammer_class.color.ENDC
    exit()

