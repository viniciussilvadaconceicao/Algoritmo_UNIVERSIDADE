'''1. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos).'''

mb = int(input('digite o tamanho do arquivo em MB:')) 
mbps = float(input('digite a velocidade do link da internet em MBPS: ')) 

mb_bits = mb * 8 * 1024 * 1024  
# 1 MB = 8 bits * 1024 KB * 1024 bytes

mbps_vel = mbps * 1024 * 1024  
# 1 Mbps = 1024 * 1024 bits por segundo

tempo_seg = mb_bits / mbps_vel
# calculando o tempo  

print(f'O tempo aproximado para baixar um o arquivo usando esse link é {tempo_seg:.1f} min.')