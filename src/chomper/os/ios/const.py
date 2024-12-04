# System call numbers

SYS_READ = 0x3
SYS_OPEN = 0x5
SYS_CLOSE = 0x6
SYS_GETPID = 0x14
SYS_GETUID = 0x18
SYS_GETEUID = 0x19
SYS_ACCESS = 0x21
SYS_GETPPID = 0x27
SYS_GETEGID = 0x2B
SYS_GETTIMEOFDAY = 0x74
SYS_CSOPS = 0xA9
SYS_RLIMIT = 0xC2
SYS_LSEEK = 0xC7
SYS_SYSCTL = 0xCA
SYS_SHM_OPEN = 0x10A
SYS_SYSCTLBYNAME = 0x112
SYS_GETTID = 0x11E
SYS_PSYNCH_MUTEXWAIT = 0x12D
SYS_ISSETUGID = 0x147
SYS_PROC_INFO = 0x150
SYS_STAT64 = 0x152
SYS_FSTAT64 = 0x153
SYS_LSTAT64 = 0x154
SYS_READ_NOCANCEL = 0x18C
SYS_OPEN_NOCANCEL = 0x18E
SYS_CLOSE_NOCANCEL = 0x18F
SYS_GETENTROPY = 0x1F4

MACH_ABSOLUTE_TIME_TRAP = 0xFFFFFFFD
MACH_TIMEBASE_INFO_TRAP = 0xFFFFFFFFFFFFFFA7
MACH_MSG_TRAP = 0xFFFFFFFFFFFFFFE1
MACH_REPLY_PORT_TRAP = 0xFFFFFFFFFFFFFFE6

KERNELRPC_MACH_VM_MAP_TRAP = 0xFFFFFFFFFFFFFFF1

# CTL Types

CTL_UNSPEC = 0
CTL_KERN = 1
CTL_VM = 2
CTL_VFS = 3
CTL_NET = 4
CTL_DEBUG = 5
CTL_HW = 6
CTL_MACHDEP = 7
CTL_USER = 8
CTL_MAXID = 9

# CTL_KERN identifiers

KERN_PROC = 14
