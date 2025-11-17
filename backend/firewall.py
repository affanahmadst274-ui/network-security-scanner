def rule_matches(rule, traffic):
    if rule.ip not in ("any", None) and rule.ip != traffic.ip:
        return False
    if rule.port is not None and rule.port != traffic.port:
        return False
    if rule.protocol not in ("any", None) and rule.protocol != traffic.protocol:
        return False
    return True

def apply_rules(rules, traffic):
    for rule in rules:
        if rule_matches(rule, traffic):
            return rule.action  
    return "allow"

