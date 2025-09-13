# graphs_kgamble

Tiny graphs library packaged for class. Includes Dijkstra's shortest path.

## Install (from GitHub)

```bash
pip install git+https://github.com/KogaBlu/graphs_kogablu.git
```

```bash
python test.py sample_graph.txt
```

## Usage

```python
from graphs_kgamble import sp
dist, path = sp.dijkstra({0:{1:4,7:8},1:{2:8},7:{6:1}}, 0)
```

## Project layout

```text
src/
  graphs_kgamble/
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
