
import tempfile
import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy  
assert numpy  
def rec_audio(filename="audiorec_"):
    q = queue.Queue()


    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())

    samplerate=None
    #filename=None
    device=None
    channels=1
    subtype=None
    try:
        if samplerate is None:
            device_info = sd.query_devices(device, 'input')
            # soundfile expects an int, sounddevice provides a float:
            samplerate = int(device_info['default_samplerate'])
        if filename is not None:
            filename = tempfile.mktemp(prefix=filename,
                                            suffix='.wav', dir='')

        # Make sure the file is opened before recording anything:
        with sf.SoundFile(filename, mode='x', samplerate=samplerate,
                        channels=channels, subtype=subtype) as file:
            with sd.InputStream(samplerate=samplerate, device=device,
                                channels=channels, callback=callback):
                print('#' * 50)
                print('press Ctrl+C to stop the recording')
                print('#' * 50)
                while True:
                    file.write(q.get())
    except KeyboardInterrupt:
        print('\nRecording finished: ' + repr(filename))
    
    return filename
        


