#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>

using namespace std;

// tetha(INITIAL_SIZE)
MultiMap::MultiMap() {
	this->capacity = INITIAL_SIZE;
	this->actualSize = 0;

	//allocate space for the array
	this->elements = new TElem[this->capacity];

	//initialize array with NULL_TELEM
	for(int i = 0; i < this->capacity; i++)
	    this->elements[i] = NULL_TELEM;
}

// best case: tetha(1)
// worst case:  Tetha(n)
// average complexity: O(n)
void MultiMap::add(TKey c, TValue v) {
    // if the load factor reaches a given value, we resize and rehash
    if(this->loadFactor() >= LOAD_FACTOR)
        this->resize();
    int i, position;
    // with i we will generate positions for the element (i - probe number)
	i = 0;
	position = this->hashingFunction(c, i);
	// we find first available position
    // our hashing function returns a permutation of the indexes of the array, so it is sure it'll find an empty position.
	while(i < this->capacity && this->elements[position] > NULL_TELEM) {
        i++;
        position = this->hashingFunction(c, i);
    }
	this->elements[position] = TElem(c,v);
	this->actualSize++;
	}

// best case: tetha(1)
//  worst case: tetha(capacity)
//  average: O(capacity)
bool MultiMap::remove(TKey c, TValue v) {
	int i, position;
	i = 0;
    position = this->hashingFunction(c, i);
    // we hash the key until we find a NULL_TELEM. If we find it, means that the hasing didn't get that far, so
    // we don't need to check further.
    while(i < this->capacity && this->elements[position] != NULL_TELEM) {
        if(this->elements[position] == TElem(c, v))
        {
            // mark the element as deleted
            this->elements[position] = DELETED_TELEM;
            this->actualSize--;
            return true;
        }
        i++;
        position = this->hashingFunction(c, i);
    }
	return  false;
}

// best case: tetha(1)
// worst case: tetha(capacity)
// average: O(capacity)
vector<TValue> MultiMap::search(TKey c) const {
	vector<TValue> elementsMatchingKey {};
    int i, position;
    i = 0;
    position = this->hashingFunction(c, i);
    // if we get to NULL_TELEM, means hashing didn't get that far, so we don't have to look further
    while(i < this->capacity && this->elements[position] != NULL_TELEM) {
	    if(this->elements[position].first == c)
	        elementsMatchingKey.push_back(this->elements[position].second);
	    i++;
        position = this->hashingFunction(c, i);
    }
	return elementsMatchingKey;
}

// tetha(1)
int MultiMap::size() const {
    return this->actualSize;
}


// tetha(1)
bool MultiMap::isEmpty() const {
    return this->actualSize == 0;
}

//  O(capacity)
MultiMapIterator MultiMap::iterator() {
	return MultiMapIterator(*this);
}


// tetha(1)
MultiMap::~MultiMap() {
	delete [] this->elements;
}

// tetha(1)
int MultiMap::firstHash(TKey key) const{
    return abs(key) % this->capacity;
}

//  tetha(1)
int MultiMap::secondHash(TKey key) const{
    return 1 + (abs(key) % (this->capacity -1));
}

// tetha(1)
int MultiMap::hashingFunction(TKey key, int i) const{
    long long result = ((long long) this->firstHash(key) + (long long) i * (long long)this->secondHash(key)) % (long long) this->capacity;
    return (int) result;
}

// resizes the hash table to one of at least double the size, whose capacity is a prime number
// O(newCapacity + oldCapacity * addComplexity)

void MultiMap::resize() {

    int newCapacity = this->nextPrime(this->capacity * 2 + 1);
    // save the old array
    TElem* oldArray = this->elements;
    // create a new array
    this->elements = new TElem[newCapacity];

    // set null telem on every position in the new array
    for(int i=0; i< newCapacity; i++)
        this->elements[i] = NULL_TELEM;

    int oldCapacity = this->capacity;
    this->capacity = newCapacity;
    // set the old size to 0, because we will rehash
    this->actualSize = 0;
    // add back the old elements
    for(int i=0; i< oldCapacity; i++)
        if(oldArray[i] > NULL_TELEM)
            this->add(oldArray[i].first, oldArray[i].second);
    delete [] oldArray;
}


//Tetha(1)
//O(sqrt(n)/2) -> O(n)
bool MultiMap::isPrime(int number) {
    if(number <= 1)
        return false;
    if(number == 2)
        return true;
    if(number % 2 == 0)
        return false;
    for(int divisor = 3; divisor * divisor <= number; divisor+= 2)
        if(number % divisor == 0)
            return false;
    return true;
}


//  O(gap * number)
// we can aproximate the complexity to O(number) since the gap is relatively small
int MultiMap::nextPrime(int number) {
    if(number % 2 == 0)
        number++;
    while(!this->isPrime(number))
        number+=2;
    return number;
}

// computes the load factor of the hash table:
// complexity: tetha(1)
double MultiMap::loadFactor() {
    return (double) this->actualSize / (double) this->capacity;
}


// best case: tetha(1)
// worst case: tetha(capacity)
// average: O(capacity)
vector<TKey> MultiMap::keySet(TKey c) const {
    vector<TValue> elementsKey {};
    int i, position;
    i = 0;
    position = this->hashingFunction(c, i);
    // if we get to NULL_TELEM, means hashing didn't get that far, so we don't have to look further
    while(i < this->capacity && this->elements[position] != NULL_TELEM) {

            elementsKey.push_back(this->elements[position].first);
        i++;
        position = this->hashingFunction(c, i);
    }

    return elementsKey;
}

