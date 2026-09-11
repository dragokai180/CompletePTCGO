from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8e36945f-2c0b-5d62-8220-c36206e66e9e',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name',
    display_name='Scrafty',
    searchable_by=['Scrafty', 'Stage 1', 'Scrafty'],
    subtypes=['Stage 1'],
    collector_number=61,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name',
    family_id=559,
    abilities=[
        Attack(
            title='Lambaste',
            game_text="If the Defending Pokémon is a Basic Pokémon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Headbang',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
