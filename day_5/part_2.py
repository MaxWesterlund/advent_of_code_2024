with open("test_input.txt", "r") as file:
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

    unvalid_updates = []
        
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
        
        if not valid:
            unvalid_updates.append(nbrs)
    
    fixed_updates = []

    for update in unvalid_updates:
        new_update = []
        for i in range(len(update)):
            if update[i] not in rules:
                new_update.append(update[i])
                continue
            index = -1
            for j in reversed(range(0, len(new_update))):
                if new_update[j] in rules[update[i]]:
                    index = j
            if index == -1:
                new_update.append(update[i])
            else:
                new_update.insert(index, update[i])
        fixed_updates.append(new_update)

    tot = 0

    for update in fixed_updates:
        if len(update) < 3:
            continue
        tot += int(update[int(len(update) / 2)])

    print(tot)