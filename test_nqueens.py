from nqueens import *

class TestnQueens(unittest.TestCase):
    def setUp(self):
        self.n = 11

    def test_check_row1( self ):
        n = self.n
        board = [ [0]*n for i in range(n) ]
        board[0][0] = 1
        for i in range(n):
            self.assertTrue(check_row( 0, i, board, n ))

    def test_check_row2( self ):
        n = self.n
        board = [ [0]*n for i in range(n) ]
        board[6][5] = 1
        for i in range(n):
            self.assertTrue(check_row( 6, i, board, n ))

    def test_check_col1( self ):
        n = self.n
        board = [ [0]*n for i in range(n) ]
        board[0][0] = 1
        for i in range(n):
            self.assertTrue(check_col( i, 0, board, n ))

    def test_check_col2( self ):
        n = self.n
        board = [ [0]*n for i in range(n) ]
        board[0][n-1] = 1
        for i in range(n):
            self.assertTrue(check_col( i, n-1, board, n ), "0,n")

    def test_check_col3( self ):
        n = self.n
        board = [ [0]*n for i in range(n) ]
        board[7][2] = 1
        for i in range(n):
            self.assertTrue(check_col( i, 2, board, n ))

    def test_mark( self ):
        n = self.n
        board = [ [0]*n for i in range(n) ]
        mark( 5, 4, board )
        self.assertTrue( board[5][4] == 1 , "(5,4)")
        mark( 7, 4, board )
        self.assertTrue( board[7][4] == 1 , "(7,4)")
        mark( 5, 7, board )
        self.assertTrue( board[5][7] == 1 , "(5,7)")
        mark( 1, 2 , board )
        self.assertTrue( board[1][2] == 1 , "(1,2)")

    def test_unmark( self ):
        n = self.n
        board = [ [0]*n for i in range(n) ]
        mark( 5, 4, board )
        mark( 7, 4, board )
        mark( 5, 7, board )
        mark( 1, 2 , board )
        unmark( 5, 4, board )
        unmark( 7, 4, board )
        unmark( 5, 7, board )
        unmark( 1, 2 , board )
        self.assertTrue( board[5][4] == 0 , "(5,4)")
        self.assertTrue( board[7][4] == 0 , "(7,4)")
        self.assertTrue( board[5][7] == 0 , "(5,7)")
        self.assertTrue( board[1][2] == 0 , "(1,2)")

    def test_diag( self ):
        n = self.n
        board = [ [0]*n for i in range(n) ]
        board[0][0] = 1
        self.assertTrue(check_diags( n-1, n-1, board, n))
        board[0][0] = 0

        board[0][n-1] = 1
        self.assertTrue(check_diags( n-1, 0, board, n ))
        board[0][n-1] = 0

        board[1][2] = 1
        self.assertTrue(check_diags( 0, 3, board, n ))
        board[1][2] = 0

if __name__ == "__main__":
    unittest.main()

