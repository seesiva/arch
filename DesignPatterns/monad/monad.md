# Monad
Monad is a design pattern used in functional decomposition in Functional programming

## Example
Lets take the SCIP example in this case
```
def square(x):
    if x<0:
        return 0
    else:
        return x * x

def sumofsquare(x,y):
    return square(x)+square(y)

```

In this case decomposition would be happening as sumofsquare(x,y)=>sumofsquare(square(x)+square(y)). In this case if the number is negative then value returned would be zero. This would become very complicated if we are doing the checks multiple times. Since the evaluate would be happening based on the notations it would be handled with ease.

## Better References
* https://www.stephanboyer.com/post/9/monads-part-1-a-design-pattern
