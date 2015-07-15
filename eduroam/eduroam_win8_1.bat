rem netsh wlan export profile name="eduroam"
netsh wlan delete profile name="eduroam"
netsh wlan add profile filename="%cd%\Wi-Fi-eduroam.xml"