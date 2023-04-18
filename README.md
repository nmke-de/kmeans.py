# kmeans

**kmeans.py** is a python script facilitating the usage of the [k-means Clustering algorithm](https://en.wikipedia.org/wiki/K-means_clustering).

**normvec.py** is a python script with the purpose to facilitate normalizing the vectors used by kmeans.py.

## But why?

I wanted to cluster some data quickly.

## Dependencies

- Python 3
- Numpy

## Usage

```
./kmeans.py [filename]

./normvec.py [input file] [output file]
```

## File Format

Both kmeans.py and normvec.py use a file format like in `example.vec`, which describes matrices with names.

- `#` begins a one-line comment.
- Lines ending on `:` that contain no tabs give the name of the matrix which is describes in the following lines. If the name ends on `*`, then the vectors of the matrix are labelled (referred to as "IndexedMatrix" in the source code, in contrast to "ListMatrix").
- All other non-empty lines describe a vector of a matrix, with the values separated by tabs. If the matrix is a "IndexedMatrix", the first element is the label of the described vector.

kmeans.py requires a ListMatrix "Centroids" and an IndexedMatrix "Vectors" in particular. normvec.py only requires "Vectors".
