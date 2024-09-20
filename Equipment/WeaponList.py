# This weapon list is pulled from Ad&d 2E Player's Option: Combat & Tactics

class WeaponsList:
    def __init__(self):
        self.weapons = {
            'Adze': {'Weight': 4, 'Size': 'S', 'Type': 'S/P', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4+1', 'Damage vs Large': '1d4', 'Knockdown': 'd6'}, 
            'Ankus': {'Weight': 4, 'Size': 'M', 'Type': 'P/B', 'Speed': 'Av(6)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd8'}, 
            # Axes
            'Battle': {'Weight': 7, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d8', 'Knockdown': 'd10'}, 
            'Hand/throwing': {'Weight': 5, 'Size': 'M', 'Type': 'S', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d4', 'Knockdown': 'd8'}, 
            'Stone': {'Weight': 6, 'Size': 'M', 'Type': 'B/S', 'Speed': 'Av(6)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d4', 'Knockdown': 'd8'}, 
            'Two-handed': {'Weight': 10, 'Size': 'L', 'Type': 'S', 'Speed': 'Sl(9)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d10', 'Damage vs Large': '2d8', 'Knockdown': 'd12'}, 
            # Axes End
            'Bagh nakh': {'Weight': 1, 'Size': 'S', 'Type': 'S', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d2', 'Damage vs Large': '1d2', 'Knockdown': 'd4'}, 
            'Belaying pin': {'Weight': 2, 'Size': 'S', 'Type': 'B', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d3', 'Knockdown': 'd6'}, 
            'Blowgun': {'Weight': 2, 'Size': 'L', 'Type': '—', 'Speed': 'Av(5)', 'Melee Reach': '—', 'Missile ROF': '2/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
                'Barbed dart': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '2/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d2', 'Knockdown': 'd4'}, 
                'Needle': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '2/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': 1, 'Damage vs Large': 1, 'Knockdown': '—'}, 
            'Bo stick': {'Weight': 4, 'Size': 'L', 'Type': 'B', 'Speed': 'Fa(3)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d4', 'Knockdown': 'd8'}, 
            'Bolas': {'Weight': 2, 'Size': 'M', 'Type': 'B', 'Speed': 'Sl(8)', 'Melee Reach': '—', 'Missile ROF': '1/rnd', 'Range': '6/12/18', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d2', 'Knockdown': 'd6'}, 
            'Boomerang': {'Weight': 2, 'Size': 'S', 'Type': 'B', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '4/8/12', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd8'}, 
            'Bottle': {'Weight': 2, 'Size': 'S', 'Type': 'B', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d2', 'Knockdown': 'd6'}, 
            # Bows
            'Composite long': {'Weight': 3, 'Size': 'L', 'Type': '(P)', 'Speed': 'Av(7)', 'Melee Reach': '—', 'Missile ROF': '2/rnd', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown':'d6'}, 
            'w/flight arrow': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '12/24/42', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6', 'Knockdown': 'd6'}, 
            'w/pile arrow': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '8/16/34', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6', 'Knockdown': 'd6'}, 
            'w/sheaf arrow': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '8/16/34', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d8', 'Knockdown': 'd6'
            }, 
            'w/stone arrow': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '12/24/42', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd6'}, 
            'Composite short': {'Weight': 2, 'Size': 'M', 'Type': '(P)', 'Speed': 'Av(6)', 'Melee Reach': '—', 'Missile ROF': '2/rnd', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'
            }, 
            'w/flight arrow': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '10/20/36', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6', 'Knockdown': 'd6'},
            'w/stone arrow': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '10/20/36', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd6'},                              
            'Long': {'Weight': 3, 'Size': 'L', 'Type': '(P)', 'Speed': 'Av(7)', 'Melee Reach': '—', 'Missile ROF': '2/rnd', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            'w/flight arrow': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '14/28/42', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6', 'Knockdown': 'd6'}, 
            'w/pile arrow': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '10/20/34', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6', 'Knockdown': 'd6'}, 
            'w/sheaf arrow': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '10/20/34', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d8', 'Knockdown': 'd6'}, 
            'w/stone arrow': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '14/28/42', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd6'}, 
            'Short': {'Weight': 2, 'Size': 'M', 'Type': '(P)', 'Speed': 'Av(7)', 'Melee Reach': '—', 'Missile ROF': '2/rnd', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            'w/flight arrow': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '10/20/30', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6', 'Knockdown': 'd6'},
            'w/stone arrow': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '10/20/30', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd6'}, 
            # Bows End             
            'Brandistock': {'Weight': 5, 'Size': 'M', 'Type': 'P', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6', 'Knockdown': 'd8'}, 
            'Caltrop': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1', 'Damage vs Large': '1d2', 'Knockdown': '—'}, 
            'Cestus': {'Weight': 2, 'Size': 'S', 'Type': 'B', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d3', 'Knockdown': 'd6'}, 
            'Chain': {'Weight': 3, 'Size': 'L', 'Type': 'B', 'Speed': 'Av(5)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4+1', 'Damage vs Large': '1d4', 'Knockdown': 'd6'}, 
            'Chakram': {'Weight': 1, 'Size': 'S', 'Type': 'S', 'Speed': 'Fa(4)', 'Melee Reach': '—', 'Missile ROF': '2/rnd', 'Range': '4/8/12', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d3', 'Knockdown': 'd4'}, 
            'Chijikiri': {'Weight': 6, 'Size': 'M', 'Type': 'P/B', 'Speed': 'Av(7)', 'Melee Reach': '1(2)', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d8', 'Knockdown': 'd6'}, 
            'Club': {'Weight': 3, 'Size': 'M', 'Type': 'B', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d3', 'Knockdown': 'd8'}, 
                'Great': {'Weight': 15, 'Size': 'L', 'Type': 'B', 'Speed': 'Sl(9)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '1d6+1', 'Knockdown': 'd12'}, 
                'War': {'Weight': 6, 'Size': 'M', 'Type': 'B/S', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '1d4+1', 'Knockdown': 'd10'}, 

            # Combined Weapons

            'Axe-pistol': {'Weight': 6, 'Size': 'M', 'Type': 'S', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '1/2 rnd', 'Range': 3/6/9, 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d4', 'Knockdown': 'd8'}, 
            'Dagger-pistol': {'Weight': 3, 'Size': 'S', 'Type': 'P', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '1/2 rnd', 'Range': 3/6/9, 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d3', 'Knockdown': 'd6'}, 
            'Hammer-pistol': {'Weight': 5, 'Size': 'M', 'Type': 'B', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '1/2 rnd', 'Range': 3/6/9, 'Damage vs Sm-Med': '1d4+1', 'Damage vs Large': '1d4', 'Knockdown': 'd10'}, 
            'Sword-pistol': {'Weight': 6, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '1/2 rnd', 'Range': 3/6/9, 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '1d6+1', 'Knockdown': 'd8'}, 

            # Crossbow

            'Cho-ku-no': {'Weight': 12, 'Size': 'M', 'Type': '—', 'Speed': 'Av(6)', 'Melee Reach': '—', 'Missile ROF': '2/rnd', 'Range': '10/20/30', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            'Hand': {'Weight': 3, 'Size': 'S', 'Type': '—', 'Speed': 'Av(5)', 'Melee Reach': '—', 'Missile ROF': '1/rnd', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            'Hand quarrel': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '4/8/12', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d2', 'Knockdown': 'd4'}, 
            'Heavy': {'Weight': 14, 'Size': 'M', 'Type': '—', 'Speed': 'Sl(10)', 'Melee Reach': '—', 'Missile ROF': '1/2 rnd', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            'Heavy quarrel': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '16/32/48', 'Damage vs Sm-Med': '1d8+1', 'Damage vs Large': '1d10+1', 'Knockdown': 'd6'}, 
            'Light': {'Weight': 7, 'Size': 'M', 'Type': '—', 'Speed': 'Av(7)', 'Melee Reach': '—', 'Missile ROF': '1/rnd', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            'Light quarrel': {'Weight': '*', 'Size': 'S', 'Type': 'P', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '12/24/36', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '1d8+1', 'Knockdown': 'd6'}, 
            'Pellet bow': {'Weight': 5, 'Size': 'M', 'Type': '—', 'Speed': 'Av(7)', 'Melee Reach': '—', 'Missile ROF': '1/rnd', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            'Pellet': {'Weight': '*', 'Size': 'S', 'Type': 'B', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '8/16/24', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd4'},

            # Daggers

            'Dagger': {'Weight': 1, 'Size': 'S', 'Type': 'P', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '2/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d3', 'Knockdown': 'd6'}, 
            'Bone b': {'Weight': 1, 'Size': 'S', 'Type': 'P', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '2/rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': '1d2', 'Damage vs Large': '1d2', 'Knockdown': 'd6'}, 
            'Jambiya': {'Weight': 1, 'Size': 'S', 'Type': 'P/S', 'Speed': 'Fa(3)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd6'}, 
            'Katar': {'Weight': 1, 'Size': 'S', 'Type': 'P', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d3+1', 'Damage vs Large': '1d3', 'Knockdown': 'd6'},            
            'Main-gauche': {'Weight': 2, 'Size': 'S', 'Type': 'P/S', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d3', 'Knockdown': 'd6'}, 
            'Parrying': {'Weight': 1, 'Size': 'S', 'Type': 'P', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d3', 'Knockdown': 'd6'}, 
            'Stiletto': {'Weight': 0.5, 'Size': 'S', 'Type': 'P', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '2/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d2', 'Knockdown': 'd4'}, 
            'Stone': {'Weight': 1, 'Size': 's', 'Type': 'P', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '2/rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d2', 'Knockdown': 'd6'},

            # Daggers End 

            'Dart': {'Weight': 0.5, 'Size': 'S', 'Type': 'P', 'Speed': 'Fa(2)', 'Melee Reach': '—', 'Missile ROF': '3/rnd', 'Range': '2/4/8', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d2', 'Knockdown': 'd4'}, 
            # Flails

            "Footman's": {'Weight': 15, 'Size': 'L', 'Type': 'B', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '2d4', 'Knockdown': 'd12'}, 
            'Grain': {'Weight': 3, 'Size': 'M', 'Type': 'B', 'Speed': 'Av(6)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd8'}, 
            "Horseman's": {'Weight': 5, 'Size': 'M', 'Type': 'B', 'Speed': 'Av(6)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4+1', 'Damage vs Large': '1d4+1', 'Knockdown': 'd10'},

            #Flintlocks

            'Belt Pistol': {'Weight': 3, 'Size': 'S', 'Type': 'P', 'Speed': 'Av(7)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '4/8/12', 'Damage vs Sm-Med': '1d8 k', 'Damage vs Large': '1d8 k', 'Knockdown': 'd8'}, 
            'Blundbuss Pistol': {'Weight': '6', 'Size': 's', 'Type': 'P', 'Speed': 'Sl(9)', 'Melee Reach': '—', 'Missile ROF': '0.33', 'Range': '2/4/8', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': 'd6', 'Knockdown': 'd10'}, 
            'Blunderbuss': {'Weight': 10, 'Size': 'M', 'Type': 'P', 'Speed': 'Sl(10)', 'Melee Reach': '—', 'Missile ROF': '0.33', 'Range': '3/6/12', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d8', 'Knockdown': 'd12'}, 
            'Carbine': {'Weight': 8, 'Size': 'M', 'Type': 'P', 'Speed': 'Av(8)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '10/20/55', 'Damage vs Sm-Med': '1d10', 'Damage vs Large': '1d10', 'Knockdown': 'd8'
            }, 
            'Horse Pistol': {'Weight': 4, 'Size': 'S', 'Type': 'P', 'Speed': 'Av(8)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '5/10/15', 'Damage vs Sm-Med': '1d10', 'Damage vs Large': '1d10', 'Knockdown': 'd8'}, 
            'Musket': {'Weight': 12, 'Size': 'M', 'Type': 'P', 'Speed': 'Sl(9)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '15/30/80', 'Damage vs Sm-Med': '1d12', 'Damage vs Large': '1d12', 'Knockdown': 'd8'},

            # Flintlocks End

            'Fork': {'Weight': 6, 'Size': 'L', 'Type': 'P', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6+1', 'Knockdown': 'd6'}, 
            'Gaff/hook': {'Weight': 2, 'Size': 'S', 'Type': 'P', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d3', 'Knockdown': 'd4'}, 
            'Grapple': {'Weight': 3, 'Size': 'S', 'Type': 'P/B', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '0.5', 'Range': '2/4/6', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd6'}, 
            'Gunpowder': {'Weight': '0.1', 'Size': '—', 'Type': '—', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            'Gunsen': {'Weight': 1, 'Size': 'S', 'Type': 'B/P', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d2', 'Knockdown': 'd4'}, 
            'Hammer': {'Weight': 3, 'Size': 'S', 'Type': 'B', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d3', 'Knockdown': 'd6'},

            # Hand Match Firearms

            'Arquebus': {'Weight': 10, 'Size': 'M', 'Type': 'P', 'Speed': 'Vsl(15)', 'Melee Reach': '—', 'Missile ROF': '0.33', 'Range': '10/30/42', 'Damage vs Sm-Med': '1d10', 'Damage vs Large': '1d10', 'Knockdown': 'd8'}, 
            'Handgunne': {'Weight': 20, 'Size': 'L', 'Type': 'P', 'Speed': 'Vsl(18)', 'Melee Reach': '—', 'Missile ROF': '0.25', 'Range': '/8/24/34', 'Damage vs Sm-Med': '1d8+2', 'Damage vs Large': '2d6+2', 'Knockdown': 'd10'}, 

            # Hand Match Firearms End
             
            'Harpoon': {'Weight': 6, 'Size': 'L', 'Type': 'P', 'Speed': 'Av(7)', 'Melee Reach': 2, 'Missile ROF': '1/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '2d6', 'Knockdown': 'd8'}, 
            'Bone': {'Weight': 5, 'Size': 'L', 'Type': 'P', 'Speed': 'Av(7)', 'Melee Reach': 2, 'Missile ROF': '1/rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d10', 'Knockdown': 'd8'}, 
            'Hatchet': {'Weight': 3, 'Size': 'S', 'Type': 'S', 'Speed': 'Fa(3)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd6'}, 
            'Holy symbol, big': {'Weight': 4, 'Size': 'S', 'Type': 'B', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d3', 'Knockdown': 'd8'}, 
            'Javelin': {'Weight': 2, 'Size': 'M', 'Type': 'P', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '4/8/12', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6', 'Knockdown': 'd6'}, 
                'Stone': {'Weight': 2, 'Size': 'M', 'Type': 'P', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '3/6/9', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd6'},
            'Jitte': {'Weight': 2, 'Size': 'S', 'Type': 'B', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d2', 'Knockdown': 'd6'}, 
            'Kama': {'Weight': 2, 'Size': 'S', 'Type': 'P/S', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d4', 'Knockdown': 'd6'}, 
            'Kau sin ke': {'Weight': 4, 'Size': 'M', 'Type': 'B', 'Speed': 'Av(6)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d6', 'Knockdown': 'd8'}, 
            'Kawanaga': {'Weight': 1, 'Size': 'S', 'Type': 'P/B', 'Speed': 'Av(7)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d2', 'Knockdown': 'd6'}, 
            'Knife': {'Weight': '0.5', 'Size': 'S', 'Type': 'S/P', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '2/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d2', 'Knockdown': 'd4'},
            'Bone': {'Weight': '0.5', 'Size': 'S', 'Type': 'P/S', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '2/rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': '1d2', 'Damage vs Large': '1d2', 'Knockdown': 'd4'},
            'Stone': {'Weight': '0.5', 'Size': 'S', 'Type': 'P/S', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '2/rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': '1d2', 'Damage vs Large': '1d2', 'Knockdown': 'd4'},
            'Throwing': {'Weight': 4, 'Size': 'M', 'Type': 'S/P', 'Speed': 'Sl(8)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '1d6+1', 'Knockdown': 'd8'}, 
            'Kusari-gama': {'Weight': 3, 'Size': 'M', 'Type': 'P/S/B', 'Speed': 'Av(6)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d4', 'Knockdown': 'd6'
            }, 

            # Lances

            'Light': {'Weight': 5, 'Size': 'L', 'Type': 'P', 'Speed': 'Av(6)', 'Melee Reach': 2, 'Missile ROF': '1/rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d8', 'Knockdown': 'd8'}, 
            'Medium': {'Weight': 10, 'Size': 'L', 'Type': 'P', 'Speed': 'Av(7)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '2d6', 'Knockdown': 'd10'}, 
            'Heavy': {'Weight': 15, 'Size': 'L', 'Type': 'P', 'Speed': 'Sl(10)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8+1', 'Damage vs Large': '3d6', 'Knockdown': 'd12'}, 
            'Jousting': {'Weight': 20, 'Size': 'L', 'Type': 'B', 'Speed': 'Sl(10)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d3-1', 'Damage vs Large': '1d2-1', 'Knockdown': 'd12'},

            # Lances End

            'Lantern': {'Weight': 3, 'Size': 'S', 'Type': 'B', 'Speed': 'Av(6)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': '1d3 *', 'Damage vs Large': '1d2 *', 'Knockdown': 'd6'}, 
            'Lasso': {'Weight': 3, 'Size': 'L', 'Type': '—', 'Speed': 'Sl(10)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '2/4/6', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 

            # Maces

            "Footman's": {'Weight': 10, 'Size': 'M', 'Type': 'B', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '1d6', 'Knockdown': 'd10'},
            "Horseman's": {'Weight': 6, 'Size': 'M', 'Type': 'B', 'Speed': 'Av(6)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d4', 'Knockdown': 'd8'},

            # Maces End

            'Mace-axe': {'Weight': 9, 'Size': 'L', 'Type': 'B/S', 'Speed': 'Sl(8)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '1d6+1', 'Knockdown': 'd10'}, 
            'Machete': {'Weight': 5, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(6)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d8', 'Knockdown': 'd6'}, 
            'Mancatcher': {'Weight': 8, 'Size': 'L', 'Type': '—', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': 'd6'},

            # Matchlock Firearms

            'Arquebus': {'Weight': 10, 'Size': 'M', 'Type': 'P', 'Speed': 'Sl(10)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '10/20/60', 'Damage vs Sm-Med': '1d10', 'Damage vs Large': '1d10', 'Knockdown': 'd8'}, 
            'Caliver': {'Weight': 11, 'Size': 'M', 'Type': 'P', 'Speed': 'Sl(9)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '8/16/48', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d8', 'Knockdown': 'd8'}, 
            'Musket w/rest': {'Weight': 20, 'Size': 'L', 'Type': 'P', 'Speed': 'Sl(12)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '12/24/72', 'Damage vs Sm-Med': '1d12', 'Damage vs Large': '1d12', 'Knockdown': 'd8'}, 

            # Matchlock Firearms End

            'Maul': {'Weight': 10, 'Size': 'L', 'Type': 'B', 'Speed': 'Sl(8)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '1d10', 'Knockdown': 'd12'}, 
            'Morningstar': {'Weight': 12, 'Size': 'M', 'Type': 'B/P', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '1d6+1', 'Knockdown': 'd10'}, 
            'Net': {'Weight': 10, 'Size': 'M', 'Type': '—', 'Speed': 'Sl(10)', 'Melee Reach': 1, 'Missile ROF': '1/2 rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            'Nunchaku': {'Weight': 3, 'Size': 'M', 'Type': 'B', 'Speed': 'Fa(3)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6', 'Knockdown': 'd8'}, 
            'Oil flask': {'Weight': 1, 'Size': 'S', 'Type': 'd', 'Speed': 'VS(15)', 'Melee Reach': '—', 'Missile ROF': '1/2 rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': 'd', 'Damage vs Large': 'd', 'Knockdown': '—'}, 
            'Parang or Machete': {'Weight': 5, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(6)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d8', 'Knockdown': 'd6'},

            # Pick

            'Farming tool': {'Weight': 8, 'Size': 'L', 'Type': 'P', 'Speed': 'Sl(8)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6+1', 'Knockdown': 'd8'},
            "Footman's": {'Weight': 6, 'Size': 'M', 'Type': 'P', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '2d4', 'Knockdown': 'd8'},
            "Horseman's": {'Weight': 4, 'Size': 'M', 'Type': 'P', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4+1', 'Damage vs Large': '1d4', 'Knockdown': 'd6'},
            'Pike': {'Weight': 12, 'Size': 'L', 'Type': 'P', 'Speed': 'Sl(13)', 'Melee Reach': 3, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d12', 'Knockdown': 'd8'}, 
            'Pilum': {'Weight': 3, 'Size': 'M', 'Type': 'P', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '3/6/9', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6', 'Knockdown': 'd6'},

            # Polearm

            'Awl Pike': {'Weight': 12, 'Size': 'L', 'Type': 'P', 'Speed': 'Sl(13)', 'Melee Reach': 3, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d12', 'Knockdown': 'd8'}, 
            'Bardiche': {'Weight': 12, 'Size': 'L', 'Type': 'S', 'Speed': 'Sl(9)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '2d6', 'Knockdown': 'd12'}, 
            'Bec de Corbin': {'Weight': 10, 'Size': 'L', 'Type': 'P/B', 'Speed': 'Sl(9)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d6', 'Knockdown': 'd10'}, 
            'Bill-Guisarme': {'Weight': 15, 'Size': 'L', 'Type': 'P/S', 'Speed': 'Sl(10)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '1d10', 'Knockdown': 'd10'}, 
            'Bill': {'Weight': 15, 'Size': 'L', 'Type': 'P/S', 'Speed': 'Sl(10)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '1d10', 'Knockdown': 'd10'}, 
            'Fauchard': {'Weight': 7, 'Size': 'L', 'Type': 'S', 'Speed': 'Sl(8)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d8', 'Knockdown': 'd8'}, 
            'Glaive': {'Weight': 8, 'Size': 'L', 'Type': 'S', 'Speed': 'Sl(8)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d10', 'Knockdown': 'd10'}, 
            'Glaive-Guisarme': {'Weight': 10, 'Size': 'L', 'Type': 'P/S', 'Speed': 'Sl(9)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '2d6', 'Knockdown': 'd10'}, 
            'Guisarme': {'Weight': 8, 'Size': 'L', 'Type': 'S', 'Speed': 'Sl(8)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '1d8', 'Knockdown': 'd10'}, 
            'Halberd': {'Weight': 15, 'Size': 'L', 'Type': 'P/S', 'Speed': 'Sl(9)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d10', 'Damage vs Large': '2d6', 'Knockdown': 'd12'}, 
            'Lajatang': {'Weight': 6, 'Size': 'L', 'Type': 'S', 'Speed': 'Av(6)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d10', 'Damage vs Large': '1d10', 'Knockdown': 'd8'}, 
            'Lucern hammer': {'Weight': 15, 'Size': 'L', 'Type': 'P/B', 'Speed': 'Sl(9)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '1d6', 'Knockdown': 'd10'},
            'Military fork': {'Weight': 7, 'Size': 'L', 'Type': 'P', 'Speed': 'Av(7)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '2d4', 'Knockdown': 'd8'}, 
            'Nagimaki': {'Weight': 6, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(6)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d8', 'Knockdown': 'd6'}, 
            'Naginata': {'Weight': 10, 'Size': 'L', 'Type': 'S', 'Speed': 'Av(7)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d10', 'Knockdown': 'd8'}, 
            'Partisan': {'Weight': 8, 'Size': 'L', 'Type': 'P', 'Speed': 'Sl(9)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6+1', 'Knockdown': 'd8'}, 
            'Ranseur': {'Weight': 7, 'Size': 'L', 'Type': 'P', 'Speed': 'Sl(8)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '2d4', 'Knockdown': 'd8'}, 
            'Spetum': {'Weight': 7, 'Size': 'L', 'Type': 'P', 'Speed': 'Sl(8)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '2d6', 'Knockdown': 'd8'}, 
            'Tetsubo': {'Weight': 8, 'Size': 'L', 'Type': 'B', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d8', 'Knockdown': 'd12'}, 
            'Voulge': {'Weight': 12, 'Size': 'L', 'Type': 'S', 'Speed': 'Sl(10)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '2d4', 'Knockdown': 'd12'}, 
            
            # Polearms End

            'Pry bar': {'Weight': 5, 'Size': 'M', 'Type': 'B', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d3', 'Knockdown': 'd8'}, 
            'Quarterstaff h': {'Weight': 4, 'Size': 'L', 'Type': 'B', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d6', 'Knockdown': 'd10'}, 
            'Rock': {'Weight': 1, 'Size': 'S', 'Type': 'B', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '2/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d2', 'Knockdown': 'd6'}, 
            'Sai': {'Weight': 2, 'Size': 'S', 'Type': 'B', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d2', 'Knockdown': 'd6'}, 
            'Sang kauw': {'Weight': 10, 'Size': 'L', 'Type': 'P/S', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d6', 'Knockdown': 'd6'}, 
            'Sap': {'Weight': '0.5', 'Size': 'S', 'Type': 'B', 'Speed': 'Fa(2)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d2', 'Damage vs Large': '1d2', 'Knockdown': 'd4'}, 
            'Scourge': {'Weight': 2, 'Size': 'S', 'Type': '—', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d2', 'Knockdown': 'd4'}, 
            'Scythe': {'Weight': 8, 'Size': 'L', 'Type': 'P/S', 'Speed': 'Sl(8)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '1d8', 'Knockdown': 'd8'}, 
            'Shuriken': {'Weight': '0.1', 'Size': 'S', 'Type': 'P', 'Speed': 'Fa(2)', 'Melee Reach': '—', 'Missile ROF': '2/rnd', 'Range': '3/6/9', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd4'}, 
            'Sickle': {'Weight': 3, 'Size': 'S', 'Type': 'S', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4+1', 'Damage vs Large': '1d4', 'Knockdown': 'd4'}, 
            'Sledge hammer': {'Weight': 10, 'Size': 'M', 'Type': 'B', 'Speed': 'Sl(8)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '1d4+1', 'Knockdown': 'd12'}, 
            'Sling': {'Weight': 1, 'Size': 'S', 'Type': '—', 'Speed': 'Av(6)', 'Melee Reach': '—', 'Missile ROF': '1/rnd', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
                'Bullet': {'Weight': '0.1', 'Size': 'S', 'Type': 'B', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': 10/20/40, 'Damage vs Sm-Med': '1d4+1', 'Damage vs Large': '1d6+1', 'Knockdown': 'd4'}, 
                'Stone': {'Weight': '0.1', 'Size': 's', 'Type': 'B', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '8/16/24', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd4'},            
            'Slow match': {'Weight': '0.1', 'Size': '—', 'Type': '—', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            'Smokepowder': {'Weight': '0.1', 'Size': '—', 'Type': '—', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            
            # Snaplock Firearms

            'Belt pistol': {'Weight': 3, 'Size': 'S', 'Type': 'P', 'Speed': 'Av(7)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '3/6/9', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d8', 'Knockdown': 'd8'}, 
            'Horse pistol': {'Weight': 4, 'Size': 'S', 'Type': 'P', 'Speed': 'Av(8)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '4/8/12', 'Damage vs Sm-Med': '1d10', 'Damage vs Large': '1d10', 'Knockdown': 'd8'},
            'Musket': {'Weight': 14, 'Size': 'M', 'Type': 'P', 'Speed': 'Sl(9)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '14/26/78', 'Damage vs Sm-Med': '1d12', 'Damage vs Large': '1d12', 'Knockdown': 'd8'},

            # Snaplock Firearms End

            'Spade': {'Weight': 5, 'Size': 'M', 'Type': 'S/B', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d4', 'Knockdown': 'd8'},

            # Spears

            'Spear': {'Weight': 5, 'Size': 'M', 'Type': 'P', 'Speed': 'Av(6)', 'Melee Reach': 1, 'Missile ROF': '1', 'Range': '2/4/6', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            'NormOne-handed': {'Weight': '—', 'Size': '—', 'Type': '—', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d8', 'Knockdown': 'd6'}, 
            'NormTwo-handed': {'Weight': '—', 'Size': '—', 'Type': '—', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '2d6', 'Knockdown': 'd8'}, 
            'Long c, h': {'Weight': 8, 'Size': 'L', 'Type': 'P', 'Speed': 'Sl(8)', 'Melee Reach': 2, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d6', 'Damage vs Large': '3d6', 'Knockdown': 'd8'},
            'StoneSpear': {'Weight': 5, 'Size': 'M', 'Type': 'P', 'Speed': 'Av(6)', 'Melee Reach': 1, 'Missile ROF': '1', 'Range': '2/3/4', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            'StoneOne-handed': {'Weight': '—', 'Size': '—', 'Type': '—', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d6', 'Knockdown': 'd6'},
            'StoneTwo-handed': {'Weight': '—', 'Size': '—', 'Type': '—', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '2d4', 'Knockdown': 'd8'}, 
            
            # Staff Slings

            'Staff sling': {'Weight': 2, 'Size': 'M', 'Type': '—', 'Speed': 'Sl(11)', 'Melee Reach': '—', 'Missile ROF': '1/rnd', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'}, 
            'Stinkpot': {'Weight': 2, 'Size': 'S', 'Type': 'B', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '6/12/18', 'Damage vs Sm-Med': '1d3', 'Damage vs Large': '1d3', 'Knockdown': 'd6'},
            'Stone': {'Weight': '2', 'Size': 'S', 'Type': 'B', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '6/12/18', 'Damage vs Sm-Med': '1d4+1', 'Damage vs Large': '1d6+1', 'Knockdown': 'd6'},

            # Swords

            'Bastard': {'Weight': 10, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(6)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'},
            'One-handed': {'Weight': '—', 'Size': '—', 'Type': '—', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d12', 'Knockdown': 'd8'},
            'Two-handed': {'Weight': '—', 'Size': '—', 'Type': '—', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '2d8', 'Knockdown': 'd10'}, 
            'Broad': {'Weight': 4, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '1d6+1', 'Knockdown': 'd8'}, 
            'Claymore': {'Weight': 8, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '2d8', 'Knockdown': 'd10'}, 
            'Cutlass': {'Weight': 4, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '1d8+1', 'Knockdown': 'd8'}, 
            'Drusus': {'Weight': 3, 'Size': 'M', 'Type': 'S', 'Speed': 'Fa(3)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '1d8+1', 'Knockdown': 'd6'}, 
            'Estoc': {'Weight': 5, 'Size': 'M', 'Type': 'P', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d8', 'Knockdown': 'd6'}, 
            'Falchion': {'Weight': 8, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '2d4', 'Knockdown': 'd8'}, 
            'Gladius': {'Weight': 3, 'Size': 'S', 'Type': 'P', 'Speed': 'Fa(3)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d8', 'Knockdown': 'd6'}, 
            'Katana': {'Weight': 6, 'Size': 'M', 'Type': 'S/P', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'},
            'One-handed': {'Weight': '—', 'Size': '—', 'Type': '—', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d10', 'Damage vs Large': '1d12', 'Knockdown': 'd6'},
            'Two-handed': {'Weight': '—', 'Size': '—', 'Type': '—', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d6', 'Damage vs Large': '2d6', 'Knockdown': 'd8'}, 
            'Khopesh': {'Weight': 7, 'Size': 'M', 'Type': 'S', 'Speed': 'Sl(9)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d4', 'Damage vs Large': '1d6', 'Knockdown': 'd8'}, 
            'Long': {'Weight': 4, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d12', 'Knockdown': 'd8'}, 
            'Ninja-to': {'Weight': 5, 'Size': 'M', 'Type': 'S/P', 'Speed': 'Fa(3)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d6', 'Knockdown': 'd6'}, 
            'No-dachi': {'Weight': 10, 'Size': 'L', 'Type': 'S/P', 'Speed': 'Sl(8)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d10', 'Damage vs Large': '1d20', 'Knockdown': 'd10'}, 
            'Rapier': {'Weight': 4, 'Size': 'M', 'Type': 'P', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d8', 'Knockdown': 'd6'}, 
            'Sabre': {'Weight': 5, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '1d8+1', 'Knockdown': 'd8'}, 
            'Sapara': {'Weight': 4, 'Size': 'S', 'Type': 'S', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '1d4', 'Knockdown': 'd6'},
            # Everything above here has been checked against the source material 
            # move this down as more is completed 
            'Scimitar': {'Weight': 4, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d8', 'Knockdown': 'd8'},
            'Great': {'Weight': '16', 'Size': 'L', 'Type': 'S', 'Speed': 'Sl(9)', 'Melee Reach': '1', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '2d6', 'Damage vs Large': '4d4', 'Knockdown': 'd10'},  
            'Short': {'Weight': 3, 'Size': 'S', 'Type': 'P', 'Speed': 'Fa(3)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d8', 'Knockdown': 'd6'}, 
            'Spatha': {'Weight': 4, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d12', 'Knockdown': 'd8'}, 
            'Sword-axe': {'Weight': 12, 'Size': 'L', 'Type': 'S', 'Speed': 'Sl(10)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8+1', 'Damage vs Large': '1d12+1', 'Knockdown': 'd10'}, 
            'Tulwar': {'Weight': 8, 'Size': 'M', 'Type': 'S', 'Speed': 'Av(5)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '2d4', 'Knockdown': 'd8'},
            'Two-handed': {'Weight': '15', 'Size': 'L', 'Type': 'S', 'Speed': 'Sl(10)', 'Melee Reach': '1', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d8', 'Knockdown': 'd6'},
            'Wakizashi': {'Weight': 3, 'Size': 'M', 'Type': 'S/P', 'Speed': 'Fa(3)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d8', 'Knockdown': 'd6'},

            # Swords End

            'Three-piece rod': {'Weight': 5, 'Size': 'L', 'Type': 'B', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6', 'Damage vs Large': '1d4', 'Knockdown': 'd8'}, 
            'Torch': {'Weight': 1, 'Size': 'M', 'Type': 'B', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': '1d4', 'Damage vs Large': '1d3', 'Knockdown': 'd6'}, 
            'Trident': {'Weight': 5, 'Size': 'L', 'Type': 'P', 'Speed': 'Av(7)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': '—', 'Damage vs Large': '—', 'Knockdown': '—'},
                'One-handed': {'Weight': '—', 'Size': '—', 'Type': '—', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d6+1', 'Damage vs Large': '2d4', 'Knockdown': 'd6'}, 
                'Two-handed': {'Weight': '—', 'Size': '—', 'Type': '—', 'Speed': '—', 'Melee Reach': '—', 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d8+1', 'Damage vs Large': '3d4', 'Knockdown': 'd8'},  
            'Vial b': {'Weight': '0.1', 'Size': 'S', 'Type': 'd', 'Speed': 'Fa(2)', 'Melee Reach': '—', 'Missile ROF': '1/rnd', 'Range': '2/3/4', 'Damage vs Sm-Med': 'd', 'Damage vs Large': 'd', 'Knockdown': '—'}, 
            'Warhammer': {'Weight': 6, 'Size': 'M', 'Type': 'B', 'Speed': 'Fa(4)', 'Melee Reach': 1, 'Missile ROF': '1/rnd', 'Range': '2/4/6', 'Damage vs Sm-Med': '1d4+1', 'Damage vs Large': '1d4', 'Knockdown': 'd8'},

            # Wheellock Firearms

            'Arquebus': {'Weight': 8, 'Size': 'M', 'Type': 'P', 'Speed': 'Sl(8)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '10/20/60', 'Damage vs Sm-Med': '1d10', 'Damage vs Large': '1d10', 'Knockdown': 'd8'},            
            'Belt pistol': {'Weight': 3, 'Size': 'S', 'Type': 'P', 'Speed': 'Av(7)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '3/6/9', 'Damage vs Sm-Med': '1d8', 'Damage vs Large': '1d8', 'Knockdown': 'd8'}, 
            'Horse pistol': {'Weight': 4, 'Size': 'S', 'Type': 'P', 'Speed': 'Av(8)', 'Melee Reach': '—', 'Missile ROF': '0.5', 'Range': '4/8/12', 'Damage vs Sm-Med': '1d10', 'Damage vs Large': '1d10', 'Knockdown': 'd8'},

            # Wheellock Firearms
             
            'Whip': {'Weight': 2, 'Size': 'M', 'Type': '—', 'Speed': 'Sl(8)', 'Melee Reach': 3, 'Missile ROF': '—', 'Range': '—', 'Damage vs Sm-Med': '1d2', 'Damage vs Large': '1', 'Knockdown': '—'}
        }
    
    def get_weapon_data(self, weapon_name):
        # Return weapon data if it exists, otherwise return None
        return self.weapons.get(weapon_name, None)