pkgname = "xfce4-dict"
pkgver = "0.8.8"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce dictionary search app"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-dict/start"
source = (
    f"$(XFCE_SITE)/apps/xfce4-dict/{pkgver[:-2]}/xfce4-dict-{pkgver}.tar.bz2"
)
sha256 = "0d0cb079d276d82c174a52c94ee4df12df490a525befc44650e261f8e5eae916"
