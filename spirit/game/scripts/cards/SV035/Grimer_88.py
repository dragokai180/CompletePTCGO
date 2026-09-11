from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='85741401-87a9-5056-9586-a04832cf138b',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name',
    display_name='Grimer',
    searchable_by=['Grimer', 'Basic', 'Grimer'],
    subtypes=['Basic'],
    collector_number=88,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=88,
    abilities=[
        Attack(
            title='Gummy Press',
            game_text="During your opponent's next turn, the Defending Pokémon's Retreat Cost is Colorless more.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
