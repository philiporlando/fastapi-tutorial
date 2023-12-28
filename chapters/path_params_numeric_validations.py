from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *,  # special syntax to allow required params without default values to follow optional params (size is after q)
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
    q: Annotated[str | None, Query(alias="item-query")] = None,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id, "size": size}
    if q:
        results.update({"q": q})
    return results
