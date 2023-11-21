class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()

        for email in emails:
            split = email.index("@")
            local = email[:split]
            domain = email[split:]
    
            local = local.replace(".", "")
            if "+" in local:
                index = local.index("+")
                local = local[:index]

            valid_email = local + domain
            s.add(valid_email)
        
        return len(s)
