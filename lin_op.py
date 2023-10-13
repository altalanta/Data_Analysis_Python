import pulp

# Create a Linear Programming problem
lp_problem = pulp.LpProblem("My_LP_Problem", pulp.LpMaximize)

# Define decision variables
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

# Define the objective function
# Maximize: 3x1 + 2x2
lp_problem += 3 * x1 + 2 * x2, "Objective"

# Define constraints
# 2x1 + x2 <= 10
lp_problem += 2 * x1 + x2 <= 10, "Constraint 1"
# x1 + 3x2 <= 12
lp_problem += x1 + 3 * x2 <= 12, "Constraint 2"

# Solve the linear optimization problem
lp_problem.solve()

# Check the status of the solution
if pulp.LpStatus[lp_problem.status] == "Optimal":
    print("Optimal Solution Found!")
    # Print the optimal values of the decision variables
    print(f"x1 = {x1.varValue}")
    print(f"x2 = {x2.varValue}")
    # Print the optimal objective value
    print(f"Optimal Objective Value = {pulp.value(lp_problem.objective)}")
else:
    print("No Optimal Solution Found!")

# The status can be other than "Optimal," such as "Infeasible" or "Unbounded," depending on the problem.
