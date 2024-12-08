with open("input.txt", "r") as file:
    content = file.read().split("\n\n")
    rule_list = content[0].split("\n")
    updates = content[1].split("\n")

    rules = {}

    for rule in rule_list:
        rule = rule.split("|")
        key = rule[0]
        value = rule[1]
        if key in rules:
            rules[key].append(value)
        else:
            rules[key] = [value]

    valid_updates = []
        
    for update in updates:
        nbrs = update.split(",")
        
        valid = True
        for i in range(len(nbrs)):
            if not valid:
                break
            for j in range(0, i):
                if nbrs[i] not in rules:
                    continue
                if nbrs[j] in rules[nbrs[i]]:
                    valid = False
                    break
        
        if valid:
            valid_updates.append(nbrs)
    
    tot = 0

    for update in valid_updates:
        if len(update) < 3:
            continue
        tot += int(update[int(len(update) / 2)])

    print(tot)
