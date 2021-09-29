#!/bin/bash
file_locations=/datarepo/dataforashok/separation_10p4__nonspinning__vertBfield
Poynx_0=$file_locations/Poynx.file_0.h5
Poynx_1=$file_locations/Poynx.file_1.h5
Poynx_2=$file_locations/Poynx.file_2.h5
Poynx_3=$file_locations/Poynx.file_3.h5
Poynx_4=$file_locations/Poynx.file_4.h5
Poynx_5=$file_locations/Poynx.file_5.h5
Poynx_6=$file_locations/Poynx.file_6.h5
Poynx_7=$file_locations/Poynx.file_7.h5
Poynx_8=$file_locations/Poynx.file_8.h5
Poynx_9=$file_locations/Poynx.file_9.h5
Poynx_10=$file_locations/Poynx.file_10.h5
Poynx_11=$file_locations/Poynx.file_11.h5
Poynx_12=$file_locations/Poynx.file_12.h5
Poynx_13=$file_locations/Poynx.file_13.h5
Poynx_14=$file_locations/Poynx.file_14.h5
Poynx_15=$file_locations/Poynx.file_15.h5



Poyny_0=$file_locations/Poyny.file_0.h5
Poyny_1=$file_locations/Poyny.file_1.h5
Poyny_2=$file_locations/Poyny.file_2.h5
Poyny_3=$file_locations/Poyny.file_3.h5
Poyny_4=$file_locations/Poyny.file_4.h5
Poyny_5=$file_locations/Poyny.file_5.h5
Poyny_6=$file_locations/Poyny.file_6.h5
Poyny_7=$file_locations/Poyny.file_7.h5
Poyny_8=$file_locations/Poyny.file_8.h5
Poyny_9=$file_locations/Poyny.file_9.h5
Poyny_10=$file_locations/Poyny.file_10.h5
Poyny_11=$file_locations/Poyny.file_11.h5
Poyny_12=$file_locations/Poyny.file_12.h5
Poyny_13=$file_locations/Poyny.file_13.h5
Poyny_14=$file_locations/Poyny.file_14.h5
Poyny_15=$file_locations/Poyny.file_15.h5


Poynz_0=$file_locations/Poynz.file_0.h5
Poynz_1=$file_locations/Poynz.file_1.h5
Poynz_2=$file_locations/Poynz.file_2.h5
Poynz_3=$file_locations/Poynz.file_3.h5
Poynz_4=$file_locations/Poynz.file_4.h5
Poynz_5=$file_locations/Poynz.file_5.h5
Poynz_6=$file_locations/Poynz.file_6.h5
Poynz_7=$file_locations/Poynz.file_7.h5
Poynz_8=$file_locations/Poynz.file_8.h5
Poynz_9=$file_locations/Poynz.file_9.h5
Poynz_10=$file_locations/Poynz.file_10.h5
Poynz_11=$file_locations/Poynz.file_11.h5
Poynz_12=$file_locations/Poynz.file_12.h5
Poynz_13=$file_locations/Poynz.file_13.h5
Poynz_14=$file_locations/Poynz.file_14.h5
Poynz_15=$file_locations/Poynz.file_15.h5



./hdf5_merge $Poynx_0 $Poyny_0 $Poynz_0  $file_locations/Poynxyz.file_0.h5
./hdf5_merge $Poynx_1 $Poyny_1 $Poynz_1  $file_locations/Poynxyz.file_1.h5
./hdf5_merge $Poynx_2 $Poyny_2 $Poynz_2  $file_locations/Poynxyz.file_2.h5
./hdf5_merge $Poynx_3 $Poyny_3 $Poynz_3  $file_locations/Poynxyz.file_3.h5
./hdf5_merge $Poynx_4 $Poyny_4 $Poynz_4  $file_locations/Poynxyz.file_4.h5
./hdf5_merge $Poynx_5 $Poyny_5 $Poynz_5  $file_locations/Poynxyz.file_5.h5
./hdf5_merge $Poynx_6 $Poyny_6 $Poynz_6  $file_locations/Poynxyz.file_6.h5
./hdf5_merge $Poynx_7 $Poyny_7 $Poynz_7  $file_locations/Poynxyz.file_7.h5
./hdf5_merge $Poynx_8 $Poyny_8 $Poynz_8  $file_locations/Poynxyz.file_8.h5
./hdf5_merge $Poynx_9 $Poyny_9 $Poynz_9  $file_locations/Poynxyz.file_9.h5
./hdf5_merge $Poynx_10 $Poyny_10 $Poynz_10  $file_locations/Poynxyz.file_10.h5
./hdf5_merge $Poynx_11 $Poyny_11 $Poynz_11  $file_locations/Poynxyz.file_11.h5
./hdf5_merge $Poynx_12 $Poyny_2 $Poynz_12  $file_locations/Poynxyz.file_12.h5
./hdf5_merge $Poynx_13 $Poyny_3 $Poynz_13  $file_locations/Poynxyz.file_13.h5
./hdf5_merge $Poynx_14 $Poyny_4 $Poynz_14  $file_locations/Poynxyz.file_14.h5
./hdf5_merge $Poynx_15 $Poyny_5 $Poynz_15  $file_locations/Poynxyz.file_15.h5

