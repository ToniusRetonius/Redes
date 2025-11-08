#!/usr/bin/env python3

import sys
from scapy.all import *
from time import *
from statistics import mean
from collections import Counter

responses = {}
only_ips = {}

for i in range(30):
    # print()
    for ttl in range(1,25):
        probe = IP(dst=sys.argv[1], ttl=ttl) / ICMP()
        t_i = time()
        ans = sr1(probe, verbose=False, timeout=0.8)
        t_f = time()
        rtt = (t_f - t_i)*1000
        if ans is not None:
            if ttl not in responses:
                responses[ttl] = []
            
            if ttl not in only_ips:
                only_ips[ttl] = []

            if (ans[ICMP].type == 11):    
                responses[ttl].append((ans.src, rtt))
                # me quedo con las ips
                only_ips[ttl].append(ans.src)

            # if ttl in responses:
            #     print(ttl, responses[ttl])

# Guardo la ip más frecuente por ttl
most_freq_ips = {}
for ttl, lista in only_ips.items():
    if lista:
        most_freq_ip = Counter(lista).most_common(1)[0][0]
        most_freq_ips[ttl] = most_freq_ip

# Capturo los rtts de esa ip más frecuente y por cada key:ttl asigno el avg_rtt (el rtt promedio)
rtts_for_most_freq_ip = {}
avg_rtt_for_most_freq_ip = {}

for ttl, lista in responses.items():
    if ttl in most_freq_ips:
        rtts_for_most_freq_ip[ttl] = [tupla for tupla in lista if tupla[0] == most_freq_ips[ttl]]
        
        # sólo me quedo con los rtts
        rtts = [rtt for (_, rtt) in rtts_for_most_freq_ip[ttl]]
        if rtts:
            avg_rtt_for_most_freq_ip[ttl] = mean(rtts)

# Imprimo
# for ttl, avg in avg_rtt_for_most_freq_ip.items():
#     print(most_freq_ips[ttl], avg)


# Ahora queda calcular el rtt entre saltos
ttls_ordenados = sorted(avg_rtt_for_most_freq_ip.keys())
rtt_entre_saltos = {}

for i in range(1, len(ttls_ordenados)):
    t1 = ttls_ordenados[i-1]
    t2 = ttls_ordenados[i]
    diff = avg_rtt_for_most_freq_ip[t2] - avg_rtt_for_most_freq_ip[t1]
    if diff > 0:
        rtt_entre_saltos[(t1, t2)] = diff

# Imprimo
for (t1,t2), diff in rtt_entre_saltos.items():
    print(t1, t2, diff)





