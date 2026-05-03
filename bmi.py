"""
Bmi Calculator - Main module.
"""
import sys

VERSION = "0.2.0"

def run(args):
    """Main entry point."""
    print(f"Bmi Calculator v{VERSION}")
    if args:
        print(f"Processing: {', '.join(args)}")
        process(args)
    else:
        print("Usage: python bmi.py [arguments]")
        print("Try: python bmi.py --help")

def process(args):
    """Process input arguments."""
    data = []
    for arg in args:
        result = arg.strip()
        if result:
            data.append(result)
            print(f"  Processed: {result}")
    print(f"\nTotal: {len(data)} items processed")
    return data

def main():
    run(sys.argv[1:])

if __name__ == "__main__":
    main()
