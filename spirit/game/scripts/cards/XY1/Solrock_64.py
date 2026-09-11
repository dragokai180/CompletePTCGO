from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b5286690-9511-5749-805e-e60210ab82a0',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name',
    display_name='Solrock',
    searchable_by=['Solrock', 'Basic', 'Solrock'],
    subtypes=['Basic'],
    collector_number=64,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=338,
    abilities=[
        Attack(
            title='Cosmic Spin',
            game_text='If Lunatone is on your Bench, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Solar Beam',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
