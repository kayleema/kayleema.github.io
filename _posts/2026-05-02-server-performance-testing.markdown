---
layout: minimal-post
title: "Testing the performance of various servers"
summary: "My notes on cross-platform command line tools, how to run them, and results."
icon: "/images/favicons/apps.png"
---

## Installation
sysbench, fio, stress-ng, iperf3

Mac
```shell
brew install sysbench fio stress-ng
```

Linux Debian-based
```shell
sudo apt install sysbench fio stress-ng
```

# Running
Mac CPU
```shell
sysbench cpu --cpu-max-prime=20000 --threads=$(sysctl -n hw.logicalcpu) run
```
Linux CPU
```shell
sysbench cpu --cpu-max-prime=20000 --threads=$(nproc) run
```
Memory
```shell
sysbench memory --memory-block-size=1M --memory-total-size=10G --memory-access-mode=rnd run
```
Mac File IO
```shell
fio --name=randwrite --ioengine=posixaio --rw=randwrite --bs=4k --numjobs=4 --size=500M --runtime=60 --group_reporting
```
Linux File IO
```shell
fio --name=randwrite --ioengine=libaio --rw=randwrite --bs=4k --numjobs=4 --size=500M --runtime=60 --group_reporting
```
SSL
```shell
openssl speed sha256
```
SSL
```shell
openssl speed rsa2048
```

# Results
## Mac Apple M4 Pro
```shell
CPU speed:
    events per second: 10843886.50

General statistics:
    total time:                          10.0001s
    total number of events:              108441576

Latency (ms):
         min:                                    0.00
         avg:                                    0.00
         max:                                   61.99
         95th percentile:                        0.00
         sum:                                33606.72

Threads fairness:
    events (avg/stddev):           9036798.0000/298897.33
    execution time (avg/stddev):   2.8006/0.03
```
```shell
10240.00 MiB transferred (3085.97 MiB/sec)


General statistics:
    total time:                          3.3181s
    total number of events:              10240

Latency (ms):
         min:                                    0.31
         avg:                                    0.32
         max:                                    2.16
         95th percentile:                        0.00
         sum:                                 3317.36

Threads fairness:
    events (avg/stddev):           10240.0000/0.00
    execution time (avg/stddev):   3.3174/0.00
```
```shell
randwrite: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=posixaio, iodepth=1
...
fio-3.42
Starting 4 processes
Jobs: 2 (f=2): [w(2),_(2)][100.0%][w=66.8MiB/s][w=17.1k IOPS][eta 00m:00s]
randwrite: (groupid=0, jobs=4): err= 0: pid=64926: Sat May  2 18:28:53 2026
  write: IOPS=26.8k, BW=105MiB/s (110MB/s)(2000MiB/19109msec)
    slat (nsec): min=0, max=3781.0k, avg=1246.92, stdev=5988.15
    clat (nsec): min=0, max=8002.0k, avg=144774.21, stdev=293525.42
     lat (usec): min=3, max=8004, avg=146.02, stdev=294.26
    clat percentiles (usec):
     |  1.00th=[    6],  5.00th=[    6], 10.00th=[    8], 20.00th=[    8],
     | 30.00th=[   11], 40.00th=[   85], 50.00th=[   99], 60.00th=[  111],
     | 70.00th=[  116], 80.00th=[  125], 90.00th=[  161], 95.00th=[ 1205],
     | 99.00th=[ 1401], 99.50th=[ 1434], 99.90th=[ 1549], 99.95th=[ 1647],
     | 99.99th=[ 5604]
   bw (  KiB/s): min=52155, max=245256, per=100.00%, avg=109685.48, stdev=8490.75, samples=146
   iops        : min=13038, max=61314, avg=27420.06, stdev=2122.73, samples=146
  lat (nsec)   : 2=0.19%
  lat (usec)   : 2=0.32%, 4=0.20%, 10=27.74%, 20=3.75%, 50=1.26%
  lat (usec)   : 100=16.68%, 250=43.75%, 500=0.82%, 750=0.08%, 1000=0.03%
  lat (msec)   : 2=5.13%, 4=0.02%, 10=0.01%
  cpu          : usr=0.82%, sys=2.26%, ctx=530657, majf=0, minf=27
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,512000,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0.00ns, window=0.00ns, percentile=100.00%, depth=1

Run status group 0 (all jobs):
  WRITE: bw=105MiB/s (110MB/s), 105MiB/s-105MiB/s (110MB/s-110MB/s), io=2000MiB (2097MB), run=19109-19109msec
```
```shell
Doing sha256 ops for 3s on 16 size blocks: 42046315 sha256 ops in 2.98s
Doing sha256 ops for 3s on 64 size blocks: 38850195 sha256 ops in 3.00s
Doing sha256 ops for 3s on 256 size blocks: 23189760 sha256 ops in 2.98s
Doing sha256 ops for 3s on 1024 size blocks: 8563494 sha256 ops in 3.00s
Doing sha256 ops for 3s on 8192 size blocks: 1236600 sha256 ops in 2.99s
Doing sha256 ops for 3s on 16384 size blocks: 623656 sha256 ops in 2.98s
version: 3.6.1
built on: Tue Jan 27 13:33:54 2026 UTC
options: bn(64,64)
compiler: clang -fPIC -arch arm64 -O3 -Wall -DL_ENDIAN -DOPENSSL_PIC -D_REENTRANT -DOPENSSL_BUILDING_OPENSSL -DNDEBUG
CPUINFO: OPENSSL_armcap=0x987d
The 'numbers' are in 1000s of bytes per second processed.
type             16 bytes     64 bytes    256 bytes   1024 bytes   8192 bytes  16384 bytes
sha256          225752.03k   828804.16k  1992140.46k  2923005.95k  3388035.85k  3428852.32k
```
```shell
Doing 2048 bits private rsa sign ops for 10s: 30483 2048 bits private RSA sign ops in 9.96s
Doing 2048 bits public rsa verify ops for 10s: 1203310 2048 bits public RSA verify ops in 9.95s
Doing 2048 bits public rsa encrypt ops for 10s: 1147580 2048 bits public RSA encrypt ops in 9.96s
Doing 2048 bits private rsa decrypt ops for 10s: 29484 2048 bits private RSA decrypt ops in 9.83s
Doing rsa2048 keygen ops for 10s: 390 rsa2048 KEM keygen ops in 9.93s
Doing rsa2048 encaps ops for 10s: 1057711 rsa2048 KEM encaps ops in 9.95s
Doing rsa2048 decaps ops for 10s: 29916 rsa2048 KEM decaps ops in 9.93s
Doing rsa2048 keygen ops for 10s: 384 rsa2048 signature keygen ops in 9.92s
Doing rsa2048 signs ops for 10s: 29743 rsa2048 signature sign ops in 9.95s
Doing rsa2048 verify ops for 10s: 1173987 rsa2048 signature verify ops in 9.94s
version: 3.6.1
built on: Tue Jan 27 13:33:54 2026 UTC
options: bn(64,64)
compiler: clang -fPIC -arch arm64 -O3 -Wall -DL_ENDIAN -DOPENSSL_PIC -D_REENTRANT -DOPENSSL_BUILDING_OPENSSL -DNDEBUG
CPUINFO: OPENSSL_armcap=0x987d
                   sign    verify    encrypt   decrypt   sign/s verify/s  encr./s  decr./s
rsa  2048 bits 0.000327s 0.000008s 0.000009s 0.000333s   3060.5 120935.7 115218.9   2999.4
                               keygen    encaps    decaps keygens/s  encaps/s  decaps/s
                    rsa2048 0.025462s 0.000009s 0.000332s      39.3  106302.6    3012.7
                               keygen     signs    verify keygens/s    sign/s  verify/s
                    rsa2048 0.025833s 0.000335s 0.000008s      38.7    2989.2  118107.3
```

## Oracle Cloud Ampere
```shell
CPU speed:
    events per second:  5113.67

General statistics:
    total time:                          10.0008s
    total number of events:              51148

Latency (ms):
         min:                                    0.77
         avg:                                    0.78
         max:                                    3.02
         95th percentile:                        0.80
         sum:                                39987.48

Threads fairness:
    events (avg/stddev):           12787.0000/38.22
    execution time (avg/stddev):   9.9969/0.00
```
```shell
10240.00 MiB transferred (2425.02 MiB/sec)


General statistics:
    total time:                          4.2212s
    total number of events:              10240

Latency (ms):
         min:                                    0.40
         avg:                                    0.41
         max:                                    1.09
         95th percentile:                        0.42
         sum:                                 4216.94

Threads fairness:
    events (avg/stddev):           10240.0000/0.00
    execution time (avg/stddev):   4.2169/0.00
```
```shell
randwrite: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=1
...
fio-3.36
Starting 4 processes
randwrite: Laying out IO file (1 file / 500MiB)
randwrite: Laying out IO file (1 file / 500MiB)
randwrite: Laying out IO file (1 file / 500MiB)
randwrite: Laying out IO file (1 file / 500MiB)

randwrite: (groupid=0, jobs=4): err= 0: pid=14380: Sat May  2 09:31:17 2026
  write: IOPS=1036k, BW=4049MiB/s (4245MB/s)(2000MiB/494msec); 0 zone resets
    slat (nsec): min=1840, max=1323.4k, avg=2947.72, stdev=11389.78
    clat (nsec): min=400, max=671227, avg=468.04, stdev=1198.72
     lat (usec): min=2, max=1326, avg= 3.42, stdev=11.50
    clat percentiles (nsec):
     |  1.00th=[  402],  5.00th=[  442], 10.00th=[  442], 20.00th=[  442],
     | 30.00th=[  442], 40.00th=[  442], 50.00th=[  442], 60.00th=[  442],
     | 70.00th=[  442], 80.00th=[  442], 90.00th=[  482], 95.00th=[  482],
     | 99.00th=[  804], 99.50th=[ 1080], 99.90th=[ 1800], 99.95th=[10176],
     | 99.99th=[23168]
  lat (nsec)   : 500=97.04%, 750=0.44%, 1000=1.95%
  lat (usec)   : 2=0.49%, 4=0.02%, 10=0.01%, 20=0.04%, 50=0.01%
  lat (usec)   : 100=0.01%, 250=0.01%, 750=0.01%
  cpu          : usr=20.03%, sys=78.74%, ctx=200, majf=0, minf=42
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,512000,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
  WRITE: bw=4049MiB/s (4245MB/s), 4049MiB/s-4049MiB/s (4245MB/s-4245MB/s), io=2000MiB (2097MB), run=494-494msec

Disk stats (read/write):
  sda: ios=0/0, sectors=0/0, merge=0/0, ticks=0/0, in_queue=0, util=0.00%
```
```shell
Doing sha256 for 3s on 16 size blocks: 13718164 sha256's in 3.00s
Doing sha256 for 3s on 64 size blocks: 12255801 sha256's in 3.00s
Doing sha256 for 3s on 256 size blocks: 8690824 sha256's in 3.00s
Doing sha256 for 3s on 1024 size blocks: 4005261 sha256's in 3.00s
Doing sha256 for 3s on 8192 size blocks: 666699 sha256's in 3.00s
Doing sha256 for 3s on 16384 size blocks: 341391 sha256's in 3.00s
version: 3.0.13
built on: Tue Apr  7 12:05:56 2026 UTC
options: bn(64,64)
compiler: gcc -fPIC -pthread -Wa,--noexecstack -Wall -fzero-call-used-regs=used-gpr -DOPENSSL_TLS_SECURITY_LEVEL=2 -Wa,--noexecstack -g -O2 -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -ffile-prefix-map=/build/openssl-A7h8By/openssl-3.0.13=. -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -mbranch-protection=standard -fdebug-prefix-map=/build/openssl-A7h8By/openssl-3.0.13=/usr/src/openssl-3.0.13-0ubuntu3.9 -DOPENSSL_USE_NODELETE -DOPENSSL_PIC -DOPENSSL_BUILDING_OPENSSL -DNDEBUG -Wdate-time -D_FORTIFY_SOURCE=3
CPUINFO: OPENSSL_armcap=0xbd
The 'numbers' are in 1000s of bytes per second processed.
type             16 bytes     64 bytes    256 bytes   1024 bytes   8192 bytes  16384 bytes
sha256           73163.54k   261457.09k   741616.98k  1367129.09k  1820532.74k  1864450.05k
```
```shell
Doing 2048 bits private rsa's for 10s: 3498 2048 bits private RSA's in 10.00s
Doing 2048 bits public rsa's for 10s: 128240 2048 bits public RSA's in 9.99s
version: 3.0.13
built on: Tue Apr  7 12:05:56 2026 UTC
options: bn(64,64)
compiler: gcc -fPIC -pthread -Wa,--noexecstack -Wall -fzero-call-used-regs=used-gpr -DOPENSSL_TLS_SECURITY_LEVEL=2 -Wa,--noexecstack -g -O2 -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -ffile-prefix-map=/build/openssl-A7h8By/openssl-3.0.13=. -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -mbranch-protection=standard -fdebug-prefix-map=/build/openssl-A7h8By/openssl-3.0.13=/usr/src/openssl-3.0.13-0ubuntu3.9 -DOPENSSL_USE_NODELETE -DOPENSSL_PIC -DOPENSSL_BUILDING_OPENSSL -DNDEBUG -Wdate-time -D_FORTIFY_SOURCE=3
CPUINFO: OPENSSL_armcap=0xbd
                  sign    verify    sign/s verify/s
rsa 2048 bits 0.002859s 0.000078s    349.8  12836.8
```

## Oracle Cloud Mini x86 64
```shell
CPU speed:
    events per second:   154.27

General statistics:
    total time:                          10.0065s
    total number of events:              1544

Latency (ms):
         min:                                    2.08
         avg:                                   12.96
         max:                                   97.10
         95th percentile:                       78.60
         sum:                                20006.49

Threads fairness:
    events (avg/stddev):           772.0000/19.00
    execution time (avg/stddev):   10.0032/0.00
```
```shell
Total operations: 700 (  391.51 per second)

700.00 MiB transferred (391.51 MiB/sec)


General statistics:
    total time:                          1.7860s
    total number of events:              700

Latency (ms):
         min:                                    0.81
         avg:                                    2.55
         max:                                   65.35
         95th percentile:                        1.93
         sum:                                 1783.95

Threads fairness:
    events (avg/stddev):           700.0000/0.00
    execution time (avg/stddev):   1.7839/0.00
```
```shell
randwrite: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=1
...
fio-3.36
Starting 4 processes
randwrite: Laying out IO file (1 file / 500MiB)
randwrite: Laying out IO file (1 file / 500MiB)
randwrite: Laying out IO file (1 file / 500MiB)
randwrite: Laying out IO file (1 file / 500MiB)
Jobs: 4 (f=4): [w(4)][100.0%][w=12.5MiB/s][w=3203 IOPS][eta 00m:00s]
randwrite: (groupid=0, jobs=4): err= 0: pid=980348: Sat May  2 09:41:15 2026
  write: IOPS=3439, BW=13.4MiB/s (14.1MB/s)(807MiB/60037msec); 0 zone resets
    slat (usec): min=4, max=302823, avg=1157.22, stdev=8312.54
    clat (nsec): min=1112, max=80793k, avg=3695.35, stdev=284094.53
     lat (usec): min=5, max=302828, avg=1160.91, stdev=8321.85
    clat percentiles (nsec):
     |  1.00th=[   1144],  5.00th=[   1160], 10.00th=[   1160],
     | 20.00th=[   1160], 30.00th=[   1176], 40.00th=[   1176],
     | 50.00th=[   1176], 60.00th=[   1192], 70.00th=[   1288],
     | 80.00th=[   1384], 90.00th=[   1512], 95.00th=[   1960],
     | 99.00th=[   9024], 99.50th=[  19072], 99.90th=[  53504],
     | 99.95th=[ 104960], 99.99th=[2834432]
   bw (  KiB/s): min= 5560, max=93009, per=100.00%, avg=13790.22, stdev=2082.42, samples=476
   iops        : min= 1390, max=23251, avg=3447.21, stdev=520.58, samples=476
  lat (usec)   : 2=95.10%, 4=1.70%, 10=2.32%, 20=0.43%, 50=0.35%
  lat (usec)   : 100=0.06%, 250=0.02%, 500=0.01%, 750=0.01%, 1000=0.01%
  lat (msec)   : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.01%, 50=0.01%
  lat (msec)   : 100=0.01%
  cpu          : usr=0.32%, sys=1.50%, ctx=6162, majf=0, minf=49
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,206506,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
  WRITE: bw=13.4MiB/s (14.1MB/s), 13.4MiB/s-13.4MiB/s (14.1MB/s-14.1MB/s), io=807MiB (846MB), run=60037-60037msec

Disk stats (read/write):
  sda: ios=529/183252, sectors=109304/1597464, merge=36/2118, ticks=10047/3596084, in_queue=3606132, util=89.51%
```
```shell
Doing 2048 bits private rsa's for 10s: 3608 2048 bits private RSA's in 9.99s
Doing 2048 bits public rsa's for 10s: 126270 2048 bits public RSA's in 9.99s
version: 3.0.13
built on: Tue Apr  7 12:05:56 2026 UTC
options: bn(64,64)
compiler: gcc -fPIC -pthread -m64 -Wa,--noexecstack -Wall -fzero-call-used-regs=used-gpr -DOPENSSL_TLS_SECURITY_LEVEL=2 -Wa,--noexecstack -g -O2 -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -ffile-prefix-map=/build/openssl-a6Kur2/openssl-3.0.13=. -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -fcf-protection -fdebug-prefix-map=/build/openssl-a6Kur2/openssl-3.0.13=/usr/src/openssl-3.0.13-0ubuntu3.9 -DOPENSSL_USE_NODELETE -DL_ENDIAN -DOPENSSL_PIC -DOPENSSL_BUILDING_OPENSSL -DNDEBUG -Wdate-time -D_FORTIFY_SOURCE=3
CPUINFO: OPENSSL_ia32cap=0xfff83203078bffff:0x209c01ab
                  sign    verify    sign/s verify/s
rsa 2048 bits 0.002769s 0.000079s    361.2  12639.6
```
```shell
Doing sha256 for 3s on 16 size blocks: 3983196 sha256's in 2.99s
Doing sha256 for 3s on 64 size blocks: 3484566 sha256's in 3.00s
Doing sha256 for 3s on 256 size blocks: 2433750 sha256's in 2.99s
Doing sha256 for 3s on 1024 size blocks: 1131944 sha256's in 3.00s
Doing sha256 for 3s on 8192 size blocks: 181820 sha256's in 3.05s
Doing sha256 for 3s on 16384 size blocks: 92540 sha256's in 3.00s
version: 3.0.13
built on: Tue Apr  7 12:05:56 2026 UTC
options: bn(64,64)
compiler: gcc -fPIC -pthread -m64 -Wa,--noexecstack -Wall -fzero-call-used-regs=used-gpr -DOPENSSL_TLS_SECURITY_LEVEL=2 -Wa,--noexecstack -g -O2 -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -ffile-prefix-map=/build/openssl-a6Kur2/openssl-3.0.13=. -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -fcf-protection -fdebug-prefix-map=/build/openssl-a6Kur2/openssl-3.0.13=/usr/src/openssl-3.0.13-0ubuntu3.9 -DOPENSSL_USE_NODELETE -DL_ENDIAN -DOPENSSL_PIC -DOPENSSL_BUILDING_OPENSSL -DNDEBUG -Wdate-time -D_FORTIFY_SOURCE=3
CPUINFO: OPENSSL_ia32cap=0xfff83203078bffff:0x209c01ab
The 'numbers' are in 1000s of bytes per second processed.
type             16 bytes     64 bytes    256 bytes   1024 bytes   8192 bytes  16384 bytes
sha256           21314.76k    74337.41k   208374.58k   386370.22k   488350.64k   505391.79k
```

## Intel n150 Mini-PC

```shell
CPU speed:
    events per second:  4193.72

General statistics:
    total time:                          10.0007s
    total number of events:              41945

Latency (ms):
         min:                                    0.94
         avg:                                    0.95
         max:                                    2.83
         95th percentile:                        0.95
         sum:                                39990.71

Threads fairness:
    events (avg/stddev):           10486.2500/6.65
    execution time (avg/stddev):   9.9977/0.00
```
```shell
10240.00 MiB transferred (4065.46 MiB/sec)


General statistics:
    total time:                          2.5176s
    total number of events:              10240

Latency (ms):
         min:                                    0.24
         avg:                                    0.25
         max:                                    0.71
         95th percentile:                        0.25
         sum:                                 2515.97

Threads fairness:
    events (avg/stddev):           10240.0000/0.00
    execution time (avg/stddev):   2.5160/0.00
```
```shell
randwrite: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=1
...
fio-3.41
Starting 4 processes
randwrite: Laying out IO file (1 file / 500MiB)
randwrite: Laying out IO file (1 file / 500MiB)
randwrite: Laying out IO file (1 file / 500MiB)
randwrite: Laying out IO file (1 file / 500MiB)

randwrite: (groupid=0, jobs=4): err= 0: pid=14478: Sat May  2 13:00:52 2026
  write: IOPS=878k, BW=3431MiB/s (3597MB/s)(2000MiB/583msec); 0 zone resets
    slat (nsec): min=1925, max=970489, avg=3335.65, stdev=3476.93
    clat (nsec): min=462, max=721179, avg=654.42, stdev=1644.18
     lat (usec): min=2, max=973, avg= 3.99, stdev= 3.87
    clat percentiles (nsec):
     |  1.00th=[  572],  5.00th=[  596], 10.00th=[  604], 20.00th=[  612],
     | 30.00th=[  620], 40.00th=[  628], 50.00th=[  628], 60.00th=[  636],
     | 70.00th=[  644], 80.00th=[  652], 90.00th=[  668], 95.00th=[  684],
     | 99.00th=[  748], 99.50th=[  844], 99.90th=[ 2960], 99.95th=[ 6304],
     | 99.99th=[22400]
   bw (  MiB/s): min= 3510, max= 3510, per=100.00%, avg=3510.67, stdev= 0.00, samples=4
   iops        : min=898730, max=898730, avg=898730.00, stdev= 0.00, samples=4
  lat (nsec)   : 500=0.53%, 750=98.51%, 1000=0.58%
  lat (usec)   : 2=0.11%, 4=0.18%, 10=0.07%, 20=0.01%, 50=0.01%
  lat (usec)   : 100=0.01%, 250=0.01%, 500=0.01%, 750=0.01%
  cpu          : usr=25.25%, sys=73.26%, ctx=817, majf=0, minf=33
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=0,512000,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
  WRITE: bw=3431MiB/s (3597MB/s), 3431MiB/s-3431MiB/s (3597MB/s-3597MB/s), io=2000MiB (2097MB), run=583-583msec

Disk stats (read/write):
    dm-0: ios=0/0, sectors=0/0, merge=0/0, ticks=0/0, in_queue=0, util=0.00%, aggrios=0/741, aggsectors=0/131136, aggrmerge=0/6, aggrticks=0/961, aggrin_queue=961, aggrutil=21.42%
  sda: ios=0/741, sectors=0/131136, merge=0/6, ticks=0/961, in_queue=961, util=21.42%
```
```shell
Doing sha256 ops for 3s on 16 size blocks: 25844302 sha256 ops in 3.00s
Doing sha256 ops for 3s on 64 size blocks: 21215194 sha256 ops in 3.00s
Doing sha256 ops for 3s on 256 size blocks: 13427519 sha256 ops in 3.00s
Doing sha256 ops for 3s on 1024 size blocks: 5439775 sha256 ops in 3.00s
Doing sha256 ops for 3s on 8192 size blocks: 829929 sha256 ops in 3.00s
Doing sha256 ops for 3s on 16384 size blocks: 421831 sha256 ops in 3.00s
version: 3.5.5
built on: Tue Apr  7 12:05:56 2026 UTC
options: bn(64,64)
compiler: gcc -fPIC -pthread -m64 -Wa,--noexecstack -Wall -fzero-call-used-regs=used-gpr -Wa,--noexecstack -g -O2 -Werror=implicit-function-declaration -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -ffile-prefix-map=/build/openssl-pn5a0v/openssl-3.5.5=. -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -fcf-protection -fdebug-prefix-map=/build/openssl-pn5a0v/openssl-3.5.5=/usr/src/openssl-3.5.5-1ubuntu3 -DOPENSSL_USE_NODELETE -DL_ENDIAN -DOPENSSL_PIC -DOPENSSL_BUILDING_OPENSSL -DZLIB -DZSTD -DNDEBUG -Wdate-time -D_FORTIFY_SOURCE=3
CPUINFO: OPENSSL_ia32cap=0x7ffaf3ffffebffff:0x98c007bc239ca7eb:0x00000810fc184410:0x0000000000040000:0x0000000000000000
The 'numbers' are in 1000s of bytes per second processed.
type             16 bytes     64 bytes    256 bytes   1024 bytes   8192 bytes  16384 bytes
sha256          137836.28k   452590.81k  1145814.95k  1856776.53k  2266259.46k  2303759.70k
```
```shell
Doing 2048 bits private rsa sign ops for 10s: 7896 2048 bits private RSA sign ops in 10.00s
Doing 2048 bits public rsa verify ops for 10s: 266480 2048 bits public RSA verify ops in 10.00s
Doing 2048 bits public rsa encrypt ops for 10s: 258589 2048 bits public RSA encrypt ops in 9.98s
Doing 2048 bits private rsa decrypt ops for 10s: 7854 2048 bits private RSA decrypt ops in 10.00s
Doing rsa2048 keygen ops for 10s: 120 rsa2048 KEM keygen ops in 10.04s
Doing rsa2048 encaps ops for 10s: 253235 rsa2048 KEM encaps ops in 9.98s
Doing rsa2048 decaps ops for 10s: 7894 rsa2048 KEM decaps ops in 10.00s
Doing rsa2048 keygen ops for 10s: 108 rsa2048 signature keygen ops in 10.01s
Doing rsa2048 signs ops for 10s: 7900 rsa2048 signature sign ops in 10.00s
Doing rsa2048 verify ops for 10s: 266118 rsa2048 signature verify ops in 10.00s
version: 3.5.5
built on: Tue Apr  7 12:05:56 2026 UTC
options: bn(64,64)
compiler: gcc -fPIC -pthread -m64 -Wa,--noexecstack -Wall -fzero-call-used-regs=used-gpr -Wa,--noexecstack -g -O2 -Werror=implicit-function-declaration -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -ffile-prefix-map=/build/openssl-pn5a0v/openssl-3.5.5=. -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -fcf-protection -fdebug-prefix-map=/build/openssl-pn5a0v/openssl-3.5.5=/usr/src/openssl-3.5.5-1ubuntu3 -DOPENSSL_USE_NODELETE -DL_ENDIAN -DOPENSSL_PIC -DOPENSSL_BUILDING_OPENSSL -DZLIB -DZSTD -DNDEBUG -Wdate-time -D_FORTIFY_SOURCE=3
CPUINFO: OPENSSL_ia32cap=0x7ffaf3ffffebffff:0x98c007bc239ca7eb:0x00000810fc184410:0x0000000000040000:0x0000000000000000
                   sign    verify    encrypt   decrypt   sign/s verify/s  encr./s  decr./s
rsa  2048 bits 0.001266s 0.000038s 0.000039s 0.001273s    789.6  26648.0  25910.7    785.4
                               keygen    encaps    decaps keygens/s  encaps/s  decaps/s
                    rsa2048 0.083667s 0.000039s 0.001267s      12.0   25374.2     789.4
                               keygen     signs    verify keygens/s    sign/s  verify/s
                    rsa2048 0.092685s 0.001266s 0.000038s      10.8     790.0   26611.8
```