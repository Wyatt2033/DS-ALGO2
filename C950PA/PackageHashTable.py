# Hash table class.
class PackageHashTable:
    def __init__(self, capacity=20):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Inserts items into hash table.
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for item in hash table.
    def search(self, key):

        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]

        else:
            return None

    # Removes item from hash table.
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)
