# SIGMA π Calculator - Real Business Examples
from pi_calculator import PiCalculator

def run_business_examples():
    calculator = PiCalculator()
    
    examples = [
        {
            "name": "Netflix: Enter Video Gaming",
            "impact": 8,
            "covenant_fit": 7,
            "domain_match": 4,
            "transformation_gain": 9,
            "context": "Streaming giant considering game development"
        },
        {
            "name": "Tesla: Launch Airline Business", 
            "impact": 9,
            "covenant_fit": 6,
            "domain_match": 2,
            "transformation_gain": 8,
            "context": "Electric car company exploring aviation"
        },
        {
            "name": "Starbucks: Cryptocurrency Payment",
            "impact": 6,
            "covenant_fit": 3,
            "domain_match": 2,
            "transformation_gain": 7,
            "context": "Coffee chain launching digital currency"
        },
        {
            "name": "Apple: Healthcare Devices",
            "impact": 9,
            "covenant_fit": 8,
            "domain_match": 7,
            "transformation_gain": 10,
            "context": "Tech company entering medical devices"
        },
        {
            "name": "McDonald's: Food Delivery Drones",
            "impact": 7,
            "covenant_fit": 8,
            "domain_match": 3,
            "transformation_gain": 9,
            "context": "Fast food chain automating delivery"
        }
    ]
    
    print("🤖 SIGMA π Calculator - Business Decision Examples\n")
    print("=" * 60)
    
    for example in examples:
        pi_score = calculator.calculate_pi_score(
            example["impact"],
            example["covenant_fit"], 
            example["domain_match"],
            example["transformation_gain"]
        )
        
        recommendation = calculator.get_recommendation(pi_score)
        
        print(f"\n📊 {example['name']}")
        print(f"Context: {example['context']}")
        print(f"π Score: {pi_score}")
        print(f"Decision: {recommendation}")
        print("-" * 40)

if __name__ == "__main__":
    run_business_examples()
