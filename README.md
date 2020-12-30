We have builed a python project which is used to store key-values and to store data in some location in laptop.Which supports create,read,modify and delete operations.Which also supports Time-To-Live property.
Where in create operation  we can add new key-value.The key isalways string(32char).
Where in read operation key can performed by providing the key and receiving the value in response.
Where in modify opertaion we can modify key-value.
Where in delete operation the key which have told to delete will be delete.
In Time-To-Live property,it will be evaluated as an integer defining the number of seconds the key must be retained in data store.Once it is expired the key will no longer be available.
The error will be returned if the data exceeded.
The size of file to store is 1GB it willl never exceed 1GB.
