Versal:VideoDecodeUnit-ReadMe
============================================

Table of Contents
=================
• Supported VDU-Features and Specification
• VDU out-of-box Examples Description
• Conguration settings for standalone pipelines
• Sample Gstreamer Pipelines
• Sample Control-Software/Openmax Pipelines


========================================
I. VDU out-of-box Examples Description
========================================

 Supported VDU out of box examples are mentioned below, Desktop application shows two VDU examples (4K AVC Decode and 4K HEVC Decode)  icons corresponding to VDU-Decode->Display usecase, more details are mentioned in Example-1.

 1. VDU-Decode → Display: Decodes AVC/HEVC encoded container stream and Displays on DP monitor. It supports aac/vorbis audio decode along with video.

===============================
II.  Steps to Verify Examples:
===============================

 1. Boot the Board (VEK280) using petalinux pre-builts.
     • Make sure the Board is connected to Ethernet, this is required to download sample video content from Xilinx web server.
     • If Board is connected to private network, then export proxy settings in /home/root/.bashrc file as below,
	     i.  create/open a bashrc file using "vi ~/.bashrc"
	     ii. Insert below line to bashrc file
		     export http_proxy="<private network proxy address>"
		     export https_proxy="<private network proxy address>"
     • If the board is not connected to internet, then compressed video files can be downloaded using host machine and copy input files into
       "/home/root/" folder. Use below commands to download the content on host linux-machine.
     • Download AVC sample file:  wget petalinux.xilinx.com/sswreleases/video-files/bbb_sunflower_2160p_30fps_normal_avc_new.mp4
     • Download HEVC sample file: wget petalinux.xilinx.com/sswreleases/video-files/bbb_sunflower_2160p_30fps_normal_hevc.mkv

 2. Example-1: (Decode → Display)
    • Matchbox Desktop will have below two applications
    • 4K AVC Decode:
	i. Click on this application, it will download sample AVC/AAC encoded bitstream and run VDU Example-1 (Decode → Display).
	ii. If the sample avc content is already present in /home/root then it will just decode→display the content.
    • 4K HEVC Decode: same as above but it uses HEVC/Voribis encoded bitstream.
    • Decode→ Display can be executed using command line option as well, use below command to run this example.
      Running the script with "-h" option shows all possible options.
	i.  vdu-demo-decode-display.sh -i /home/root/bbb_sunflower_2160p_30fps_normal_avc_new.mp4 -c avc -a aac -z allegrodecIP0
	ii. vdu-demo-decode-display.sh -i /home/root/bbb_sunflower_2160p_30fps_normal_hevc.mkv -c hevc -a vorbis -z allegrodecIP0
    • Run below command to play youtube video, make sure ethernet is connected to board.
	i. vdu-demo-decode-display.sh -u "youtube-URL"
    • Run below command for help
	i. vdu-demo-decode-display.sh -h

  Note: Currently vek280 has some HDMI issues so will be only supporting decode->fakevideosink.

===============================
III. Sample Gstreamer Pipelines
==============================

 "$gst-inspect-1.0 <element_name>" can be used to check the description of gstreamer elements and its properties.

 For Ex: To get description of each parameters for “omxh264dec” element run as below:
 xilinx-vek280-es1-20231:~#gst-inspect-1.0 omxh264dec

 H264 Decode:
 ===========
 Decode h264 input file and display on DP monitor.

 >> gst-launch-1.0 filesrc location="input-file.mp4" ! qtdemux name=demux demux.video_0 ! h264parse ! omxh264dec device=/dev/allegroDecodeIP0 ! queue max-size-bytes=0 ! kmssink bus-id=fd4a0000.display fullscreen-overlay=1

 H265 Decode:
 ===========
 Decode h265 input file and display on DP monitor.

 >> gst-launch-1.0 filesrc location="input-file.mp4" ! qtdemux name=demux demux.video_0 ! h265parse ! omxh265dec device=/dev/allegroDecodeIP0 ! queue max-size-bytes=0 ! kmssink bus-id=fd4a0000.display fullscreen-overlay=1
 (Note: Input-file.mp4 could be of any format ( 420/422 8bit , 420/422 10bit))

 Higher bitrate bitstream decoding: Decoder may take more than one frame period time for high bitrate decoding (> 100Mbps). Use below options to get better decoder performance.
 • Increase internal entropy buffers count to 9.
 • Add a queue at decoder input side.
 • The below command decodes h264 video file using 9 internal entropy buffers.

 >> gst-launch-1.0 filesrc location="input-file.mp4" ! qtdemux name=demux demux.video_0 ! h264parse ! queue max-size-bytes=0 ! omxh264dec device=/dev/allegroDecodeIP0 internal-entropy-buffers=9 ! queue max-size-bytes=0 ! kmssink bus-id=fd4a0000.display fullscreen-overlay=1


 Multistream Decoding:
 ====================
 Decode h265 video using 4 decoder elements simultaneously and save them to separate files

 >> gst-launch-1.0 filesrc location=input_1920x1080.mp4 ! qtdemux ! h265parse ! tee name=t t. ! queue ! omxh265dec device=/dev/allegroDecodeIP0 ! queue max-size-bytes=0 ! filesink location=output_0_1920x1080.yuv t. ! queue ! omxh265dec device=/dev/allegroDecodeIP1 ! queue max-size-bytes=0 ! filesink location=output_1_1920x1080.yuv t. ! queue ! omxh265dec device=/dev/allegroDecodeIP3 ! queue max-size-bytes=0 ! filesink location=output_2_1920x1080.yuv t. ! queue ! omxh265dec device=/dev/allegroDecodeIP4 ! queue max-size-bytes=0 ! filesink location=output_3_1920x1080.yuv

 Note: tee element is used to feed same input file into 4 decoder instances, user can use separate gst-launch-1.0 application to feed different inputs.


=========================================
Sample Openmax/Control-Software Pipelines
=========================================

 Openmax Examples
 ================

 �"omx_decoder –help�" shows all the options for decoder application
 �"omx_encoder –help�" shows all the options for encoder application

 Decode File to File:
 >> omx_decoder input-file.h265 -hevc -o out.yuv --device /dev/allegroDecodeIP0

 (Note: Input YUV file should be in NV12 format)

 Control-Software Examples
 =========================

 Decode File to File:

 H264 Decode:
 >> ctrlsw_decoder -avc -in input-avc-file.h264 -out ouput.yuv --device /dev/allegroDecodeIP0

 H265 Decode:
 >> ctrlsw_decoder -hevc -in input-hevc-file.h265 -out ouput.yuv --device /dev/allegroDecodeIP0


Note: Users can use this as a demo example to run decode applications at control software with different encoder configurations.
