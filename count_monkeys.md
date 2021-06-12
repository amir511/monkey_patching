## Counts the number of monkeys on the tree!
### Successfull response example:
Status code: `200 OK`
```json
{
    "message":  "Found 10 monkeys on the tree!"
}
```
### Unprocessable entity response:
```json
{
    "status_code": 422,
    "detail": "A tree can only handle up to 10 Monkeys!!",
    "headers": null
}
```
