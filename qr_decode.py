#!/usr/bin/env python

import sys
import qrtools

image = sys.argv[1]
qr = qrtools.QR()
qr.decode(image)

print qr.data
