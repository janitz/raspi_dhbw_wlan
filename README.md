### raspi_dhbw_wlan
## Connect Raspi to WIFI
This Document shows how to connect the raspberry pi to the DHBW-802.1x WIFI access point:

 - `sudo startx` to start The GUI with root rights
 - create the folder `certs` in `/etc/`
 - put [ca.cer](http://github.com/janitz/raspi_dhbw_wlan/blob/master/ca.cer) to `/etc/certs/`
 - replace the [wpa_supplicant.conf](https://github.com/janitz/raspi_dhbw_wlan/blob/master/wpa_supplicant.conf) in `/etc/wpa_supplicant/`
 - change the values for `identity` and `password` in `/etc/wpa_supplicant/wpa_supplicant.conf`
 - restart the raspberry pi

