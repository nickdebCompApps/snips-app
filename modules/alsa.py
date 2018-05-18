import alsaaudio


class Alsa():
    
    def __init__(self):
        self.mixer = alsaaudio.Mixer('PCM')
        self.volume = int(self.mixer.getvolume()[0])
        
        
    def volumeUp(self):
        if self.volume <= 90:
            self.volume + 10
        if self.volume >= 91:
            self.volume = 100
        self.mixer.setvolume(self.volume)
        
    def volumeDown(self):
        if self.volume <= 10:
            sef.volume = self.volume = 0
        if self.volume >= 11:
            self.volume = self.volume - 10
        self.mixer.setvolume(self.volume)
        
    def volumeSet(self, volume):
        self.volume = volume
        self.mixer.setvolume(self.volume)