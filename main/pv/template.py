pkgname = "pv"
pkgver = "1.9.31"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "gettext-devel"]
pkgdesc = "Tool for monitoring the progress of data through a pipeline"
license = "GPL-3.0-or-later"
url = "https://www.ivarch.com/programs/pv.shtml"
source = f"https://www.ivarch.com/programs/sources/pv-{pkgver}.tar.gz"
sha256 = "a35e92ec4ac0e8f380e8e840088167ae01014bfa008a3a9d6506b848079daedf"


def post_extract(self):
    self.rm("po/Makefile.in.in")
