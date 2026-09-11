from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9613a4ff-5960-5797-9e7f-8423c71bd7c2',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name',
    display_name='Tarountula',
    searchable_by=['Tarountula', 'Basic', 'Tarountula'],
    subtypes=['Basic'],
    collector_number=16,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=917,
    abilities=[
        Attack(
            title='String Haul',
            game_text="Flip a coin. If heads, switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
