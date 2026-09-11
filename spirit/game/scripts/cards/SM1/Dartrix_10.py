from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='054f4049-6565-5306-bde5-3147588cb569',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name',
    display_name='Dartrix',
    searchable_by=['Dartrix', 'Stage 1', 'Dartrix'],
    subtypes=['Stage 1'],
    collector_number=10,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name',
    family_id=722,
    abilities=[
        Attack(
            title='Sharp Blade Quill',
            game_text="This attack does 20 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Leaf Blade',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
