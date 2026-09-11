from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='73809e12-57a5-51ed-85b6-dc5e360e3ae9',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name',
    display_name='Tarountula',
    searchable_by=['Tarountula', 'Basic', 'Tarountula'],
    subtypes=['Basic'],
    collector_number=17,
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
            title='String Shot',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
