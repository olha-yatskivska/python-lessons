# Logic Flow: Compute Pay Function

```mermaid
graph TD
    Start([Start Function]) --> Input[/Parameters: hours, rate/]
    Input --> Condition{hours <= 40?}
    
    Condition -- Yes (Normal) --> Regular[pay = hours * rate]
    Condition -- No (Overtime) --> Overtime[pay = 40 * rate + overtime_hours * rate * 1.5]
    
    Regular --> Return[return pay]
    Overtime --> Return
    Return --> End([End / Result])
```

## Test Scenarios 3BVA:

* **Scenario 1 (Boundary):** Exactly 40 hours

* **Scenario 2 (Normal):** Less than 40 hours

* **Scenario 3 (Overtime):** More than 40 hours

