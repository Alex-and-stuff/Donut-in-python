import math
import numpy as np
import os
import sys
theta_spacing = 0.07
phi_spacing = 0.02
screen_width = 70
screen_height = 40
R1 = 1
R2 = 2
K2 = 5
K1 = screen_width*K2*2/(9*(R1+R2))
# K1 = 20
luminance_chart = ['\033[31;5m.\033[0m', '\033[91;5m,\033[0m', '\033[33;5m-\033[0m', '\033[93;5m~\033[0m', 
                   '\033[92;5m:\033[0m', '\033[32;5m;\033[0m', '\033[36;5m=\033[0m', '\033[94;5m!\033[0m', 
                   '\033[34;5m*\033[0m', '\033[35;5m#\033[0m', '\033[95;5m$\033[0m', '\033[97;5m@\033[0m'] 
#luminance_chart = ['.', ',', '-', ';', ':', ';', '=', '!', '*', '#', '$', '@'] 

def show_donut(A, B):
    sinA = math.sin(A)
    cosA = math.cos(A)
    sinB = math.sin(B)
    cosB = math.cos(B)
    
    output = [[' ' for i in range(screen_width)] for j in range(screen_height)]
    z_buffer = [[0 for i in range(screen_width)] for j in range(screen_height)]

    for theta in np.arange(0, 2*math.pi, theta_spacing):
        costheta = math.cos(theta)
        sintheta = math.sin(theta)
        for phi in np.arange(0, 2*math.pi, phi_spacing):
            cosphi = math.cos(phi)
            sinphi = math.sin(phi)
            circlex = R2 + R1*costheta
            circley = R1*sintheta

            x = circlex*(cosB*cosphi + sinA*sinB*sinphi) - circley*cosA*sinB
            y = circlex*(sinB*cosphi - sinA*cosB*sinphi) + circley*cosA*cosB
            z = K2 + cosA*circlex*sinphi + circley*sinA
            ooz = 1/z

            xp = int(screen_width/2 + K1*ooz*x)
            yp = int(screen_height/2 - K1*ooz*y)
            if xp > screen_width or yp > screen_height:
                print('xp: ', xp, 'yp: ', yp, 'ooz: ', ooz, 'K1: ', K1, 'x: ', x, 'y: ', y, K1*ooz*x, K1*ooz*y)

            L = cosphi*costheta*sinB - cosA*costheta*sinphi - sinA*sintheta + cosB*(cosA*sintheta - costheta*sinA*sinphi)
            if L > 0:
                if ooz > z_buffer[yp][xp]:
                    z_buffer[yp][xp] = ooz
                    luminance_index = int(L*8)
                    output[yp][xp] = luminance_chart[luminance_index]

    #  print out output values individualy
    # for j in range(screen_height):
    #     for i in range(screen_width):
    #         print(output[j][i], end = '') #  , prevents newline
    #     print('')
    #os.system('cls')
    print('\x1b[H')
    print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in output]))
    #os.system('cls' if os.name == 'nt' else 'clear')

#print('\x1b[H')

for i in range(1500):
    show_donut(i/10,i/10-i/30)
    # for i in range(5000):
    #     a = 0
    #print('\x1b[2K\r') # ANSI escape code -> "\x1b": escape, "[2k": erase current line
    #os.system('cls' if os.name == 'nt' else 'clear')
    

print('\ndone!')
