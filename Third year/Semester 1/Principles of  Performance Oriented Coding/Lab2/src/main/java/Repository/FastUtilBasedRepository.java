package Repository;

import it.unimi.dsi.fastutil.doubles.Double2DoubleMap;
import it.unimi.dsi.fastutil.doubles.Double2DoubleOpenHashMap;

public class FastUtilBasedRepository {
    private Double2DoubleMap map;

    public FastUtilBasedRepository() {
        this.map = new Double2DoubleOpenHashMap();
    }

    public void add(double d1, double d2) {
        map.put(d1, d2);
    }

    public boolean contains(double value) {
        return map.containsValue(value);
    }

    public void remove(double key) {
        map.remove(key);
    }
}