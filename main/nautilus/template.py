pkgname = "nautilus"
pkgver = "48.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtests=headless"]
hostmakedepends = [
    "cmake",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "gexiv2-devel",
    "glib-devel",
    "gnome-autoar-devel",
    "gnome-desktop-devel",
    "gst-plugins-base-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libcloudproviders-devel",
    "libportal-devel",
    "libxml2-devel",
    "tinysparql-devel",
]
depends = ["desktop-file-utils", "localsearch", "tinysparql"]
checkdepends = ["dbus", "localsearch", "tinysparql", "python-gobject"]
pkgdesc = "GNOME file manager"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Apps/Files"
source = f"$(GNOME_SITE)/nautilus/{pkgver[: pkgver.find('.')]}/nautilus-{pkgver}.tar.xz"
sha256 = "a030f6163f8a68064fae5a9e89e37f19cbb293de2e12a19dd5e210956d0df4b5"
options = ["!cross"]


@subpackage("nautilus-devel")
def _(self):
    return self.default_devel()


@subpackage("nautilus-libs")
def _(self):
    return self.default_libs()
