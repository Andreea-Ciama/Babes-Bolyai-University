#pragma once

typedef int TElem;

class DynamicVector
{
private:
	TElem* elems;
	int length;
	int capacity;

public:
	// default constructor for a DynamicVector
	DynamicVector(int capacity = 10);

	// copy constructor for a DynamicVector
	DynamicVector(const DynamicVector& v);

	// destructor
	~DynamicVector();

	// adds an element to the current DynamicVector
	void addElem(const TElem& e);

	// returns the number of elements from the DynamicVector
	int getLength() const;

	// returns all elements from the DynamicVector
	TElem* getAllElems() const;

	// deletes an element from the current DynamicVector
	void deleteElem(int pos);

private:
	// resizes the current DynamicVector, multiplying its capacity by a given factor (real number)
	void resize(double factor = 2);
};