class HashMap:

    def __init__(self, size):
        '''
        Creates empty bucket list of given size
        '''
        self.size = size
        self.hash_table = self.create_buckets()
 

    def create_buckets(self):
        '''
        Returns list of buckets
        '''
        return [[] for _ in range(self.size)]
 

    def set_val(self, key, val):
        '''
        Inserts values into hash map
        '''
       
        hashed_key = hash(key) % self.size
         
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            if record_key == key:
                found_key = True
                break
 
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
 

    def get_val(self, key):
        '''
        Return searched value with specific key
        '''
        
        hashed_key = hash(key) % self.size
         
        
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            if record_key == key:
                found_key = True
                break
 
        if found_key:
            return record_val
        else:
            return "No record found"
        
        
    def delete_val(self, key):
        '''
        Remove a value with specific key
        '''

        hashed_key = hash(key) % self.size
         
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
 