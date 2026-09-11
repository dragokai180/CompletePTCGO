from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5e1be38a-8ddb-543c-bad9-279ad9385437',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name',
    display_name='Scrafty',
    searchable_by=['Scrafty', 'Stage 1', 'Scrafty'],
    subtypes=['Stage 1'],
    collector_number=51,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name',
    family_id=559,
    abilities=[
        Attack(
            title='Dangerous Head',
            game_text="If your opponent's Active Pokémon is a Basic Pokémon, this attack does 50 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Hammer In',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
