import re

class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password
        self.criteria = {
            "length": self._check_length,
            "uppercase": self._check_uppercase,
            "lowercase": self._check_lowercase,
            "digits": self._check_digits,
            "special": self._check_special_characters
        }
    
    def _check_length(self):
        """Check if password has at least 8 characters."""
        return len(self.password) >= 8

    def _check_uppercase(self):
        """Check if password contains at least one uppercase letter."""
        return bool(re.search(r"[A-Z]", self.password))

    def _check_lowercase(self):
        """Check if password contains at least one lowercase letter."""
        return bool(re.search(r"[a-z]", self.password))

    def _check_digits(self):
        """Check if password contains at least one digit."""
        return bool(re.search(r"\d", self.password))

    def _check_special_characters(self):
        """Check if password contains at least one special character."""
        return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", self.password))

    def evaluate_strength(self):
        """Evaluate password strength based on criteria."""
        score = 0
        feedback = []

        for criterion, check in self.criteria.items():
            if check():
                score += 1
            else:
                feedback.append(f"Missing {criterion}")

        # Determine strength level
        strength_levels = {
            5: "Very Strong",
            4: "Strong",
            3: "Medium",
            2: "Weak",
            1: "Very Weak"
        }
        
        strength = strength_levels.get(score, "Very Weak")
        
        # Provide detailed feedback
        feedback_message = (
            f"Password Strength: {strength} ({score}/5)\n"
            + ("All criteria met!" if score == 5 else "Suggestions:\n" + "\n".join(feedback))
        )
        
        return feedback_message

# Example usage
password = input("Enter a password to check its strength: ")
checker = PasswordStrengthChecker(password)
print(checker.evaluate_strength())
