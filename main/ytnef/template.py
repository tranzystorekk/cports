pkgname = "ytnef"
pkgver = "2.1.2"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Yerase's TNEF Stream Reader"
license = "GPL-2.0-or-later"
url = "https://github.com/Yeraze/ytnef"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "340f03f495884611209e9c0bc943fad06ce920e8c79655aa228d5ca7418dc360"


@subpackage("ytnef-devel")
def _(self):
    return self.default_devel()


@subpackage("ytnef-progs")
def _(self):
    self.depends += ["perl-mailtools", "perl-mime-tools"]

    return self.default_progs()
