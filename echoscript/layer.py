from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):

        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
        print(messageProtocolEntity)
        self.toLower(messageProtocolEntity.forward('553197672138@s.whatsapp.net'))
        self.toLower(messageProtocolEntity.ack(True))
        self.toLower(messageProtocolEntity.ack(True))


    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

    def onTextMessage(self,messageProtocolEntity):
        # just print info
        print("Echoing %s to %s" % (messageProtocolEntity.getBody(), messageProtocolEntity.getFrom(False)))
