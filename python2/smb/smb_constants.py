
# Values for Command field in SMB message header
SMB_COM_CREATE_DIRECTORY = 0x00
SMB_COM_DELETE_DIRECTORY = 0x01
SMB_COM_CLOSE = 0x04
SMB_COM_DELETE = 0x06
SMB_COM_RENAME = 0x07
SMB_COM_TRANSACTION = 0x25
SMB_COM_ECHO = 0x2B
SMB_COM_OPEN_ANDX = 0x2D
SMB_COM_READ_ANDX = 0x2E
SMB_COM_WRITE_ANDX = 0x2F
SMB_COM_TRANSACTION2 = 0x32
SMB_COM_NEGOTIATE = 0x72
SMB_COM_SESSION_SETUP_ANDX = 0x73
SMB_COM_TREE_CONNECT_ANDX = 0x75
SMB_COM_NT_TRANSACT = 0xA0
SMB_COM_NT_CREATE_ANDX = 0xA2

SMB_COMMAND_NAMES = {
    0x00: 'SMB_COM_CREATE_DIRECTORY',
    0x01: 'SMB_COM_DELETE_DIRECTORY',
    0x04: 'SMB_COM_CLOSE',
    0x06: 'SMB_COM_DELETE',
    0x25: 'SMB_COM_TRANSACTION',
    0x2B: 'SMB_COM_ECHO',
    0x2D: 'SMB_COM_OPEN_ANDX',
    0x2E: 'SMB_COM_READ_ANDX',
    0x2F: 'SMB_COM_WRITE_ANDX',
    0x32: 'SMB_COM_TRANSACTION2',
    0x72: 'SMB_COM_NEGOTIATE',
    0x73: 'SMB_COM_SESSION_SETUP_ANDX',
    0x75: 'SMB_COM_TREE_CONNECT_ANDX',
    0xA0: 'SMB_COM_NT_TRANSACT',
    0xA2: 'SMB_COM_NT_CREATE_ANDX',
}

# Bitmask for Flags field in SMB message header
SMB_FLAGS_LOCK_AND_READ_OK = 0x01       # LANMAN1.0
SMB_FLAGS_BUF_AVAIL = 0x02              # LANMAN1.0, Obsolete
SMB_FLAGS_CASE_INSENSITIVE = 0x08       # LANMAN1.0, Obsolete
SMB_FLAGS_CANONICALIZED_PATHS = 0x10    # LANMAN1.0, Obsolete
SMB_FLAGS_OPLOCK = 0x20                 # LANMAN1.0, Obsolete
SMB_FLAGS_OPBATCH = 0x40                # LANMAN1.0, Obsolete
SMB_FLAGS_REPLY = 0x80                  # LANMAN1.0

# Bitmask for Flags2 field in SMB message header
SMB_FLAGS2_LONG_NAMES = 0x0001              # LANMAN2.0
SMB_FLAGS2_EAS = 0x0002                     # LANMAN1.2
SMB_FLAGS2_SMB_SECURITY_SIGNATURE = 0x0004  # NT LANMAN
SMB_FLAGS2_IS_LONG_NAME = 0x0040            # NT LANMAN
SMB_FLAGS2_DFS = 0x1000                     # NT LANMAN
SMB_FLAGS2_REPARSE_PATH = 0x0400            #
SMB_FLAGS2_EXTENDED_SECURITY = 0x0800       #
SMB_FLAGS2_PAGING_IO = 0x2000               # NT LANMAN
SMB_FLAGS2_NT_STATUS = 0x4000               # NT LANMAN
SMB_FLAGS2_UNICODE = 0x8000                 # NT LANMAN

# Bitmask for Capabilities field in SMB_COM_SESSION_SETUP_ANDX response
# [MS-SMB]: 2.2.4.5.2.1 (Capabilities field)
CAP_RAW_MODE = 0x01
CAP_MPX_MODE = 0x02
CAP_UNICODE = 0x04
CAP_LARGE_FILES = 0x08
CAP_NT_SMBS = 0x10
CAP_RPC_REMOTE_APIS = 0x20
CAP_STATUS32 = 0x40
CAP_LEVEL_II_OPLOCKS = 0x80
CAP_LOCK_AND_READ = 0x0100
CAP_NT_FIND = 0x0200
CAP_DFS = 0x1000
CAP_INFOLEVEL_PASSTHRU = 0x2000
CAP_LARGE_READX = 0x4000
CAP_LARGE_WRITEX = 0x8000
CAP_LWIO = 0x010000
CAP_UNIX = 0x800000
CAP_COMPRESSED = 0x02000000
CAP_DYNAMIC_REAUTH = 0x20000000
CAP_PERSISTENT_HANDLES = 0x40000000
CAP_EXTENDED_SECURITY = 0x80000000

# Value for Action field in SMB_COM_SESSION_SETUP_ANDX response
SMB_SETUP_GUEST = 0x0001
SMB_SETUP_USE_LANMAN_KEY = 0X0002

# Bitmask for SecurityMode field in SMB_COM_NEGOTIATE response
NEGOTIATE_USER_SECURITY = 0x01
NEGOTIATE_ENCRYPT_PASSWORDS = 0x02
NEGOTIATE_SECURITY_SIGNATURES_ENABLE = 0x04
NEGOTIATE_SECURITY_SIGNATURES_REQUIRE = 0x08

# Available constants for Service field in SMB_COM_TREE_CONNECT_ANDX request
# [MS-CIFS]: 2.2.4.55.1 (Service field)
SERVICE_PRINTER = 'LPT1:'
SERVICE_NAMED_PIPE = 'IPC'
SERVICE_COMM = 'COMM'
SERVICE_ANY = '?????'

# Bitmask for Flags field in SMB_COM_NT_CREATE_ANDX request
# [MS-CIFS]: 2.2.4.64.1
# [MS-SMB]: 2.2.4.9.1
NT_CREATE_REQUEST_OPLOCK = 0x02
NT_CREATE_REQUEST_OPBATCH = 0x04
NT_CREATE_OPEN_TARGET_DIR = 0x08
NT_CREATE_REQUEST_EXTENDED_RESPONSE = 0x10  # Defined in [MS-SMB]: 2.2.4.9.1

# Bitmask for DesiredAccess field in SMB_COM_NT_CREATE_ANDX request
# and SMB2CreateRequest class
# Also used for MaximalAccess field in SMB2TreeConnectResponse class
# [MS-CIFS]: 2.2.4.64.1
# [MS-SMB2]: 2.2.13.1.1
FILE_READ_DATA = 0x01
FILE_WRITE_DATA = 0X02
FILE_APPEND_DATA = 0x04
FILE_READ_EA = 0x08
FILE_WRITE_EA = 0x10
FILE_EXECUTE = 0x20
FILE_READ_ATTRIBUTES = 0x80
FILE_WRITE_ATTRIBUTES = 0x0100
DELETE = 0x010000
READ_CONTROL = 0x020000
WRITE_DAC = 0x040000
WRITE_OWNER = 0x080000
SYNCHRONIZE = 0x100000
ACCESS_SYSTEM_SECURITY = 0x01000000
MAXIMUM_ALLOWED = 0x02000000
GENERIC_ALL = 0x10000000
GENERIC_EXECUTE = 0x20000000
GENERIC_WRITE = 0x40000000
GENERIC_READ = 0x80000000L

# SMB_EXT_FILE_ATTR bitmask ([MS-CIFS]: 2.2.1.2.3)
# Includes extensions defined in [MS-SMB] 2.2.1.2.1
# Bitmask for FileAttributes field in SMB_COM_NT_CREATE_ANDX request ([MS-CIFS]: 2.2.4.64.1)
# Also used for FileAttributes field in SMB2CreateRequest class ([MS-SMB2]: 2.2.13)
ATTR_READONLY = 0x01
ATTR_HIDDEN = 0x02
ATTR_SYSTEM = 0x04
ATTR_DIRECTORY = 0x10
ATTR_ARCHIVE = 0x20
ATTR_NORMAL = 0x80
ATTR_TEMPORARY = 0x0100
ATTR_SPARSE = 0x0200
ATTR_REPARSE_POINT = 0x0400
ATTR_COMPRESSED = 0x0800
ATTR_OFFLINE = 0x1000
ATTR_NOT_CONTENT_INDEXED = 0x2000
ATTR_ENCRYPTED = 0x4000
POSIX_SEMANTICS = 0x01000000
BACKUP_SEMANTICS = 0x02000000
DELETE_ON_CLOSE = 0x04000000
SEQUENTIAL_SCAN = 0x08000000
RANDOM_ACCESS = 0x10000000
NO_BUFFERING = 0x20000000
WRITE_THROUGH = 0x80000000

# Bitmask for ShareAccess field in SMB_COM_NT_CREATE_ANDX request
# and SMB2CreateRequest class
# [MS-CIFS]: 2.2.4.64.1
# [MS-SMB2]: 2.2.13
FILE_SHARE_NONE = 0x00
FILE_SHARE_READ = 0x01
FILE_SHARE_WRITE = 0x02
FILE_SHARE_DELETE = 0x04

# Values for CreateDisposition field in SMB_COM_NT_CREATE_ANDX request
# and SMB2CreateRequest class
# [MS-CIFS]: 2.2.4.64.1
# [MS-SMB2]: 2.2.13
FILE_SUPERSEDE = 0x00
FILE_OPEN = 0x01
FILE_CREATE = 0x02
FILE_OPEN_IF = 0x03
FILE_OVERWRITE = 0x04
FILE_OVERWRITE_IF = 0x05

# Bitmask for CreateOptions field in SMB_COM_NT_CREATE_ANDX request
# and SMB2CreateRequest class
# [MS-CIFS]: 2.2.4.64.1
# [MS-SMB2]: 2.2.13
FILE_DIRECTORY_FILE = 0x01
FILE_WRITE_THROUGH = 0x02
FILE_SEQUENTIAL_ONLY = 0x04
FILE_NO_INTERMEDIATE_BUFFERING = 0x08
FILE_SYNCHRONOUS_IO_ALERT = 0x10
FILE_SYNCHRONOUS_IO_NONALERT = 0x20
FILE_NON_DIRECTORY_FILE = 0x40
FILE_CREATE_TREE_CONNECTION = 0x80
FILE_COMPLETE_IF_OPLOCKED = 0x0100
FILE_NO_EA_KNOWLEDGE = 0x0200
FILE_OPEN_FOR_RECOVERY = 0x0400
FILE_RANDOM_ACCESS = 0x0800
FILE_DELETE_ON_CLOSE = 0x1000
FILE_OPEN_BY_FILE_ID = 0x2000
FILE_OPEN_FOR_BACKUP_INTENT = 0x4000
FILE_NO_COMPRESSION = 0x8000
FILE_RESERVE_OPFILTER = 0x100000
FILE_OPEN_NO_RECALL = 0x400000
FILE_OPEN_FOR_FREE_SPACE_QUERY = 0x800000

# Values for ImpersonationLevel field in SMB_COM_NT_CREATE_ANDX request
# and SMB2CreateRequest class
# For interpretations about these values, refer to [MS-WSO] and [MSDN-IMPERS]
# [MS-CIFS]: 2.2.4.64.1
# [MS-SMB]: 2.2.4.9.1
# [MS-SMB2]: 2.2.13
SEC_ANONYMOUS = 0x00
SEC_IDENTIFY = 0x01
SEC_IMPERSONATE = 0x02
SEC_DELEGATION = 0x03   # Defined in [MS-SMB]: 2.2.4.9.1

# Values for SecurityFlags field in SMB_COM_NT_CREATE_ANDX request
# [MS-CIFS]: 2.2.4.64.1
SMB_SECURITY_CONTEXT_TRACKING = 0x01
SMB_SECURITY_EFFECTIVE_ONLY = 0x02

# Bitmask for Flags field in SMB_COM_TRANSACTION2 request
# [MS-CIFS]: 2.2.4.46.1
DISCONNECT_TID = 0x01
NO_RESPONSE = 0x02

# Bitmask for basic file attributes
# [MS-CIFS]: 2.2.1.2.4
SMB_FILE_ATTRIBUTE_NORMAL = 0x00
SMB_FILE_ATTRIBUTE_READONLY = 0x01
SMB_FILE_ATTRIBUTE_HIDDEN = 0x02
SMB_FILE_ATTRIBUTE_SYSTEM = 0x04
SMB_FILE_ATTRIBUTE_VOLUME = 0x08
SMB_FILE_ATTRIBUTE_DIRECTORY = 0x10
SMB_FILE_ATTRIBUTE_ARCHIVE = 0x20
SMB_SEARCH_ATTRIBUTE_READONLY = 0x0100
SMB_SEARCH_ATTRIBUTE_HIDDEN = 0x0200
SMB_SEARCH_ATTRIBUTE_SYSTEM = 0x0400
SMB_SEARCH_ATTRIBUTE_DIRECTORY = 0x1000
SMB_SEARCH_ATTRIBUTE_ARCHIVE = 0x2000

# Bitmask for OptionalSupport field in SMB_COM_TREE_CONNECT_ANDX response
SMB_TREE_CONNECTX_SUPPORT_SEARCH = 0x0001
SMB_TREE_CONNECTX_SUPPORT_DFS = 0x0002

# Bitmask for security information fields, specified as
# AdditionalInformation in SMB2
# [MS-SMB]: 2.2.7.4
# [MS-SMB2]: 2.2.37
OWNER_SECURITY_INFORMATION = 0x00000001
GROUP_SECURITY_INFORMATION = 0x00000002
DACL_SECURITY_INFORMATION = 0x00000004
SACL_SECURITY_INFORMATION = 0x00000008
LABEL_SECURITY_INFORMATION = 0x00000010
ATTRIBUTE_SECURITY_INFORMATION = 0x00000020
SCOPE_SECURITY_INFORMATION = 0x00000040
BACKUP_SECURITY_INFORMATION = 0x00010000
