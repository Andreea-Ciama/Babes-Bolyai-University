#include "DynamicVector.h"


DynamicVector::DynamicVector(int capacity)
{
	this->length = 0;
	this->capacity = capacity;
	this->elems = new TElem[capacity];
}

DynamicVector::DynamicVector(const DynamicVector& v)
{
	this->length = v.length;
	this->capacity = v.capacity;
	this->elems = new TElem[this->capacity];

	for (int i = 0; i < this->length; i++)
		this->elems[i] = v.elems[i];
}

DynamicVector::~DynamicVector()
{
	delete[] this->elems;
}

void DynamicVector::addElem(const TElem& elem)
{
	if (this->length == this->capacity)
		this->resize();
	this->elems[this->length] = elem;
	this->length++;
}

int DynamicVector::getLength() const
{
	return this->length;
}

TElem* DynamicVector::getAllElems() const
{
	return this->elems;
}

void DynamicVector::resize(double factor)
{
	this->capacity *= 2;
	TElem* aux = new TElem[this->capacity];

	for (int i = 0; i < this->length; i++)
		aux[i] = this->elems[i];

	delete[] this->elems;
	this->elems = aux;
}

void DynamicVector::deleteElem(int pos)
{
	for (int i = pos; i < this->length - 1; i++)
		this->elems[i] = this->elems[i + 1];
	this->length--;
}