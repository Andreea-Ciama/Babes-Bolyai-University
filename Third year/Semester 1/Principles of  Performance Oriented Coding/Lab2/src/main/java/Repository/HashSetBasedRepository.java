package Repository;

import java.util.HashSet;

public class HashSetBasedRepository<T> implements InMemoryRepository<T> {
    private HashSet<T> set;
    
    public HashSetBasedRepository () {
        this.set = new HashSet<>();
    }

    @Override
    public void add(T elem) {
        set.add(elem);
    }

    @Override
    public boolean contains(T elem) {
        return set.contains(elem);
    }

    @Override
    public void remove(T elem) {
        set.remove(elem);
    }
}