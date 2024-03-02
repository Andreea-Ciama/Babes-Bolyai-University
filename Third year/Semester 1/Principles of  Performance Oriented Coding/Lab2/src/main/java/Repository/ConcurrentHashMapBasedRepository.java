package Repository;

import java.util.concurrent.ConcurrentHashMap;

public class ConcurrentHashMapBasedRepository<K, V> {
    private ConcurrentHashMap<K, V> map;
    
    public ConcurrentHashMapBasedRepository () {
        this.map = new ConcurrentHashMap<>();
    }

    public void add(K key, V value) {
        map.put(key, value);
    }

    public boolean contains(V elem) {
        return map.contains(elem);
    }

    public void remove(V elem) {
        map.remove(elem);
    }
}