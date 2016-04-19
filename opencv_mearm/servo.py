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



