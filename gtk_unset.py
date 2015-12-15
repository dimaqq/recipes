my_rc = \
"""
style "my button"
{
  engine "" {}
}
widget "*.my button" style "my button"
"""

b = gtk.Button()
b.set_name("my button")
# and now you can...
b.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("pink"))

# originally posted as http://code.activestate.com/recipes/576840-unset-engine-in-gtkrc-unset-widget-style-in-gtk/
