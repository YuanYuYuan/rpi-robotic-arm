import wx
from Adafruit_PWM_Servo_Driver import PWM
import time


# Initialise the PWM device using the default address
pwm = PWM(0x40)
pwm.setPWMFreq(50)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

def setServoPulse(channel, pulse):
    print "pulse = %d " % pulse
    output_duty_cycle = pulse * 4096 / 20000
    print "output_duty_cycle = %d per 12bits" % output_duty_cycle
    pwm.setPWM(channel, 0, output_duty_cycle)

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (600, 200), pos = (700, 300))
        panel = wx.Panel(self)
        self.Bind(wx.EVT_CHAR_HOOK, self.OnKeyUp)
        
        for i in range (0,4):
            label = wx.StaticText(panel, label = "Servo"+ str(i), pos = (30 + i * 150, 10), id = i)
            slider = wx.Slider(panel, minValue = 700, maxValue = 2400, value = 1500, 
                    style = wx.SL_VERTICAL | wx.SL_LABELS, pos = (150 * i, 50), size = (100,100), id = i) 
            slider.Bind(wx.EVT_SCROLL, self.servo)

    def OnKeyUp(self, event):
        keyCode = event.GetKeyCode()
        if keyCode == wx.WXK_ESCAPE:
            pwm.softwareReset()            
            self.Close()

    def servo(self, event):
        slider = event.GetEventObject()
        id = slider.GetId()
        value = slider.GetValue()
        print "Servo%d:  %d" % (id, value)
        setServoPulse(id, value)
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "MeArm")
        frame.Show(True)
        return True

app = MyApp()
app.MainLoop()


