import wx
from cStringIO import StringIO


class MEraseBackground(object):
	"""
	Requires __init__ call
	"""
	def __init__(self, bg_bmp=None):
		self.__bg_bmp = bg_bmp or self.__getDefaultBackgroundBitmap()
		self.GetClientWindow().Bind(wx.EVT_ERASE_BACKGROUND, self.__onEraseBackground)

	def __getDefaultBackgroundBitmap(self):
		return wx.BitmapFromImage(wx.ImageFromStream(StringIO('''\
\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00T\x00\x00\x00T\x08\x06\x00\
\x00\x00\x1ck\x10\xc1\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\
\x01\x7fIDATx\x9c\xed\xdc[j\x821\x14\x00\xe1\xa3\x06/\xad\x82\x9bw\x0b\xbeuo\
\x85\xdajE\xd1\r\x84_\x88\x93\x90\xc0|\x8f\rX\x19\x08\x1c\x92\xb4\xb3\xc3\
\xf1\xeb\x11\xc2\xa4\x88\x88\xfdn\x9b]\xfc\xfe9\xc5\xe7f\x9d]\xfb=_&\xd7\xd6\
\xabev\xed\xf2\x7f-\xfe\xcc\x11\xd6\xe6\xd9\x9f\xaa\x98Aa\x06\x85\x19\x14fP\
\xd8\xcc\xb1\x89\x95""\xd2b\x91]\xbc\xdd\xef]\x8dF\xa5\xdfsj\x8d\x1e\x19\xdd\
\xf20\x83\xc2\x0c\n3(\xcc\xa00\xc7&X\x8a\x88*#N\x8d\x13\xac\xd2\xb5\xed\xc7&\
\xbbv\xfa;\xe3\x9f\xe9\x96\x87\x19\x14fP\x98Aa\x06\x8596\xc1\xaa\x8dM\xa3\
\xac\xd1\'Xny\x98Aa\x06\x85\x19\x14fP\x98c\x13\xac\xda\xd8T\xe3Bm\x84\xf7Rny\
\x98Aa\x06\x85\x19\x14fP\x98c\x13,ED\x95K\xacQ.\xfe|\xdb\xd49\x83\xc2\x0c\n3\
(\xcc\xa00\xc7&Xw\x97t#\x9c(M}O\xb7<\xcc\xa00\x83\xc2\x0c\n3(\xcc\xb1\t\xf6r\
l\xea\xe9iwO\x17\x86\x9e65bP\x98Aa\x06\x85\x19\x14\xe6\xd8\x04\x1b\xeamS\xeb\
\xbf\xa4+\x19\x19\xdd\xf20\x83\xc2\x0c\n3(\xcc\xa00\xc7&\xd8P\xff\xb7i\x841\
\xcd-\x0f3(\xcc\xa00\x83\xc2\x0c\nsl\x82\xbdu\xda\xd4\xf2\x14\xa7\xb7\x8b?\
\xc7\xa6F\x0c\n3(\xcc\xa00\x83\xc2\x1c\x9b`\xdd\xbdmj}\x82E\xff>\xb7<\xcc\
\xa00\x83\xc2\x0c\n3(\xec\tAm\xb0\xe4\x1d\x8a\xad\xb5\x00\x00\x00\x00IEND\
\xaeB`\x82'''
		)))

	def __onEraseBackground(self, evt):
		dc = evt.GetDC()

		if not dc:
			dc = wx.ClientDC(self.GetClientWindow())

		# tile the background bitmap
		sz = self.GetClientSize()
		w = self.__bg_bmp.GetWidth()
		h = self.__bg_bmp.GetHeight()
		x = 0
		
		while x < sz.width:
			y = 0

			while y < sz.height:
				dc.DrawBitmap(self.__bg_bmp, x, y)
				y = y + h

			x = x + w
