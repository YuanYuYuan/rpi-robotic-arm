from Adafruit_PWM_Servo_Driver import PWM

# Initialise the PWM device using the default address
pwm = PWM(0x40)
pwm.setPWMFreq(50)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

def setServoPulse(channel, pulse):
    if pulse > 2400:
        pulse = 2400
    elif pulse < 700:
        pulse = 700
    print "pulse = %d " % pulse
    output_duty_cycle = pulse * 4096 / 20000
    print "output_duty_cycle = %d per 12bits" % output_duty_cycle
    pwm.setPWM(channel, 0, output_duty_cycle)


def idle_motion():
    idle_frame = [1620, 1300, 2000, 1000]
    for i in range(4):
        setServoPulse(i, idle_frame[i])

def grip_motion():
    grip_frame = [1620, 2000, 2000, 2200]
    for i in range(3):
        setServoPulse(i + 1, grip_frame[i + 1])

def back_motion():
    back_frame = [1620, 1300, 2000, 2200]
    for i in range(3):
        setServoPulse(i + 1, back_frame[i + 1])




