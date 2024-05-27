# Dumping the flash

the flash chip in the Max model V1.1 is an Foresee FMDNN008G EMMC chip. 

the EMMc chip is an bga153 chip. [link](https://xonstorage.blob.core.windows.net/pdf/foresee_femdnn008g08a39_xonjuly20_20_link.pdf) 

if it's desoldered it could be read by [such a device](https://www.amazon.com/ALLSOCKET-eMMC153-FBGA153-169-KMVTU000LM-B503-THGBM5G7A4JBA4W/dp/B06Y55DKND/ref=cm_cr_arp_d_pb_opt?ie=UTF8&th=1)

Before buying a 100$ device, might be better to find out if other ways are possible. this device is also not really needed, as the chip could also be hacky soldered into an sd card reader. The protocol used is apparently the same as an sd card. [This](https://www.youtube.com/watch?v=ny82c3wLOFo) video suggests this.
Would still need a heat gun of some sort to desolder the chip from the mainboard.

found a [github page](https://github.com/voltlog/emmc-wfbga153-microsd) which a emmc chip can be soldered to, and can then be plugged into a computer. so for a few $ and a reflow soldering station, it might be possible to read the flash.