import ops
import iopc

def MAIN_ENV(args):
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]

    return False

def MAIN_EXTRACT(args):
    pkg_path = args["pkg_path"]

    return True

def MAIN_CONFIGURE(args):
    output_dir = args["output_path"]
    return True

def MAIN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN_INSTALL(args):
    output_dir = args["output_path"]
    iopc.make_initramfs(iopc.getTargetRootfs(), iopc.getBaseRootFile(""))

    return False

def MAIN_CLEAN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN(args):
    print "initramfs_cpio_gz"

