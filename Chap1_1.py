def cal_to_sec(time):
    ans = (int(time[0])*3600)+(int(time[1]*60))+int(time[2])
    return ans

print('*** Converting hh.mm.ss to seconds ***')
time = list(map(int,input('Enter hh mm ss : ').split()))

if int(time[1]) > 59 or int(time[1]) < 0:
    print(f'mm({time[1]}) is invalid!')
elif int(time[2]) > 59 or int(time[2]) < 0:
    print(f'ss({time[2]}) is invalid!')
else: print(f"{time[0]:02d}:{time[1]:02d}:{time[2]:02d} = " f'{cal_to_sec(time):,} seconds')