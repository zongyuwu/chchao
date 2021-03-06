import os

def playMusic(sheet):
	for i in range(len(sheet)):
		for (frq, dur) in sheet[i]:
			os.system("beep -f " + str(frq) + " -l " + str(dur*60*1000/tempo))
	
tempo = 150

C0 = 16
C0sharp = 17
D0 = 18
D0sharp = 19
E0 = 20
F0 = 21
F0sharp = 23
G0 = 24
G0sharp = 25
A0 = 27
A0sharp = 29
B0 = 30
C1 = 32
C1sharp = 34
D1 = 36
D1sharp = 38
E1 = 41
F1 = 43
F1sharp = 46
G1 = 49
G1sharp = 51
A1 = 55
A1sharp = 58
B1 = 61
C2 = 65
C2sharp = 69
D2 = 73
D2sharp = 77
E2 = 82
F2 = 87
F2sharp = 92
G2 = 98
G2sharp = 103
A2 = 110
A2sharp = 116
B2 = 123
C3 = 130
C3sharp = 138
D3 = 146
D3sharp = 155
E3 = 164
F3 = 174
F3sharp = 185
G3 = 196
G3sharp = 207
A3 = 220
A3sharp = 233
B3 = 246
C4 = 261
C4sharp = 277
D4 = 293
D4sharp = 311
E4 = 329
F4 = 349
F4sharp = 369
G4 = 392
G4sharp = 415
A4 = 440
A4sharp = 466
B4 = 493
C5 = 523
C5sharp = 554
D5 = 587
D5sharp = 622
E5 = 659
F5 = 698
F5sharp = 739
G5 = 783
G5sharp = 830
A5 = 880
A5sharp = 932
B5 = 987
C6 = 1046
C6sharp = 1108
D6 = 1174
D6sharp = 1244
E6 = 1318
F6 = 1396
F6sharp = 1479
G6 = 1567
G6sharp = 1661
A6 = 1760
A6sharp = 1864
B6 = 1975
C7 = 2093
C7sharp = 2217
D7 = 2349
D7sharp = 2489
E7 = 2637
F7 = 2793
F7sharp = 2959
G7 = 3135
G7sharp = 3322
A7 = 3520
A7sharp = 3729
B7 = 3951
C8 = 4186
C8sharp = 4434
D8 = 4698
D8sharp = 4978
E8 = 5274
F8 = 5587
F8sharp = 5919
G8 = 6271
G8sharp = 6644
A8 = 7040
A8sharp = 7458
B8 = 7902
STOP = 1

music = [[]]
music.append([
# 1
	(D4, 0.75),
	(D4, 0.75),
	(C4, 0.5),
	(D4, 0.75),
	(D4, 0.75),
	(C4, 0.5),
])
music.append([
	(D4, 0.75),
	(D4, 0.75),
	(C4, 0.5),
	(D4, 1),
	(F4, 1),
])
music.append([
# 3
	(D4, 0.75),
	(D4, 0.75),
	(C4, 0.5),
	(D4, 0.75),
	(D4, 0.75),
	(C4, 0.5),
])
music.append([
	(D4, 1),
	(F4, 1),
	(G4, 1),
	(A4, 1),
])
music.append([
# 5
	(G4, 0.5),
	(A4, 0.5),
	(D4, 0.25),
	(C4, 0.25),
	(D4, 0.25),
	(C4, 0.25),
	(G4, 0.5),
	(A4, 0.5),
	(D4, 0.25),
	(C4, 0.25),
	(D4, 0.25),
	(C4, 0.25),
])
music.append([
	(G4, 0.5),
	(A4, 0.5),
	(D4, 0.25),
	(C4, 0.25),
	(D4, 0.25),
	(C4, 0.25),
	(F4, 0.5),
	(E4, 0.1666),
	(F4, 0.1666),
	(E4, 0.1666),
	(D4, 0.5),
	(C4, 0.5),
])
music.append([
# 7
	(G4, 0.5),
	(A4, 0.5),
	(D4, 0.25),
	(C4, 0.25),
	(D4, 0.25),
	(C4, 0.25),
	(G4, 0.5),
	(A4, 0.5),
	(D4, 0.25),
	(C4, 0.25),
	(D4, 0.25),
	(C4, 0.25),
])
music.append([
	(G4, 0.5),
	(A4, 0.5),
	(C5, 0.5),
	(F5, 0.5),
	(E5, 0.25),
	(F5, 0.25),
	(E5, 0.25),
	(D5, 0.25),
	(C5, 0.5),
	(A4, 0.5),
])
music.append([
# 9
	(G4, 0.5),
	(A4, 0.5),
	(D4, 0.25),
	(C4, 0.25),
	(D4, 0.25),
	(C4, 0.25),
	(G4, 0.5),
	(A4, 0.5),
	(D4, 0.25),
	(C4, 0.25),
	(D4, 0.25),
	(C4, 0.25),
])
music.append([
	(G4, 0.5),
	(A4, 0.5),
	(D4, 0.25),
	(C4, 0.25),
	(D4, 0.25),
	(C4, 0.25),
	(F4, 0.5),
	(E4, 0.1666),
	(F4, 0.1666),
	(E4, 0.1666),
	(D4, 0.5),
	(C4, 0.5),
])
music.append([
# 11
	(D4, 0.5),
	(C4, 0.25),
	(D4, 0.25),
	(F4, 0.5),
	(D4, 0.25),
	(G4, 0.25),
	(A4, 0.5),
	(G4, 0.25),
	(A4, 0.25),
	(C5, 0.25),
	(F5, 0.25),
	(A4, 0.25),
	(C5, 0.25),
])
music.append([
	(F5, 0.5),
	(E5, 0.1666),
	(F5, 0.1666),
	(E5, 0.1666),
	(D5, 0.5),
	(C5, 0.5),
	(D5, 1),
	(D5, 0.5),
	(F5, 0.5),
])
# 13
music.append([
	(G5, 0.5),
	(A5, 0.5),
	(D5, 0.25),
	(C5, 0.25),
	(D5, 0.25),
	(C5, 0.25),
	(G5, 0.5),
	(A5, 0.5),
	(D5, 0.25),
	(C5, 0.25),
	(D5, 0.25),
	(C5, 0.25),
])
music.append([
	(G5, 0.5),
	(A5, 0.5),
	(D5, 0.25),
	(C5, 0.25),
	(D5, 0.25),
	(C5, 0.25),
	(F5, 0.5),
	(E5, 0.1666),
	(F5, 0.1666),
	(E5, 0.1666),
	(D5, 0.5),
	(C5, 0.5),
])
music.append([
# 15
	(G5, 0.5),
	(A5, 0.5),
	(D5, 0.25),
	(C5, 0.25),
	(D5, 0.25),
	(C5, 0.25),
	(G5, 0.5),
	(A5, 0.5),
	(D5, 0.25),
	(C5, 0.25),
	(D5, 0.25),
	(C5, 0.25),
])
music.append([
	(G5, 0.5),
	(A5, 0.5),
	(C6, 0.5),
	(F6, 0.5),
	(E6, 0.25),
	(F6, 0.25),
	(E6, 0.25),
	(D6, 0.25),
	(C6, 0.5),
	(A5, 0.5),
])
# 17
music.append([
	(G5, 0.5),
	(A5, 0.5),
	(D5, 0.25),
	(C5, 0.25),
	(D5, 0.25),
	(C5, 0.25),
	(G5, 0.5),
	(A5, 0.5),
	(D5, 0.25),
	(C5, 0.25),
	(D5, 0.25),
	(C5, 0.25),
])
music.append([
	(G5, 0.5),
	(A5, 0.5),
	(D5, 0.25),
	(C5, 0.25),
	(D5, 0.25),
	(C5, 0.25),
	(F5, 0.5),
	(E5, 0.1666),
	(F5, 0.1666),
	(E5, 0.1666),
	(D5, 0.5),
	(C5, 0.5),
])
# 19
music.append([
	(A5, 0.25),
	(G5, 0.25),
	(A5, 0.25),
	(C6, 0.25),
	(D6, 0.25),
	(C6, 0.25),
	(A5, 0.25),
	(G5, 0.25),
	(D5, 0.5),
	(F5, 0.5),
	(G5, 0.5),
	(A5, 0.5),
])
music.append([
	(D5, 0.75),
	(D5, 0.75),
	(C5, 0.5),
	(D5, 1),
	(STOP, 1),
])

""" melody """
# 21
music.append([
	(D5, 0.75),
	(D5, 0.25),
	(D5, 0.5),
	(C5, 0.5),
	(D5, 0.5),
	(F5, 0.5),
	(F5, 0.5),
	(G5, 0.5),
])
music.append([
	(D5, 0.75),
	(D5, 0.25),
	(D5, 0.5),
	(C5, 0.5),
	(D5, 0.5),
	(C5, 0.5),
	(A4, 0.5),
	(C5, 0.5),
])
# 23
music.append([
	(D5, 0.75),
	(D5, 0.25),
	(D5, 0.5),
	(C5, 0.5),
	(D5, 0.5),
	(F5, 0.5),
	(G5, 0.5),
	(A5, 0.5),
])
music.append([
	(A5, 1),
	(G5, 0.5),
	(A5, 0.25),
	(G5, 0.25),
	(F5, 1),
	(D5, 1),
])
# 25
music += music[21:21+4]
# 29
music.append([
	(F5, 1),
	(E5, 1),
	(D5, 1),
	(C5, 1),
])
music.append([
	(C5, 0.5),
	(D5, 0.25),
	(C5, 0.25),
	(A4, 0.5),
	(G4, 0.5),
	(A4, 2),
])
# 31
music.append([
	(A4, 0.5),
	(C5, 0.5),
	(D5, 1),
	(G5, 1),
	(E5, 1),
])
music.append([
	(F5, 1),
	(E5, 0.5),
	(C5, 0.5),
	(D5, 2),
])
# 33
music.append(music[29])
music.append([
	(C5, 0.5),
	(D5, 0.25),
	(C5, 0.25),
	(A4, 0.5),
	(G4, 0.5),
	(A4, 1),
	(A4, 0.5),
	(C5, 0.5),
])
# 35
music.append([
	(D5, 0.5),
	(D5, 1),
	(D5, 0.5),
	(F5, 1),
	(G5, 1),
])
music.append([
	(E5, 2),
	(STOP, 1),
	(D5, 0.5),
	(F5, 0.5),
])

# 37
music.append([
	(G5, 0.75),
	(G5, 0.75),
	(A5, 0.5),
	(A5, 1),
	(STOP, 0.5),
	(A5, 0.5),
])
music.append([
	(C6, 0.5),
	(D6, 0.5),
	(G5, 0.5),
	(F5, 0.5),
	(A5, 1),
	(D5, 0.5),
	(F5, 0.5),
])
# 39
music.append([
	(G5, 0.75),
	(G5, 0.75),
	(A5, 0.5),
	(A5, 1),
	(STOP, 0.5),
	(A5, 0.5),
])
music.append([
	(A5sharp, 0.5),
	(A5, 0.5),
	(G5, 0.5),
	(F5, 0.5),
	(F5, 1),
	(D5, 0.5),
	(F5, 0.5),
])
# 41
music += music[37:37+2]
# 43
music.append([
	(A5sharp, 1),
	(A5, 1),
	(G5, 1),
	(F5, 1),
])
music.append([
	(G5, 0.5),
	(A5, 0.5),
	(E5, 0.5),
	(C5, 0.5),
	(D5, 1),
	(D5, 0.5),
	(F5, 0.5),
])
# 45 
music += music[37:37+7]
music.append([
	(G5, 0.5),
	(F5, 0.5),
	(A5, 0.5),
	(C6, 0.5),
	(D6, 2),
])
# 53
music.append([
	(D6, 0.5),
	(D6, 0.5),
	(D6, 0.5),
	(D6, 0.5),
	(D6, 0.5),
	(D6, 0.5),
	(D6, 0.25),
	(C6, 0.25),
	(A5, 0.5),
])
music.append([
	(G5, 0.5),
	(G5, 0.5),
	(G5, 0.5),
	(G5, 0.5),
	(G5, 0.5),
	(G5, 0.5),
	(G5, 0.25),
	(F5, 0.25),
	(D5, 0.5),
])
# 55	
music.append([
	(D5, 0.5),
	(D5, 0.5),
	(D5, 0.5),
	(D5, 0.5),
	(D5, 0.5),
	(D5, 0.5),
	(D5, 0.25),
	(C5, 0.25),
	(A4, 0.5),
])
music.append([
	(G4, 0.5),
	(A4, 0.25),
	(G4, 0.25),
	(A4, 0.25),
	(C5, 0.25),
	(C5sharp, 0.25),
	(D5, 0.25),
	(E5, 0.1666),
	(G5, 0.1666),
	(A5, 0.1666),
	(D6, 0.25),
	(F6, 0.25),
	(E6, 0.5),
	(D6, 0.25),
	(E6, 0.25),
])
# 57
music.append([
	(A5, 0.25),
	(F5, 0.25),
	(D5, 0.25),
	(A5, 0.5),
	(A5, 0.25),
	(F5, 0.25),
	(D5, 0.25),
	(A5, 0.25),
	(F5, 0.25),
	(D5, 0.25),
	(A5, 0.5),
	(A5, 0.25),
	(F5, 0.25),
	(D5, 0.25),
])
music.append([
	(A5sharp, 0.25),
	(G5, 0.25),
	(D5sharp, 0.25),
	(A5sharp, 0.5),
	(A5sharp, 0.25),
	(G5, 0.25),
	(D5sharp, 0.25),
	(A5sharp, 0.25),
	(G5, 0.25),
	(D5sharp, 0.25),
	(A5sharp, 0.5),
	(A5sharp, 0.25),
	(G5, 0.25),
	(D5sharp, 0.25),
])
# 59
music.append([
	(A5sharp, 0.25),
	(F5, 0.25),
	(D5, 0.25),
	(A5sharp, 0.5),
	(A5sharp, 0.25),
	(F5, 0.25),
	(D5, 0.25),
	(A5sharp, 0.25),
	(F5, 0.25),
	(D5, 0.25),
	(A5sharp, 0.5),
	(A5sharp, 0.25),
	(F5, 0.25),
	(D5, 0.25),
])
music.append([
	(G5, 0.25),
	(E5, 0.25),
	(C5, 0.25),
	(G5, 0.5),
	(G5, 0.25),
	(E5, 0.25),
	(C5, 0.25),
	(A5, 0.25),
	(E5, 0.25),
	(C5sharp, 0.25),
	(A5, 0.5),
	(A5, 0.25),
	(E5, 0.25),
	(C5sharp, 0.25),
])
# 61
music.append([
	(A5, 0.25),
	(F5, 0.25),
	(D5, 0.25),
	(A5, 0.25),
	(D6, 0.25),
	(A5, 0.25),
	(F5, 0.25),
	(D5, 0.25),
	(A5, 0.25),
	(F5, 0.25),
	(D5, 0.25),
	(A5, 0.25),
	(F6, 0.1666),
	(E6, 0.1666),
	(D6, 0.1666),
	(A5, 0.25),
	(F5, 0.25),
])
music.append([
	(A5sharp, 0.25),
	(G5, 0.25),
	(D5sharp, 0.25),
	(A5sharp, 0.25),
	(D6sharp, 0.25),
	(A5sharp, 0.25),
	(G5, 0.25),
	(D5sharp, 0.25),
	(A5sharp, 0.25),
	(G5, 0.25),
	(D5sharp, 0.25),
	(A5sharp, 0.25),
	(G6, 0.1666),
	(F6, 0.1666),
	(D6sharp, 0.1666),
	(A5sharp, 0.25),
	(G5, 0.25),
])
# 63
music.append([
	(D6, 0.25),
	(A5sharp, 0.25),
	(F5, 0.25),
	(A5sharp, 0.25),
	(F6, 0.25),
	(A5sharp, 0.25),
	(D6, 0.25),
	(F6, 0.25),
	(A6sharp, 0.25),
	(F6, 0.25),
	(D6, 0.25),
	(A5sharp, 0.25),
	(A5sharp, 0.25),
	(G5, 0.25),
	(F5, 0.25),
	(D5, 0.25),
])
music.append([
	(C5, 0.25),
	(G4, 0.25),
	(E4, 0.25),
	(C4, 0.25),

	(G3, 0.25),
	(A3, 0.25),
	(C4, 0.25),
	(D4, 0.25),

	(E4, 0.25),
	(G4, 0.25),
	(A4, 0.25),
	(C5sharp, 0.25),

	(A4, 0.0833),
	(A4sharp, 0.0833),
	(B4, 0.0833),
	(C5, 0.0833),
	(C5sharp, 0.0833),
	(D5, 0.0833),
	(D5sharp, 0.0833),
	(E5, 0.0833),
	(F5, 0.0833),
	(F5sharp, 0.0833),
	(G5, 0.0833),
	(G5sharp, 0.0833),
	(A5, 0.0833),
])
# 65
music.append([
	(A5, 0.1666),
	(F5, 0.1666),
	(G5, 0.1666),
	(F5, 0.1666),
	(G5, 0.1666),
	(A5, 0.1666),
	
	(F5, 0.1666),
	(G5, 0.1666),
	(A5, 0.1666),
	(G5, 0.1666),
	(F5, 0.1666),
	(E5, 0.1666),
	
	(G5, 0.1666),
	(E5, 0.1666),
	(F5, 0.1666),
	(G5, 0.1666),
	(F5, 0.1666),
	(E5, 0.1666),
	
	(D5, 0.1666),
	(E5, 0.1666),
	(D5, 0.1666),
	(E5, 0.1666),
	(D5, 0.1666),
	(C5, 0.1666),
])
music.append([
	(A4, 0.1666),
	(G4, 0.1666),
	(A4, 0.1666),
	(G4, 0.1666),
	(F4, 0.1666),
	(E4, 0.1666),

	(F4, 0.1666),
	(G4, 0.1666),
	(F4, 0.1666),
	(G4, 0.1666),
	(F4, 0.1666),
	(G4, 0.1666),
	(D4, 2)
])
# 67
music.append([
	(D3, 0.25),
	(D3, 0.25),
	(E3, 0.25),
	(E3, 0.25),
	(F3, 0.25),
	(F3, 0.25),
	(A3, 0.25),
	(A3, 0.25),
	
	(G3, 0.25),
	(A3, 0.25),
	(G3, 0.25),
	(G3, 0.25),

	(E4, 0.1666),
	(F4, 0.1666),
	(E4, 0.1666),
	(D4, 0.1666),
	(E4, 0.1666),
	(F4, 0.1666),
])
music.append([
	(A4, 1),
	(C5, 0.5),
	(A4, 0.5),
	(A4, 2),
])
# 69
music.append([
	(D3, 0.25),
	(D3, 0.25),
	(C3, 0.25),
	(C3, 0.25),
	(F3, 0.25),
	(F3, 0.25),
	(E3, 0.25),
	(E3, 0.25),
	
	(A3, 0.25),
	(A3, 0.25),
	(G3, 0.25),
	(G3, 0.25),
	(D4, 0.25),
	(D4, 0.25),
	(C4, 0.25),
	(C4, 0.25),
])
music.append([
	(G4, 0.25),
	(G4, 0.25),
	(F4, 0.25),
	(F4, 0.25),
	(C5, 0.5),
	(C5, 0.5),
	(C5, 2),
])
# 71
music.append([
	(F5, 0.25),
	(D5, 0.25),
	(A4sharp, 0.25),
	(F4, 0.25),
	(D4, 0.25),
	(F4, 0.25),
	(A4sharp, 0.25),
	(D5, 0.25),
	
	(G5, 0.25),
	(E5, 0.25),
	(C5, 0.25),
	(G4, 0.25),
	(E4, 0.25),
	(G4, 0.25),
	(C5, 0.25),
	(E5, 0.25),
])
music.append([
	(A5, 0.75),
	(G5, 0.75),
	(A5, 0.25),
	(G5, 0.25),
	(A5, 2),
])
# 73
music += music[29:29+15]
music.append([
	(G5, 0.5),
	(A5, 0.5),
	(G5, 0.5),
	(A5, 0.5),
	(A5, 1),
	(E5, 0.5),
	(G5, 0.5),
])

# 89
for measure in music[37:37+7]:
	m = []
	for (frq, dur) in measure:
		m += [(int(frq*1.1224), dur)]
	music += [m]
music.append([
	(A5, 0.5),
	(G5, 0.5),
	(B5, 0.5),
	(D6, 0.5),
	(E6, 2),
])
# 97
for measure in music[5:5+15]:
	m = []
	for (frq, dur) in measure:
		m += [(int(frq*1.1224), dur)]
	music += [m]
music.append([
	(E6, 0.75),
	(E6, 0.75),
	(D6, 0.5),
	(E6, 1),
	(STOP, 0.5),
	(D6, 0.25),
	(D6sharp, 0.25),
])
music.append([
	(E6, 0.75),
	(E6, 0.75),
	(D6, 0.5),
	(E6, 1),
	(STOP, 1),
])





def main():
	playMusic(music)

main()
