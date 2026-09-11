from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4d5b21e7-8766-5357-970a-f13f39caeaf4',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name',
    display_name='Capsakid',
    searchable_by=['Capsakid', 'Basic', 'Capsakid'],
    subtypes=['Basic'],
    collector_number=27,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=951,
    abilities=[
        Attack(
            title='Slightly Spicy',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
