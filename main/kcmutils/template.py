pkgname = "kcmutils"
pkgver = "6.6.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kxmlgui-devel",
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Utilities for KDE System Settings modules"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcmutils/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcmutils-{pkgver}.tar.xz"
sha256 = "8f1b9f26ce7b055cec46a9521eab75f910ae9c395aada88d6d82cf395459b270"
hardening = ["vis"]


@subpackage("kcmutils-devel")
def _(self):
    self.depends += [
        "kconfigwidgets-devel",
        "kcoreaddons-devel",
        "qt6-qtdeclarative-devel",
    ]

    return self.default_devel()