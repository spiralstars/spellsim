names = ['Accio',
    'Aguamenti',
    'Alohomora',
    'Anapneo',
    'AntiCheating',
    'AntiDisapparition',
    'Aparecium',
    'Avada Kedavra',
    'Avis',
    'Babbling Curse',
    'Banishing Charm',
    'Bat-Bogey Hex',
    'Bedazzling Hex',
    'Bubble-Head Charm',
    'Caterwauling Charm',
    'Cave Inimicum',
    'Cheering Charm',
    'Colloportus',
    'Colour-Change Charm',
    'Confringo',
    'Confundo',
    'Conjunctivitus',
    'Crucio',
    'Defodio',
    'Deletrius',
    'Densaugeo',
    'Deprimo',
    'Descendo',
    'Diffindo',
    'Disillusionment',
    'Dissendium',
    'Duro',
    'Engorgio',
    'Entrail-Expelling Curse',
    'Episkey',
    'Erecto',
    'Evanesco',
    'Expecto Patronum',
    'Expelliarmus',
    'Expulso',
]
for name in names:
    name = name.replace(' ', '').replace('-', '')
    # out_file = open("src/edu/hogwarts/SpellSim/Spells/{name}.java".format(name=name), 'w')
    out_file = open("src/{name}.java".format(name=name), 'w')

    out_file.write("""package edu.hogwarts.SpellSim.Spells;

class {name} implements Spell {{
    public String name = "{name}";

    public void invokeOn(Subject subject) {{
        throw new NotImplementedError("Not yet implemented.");
    }}
}}

    """.format(
        name=name
    ))
    out_file.close()
