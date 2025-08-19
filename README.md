# -sigma-Pi-calculator
AI-powered business decision scoring system
File 1: pi_calculator.py# SIGMA Pi Calculator - Core Engine
# This calculates business decision scores

class PiCalculator:
    def __init__(self):
        # Default weights (you can adjust these)
        self.w1_impact = 0.30           # 30% weight on financial impact
        self.w2_covenant = 0.20         # 20% weight on company fit
        self.w3_domain = 0.25           # 25% weight on expertise match
        self.w4_transformation = 0.25   # 25% weight on growth potential
    
    def calculate_pi_score(self, impact, covenant_fit, domain_match, transformation_gain):
        """
        Calculate the π (pi) score for any business decision
        
        All inputs should be rated 1-10 where:
        - 1 = Very Poor
        - 5 = Average  
        - 10 = Exceptional
        """
        pi_score = (
            self.w1_impact * impact +
            self.w2_covenant * covenant_fit +
            self.w3_domain * domain_match +
            self.w4_transformation * transformation_gain
        )
        
        return round(pi_score, 2)
    
    def get_recommendation(self, pi_score):
        """Convert π score to business recommendation"""
        if pi_score >= 8.0:
            return "🚀 HIGHLY RECOMMENDED - Execute immediately"
        elif pi_score >= 6.5:
            return "✅ RECOMMENDED - Strong strategic fit"  
        elif pi_score >= 5.0:
            return "⚠️ CONSIDER - Proceed with caution"
        elif pi_score >= 3.0:
            return "❌ NOT RECOMMENDED - High risk"
        else:
            return "🛑 AVOID - Major red flags"

# Example usage
if __name__ == "__main__":
    calculator = PiCalculator()
    
    # Example: Should we launch a new mobile app?
    impact = 8              # High revenue potential
    covenant_fit = 7        # Matches our digital strategy
    domain_match = 6        # We have some mobile experience
    transformation_gain = 9 # Could revolutionize customer experience
    
    pi_score = calculator.calculate_pi_score(impact, covenant_fit, domain_match, transformation_gain)
    recommendation = calculator.get_recommendation(pi_score)
    
    print(f"π Score: {pi_score}")
    print(f"Recommendation: {recommendation}")
