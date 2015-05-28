import wx
from toolib.wx.TestApp import TestApp
from toolib.wx.grid.Grid  import Grid
from toolib.wx.grid.table.List2dTable import List2dTable

class MyGrid(Grid):
	pass

ROWS = 256 * 16
COLS = 16

def test():

	def oninit(self):
		self.grid = MyGrid(self, -1)
		self.grid.SetTable(List2dTable())
		self.grid.AppendRows(ROWS)
		self.grid.AppendCols(COLS)

		for i in xrange(ROWS * COLS):
			self.grid.GetTable().SetValue(i/COLS, i % COLS, unichr(i))#"0x%02X: %s" % (i, chr(i)))

		for i in xrange(COLS):
			self.grid.SetColSize(i, 20)

	def ondestroy(self):
		pass

	TestApp(oninit, ondestroy).MainLoop()

if __name__ == '__main__':
	test()
