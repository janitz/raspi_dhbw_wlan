### raspi_dhbw_wlan
## Connect Raspberry Pi to WIFI
This document shows how to connect the raspberry pi to the DHBW-802.1x WIFI access point:

 - `sudo startx` to start the GUI with root rights
 - create the folder `certs` in `/etc/`
 - put [ca.cer](http://github.com/janitz/raspi_dhbw_wlan/blob/master/ca.cer) to `/etc/certs/`
 - replace the [wpa_supplicant.conf](https://github.com/janitz/raspi_dhbw_wlan/blob/master/wpa_supplicant.conf) in `/etc/wpa_supplicant/`
 - change the values for `identity` and `password` in `/etc/wpa_supplicant/wpa_supplicant.conf`
 - stop the wifi with `ifdown wlan0`
 - restart the wifi with `ifup wlan0`

