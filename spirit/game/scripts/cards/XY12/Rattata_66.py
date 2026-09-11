from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8508fd09-24c1-59d3-b17d-c7af8e24e563',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name',
    display_name='Rattata',
    searchable_by=['Rattata', 'Basic', 'Rattata'],
    subtypes=['Basic'],
    collector_number=66,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=19,
    abilities=[
        Ability(
            title='Mischievous Fang',
            game_text="When you play this Pokémon from your hand onto your Bench, you may discard all Pokémon Tool cards attached to your opponent's Active Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
