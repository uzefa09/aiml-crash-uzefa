# Day 7 Task 3: Tiny Class with Useful Method

class Intern:
    def __init__(self, name: str, domain: str, project: str):
        self.name = name
        self.domain = domain
        self.project = project

    def summary(self) -> str:
        return f"Intern: {self.name} | Domain: {self.domain} | Project: {self.project}"

intern1 = Intern("Uzefa Shaikh", "AI/ML", "E-Commerce EDA")
print(intern1.summary())