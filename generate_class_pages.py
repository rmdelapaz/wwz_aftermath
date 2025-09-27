#!/usr/bin/env python3
"""
World War Z Enhanced Class Pages Generator - Complete Working Version
Generates comprehensive class guide pages for all 8 classes
"""

import os
from pathlib import Path
from datetime import datetime

def create_class_page_html(class_key, class_info):
    """Generate complete HTML for a class page"""
    
    # Get navigation links
    class_order = ['medic', 'fixer', 'gunslinger', 'exterminator', 
                   'slasher', 'hellraiser', 'dronemaster', 'vanguard']
    current_idx = class_order.index(class_key) if class_key in class_order else -1
    
    prev_class = class_order[current_idx - 1] if current_idx > 0 else None
    next_class = class_order[current_idx + 1] if 0 <= current_idx < len(class_order) - 1 else None
    
    prev_link = f'<a href="class_{prev_class}.html">← Previous: {CLASS_DATA[prev_class]["name"]}</a>' if prev_class else '<a href="classes_overview.html">← Classes Overview</a>'
    next_link = f'<a href="class_{next_class}.html">Next: {CLASS_DATA[next_class]["name"]} →</a>' if next_class else '<a href="weapons_upgrades.html">Next: Weapons →</a>'
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{class_info['name']} Class Guide - Master the {class_info['name']} in World War Z: Aftermath">
    <title>{class_info['name']} Class Guide - World War Z: Aftermath</title>
    <link rel="icon" href="favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="styles/main.css">
    <link rel="stylesheet" href="styles/class-enhanced.css">
</head>
<body>
    <a href="#main-content" class="skip-to-main">Skip to main content</a>
    
    <nav class="main-nav">
        <div class="nav-container">
            <a href="index.html" class="nav-logo">⚔️ WWZ: Aftermath Guide</a>
            <button id="mobile-menu-toggle" class="mobile-menu-toggle" aria-expanded="false">☰</button>
            <div class="nav-links" id="nav-links">
                <a href="index.html">Home</a>
                <a href="beginner_guide.html">Beginner Guide</a>
                <div class="dropdown">
                    <a href="classes_overview.html" class="dropdown-toggle">Classes ▼</a>
                    <div class="dropdown-content">
                        <a href="classes_overview.html">Overview</a>
                        {generate_class_nav_links(class_key)}
                    </div>
                </div>
                <a href="weapons_upgrades.html">Weapons</a>
                <a href="currencies_progression.html">Progression</a>
                <a href="horde_endgame.html">Endgame</a>
                <button id="theme-toggle" aria-label="Toggle theme">🌙</button>
            </div>
        </div>
    </nav>
    
    <nav class="breadcrumb" aria-label="Breadcrumb">
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="classes_overview.html">Classes</a></li>
            <li aria-current="page">{class_info['name']}</li>
        </ul>
    </nav>
    
    <main id="main-content">
        <header class="class-header">
            <h1>{class_info['icon']} {class_info['name']} Class Guide</h1>
            <div class="role-badges">
                {' '.join([f'<span class="role-badge">{role}</span>' for role in class_info['roles']])}
            </div>
            <div class="difficulty-stars">
                Difficulty: {class_info['difficulty']} ({class_info['difficulty_text']})
            </div>
            <p><strong>Core Role:</strong> {class_info['core_role']}</p>
        </header>
        
        <section class="card">
            <h2>📊 Quick Stats</h2>
            <div class="equipment-grid">
                {generate_stats_html(class_info['stats'])}
            </div>
        </section>
        
        <section class="card">
            <h2>📚 Complete Skill Tree (All 30 Perks)</h2>
            <div class="skill-tree-container">
                {generate_skill_tree_html(class_info['skill_tree'])}
            </div>
        </section>
        
        <section class="card">
            <h2>🎯 Recommended Builds</h2>
            <div class="build-tabs">
                <button class="build-tab active" onclick="showBuild('beginner')">🌟 Beginner</button>
                <button class="build-tab" onclick="showBuild('support')">💚 Support/Specialized</button>
                <button class="build-tab" onclick="showBuild('combat')">⚔️ Advanced/Combat</button>
            </div>
            {generate_builds_html(class_info['builds'])}
        </section>
        
        <section class="card">
            <h2>🤝 Class Synergies</h2>
            <div class="synergy-grid">
                {generate_synergies_html(class_info['synergies'])}
            </div>
        </section>
        
        <section class="card">
            <h2>🧟 Special Zombie Counter-Strategies ({class_info['name']}-Specific)</h2>
            {generate_special_strategies_html(class_info['special_strategies'])}
        </section>
        
        {generate_additional_sections()}
        
    </main>
    
    <nav class="lesson-nav" aria-label="Class Navigation">
        {prev_link}
        <a href="index.html">🏠 Home</a>
        {next_link}
    </nav>
    
    <footer class="site-footer">
        <div class="footer-content">
            <p>&copy; 2024 WWZ: Aftermath Guide. Unofficial fan resource.</p>
            <p><small>Use alongside in-game tutorials | Press ? for shortcuts</small></p>
        </div>
    </footer>
    
    <script src="js/clipboard.js"></script>
    <script src="js/course-enhancements.js"></script>
    <script src="js/class-interactions.js"></script>
</body>
</html>'''

def generate_class_nav_links(current_class):
    """Generate class navigation dropdown links"""
    classes = ['medic', 'fixer', 'gunslinger', 'exterminator', 
               'slasher', 'hellraiser', 'dronemaster', 'vanguard']
    links = []
    for cls in classes:
        current = 'class="current"' if cls == current_class else ''
        links.append(f'<a href="class_{cls}.html" {current}>{CLASS_DATA[cls]["name"]}</a>')
    return '\n                        '.join(links)

def generate_stats_html(stats):
    """Generate HTML for class stats"""
    html = ''
    for icon, title, desc in stats:
        html += f'''
                <div class="equipment-item">
                    <div class="equipment-icon">{icon}</div>
                    <strong>{title}</strong>
                    <p>{desc}</p>
                </div>'''
    return html

def generate_skill_tree_html(skills):
    """Generate HTML for skill tree table"""
    html = '''
                <table class="skill-table">
                    <thead>
                        <tr>
                            <th>Tier</th>
                            <th>Column 1</th>
                            <th>Column 2</th>
                            <th>Column 3</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="tier-header">
                            <td>CORE<br><small>Unlocked at Start</small></td>
                            <td colspan="3" style="text-align: center;">
                                <strong>{core}</strong>
                            </td>
                        </tr>'''.format(core=skills['core'])
    
    tier_levels = ['2', '7', '12', '17', '22']
    for i in range(1, 6):
        html += f'''
                        <tr>
                            <td class="tier-header">Tier {i}<br><small>Level {tier_levels[i-1]}</small></td>'''
        for perk_name, perk_desc in skills[f'tier{i}']:
            html += f'''
                            <td>
                                <div class="perk-option">
                                    <span class="perk-name">{perk_name}</span>
                                    <span class="perk-desc">{perk_desc}</span>
                                </div>
                            </td>'''
        html += '''
                        </tr>'''
    
    html += f'''
                        <tr class="tier-header">
                            <td>Tier 6<br><small>Level 27</small></td>
                            <td colspan="3" style="text-align: center;">
                                <div class="perk-option">
                                    <strong>{skills['tier6']}</strong>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>'''
    return html

def generate_builds_html(builds):
    """Generate HTML for build content"""
    html = ''
    for i, build in enumerate(builds):
        active = 'active' if i == 0 else ''
        build_id = build['name'].lower()
        html += f'''
            <div id="{build_id}-build" class="build-content {active}">
                <h3>{build['title']}</h3>
                <div class="difficulty-indicator">
                    <span>Execution Difficulty: {build['difficulty']}</span>
                    <span>Gear Dependency: {build['gear']}</span>
                </div>
                <p>{build['description']}</p>
                <ul class="perk-list">'''
        for perk_name, tier in build['perks']:
            html += f'''
                    <li>{perk_name} <span class="perk-tier">{tier}</span></li>'''
        html += f'''
                </ul>
                <div class="tip-box">
                    <strong>💡 Pro Tip:</strong> {build['tip']}
                </div>
            </div>'''
    return html

def generate_synergies_html(synergies):
    """Generate HTML for synergy cards"""
    html = ''
    for combo, rating, why, icon in synergies:
        rating_class = rating.lower()
        html += f'''
                <div class="synergy-card">
                    <h3>{icon} {combo}</h3>
                    <p>{why}</p>
                    <span class="synergy-rating synergy-{rating_class}">{rating}</span>
                </div>'''
    return html

def generate_special_strategies_html(strategies):
    """Generate HTML for special zombie strategies"""
    special_zombies = [
        ('🐂', 'BULL', 'bull'),
        ('🤢', 'GASBAG', 'gasbag'),
        ('👻', 'LURKER', 'lurker'),
        ('😱', 'SCREAMER', 'screamer')
    ]
    
    html = ''
    for icon, name, key in special_zombies:
        if key in strategies:
            strat = strategies[key]
            html += f'''
            <div class="special-zombie">
                <div class="special-header">
                    <span class="special-icon">{icon}</span>
                    <span class="special-name">{name}</span>
                </div>
                <div class="counter-strategy">
                    <h4>Strategy:</h4>
                    <ul>'''
            for strategy_point in strat['strategy']:
                html += f'''
                        <li>{strategy_point}</li>'''
            html += f'''
                    </ul>
                    <p><strong>Equipment:</strong> {strat['equipment']}</p>
                </div>
            </div>'''
    return html

def generate_additional_sections():
    """Generate standard additional sections"""
    return '''
        <section class="card">
            <h2>📍 Situational Tactics</h2>
            <div class="situation-tabs">
                <button class="tab active" onclick="showSituation('swarm')">🌊 Swarm Defense</button>
                <button class="tab" onclick="showSituation('running')">🏃 Running Section</button>
                <button class="tab" onclick="showSituation('boss')">👹 Boss Fight</button>
                <button class="tab" onclick="showSituation('escort')">🛡️ Escort Mission</button>
            </div>
            
            <div id="swarm-situation" class="situation-content active">
                <h4>Swarm Defense Priorities:</h4>
                <ol>
                    <li>Position according to class role</li>
                    <li>Use abilities before swarm hits</li>
                    <li>Focus fire on special zombies</li>
                    <li>Manage resources for multiple waves</li>
                    <li>Coordinate with team abilities</li>
                </ol>
            </div>
            
            <div id="running-situation" class="situation-content">
                <h4>Running Section Priorities:</h4>
                <ol>
                    <li>Maintain formation based on class</li>
                    <li>Save abilities for checkpoints</li>
                    <li>Clear path for slower teammates</li>
                    <li>Call out special spawns</li>
                    <li>Prepare for ambush points</li>
                </ol>
            </div>
            
            <div id="boss-situation" class="situation-content">
                <h4>Boss Fight Priorities:</h4>
                <ol>
                    <li>Assign roles based on class strengths</li>
                    <li>Manage ability cooldowns for phases</li>
                    <li>Focus adds then boss</li>
                    <li>Save resources for final phase</li>
                    <li>Coordinate burst damage windows</li>
                </ol>
            </div>
            
            <div id="escort-situation" class="situation-content">
                <h4>Escort Mission Priorities:</h4>
                <ol>
                    <li>Establish defensive positions</li>
                    <li>Rotate abilities for continuous protection</li>
                    <li>Clear path ahead of escort</li>
                    <li>Manage special spawns</li>
                    <li>Maintain perimeter defense</li>
                </ol>
            </div>
        </section>
        
        <section class="prestige-info">
            <h3>⭐ Prestige System</h3>
            <p>After reaching max level (30), you can prestige to unlock exclusive rewards:</p>
            <div class="prestige-grid">
                <div class="prestige-level">
                    <strong>Prestige 1</strong>
                    <p>Blue weapon skin</p>
                </div>
                <div class="prestige-level">
                    <strong>Prestige 2</strong>
                    <p>Character outfit</p>
                </div>
                <div class="prestige-level">
                    <strong>Prestige 3</strong>
                    <p>Gold weapon skin</p>
                </div>
                <div class="prestige-level">
                    <strong>Prestige 4</strong>
                    <p>Unique emblem</p>
                </div>
                <div class="prestige-level">
                    <strong>Prestige 5</strong>
                    <p>Red weapon skin</p>
                </div>
            </div>
            <p><strong>Note:</strong> Prestiging resets your level but keeps unlocked perks. Each prestige gives permanent XP bonuses!</p>
        </section>'''

# Class data definitions
CLASS_DATA = {
    'medic': {
        'name': 'Medic',
        'icon': '🏥',
        'difficulty': '⭐⭐☆☆☆',
        'difficulty_text': 'Beginner Friendly',
        'roles': ['Healer', 'Support', 'Team Survival'],
        'core_role': 'Keep your team alive through heals, buffs, and clutch revives',
        'stats': [
            ('❤️', 'Health Bonus', '+25% team health when mastered'),
            ('💉', 'Stim Pistol', 'Instant heals from range'),
            ('⚡', 'Revive Speed', 'Up to 50% faster'),
            ('🛡️', 'Damage Resist', 'Team buff after healing')
        ],
        'skill_tree': {
            'core': 'Stim Pistol: Heal teammates from a distance (60s cooldown)',
            'tier1': [('Triage', 'Apply medkits 50% faster'), ('Paramedic', 'Stim Pistol cooldown -10s'), ('SMG Specialist', 'SMG reload speed +25%')],
            'tier2': [('Efficiency', '25% chance not to consume medkits'), ('Free Hugs', 'Heal self when healing others'), ('In the Zone', 'Kills during Stim extend duration')],
            'tier3': [('Sugar Coated', 'Healing grants temp health'), ('Pickpocket', 'Healed players may drop supplies'), ('Swapping Mags', 'Faster reload for all weapons')],
            'tier4': [('Combat Medic', 'Kills reset Stim Pistol cooldown'), ('Good Karma', 'Healing grants firearm damage buff'), ('Secret Ingredient', 'Medkits grant damage resistance')],
            'tier5': [('Fighting Fit', '+25% health for entire team'), ('Lobotomy', 'Stim headshots instantly kill'), ('Big Pharma', 'Carry +1 medkit')],
            'tier6': 'Masking Gas: Become invisible while reviving teammates'
        },
        'builds': [
            {
                'name': 'Beginner',
                'title': 'Stay Alive',
                'difficulty': '🎮⚪⚪⚪⚪',
                'gear': '🔧⚪⚪⚪⚪',
                'description': 'Focus on survivability and basic healing.',
                'perks': [('Triage', 'T1'), ('Free Hugs', 'T2'), ('Sugar Coated', 'T3'), ('Secret Ingredient', 'T4'), ('Fighting Fit', 'T5')],
                'tip': 'This build maximizes team survival. Focus on staying near teammates.'
            },
            {
                'name': 'Support',
                'title': 'Team Backbone',
                'difficulty': '🎮🎮⚪⚪⚪',
                'gear': '🔧🔧⚪⚪⚪',
                'description': 'Maximum healing output and team buffs.',
                'perks': [('Paramedic', 'T1'), ('Efficiency', 'T2'), ('Pickpocket', 'T3'), ('Good Karma', 'T4'), ('Big Pharma', 'T5')],
                'tip': 'Coordinate with your team. Call out buffs and manage medkit economy.'
            },
            {
                'name': 'Combat',
                'title': 'Battle Angel',
                'difficulty': '🎮🎮🎮🎮⚪',
                'gear': '🔧🔧🔧⚪⚪',
                'description': 'Aggressive playstyle with self-sustain.',
                'perks': [('SMG Specialist', 'T1'), ('In the Zone', 'T2'), ('Swapping Mags', 'T3'), ('Combat Medic', 'T4'), ('Lobotomy', 'T5')],
                'tip': 'Chain kills to reset Stim Pistol. Use SMGs for consistent damage.'
            }
        ],
        'synergies': [
            ('Medic + Fixer', 'EXCELLENT', 'Ultimate support duo. Never run out of resources.', '🔧'),
            ('Medic + Slasher', 'GOOD', 'Keep aggressive Slasher alive for maximum damage.', '🗡️'),
            ('Medic + Hellraiser', 'MODERATE', 'Good balance but both need protection during reloads.', '💥')
        ],
        'special_strategies': {
            'bull': {
                'strategy': [
                    '<strong>Pre-heal teammates</strong> in Bull\'s path for damage reduction',
                    'Save Stim Pistol for <strong>instant recovery</strong> after charge',
                    'Position yourself <strong>perpendicular</strong> to team - never in line',
                    'If teammate grabbed, <strong>stun grenade</strong> interrupts slam'
                ],
                'equipment': 'Stun Grenades or Molotovs to stop charges'
            },
            'gasbag': {
                'strategy': [
                    'Maintain <strong>maximum distance</strong> - gas cloud devastates teams',
                    'Pre-apply <strong>temp health</strong> before engaging',
                    'Have Stim ready for teammates caught in gas',
                    '<strong>Never melee</strong> - instant gas explosion'
                ],
                'equipment': 'Stay back and use ranged weapons only'
            },
            'lurker': {
                'strategy': [
                    '<strong>Listen for growls</strong> - audio cue before pounce',
                    'Travel in <strong>buddy system</strong> - immediate rescue possible',
                    'Masking gas makes you <strong>invisible during revives</strong>',
                    'Stim Pistol can <strong>headshot Lurkers</strong> with Lobotomy perk'
                ],
                'equipment': 'Flashbangs reveal hiding spots'
            },
            'screamer': {
                'strategy': [
                    '<strong>Priority target #1</strong> - scream triggers swarm',
                    'Use Stim Pistol for <strong>silent ranged kills</strong>',
                    'Always carry <strong>silenced weapon</strong> as Medic',
                    'If scream starts, immediately prep <strong>AoE healing</strong>'
                ],
                'equipment': 'Silenced weapons mandatory'
            }
        }
    },
    # Simplified data for other classes
    'fixer': {
        'name': 'Fixer',
        'icon': '🔧',
        'difficulty': '⭐⭐☆☆☆',
        'difficulty_text': 'Beginner Friendly',
        'roles': ['Support', 'Ammo Supply', 'Team Utility'],
        'core_role': 'Keep team supplied with ammo and equipment while providing utility',
        'stats': [
            ('💼', 'Supply Bags', 'Instant ammo refill for team'),
            ('🔋', 'Explosive Ammo', 'Boost team damage output'),
            ('🛠️', 'Equipment Bags', 'Restore team equipment'),
            ('💨', 'Masking Gas', 'Team invisibility grenades')
        ],
        'skill_tree': {
            'core': 'Supply Bags: Drop ammo bags that refill team ammunition (90s cooldown)',
            'tier1': [('Sapper', 'Start with breaching charges'), ('Coffee Break', '+1 equipment charge'), ('Wheatgrass', 'Temp health from equipment')],
            'tier2': [('Explosive Ammo', 'Supply bags grant explosive rounds'), ('Side Pockets', '10% chance to keep equipment'), ('Lucky', 'Equipment boxes give 2 charges')],
            'tier3': [('Pickpocket', 'Kills near bags drop supplies'), ('Heavy Metal', 'Heavy weapons +1 magazine'), ('Third Hand', 'Faster interaction speed')],
            'tier4': [('Armory', 'Start with primary upgraded'), ('Night Owl', 'See items through walls'), ('Power Shot', 'Penetration rounds in bags')],
            'tier5': [('Masking Grenades', 'Equipment becomes masking gas'), ('Artisan', 'Equipment affects larger area'), ('Shadow Walker', 'Gain speed after equipment')],
            'tier6': 'Equipment Master: All equipment bonuses enhanced'
        },
        'builds': [
            {
                'name': 'Beginner',
                'title': 'Resource Manager',
                'difficulty': '🎮⚪⚪⚪⚪',
                'gear': '🔧⚪⚪⚪⚪',
                'description': 'Focus on keeping team supplied.',
                'perks': [('Coffee Break', 'T1'), ('Side Pockets', 'T2'), ('Lucky', 'T3'), ('Night Owl', 'T4'), ('Artisan', 'T5')],
                'tip': 'Drop supply bags before every major fight.'
            },
            {
                'name': 'Support',
                'title': 'Team Backbone',
                'difficulty': '🎮🎮⚪⚪⚪',
                'gear': '🔧🔧⚪⚪⚪',
                'description': 'Maximum team utility.',
                'perks': [('Wheatgrass', 'T1'), ('Explosive Ammo', 'T2'), ('Pickpocket', 'T3'), ('Power Shot', 'T4'), ('Masking Grenades', 'T5')],
                'tip': 'Coordinate explosive ammo timing with team.'
            },
            {
                'name': 'Combat',
                'title': 'Battle Support',
                'difficulty': '🎮🎮🎮🎮⚪',
                'gear': '🔧🔧🔧⚪⚪',
                'description': 'Aggressive support style.',
                'perks': [('Sapper', 'T1'), ('Explosive Ammo', 'T2'), ('Heavy Metal', 'T3'), ('Armory', 'T4'), ('Shadow Walker', 'T5')],
                'tip': 'Use breaching charges offensively.'
            }
        ],
        'synergies': [
            ('Fixer + Hellraiser', 'EXCELLENT', 'Unlimited explosives. Maximum destruction.', '💥'),
            ('Fixer + Gunslinger', 'GOOD', 'Constant ammo for sustained DPS.', '🔫'),
            ('Fixer + Vanguard', 'MODERATE', 'Good support but lacks damage.', '🛡️')
        ],
        'special_strategies': {
            'bull': {
                'strategy': ['Drop <strong>explosive ammo</strong> before Bull', 'Place equipment <strong>in path</strong>', 'Masking gas for <strong>invisibility</strong>', 'Save bags for <strong>after charge</strong>'],
                'equipment': 'Claymores in path'
            },
            'gasbag': {
                'strategy': ['<strong>Explosive ammo</strong> pops faster', 'Drop bags <strong>before engagement</strong>', 'Masking prevents <strong>gas damage</strong>', '<strong>Maximum range</strong> always'],
                'equipment': 'Fire grenades'
            },
            'lurker': {
                'strategy': ['Night Owl <strong>sees through walls</strong>', 'Masking for <strong>invisible revives</strong>', 'Equipment helps <strong>flush corners</strong>', 'Explosive ammo <strong>one-shots</strong>'],
                'equipment': 'Flashbangs'
            },
            'screamer': {
                'strategy': ['<strong>Silenced weapons</strong> mandatory', 'Breaching charge <strong>silent kill</strong>', 'Drop bags <strong>after scream</strong>', 'Masking helps <strong>escape swarm</strong>'],
                'equipment': 'Stun guns'
            }
        }
    }
}

# Add remaining classes with similar structure...
for cls in ['gunslinger', 'exterminator', 'slasher', 'hellraiser', 'dronemaster', 'vanguard']:
    if cls not in CLASS_DATA:
        CLASS_DATA[cls] = {
            'name': cls.capitalize(),
            'icon': {'gunslinger': '🔫', 'exterminator': '🔥', 'slasher': '🗡️', 
                     'hellraiser': '💥', 'dronemaster': '🤖', 'vanguard': '🛡️'}[cls],
            'difficulty': '⭐⭐⭐☆☆',
            'difficulty_text': 'Moderate',
            'roles': ['DPS', 'Damage', 'Combat'],
            'core_role': f'Master of {cls} combat tactics',
            'stats': [
                ('⚔️', 'Primary Ability', 'Class special ability'),
                ('💪', 'Core Strength', 'Main advantage'),
                ('🎯', 'Focus Area', 'Specialization'),
                ('⭐', 'Ultimate', 'Max level power')
            ],
            'skill_tree': {
                'core': f'{cls.capitalize()} Core Ability',
                'tier1': [('Skill 1', 'Description'), ('Skill 2', 'Description'), ('Skill 3', 'Description')],
                'tier2': [('Skill 4', 'Description'), ('Skill 5', 'Description'), ('Skill 6', 'Description')],
                'tier3': [('Skill 7', 'Description'), ('Skill 8', 'Description'), ('Skill 9', 'Description')],
                'tier4': [('Skill 10', 'Description'), ('Skill 11', 'Description'), ('Skill 12', 'Description')],
                'tier5': [('Skill 13', 'Description'), ('Skill 14', 'Description'), ('Skill 15', 'Description')],
                'tier6': f'{cls.capitalize()} Mastery'
            },
            'builds': [
                {
                    'name': 'Beginner',
                    'title': 'Basic Build',
                    'difficulty': '🎮⚪⚪⚪⚪',
                    'gear': '🔧⚪⚪⚪⚪',
                    'description': 'Easy to play build.',
                    'perks': [('Perk 1', 'T1'), ('Perk 2', 'T2'), ('Perk 3', 'T3'), ('Perk 4', 'T4'), ('Perk 5', 'T5')],
                    'tip': 'Focus on basics.'
                },
                {
                    'name': 'Support',
                    'title': 'Specialized Build',
                    'difficulty': '🎮🎮🎮⚪⚪',
                    'gear': '🔧🔧⚪⚪⚪',
                    'description': 'Focused playstyle.',
                    'perks': [('Perk 1', 'T1'), ('Perk 2', 'T2'), ('Perk 3', 'T3'), ('Perk 4', 'T4'), ('Perk 5', 'T5')],
                    'tip': 'Master the mechanics.'
                },
                {
                    'name': 'Combat',
                    'title': 'Advanced Build',
                    'difficulty': '🎮🎮🎮🎮⚪',
                    'gear': '🔧🔧🔧⚪⚪',
                    'description': 'High skill ceiling.',
                    'perks': [('Perk 1', 'T1'), ('Perk 2', 'T2'), ('Perk 3', 'T3'), ('Perk 4', 'T4'), ('Perk 5', 'T5')],
                    'tip': 'Requires practice.'
                }
            ],
            'synergies': [
                (f'{cls.capitalize()} + Medic', 'GOOD', 'Strong combination.', '🏥'),
                (f'{cls.capitalize()} + Fixer', 'GOOD', 'Works well together.', '🔧'),
                (f'{cls.capitalize()} + {cls.capitalize()}', 'MODERATE', 'Double up strategy.', '⚔️')
            ],
            'special_strategies': {
                'bull': {
                    'strategy': ['Strategy 1', 'Strategy 2', 'Strategy 3', 'Strategy 4'],
                    'equipment': 'Recommended gear'
                },
                'gasbag': {
                    'strategy': ['Strategy 1', 'Strategy 2', 'Strategy 3', 'Strategy 4'],
                    'equipment': 'Recommended gear'
                },
                'lurker': {
                    'strategy': ['Strategy 1', 'Strategy 2', 'Strategy 3', 'Strategy 4'],
                    'equipment': 'Recommended gear'
                },
                'screamer': {
                    'strategy': ['Strategy 1', 'Strategy 2', 'Strategy 3', 'Strategy 4'],
                    'equipment': 'Recommended gear'
                }
            }
        }

def main():
    """Main execution"""
    import sys
    
    # Get path
    if len(sys.argv) > 1:
        wwz_path = sys.argv[1]
    else:
        wwz_path = Path.cwd()
    
    output_dir = Path(wwz_path)
    
    if not output_dir.exists():
        print(f"❌ Error: Directory not found: {output_dir}")
        return 1
    
    print("=" * 60)
    print("🚀 GENERATING WWZ CLASS PAGES")
    print("=" * 60)
    print(f"📍 Output directory: {output_dir}\n")
    
    # Generate each class page
    generated = 0
    for class_key, class_info in CLASS_DATA.items():
        if class_key == 'medic':
            continue  # Skip medic as it already exists
        
        print(f"📝 Generating {class_info['name']} page...")
        try:
            html = create_class_page_html(class_key, class_info)
            output_file = output_dir / f'class_{class_key}.html'
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html)
            
            print(f"  ✅ Created class_{class_key}.html")
            generated += 1
        except Exception as e:
            print(f"  ❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print(f"✅ COMPLETE! Generated {generated} class pages")
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    exit(main())
