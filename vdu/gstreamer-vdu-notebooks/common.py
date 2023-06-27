#   Copyright (C) 2023 Advanced Micro Devices, Inc.
#   All rights reserved.
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#
#   1.  Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#   2.  Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#   3.  Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#   THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#   PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#   OR BUSINESS INTERRUPTION). HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#   WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
#   OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

class common_vdu_demo_decode_display:
    def cmd_line_args_generator(INPUT_FILE_PATH, INPUT_URL, CODEC_TYPE, AUDIO_CODEC, DISPLAY_DEVICE, SHOW_FPS, LOOP_VIDEO, INTERNAL_ENTROPY_BUFFERS, PROXY_SERVER_URL, AUDIO_SINK, AUDIO_OUTPUT, SINK_NAME, DEC_INSTANCE):
        CMD_LINE_ARGS = []
        if(len(INPUT_FILE_PATH) != 0):
        	CMD_LINE_ARGS.append('-i')
        	CMD_LINE_ARGS.append(INPUT_FILE_PATH)
        if(len(INPUT_URL) != 0):
        	CMD_LINE_ARGS.append('-u')
        	CMD_LINE_ARGS.append(INPUT_URL)
        if(len(INPUT_FILE_PATH) == 0 and len(INPUT_URL) == 0):
        	CMD_LINE_ARGS.append('-i')
        	CMD_LINE_ARGS.append("/usr/share/movies/bbb_sunflower_2160p_30fps_normal.mp4")
        if(len(CODEC_TYPE) != 0):
        	CMD_LINE_ARGS.append('-c')
        	CMD_LINE_ARGS.append(CODEC_TYPE)
        if(AUDIO_CODEC != 'none'):
        	CMD_LINE_ARGS.append('-a')
        	CMD_LINE_ARGS.append(AUDIO_CODEC)
        if(DISPLAY_DEVICE == 'DP'):
            CMD_LINE_ARGS.append('-d')
            DISPLAY_DEVICE = 'fd4a0000.display'
            CMD_LINE_ARGS.append(DISPLAY_DEVICE)
        elif(DISPLAY_DEVICE == 'HDMI'):
            CMD_LINE_ARGS.append('-d')
            DISPLAY_DEVICE = 'a0070000.v_mix'
            CMD_LINE_ARGS.append(DISPLAY_DEVICE)
        if(SHOW_FPS == 1):
        	CMD_LINE_ARGS.append('-f')
        if(LOOP_VIDEO == 1):
        	CMD_LINE_ARGS.append('-l')
        if(INTERNAL_ENTROPY_BUFFERS != '5'):
        	CMD_LINE_ARGS.append('-e')
        	CMD_LINE_ARGS.append(INTERNAL_ENTROPY_BUFFERS)
        if(len(PROXY_SERVER_URL) != 0):
        	CMD_LINE_ARGS.append('-p')
        	CMD_LINE_ARGS.append(PROXY_SERVER_URL)
        if(AUDIO_SINK == 'pulsesink'):
        	CMD_LINE_ARGS.append('--use-pulsesink')
        elif(AUDIO_SINK == 'alsasink'):
        	CMD_LINE_ARGS.append('--use-alsasink')
        if(len(AUDIO_OUTPUT) != 0):
        	CMD_LINE_ARGS.append('--audio-output')
        	CMD_LINE_ARGS.append(AUDIO_OUTPUT)
        if(SINK_NAME != 'kmssink'):
        	CMD_LINE_ARGS.append('-o')
        	CMD_LINE_ARGS.append(SINK_NAME)
        if(len(DEC_INSTANCE) != 0):
                CMD_LINE_ARGS.append('-z')
                CMD_LINE_ARGS.append(DEC_INSTANCE)
        CMD_LINE_ARGS = " ".join(CMD_LINE_ARGS)
        print("sh common_vdu_demo_decode_display.sh", CMD_LINE_ARGS)
        return CMD_LINE_ARGS
class common_vdu_demo_decode_display_1:
    def cmd_line_args_generator_1(INPUT_FILE_PATH, INPUT_URL, CODEC_TYPE1, AUDIO_CODEC, DISPLAY_DEVICE, SHOW_FPS, LOOP_VIDEO, INTERNAL_ENTROPY_BUFFERS, PROXY_SERVER_URL, AUDIO_SINK, AUDIO_OUTPUT, SINK_NAME, DEC_INSTANCE):
        CMD_LINE_ARGS1 = []
        if(len(INPUT_FILE_PATH) != 0):
        	CMD_LINE_ARGS1.append('-i')
        	CMD_LINE_ARGS1.append(INPUT_FILE_PATH)
        if(len(INPUT_URL) != 0):
        	CMD_LINE_ARGS1.append('-u')
        	CMD_LINE_ARGS1.append(INPUT_URL)
        if(len(INPUT_FILE_PATH) == 0 and len(INPUT_URL) == 0):
        	CMD_LINE_ARGS1.append('-i')
        	CMD_LINE_ARGS1.append("/usr/share/movies/bbb_sunflower_2160p_30fps_normal.mp4")
        if(CODEC_TYPE1 != 'none' and len(CODEC_TYPE1) != 0):
                CMD_LINE_ARGS1.append('--codec-type1')
                CMD_LINE_ARGS1.append(CODEC_TYPE1)
                print("Value of CODEC_TYPE1",CODEC_TYPE1)
        if(AUDIO_CODEC != 'none'):
        	CMD_LINE_ARGS1.append('-a')
        	CMD_LINE_ARGS1.append(AUDIO_CODEC)
        if(DISPLAY_DEVICE == 'DP'):
            CMD_LINE_ARGS1.append('-d')
            DISPLAY_DEVICE = 'fd4a0000.display'
            CMD_LINE_ARGS1.append(DISPLAY_DEVICE)
        elif(DISPLAY_DEVICE == 'HDMI'):
            CMD_LINE_ARGS1.append('-d')
            DISPLAY_DEVICE = 'a0070000.v_mix'
            CMD_LINE_ARGS1.append(DISPLAY_DEVICE)
        if(SHOW_FPS == 1):
        	CMD_LINE_ARGS1.append('-f')
        if(LOOP_VIDEO == 1):
        	CMD_LINE_ARGS1.append('-l')
        if(INTERNAL_ENTROPY_BUFFERS != '5'):
        	CMD_LINE_ARGS1.append('-e')
        	CMD_LINE_ARGS1.append(INTERNAL_ENTROPY_BUFFERS)
        if(len(PROXY_SERVER_URL) != 0):
        	CMD_LINE_ARGS1.append('-p')
        	CMD_LINE_ARGS1.append(PROXY_SERVER_URL)
        if(AUDIO_SINK == 'pulsesink'):
        	CMD_LINE_ARGS1.append('--use-pulsesink')
        elif(AUDIO_SINK == 'alsasink'):
        	CMD_LINE_ARGS1.append('--use-alsasink')
        if(len(AUDIO_OUTPUT) != 0):
        	CMD_LINE_ARGS1.append('--audio-output')
        	CMD_LINE_ARGS1.append(AUDIO_OUTPUT)
        if(SINK_NAME != 'kmssink'):
        	CMD_LINE_ARGS1.append('-o')
        	CMD_LINE_ARGS1.append(SINK_NAME)
        if(len(DEC_INSTANCE) != 0):
                CMD_LINE_ARGS1.append('-z')
                CMD_LINE_ARGS1.append(DEC_INSTANCE)
        CMD_LINE_ARGS1 = " ".join(CMD_LINE_ARGS1)
        print("sh common_vdu_demo_decode_display_1.sh", CMD_LINE_ARGS1)
        return CMD_LINE_ARGS1
class common_vdu_demo_decode_display_2:
    def cmd_line_args_generator_2(INPUT_FILE_PATH, INPUT_URL, CODEC_TYPE2, AUDIO_CODEC, DISPLAY_DEVICE, SHOW_FPS, LOOP_VIDEO, INTERNAL_ENTROPY_BUFFERS, PROXY_SERVER_URL, AUDIO_SINK, AUDIO_OUTPUT, SINK_NAME, DEC_INSTANCE):
        CMD_LINE_ARGS2 = []
        if(len(INPUT_FILE_PATH) != 0):
        	CMD_LINE_ARGS2.append('-i')
        	CMD_LINE_ARGS2.append(INPUT_FILE_PATH)
        if(len(INPUT_URL) != 0):
        	CMD_LINE_ARGS2.append('-u')
        	CMD_LINE_ARGS2.append(INPUT_URL)
        if(len(INPUT_FILE_PATH) == 0 and len(INPUT_URL) == 0):
        	CMD_LINE_ARGS2.append('-i')
        	CMD_LINE_ARGS2.append("/usr/share/movies/bbb_sunflower_2160p_30fps_normal.mp4")
        if(CODEC_TYPE2 != 'none' and len(CODEC_TYPE2) != 0):
                CMD_LINE_ARGS2.append('--codec-type2')
                CMD_LINE_ARGS2.append(CODEC_TYPE2)
                print("Value of CODEC_TYPE2",CODEC_TYPE2)
        if(AUDIO_CODEC != 'none'):
        	CMD_LINE_ARGS2.append('-a')
        	CMD_LINE_ARGS2.append(AUDIO_CODEC)
        if(DISPLAY_DEVICE == 'DP'):
            CMD_LINE_ARGS2.append('-d')
            DISPLAY_DEVICE = 'fd4a0000.display'
            CMD_LINE_ARGS2.append(DISPLAY_DEVICE)
        elif(DISPLAY_DEVICE == 'HDMI'):
            CMD_LINE_ARGS2.append('-d')
            DISPLAY_DEVICE = 'a0070000.v_mix'
            CMD_LINE_ARGS2.append(DISPLAY_DEVICE)
        if(SHOW_FPS == 1):
        	CMD_LINE_ARGS2.append('-f')
        if(LOOP_VIDEO == 1):
        	CMD_LINE_ARGS2.append('-l')
        if(INTERNAL_ENTROPY_BUFFERS != '5'):
        	CMD_LINE_ARGS2.append('-e')
        	CMD_LINE_ARGS2.append(INTERNAL_ENTROPY_BUFFERS)
        if(len(PROXY_SERVER_URL) != 0):
        	CMD_LINE_ARGS2.append('-p')
        	CMD_LINE_ARGS2.append(PROXY_SERVER_URL)
        if(AUDIO_SINK == 'pulsesink'):
        	CMD_LINE_ARGS2.append('--use-pulsesink')
        elif(AUDIO_SINK == 'alsasink'):
        	CMD_LINE_ARGS2.append('--use-alsasink')
        if(len(AUDIO_OUTPUT) != 0):
        	CMD_LINE_ARGS2.append('--audio-output')
        	CMD_LINE_ARGS2.append(AUDIO_OUTPUT)
        if(SINK_NAME != 'kmssink'):
        	CMD_LINE_ARGS2.append('-o')
        	CMD_LINE_ARGS2.append(SINK_NAME)
        if(len(DEC_INSTANCE) != 0):
                CMD_LINE_ARGS2.append('-z')
                CMD_LINE_ARGS2.append(DEC_INSTANCE)
        CMD_LINE_ARGS2 = " ".join(CMD_LINE_ARGS2)
        print("sh common_vdu_demo_decode_display_2.sh", CMD_LINE_ARGS2)
        return CMD_LINE_ARGS2
class common_vdu_demo_decode_display_3:
    def cmd_line_args_generator_3(INPUT_FILE_PATH, INPUT_URL, CODEC_TYPE3, AUDIO_CODEC, DISPLAY_DEVICE, SHOW_FPS, LOOP_VIDEO, INTERNAL_ENTROPY_BUFFERS, PROXY_SERVER_URL, AUDIO_SINK, AUDIO_OUTPUT, SINK_NAME, DEC_INSTANCE):
        CMD_LINE_ARGS3 = []
        if(len(INPUT_FILE_PATH) != 0):
        	CMD_LINE_ARGS3.append('-i')
        	CMD_LINE_ARGS3.append(INPUT_FILE_PATH)
        if(len(INPUT_URL) != 0):
        	CMD_LINE_ARGS3.append('-u')
        	CMD_LINE_ARGS3.append(INPUT_URL)
        if(len(INPUT_FILE_PATH) == 0 and len(INPUT_URL) == 0):
        	CMD_LINE_ARGS3.append('-i')
        	CMD_LINE_ARGS3.append("/usr/share/movies/bbb_sunflower_2160p_30fps_normal.mp4")
        if(CODEC_TYPE3 != 'none' and len(CODEC_TYPE3) != 0):
                CMD_LINE_ARGS3.append('--codec-type3')
                CMD_LINE_ARGS3.append(CODEC_TYPE3)
                print("Value of CODEC_TYPE3",CODEC_TYPE3)
        if(AUDIO_CODEC != 'none'):
        	CMD_LINE_ARGS3.append('-a')
        	CMD_LINE_ARGS3.append(AUDIO_CODEC)
        if(DISPLAY_DEVICE == 'DP'):
            CMD_LINE_ARGS3.append('-d')
            DISPLAY_DEVICE = 'fd4a0000.display'
            CMD_LINE_ARGS3.append(DISPLAY_DEVICE)
        elif(DISPLAY_DEVICE == 'HDMI'):
            CMD_LINE_ARGS3.append('-d')
            DISPLAY_DEVICE = 'a0070000.v_mix'
            CMD_LINE_ARGS3.append(DISPLAY_DEVICE)
        if(SHOW_FPS == 1):
        	CMD_LINE_ARGS3.append('-f')
        if(LOOP_VIDEO == 1):
        	CMD_LINE_ARGS3.append('-l')
        if(INTERNAL_ENTROPY_BUFFERS != '5'):
        	CMD_LINE_ARGS3.append('-e')
        	CMD_LINE_ARGS3.append(INTERNAL_ENTROPY_BUFFERS)
        if(len(PROXY_SERVER_URL) != 0):
        	CMD_LINE_ARGS3.append('-p')
        	CMD_LINE_ARGS3.append(PROXY_SERVER_URL)
        if(AUDIO_SINK == 'pulsesink'):
        	CMD_LINE_ARGS3.append('--use-pulsesink')
        elif(AUDIO_SINK == 'alsasink'):
        	CMD_LINE_ARGS3.append('--use-alsasink')
        if(len(AUDIO_OUTPUT) != 0):
        	CMD_LINE_ARGS3.append('--audio-output')
        	CMD_LINE_ARGS3.append(AUDIO_OUTPUT)
        if(SINK_NAME != 'kmssink'):
        	CMD_LINE_ARGS3.append('-o')
        	CMD_LINE_ARGS3.append(SINK_NAME)
        if(len(DEC_INSTANCE) != 0):
                CMD_LINE_ARGS3.append('-z')
                CMD_LINE_ARGS3.append(DEC_INSTANCE)
        CMD_LINE_ARGS3 = " ".join(CMD_LINE_ARGS3)
        print("sh common_vdu_demo_decode_display_3.sh", CMD_LINE_ARGS3)
        return CMD_LINE_ARGS3



