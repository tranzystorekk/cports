pkgname = "xkbcomp"
pkgver = "1.4.7"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "bison", "xorg-util-macros"]
makedepends = ["libx11-devel", "libxkbfile-devel"]
pkgdesc = "XKBD keymap compiler"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xkbcomp-{pkgver}.tar.gz"
sha256 = "00cecc490fcbe2f789cf13c408c459673c2c33ab758d802677321cffcda35373"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("xkbcomp-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
