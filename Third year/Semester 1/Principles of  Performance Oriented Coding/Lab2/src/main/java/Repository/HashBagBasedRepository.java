package Repository;

import org.eclipse.collections.impl.bag.mutable.HashBag;

public class HashBagBasedRepository<T> implements InMemoryRepository<T> {
    private HashBag<T> bag;
    
    public HashBagBasedRepository () {
        this.bag = new HashBag<>();
    }

    @Override
    public void add(T elem) {
        bag.add(elem);
    }

    @Override
    public boolean contains(T elem) {
        return bag.contains(elem);
    }

    @Override
    public void remove(T elem) {
        bag.remove(elem);
    }
}