"""
===============================================================================
 Name        : spells.py
 Author(s)   :
 Version     : 0.1
 Description : Provides spell casting functions with cooldown tracking.
            
 notes:
    -  Requires pyautogui library.
===============================================================================

 

"""

import time
import pyautogui

# Define spells and their corresponding keys
spells = {
    'health_pot': '1',
    'mana_pot': '2',
}

# Track cooldowns for all spells
can_cast_spell = {spell: 0 for spell in spells}


def cast_spell(spell_name: str, wait: float):
    """
    Cast a spell and update its cooldown.

    Args:
        spell_name (str): Name of the spell to cast.
        wait (float): Cooldown duration in seconds.

    Returns:
        None
    """
    key = spells[spell_name]
    print('Casting spell:', spell_name)
    # pyautogui.press(key)  # Uncomment to enable actual key press
    can_cast_spell[spell_name] = time.time() + wait
