'''
Created on 2018
@author: HSong
'''
from labs.common import ConfigConst, ConfigUtil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SmtpClientConnector(object):
    '''
    classdocs
    '''
    config = ConfigUtil.ConfigUtil('../../../data/ConnectedDevicesConfig.props')

    def __init__(self):
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))

# Reading Config from the file and push message.        
    def publishMessage(self, topic, data):
        host = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.HOST_KEY)
        port = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.PORT_KEY)
        fromAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.FROM_ADDRESS_KEY)
        toAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.TO_ADDRESS_KEY)
        authToken = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.USER_AUTH_TOKEN_KEY)
        msg = MIMEMultipart('related')
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic
        msgBody = str(data)
        msg.attach(MIMEText(msgBody))
        msgText = msg.as_string()
        
# Methods of e-mail publication
        smtpServer = smtplib.SMTP_SSL(host,port)
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken)
        smtpServer.sendmail(fromAddr, toAddr, msgText)
        smtpServer.close()
