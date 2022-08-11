# underwater-explorer


## Ros installation

http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi



## Camera library

> libcamera (see: libcamera-hello)

* starting stream on pi:

libcamera-vid -t 0 --inline --listen -o tcp://0.0.0.0:<port>

* listen on client 

vlc tcp/h264://<ip-addr-of-server>:<port>
