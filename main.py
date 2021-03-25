from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.utils import platform

KV = '''
BoxLayout:
    id: box
    orientation: "vertical"
    spacing: 15
    
    MDToolbar:
        title: "Kivy Service Demo"
    
    MDRaisedButton:
		id: mybutton
		pos_hint: {"center_x": 0.5, "center_y": 0.5}
        text: "Send Push Notification"
        on_press: app.button_pressed()
        
    MDLabel:
        id: mylabel
        halign: "center"
        text: ""
'''

class Main(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        if platform == 'android':
            from jnius import autoclass
            service = autoclass('org.test.myapp.ServiceMyservice')
            mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            argument = ''
            service.start(mActivity, argument)
            label = self.root.ids.mylabel
            label.text += "\nservice started"

    def button_pressed(self):
        import plyer
        plyer.notification.notify(title='Button pressed', message="Notification using plyer")
        label = self.root.ids.mylabel
        label.text += "\npush notification sent"


Main().run()
