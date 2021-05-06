#!/usr/bin/env python
import sys
import time
import dbus
import dbus.service
import dbus.mainloop.glib
from qtpy.QtWidgets import QApplication

class LyricsAdapter(dbus.service.Object):
    def __init__(self, name, session):
        dbus.service.Object.__init__(self, name, session)

    @dbus.service.method(
        "local.musicbox.Lyrics", in_signature="s", out_signature=""
    )
    def refresh_lyrics(self, text):
        print("  " + text, flush=True)

    @dbus.service.method("local.musicbox.Lyrics", in_signature="", out_signature="")
    def exit(self):
        print("", flush=True)
        # QApplication.quit()
        # sys.exit(0)

def exit(self):
    QApplication.quit()
    sys.exit(0)

def main():
    app = QApplication(sys.argv)
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    session_bus = dbus.SessionBus()
    name = dbus.service.BusName("org.musicbox.Bus", session_bus)
    lyrics = LyricsAdapter(session_bus, "/")
    app.exec_()

if __name__ == "__main__":
    main()
