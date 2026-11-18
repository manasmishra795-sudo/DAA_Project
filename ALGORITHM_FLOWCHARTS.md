# Algorithm flowcharts

## Iterative exponentiation by squaring

```mermaid
flowchart TD
    A([Start]) --> B[Set result = 1, factor = base, power = exponent]
    B --> C{power > 0?}
    C -- No --> D[Return result]
    C -- Yes --> E{power is odd?}
    E -- Yes --> F[result = result * factor]
    E -- No --> G[Skip result multiplication]
    F --> H[factor = factor * factor]
    G --> H
    H --> I[power = floor(power / 2)]
    I --> C
    D --> J([End])
```

## Modular exponentiation

```mermaid
flowchart TD
    A([Start]) --> B[Validate exponent and modulus]
    B --> C[ result = 1 mod n; factor = base mod n ]
    C --> D{power > 0?}
    D -- No --> E[Return result]
    D -- Yes --> F{power is odd?}
    F -- Yes --> G[result = result * factor mod n]
    F -- No --> H[Skip result update]
    G --> I[factor = factor * factor mod n]
    H --> I
    I --> J[power = floor(power / 2)]
    J --> D
    E --> K([End])
```
