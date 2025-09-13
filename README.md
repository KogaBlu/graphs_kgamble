# graphs_kogablu

Tiny graphs library packaged for class. Includes Dijkstra's shortest path.

## Install (from GitHub)

```bash
pip install git+https://github.com/<your-username>/graphs_kogablu.git
```

## Run the example driver

```bash
python -m graphs_kogablu_demo  # coming soon
```

Or use the provided `test.py`:

```bash
python test.py sample_graph.txt
```

## Usage

```python
from graphs_kogablu import sp
dist, path = sp.dijkstra({0:{1:4,7:8},1:{2:8},7:{6:1}}, 0)
```

## Project layout

```text
src/
  graphs_kogablu/
    __init__.py
    sp.py
    heapq.py
test.py
pyproject.toml
README.md
```

## Notes
- `sp.py` imports the bundled `heapq` with a **relative import** to avoid
  accidentally pulling Python's stdlib `heapq`.
