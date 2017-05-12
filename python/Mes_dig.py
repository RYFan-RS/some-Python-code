import wx
import os
class App(wx.App):
    dlg = ''
    def OnInit(self): 
        global dlg
        dlg = wx.MessageDialog(None,'would you like answer a question?','Exceuse me',wx.YES_NO|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if result == wx.ID_YES:
            print '谢谢你的参与！'
            app2 =App2(False)
            app2.MainLoop()                 
        else :
            print '抱歉打扰了！'
                   
        dlg.Destroy()
        return True
class App2(wx.App):
    def OnInit(self):
        dlg2 = wx.TextEntryDialog(None,'what language do you like?','A question','python')
        if dlg2.ShowModal() == wx.ID_OK:
            print '你最喜欢的编程语言是:',dlg2.GetValue()
        print '文件浏览过滤功能：'
        app3 = App3()
        app3.MainLoop()
        return True   
class App3(wx.App):
    def OnInit(self):
        fileFilter = "Python source(*.py)|*.py|All files(*.*)|*.*"
        dlg3 = wx.FileDialog(None,'choose file',os.getcwd(),'',fileFilter,wx.OPEN)
        dlg3.ShowModal()
        dlg3.Destroy()
        return True
if __name__ == '__main__':
    app = App(False)           
    app.MainLoop()
   