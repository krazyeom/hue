
from cffi import FFI
import sys

ffi = FFI()
ffi.cdef("""     // some declarations from the man page
    struct passwd {
        char *pw_name;
        ...;
    };
    struct passwd *getpwuid(int uid);
""")
C = ffi.verify("""   // passed to the real C compiler
#include <sys/types.h>
#include <pwd.h>
""", libraries=[],    # or a list of libraries to link with
     force_generic_engine=hasattr(sys, '_force_generic_engine_'))
