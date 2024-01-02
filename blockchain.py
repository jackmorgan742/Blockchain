class Transaction():
    
    def __init__(self, from_user, to_user, amount):
        '''
        Initializes single transaction of HuskyCoin (sending user, receiving user, and amount being sent or received)
        '''
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount


    def __repr__(self):
        '''
        Returns string representation of transaction (from, to, amount)
        '''
        return f'{self.from_user}, {self.to_user}, {self.amount}'
    



class Block():

    def __init__(self, transactions=None):
        '''
        Initializes Block class by providing a collection of transaction objects
        '''
        self.transactions = transactions if transactions is not None else []
        self.previous_block_hash = None


    def add_transaction(self, transaction):
        '''
        Adds single transaction to the block
        '''
        self.transactions.append(transaction)


    def __hash__(self):
        '''
        Returns hash of the previous block in the chain
        '''
        return hash((tuple(self.transactions), self.previous_block_hash))
    

    def __eq__(self, other):
        '''
        Returns which transactions match up with the correct one in the chain
        '''
        return isinstance(other, Block) and (self.transactions == other.transactions) and (self.previous_block_hash == other.previous_block_hash)
    

    def __repr__(self):
        '''
        String representation of the transactions
        '''
        return str(self.transactions)




class Ledger():

    def __init__(self):
        '''
        Initializes hashmap for the Ledger class
        '''
        self._hashmap = {}
    

    def has_funds(self, user, amount):
         '''
         Checks if the sending user has sufficient HuskyCoin funds when trying to transfer HuskyCoin
         '''
         if user not in self._hashmap:
             return False
         balance = self._hashmap.get(user)
         return balance >= amount
    

    def add_user(self, user):
        '''
        Adds a user to the hashmap
        '''
        self._hashmap[user] = 0


    def deposit(self, user, amount):
        '''
        Adds an amount of HuskyCoin to the given user
        '''
        if user in self._hashmap:
            self._hashmap[user] += amount
        else:
            self._hashmap[user] = amount


    def transfer(self, from_user, to_user, amount):
        '''
        Subtracts an amount of HuskyCoin from the given user
        '''
        if not self.has_funds(from_user, amount):
            return False
        self._hashmap[from_user] -= amount
        self.deposit(to_user, amount)
        return True
    

    def __repr__(self):
        '''
        String representation of the ledger
        '''
        return str(self._hashmap)




class Blockchain():
    '''Contains the chain of blocks.'''

    #########################
    # Do not use these three values in any code that you write. 
    _ROOT_BC_USER = "ROOT"            # Name of root user account.  
    _BLOCK_REWARD = 1000              # Amoung of HuskyCoin given as a reward for mining a block
    _TOTAL_AVAILABLE_TOKENS = 999999  # Total balance of HuskyCoin that the ROOT user receives in block0
    #########################


    def __init__(self):
        '''
        Initializes Blockchain class by providing a list of block objects
        '''
        self._blockchain = list()     # Use the Python List for the chain of blocks
        self._bc_ledger = Ledger()    # The ledger of HuskyCoin balances
        # Create the initial block0 of the blockchain, also called the "genesis block"
        self._create_genesis_block()


    # This method is complete. No additional code needed.
    def _create_genesis_block(self):
        '''Creates the initial block in the chain.
        This is NOT how a blockchain usually works, but it is a simple way to give the
        Root user HuskyCoin that can be subsequently given to other users'''
        trans0 = Transaction(self._ROOT_BC_USER, self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)
        block0 = Block([trans0])
        self._blockchain.append(block0)
        self._bc_ledger.deposit(self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)


    # This method is complete. No additional code needed.
    def distribute_mining_reward(self, user):
        '''
        You need to give HuskyCoin to some of your users before you can transfer HuskyCoing
        between users. Use this method to give your users an initial balance of HuskyCoin.
        (In the Bitcoin network, users compete to solve a meaningless mathmatical puzzle.
        Solving the puzzle takes a tremendious amount of copmputing power and consuming a lot
        of energy. The first node to solve the puzzle is given a certain amount of Bitcoin.)
        In this assigment, you do not need to understand "mining." Just use this method to 
        provide initial balances to one or more users.'''
        trans = Transaction(self._ROOT_BC_USER, user, self._BLOCK_REWARD)
        block = Block([trans])
        self.add_block(block)


    def add_block(self, block):
        '''
        Return True/False value indicating whether the block was successfully added to 
        the chain, stores hash of previous block in block being added, returns false if 
        transaction is invalid, updates ledger of balances
        '''
        block.previous_block_hash = hash(self._blockchain[-1])
        for i in block.transactions:
            if not self._bc_ledger.has_funds(Transaction.from_user, Transaction.amount):
                return False
        for i in block.transactions:
            self._bc_ledger.transfer(Transaction.from_user, Transaction.to_user, Transaction.amount)
        self._blockchain.append(block)
        return True


    def validate_chain(self):
        '''
        Return a list of blocks that have been "tampered" with
        '''
        blocks_tampered = []
        for i in range(1, len(self._blockchain)):
            if hash(self._blockchain[i - 1]) != self._blockchain[i].previous_block_hash:
                blocks_tampered.append(self._blockchain[i])
        return blocks_tampered


    def __repr__(self):
        '''
        Returns string representation of blockchain
        '''
        return str(self._blockchain)
