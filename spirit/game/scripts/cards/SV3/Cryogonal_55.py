from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f4598966-0106-5c59-b753-217c082e28d3',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cryogonal.Name',
    display_name='Cryogonal',
    searchable_by=['Cryogonal', 'Basic', 'Cryogonal'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=615,
    abilities=[
        Attack(
            title='First Freeze',
            game_text="If you go second and it's your first turn, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
