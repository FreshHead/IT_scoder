import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window(title='Проверка выделения текста')
window.set_resizable(False)
window.connect('delete-event', Gtk.main_quit)

source_label = Gtk.Label("Текст:")

text_view = Gtk.TextView()
text_view.set_size_request(500, 200)
buffer = text_view.get_buffer()

text = "Word SELECTED must be selected right now."
word_to_select = "SELECTED"

buffer.insert_at_cursor(text)

selection_start = text.find(word_to_select)
selection_end = selection_start + len(word_to_select)

start_iter = buffer.get_iter_at_offset(selection_start)
end_iter = buffer.get_iter_at_offset(selection_end)
buffer.select_range(start_iter, end_iter)

layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
window.add(layout)
layout.pack_start(text_view, False, False, 0)

window.show_all()
Gtk.main()
