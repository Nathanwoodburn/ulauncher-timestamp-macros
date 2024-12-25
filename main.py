import json
import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
import datetime

logger = logging.getLogger(__name__)


class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        logger.info('preferences %s' % json.dumps(extension.preferences))
        # data = event.get_data()
        # print("my event", event.get_keyword())
        # print('{0:%Y-%m-%d}'.format(datetime.datetime.now()))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                        name='Unix Timestamp',
                                         description='Enter to copy to the clipboard',
                                         on_enter=CopyToClipboardAction('{0:%s}'.format(datetime.datetime.now()))))
        
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='Unix Timestamp (milliseconds)',
                                         description='Enter to copy to the clipboard',
                                         on_enter=CopyToClipboardAction('{0:%s}'.format(datetime.datetime.now()))))


        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='YYYY-MM-DD',
                                         description='Enter to copy to the clipboard',
                                         on_enter=CopyToClipboardAction('{0:%Y-%m-%d}'.format(datetime.datetime.now()))))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='HH:mm',
                                         description='Enter to copy to the clipboard',
                                         on_enter=CopyToClipboardAction(
                                             '{0:%H:%M}'.format(datetime.datetime.now()))))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='YYYY-MM-DD HH:mm',
                                         description='Enter to copy to the clipboard',
                                         on_enter=CopyToClipboardAction(
                                             '{0:%Y-%m-%d %H:%M}'.format(datetime.datetime.now()))))        
        
        return RenderResultListAction(items)


if __name__ == '__main__':
    DemoExtension().run()
