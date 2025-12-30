#!/usr/bin/env python3
"""API Chameleon - Because APIs change colors faster than a chameleon on a disco floor."""

import json
import difflib
import sys
from datetime import datetime
from typing import Dict, Any, Optional

class APISniffer:
    """Sniffs API responses like a bloodhound with a networking degree."""
    
    def __init__(self, name: str = "API"):
        self.name = name
        self.last_response: Optional[Dict[str, Any]] = None
        self.last_timestamp: Optional[str] = None
        
    def sniff(self, response_data: Dict[str, Any]) -> bool:
        """Sniffs current response, barks if different from last one."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if self.last_response is None:
            print(f"🐍 First sniff for {self.name} at {timestamp}")
            self._save_snapshot(response_data, timestamp)
            return True
        
        if self.last_response == response_data:
            print(f"✅ {self.name} hasn't changed its spots! ({timestamp})")
            return True
        
        print(f"🚨 ALERT! {self.name} is shape-shifting! ({timestamp})")
        self._show_differences(response_data)
        self._save_snapshot(response_data, timestamp)
        return False
    
    def _save_snapshot(self, data: Dict[str, Any], timestamp: str):
        """Saves response like a squirrel hiding nuts for winter."""
        self.last_response = data.copy()
        self.last_timestamp = timestamp
    
    def _show_differences(self, new_data: Dict[str, Any]):
        """Shows differences with more drama than a reality TV show."""
        old_json = json.dumps(self.last_response, indent=2)
        new_json = json.dumps(new_data, indent=2)
        
        print(f"\n📅 Last stable: {self.last_timestamp}")
        print("\n🔍 Spot the differences (they're hiding):")
        
        diff = difflib.unified_diff(
            old_json.splitlines(keepends=True),
            new_json.splitlines(keepends=True),
            fromfile='old',
            tofile='new',
            lineterm=''
        )
        
        for line in diff:
            if line.startswith('+') and not line.startswith('+++'):
                print(f"🟢 {line}")
            elif line.startswith('-') and not line.startswith('---'):
                print(f"🔴 {line}")
        print()


def main():
    """Main function - where the magic (and debugging tears) happens."""
    # Example usage - replace with your actual API calls
    print("\n=== API Chameleon Detector ===\n")
    
    sniffer = APISniffer("My Fickle API")
    
    # Simulate API responses (replace these with real API calls)
    stable_response = {"status": "ok", "data": [1, 2, 3], "version": "1.0"}
    changed_response = {"status": "ok", "data": [1, 2], "version": "1.1"}  # Oops!
    
    print("Test 1: First call")
    sniffer.sniff(stable_response)
    
    print("\nTest 2: Same response")
    sniffer.sniff(stable_response)
    
    print("\nTest 3: Sneaky change!")
    sniffer.sniff(changed_response)
    
    print("\n💡 Tip: Integrate this between your API calls to catch shape-shifters!")

if __name__ == "__main__":
    main()