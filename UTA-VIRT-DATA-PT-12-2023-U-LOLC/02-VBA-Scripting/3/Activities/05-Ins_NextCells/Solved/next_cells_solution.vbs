Sub challenge_2()


dim table_row as Integer
dim ticker_name as String
dim yearly_change as Double 
dim percent_change as Double
dim total_vol as Double
total_vol = 0

table_row = 2
last_row = Cells(Rows.Count, 1).End(xlUp).Row

For i = 2 to last_row
  If Cells(i + 1, column).Value <> Cells(i, column).Value Then
    ticker_name = Cells(i, 1).value






End Sub