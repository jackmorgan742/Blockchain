import unittest
from blockchain import Transaction, Block, Ledger, Blockchain




class TestTransaction(unittest.TestCase):

    def test__init__(self):
        '''
        Tests init functionality of transaction class (also tests repr function since that is responsible for converting the object to a readable string)
        '''
        self.assertEqual(str(Transaction('Dave', 'John', 500)), 'Dave, John, 500')




class TestBlock(unittest.TestCase):

    #no need for __hash__ testing because if the blockchain/block classes work then that auto tests __hash__ functionality

    def test_init(self):
        '''
        Tests init functionality of Block class (also tests repr function that is responsible for converting the object to a readable string)
        '''
        self.assertEqual(str(Block([Transaction('Dave', 'John', 500), Transaction('Phil', 'Bob', 500)])), '[Dave, John, 500, Phil, Bob, 500]')

        #tests if the block initializes at an empty list and None for a prev_hash
        b1 = Block()
        self.assertEqual(b1.transactions, [])
        self.assertEqual(b1.previous_block_hash, None)


    def test_add_transaction(self):
        '''
        tests add_transaction funtionality within the Block class
        '''
        t1 = Transaction('Dave', 'John', 500) 
        b1 = Block()
        b1.add_transaction(t1)
        self.assertEqual(b1.transactions, [t1])


    def test_eq(self):
        '''
        Tests __eq__ magic method functionality within the Block class
        '''
        b1 = Block()
        b2 = Block()
        self.assertTrue(b1 == b2)

        t1 = Transaction('Dave', 'John', 500) 
        t2 = Transaction('Phil', 'Bob', 400) 
        self.assertFalse(Block(t1) == Block(t2))

   


class TestLedger(unittest.TestCase):

    #has_funds was already implemented and confirmed to be working so I do not need to test it

    def test_init(self):
        '''
        Tests init functionality of Ledger class (also tests repr function that is responsible for converting the object to a readable string)
        '''
        l1 = Ledger()
        self.assertEqual(l1._hashmap, {})


    def test_add_user(self):
        '''
        Tests functionality of add_user method 
        '''
        l1 = Ledger()
        l1.add_user('Bob')
        self.assertEqual(l1._hashmap['Bob'], 0)


    def test_deposit(self):
        '''
        Tests functionality of deposit method 
        '''
        l1 = Ledger()
        l1.deposit('Bob', 500)
        self.assertEqual(l1._hashmap['Bob'], 500)


    def test_transfer(self):
        '''
        Tests functionality of transfer method 
        '''
        l1 = Ledger()
        l1.deposit('Bob', 500)
        transfer1 = l1.transfer('Bob', 'Phil', 500)
        self.assertTrue(transfer1)

        l2 = Ledger()
        l2.deposit('Bob', 500)
        transfer2 = l2.transfer('Bob', 'Phil', 1000)
        self.assertFalse(transfer2)




class TestBlockchain(unittest.TestCase):

    #init, create_genesis_block, and distribute_mining_reward were already implemented and confirmed to be working so I do not need to test them

    def test_add_block(self): 
        '''
        Tests functionality of add_block method
        '''
        b1 = Block()
        bc1 = Blockchain()
        i = bc1.add_block(b1)
        self.assertTrue(i)


    def test_validate_chain(self):
        '''
        Tests functionality of validate_chain method 
        '''
        bc1 = Blockchain()
        tampered = bc1.validate_chain()
        self.assertEqual(tampered, [])




if __name__ == '__main__':
    unittest.main()