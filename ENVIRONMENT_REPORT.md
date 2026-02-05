# Environment Report

Generated on: 2026-02-05T05:10:19.723239+00:00

## OS and Kernel
$ uname -a
Linux becf976fd058 6.12.47 #1 SMP Mon Oct 27 10:01:15 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux

$ cat /etc/os-release
PRETTY_NAME="Ubuntu 24.04.3 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.3 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo

## Uptime and Load
$ uptime
05:10:19 up  1:55,  0 user,  load average: 0.32, 0.10, 0.03

$ cat /proc/uptime
6921.61 20691.57

## CPU
$ lscpu
Architecture:                            x86_64
CPU op-mode(s):                          32-bit, 64-bit
Address sizes:                           46 bits physical, 57 bits virtual
Byte Order:                              Little Endian
CPU(s):                                  3
On-line CPU(s) list:                     0-2
Vendor ID:                               GenuineIntel
Model name:                              Intel(R) Xeon(R) Platinum 8370C CPU @ 2.80GHz
BIOS Model name:                           CPU @ 0.0GHz
BIOS CPU family:                         0
CPU family:                              6
Model:                                   106
Thread(s) per core:                      1
Core(s) per socket:                      3
Socket(s):                               1
Stepping:                                6
BogoMIPS:                                5586.87
Flags:                                   fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves arat avx512vbmi umip avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid fsrm arch_capabilities
Hypervisor vendor:                       KVM
Virtualization type:                     full
L1d cache:                               96 KiB (2 instances)
L1i cache:                               64 KiB (2 instances)
L2 cache:                                2.5 MiB (2 instances)
L3 cache:                                48 MiB (1 instance)
NUMA node(s):                            1
NUMA node0 CPU(s):                       0-2
Vulnerability Gather data sampling:      Not affected
Vulnerability Indirect target selection: Vulnerable
Vulnerability Itlb multihit:             Not affected
Vulnerability L1tf:                      Not affected
Vulnerability Mds:                       Not affected
Vulnerability Meltdown:                  Not affected
Vulnerability Mmio stale data:           Vulnerable
Vulnerability Reg file data sampling:    Not affected
Vulnerability Retbleed:                  Vulnerable
Vulnerability Spec rstack overflow:      Not affected
Vulnerability Spec store bypass:         Vulnerable
Vulnerability Spectre v1:                Vulnerable: __user pointer sanitization and usercopy barriers only; no swapgs barriers
Vulnerability Spectre v2:                Vulnerable; STIBP: disabled; PBRSB-eIBRS: Not affected; BHI: Vulnerable
Vulnerability Srbds:                     Not affected
Vulnerability Tsa:                       Not affected
Vulnerability Tsx async abort:           Not affected
Vulnerability Vmscape:                   Not affected

## Memory
$ free -h
total        used        free      shared  buff/cache   available
Mem:            17Gi       923Mi        16Gi       5.0Mi       912Mi        17Gi
Swap:             0B          0B          0B

## Disk and Filesystems
$ lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,FSTYPE
NAME       SIZE TYPE MOUNTPOINT FSTYPE
vda         64G disk /          
pmem0      254M disk            
└─pmem0p1  253M part

$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/vda         63G   26G   34G  44% /
tmpfs            64M     0   64M   0% /dev
shm             989M     0  989M   0% /dev/shm
kataShared      3.0M   36K  3.0M   2% /etc/hosts

## I/O quick test (dd write/read)
$ rm -f /tmp/io_test.bin; dd if=/dev/zero of=/tmp/io_test.bin bs=1G count=1 conv=fdatasync 2>&1; dd if=/tmp/io_test.bin of=/dev/null bs=1G count=1 2>&1; rm -f /tmp/io_test.bin
1+0 records in
1+0 records out
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 6.19554 s, 173 MB/s
1+0 records in
1+0 records out
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 3.18881 s, 337 MB/s

## Network interfaces
$ command -v ip || true
(no output)

$ command -v ifconfig || true
(no output)

## Network throughput quick test (curl 10MB)
$ curl -L -o /dev/null -s -w "speed=%{speed_download} bytes/s,time=%{time_total}s,code=%{http_code},size=%{size_download}\n" https://proof.ovh.net/files/10Mb.dat
speed=580626 bytes/s,time=18.059399s,code=200,size=10485760

## Language runtimes and toolchain versions
$ python3 --version
Python 3.10.19

$ node --version
v22.21.1

$ npm --version
11.4.2
npm warn Unknown env config "http-proxy". This will stop working in the next major version of npm.

$ go version
go version go1.25.1 linux/amd64

$ rustc --version
rustc 1.92.0 (ded5c06cf 2025-12-08)

$ cargo --version
cargo 1.92.0 (344c4567c 2025-10-21)

$ java --version | head -n 1
openjdk 25.0.1 2025-10-21

$ javac --version
javac 25.0.1

$ ruby --version
ruby 3.2.3 (2024-01-18 revision 52bb2ac0a6) [x86_64-linux]

$ php --version | head -n 1
PHP 8.5.3-dev (cli) (built: Jan 12 2026 17:52:50) (NTS)

$ perl -v | head -n 2
This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi

$ gcc --version | head -n 1
gcc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0

$ g++ --version | head -n 1
g++ (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0

$ clang --version | head -n 1
clang version 17.0.0 (https://github.com/swiftlang/llvm-project.git 9784760565e8cae0bc0b97bad69aaf498408dc3d)

$ git --version
git version 2.43.0

docker: not found
kubectl: not found
terraform: not found
ansible-playbook: not found

## Python package tooling
$ python3 -m pip --version
pip 25.3 from /root/.pyenv/versions/3.10.19/lib/python3.10/site-packages/pip (python 3.10)

## Common CLI tools presence
rg: found
fd: not found
jq: found
yq: not found
make: found
cmake: found
ninja: found
sqlite3: found
psql: not found
mysql: not found
redis-cli: not found
curl: found
wget: found
tar: found
unzip: found
zip: found
tmux: not found
screen: not found
htop: not found
vim: not found
nvim: not found
