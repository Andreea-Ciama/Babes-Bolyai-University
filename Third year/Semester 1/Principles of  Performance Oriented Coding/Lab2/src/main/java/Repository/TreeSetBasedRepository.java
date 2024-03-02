package Repository;

import Repository.InMemoryRepository;

import java.util.TreeSet;

public class TreeSetBasedRepository<T> implements InMemoryRepository<T> {
    private TreeSet<T> set;
    
    public TreeSetBasedRepository () {
        this.set = new TreeSet<>();
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