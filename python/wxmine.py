import wx
########################################################################

class MyFirstFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
        wx.Frame.__init__(self,None,-1,'测试位置',size=(300,300))
        panel = wx.Panel(self,-1)
        #sizer = wx.BoxSizer(wx.VERTICAL)
        #panel.SetSizer(sizer)
        #txt = wx.StaticText(panel,-1,'hello world Fan')
        #sizer.Add(txt,0,wx.TOP|wx.LEFT,100)
        #self.Centre()
        panel.Bind(wx.EVT_MOTION,self.OnMove)
        wx.StaticText(panel,-1,'position is:',pos = (10,12))
        self.posCtrl = wx.TextCtrl(panel,-1,"",pos = (120,10))
    def OnMove(self,event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s,%s"%(pos.x,pos.y))
if __name__ =='__main__':
    
    app = wx.PySimpleApp()
       # frame = MyFirstFrame(None)
    frame = MyFirstFrame()
    #frameid = frame.GetId()
    #print frameid
    frame.Show(True)
    app.MainLoop()
    
    