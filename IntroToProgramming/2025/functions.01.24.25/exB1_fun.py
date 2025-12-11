def list_elements(elements):
    element_reg = []
    for x in range(1, elements + 1):
        element_reg.append(input(f"Element({x}): ").strip())

    for x in range(0, elements):
        print(f"{x}) {element_reg[x]}")
