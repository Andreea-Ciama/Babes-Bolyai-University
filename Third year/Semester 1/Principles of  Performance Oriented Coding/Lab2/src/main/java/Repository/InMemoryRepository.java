package Repository;

public interface InMemoryRepository<T> {
    public void add(T elem);
    public boolean contains(T elem);
    public void remove(T elem);
}
