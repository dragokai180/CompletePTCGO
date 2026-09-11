from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b58115cd-a6f9-54f1-aabc-f285eb419b20',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name',
    display_name='Capsakid',
    searchable_by=['Capsakid', 'Basic', 'Capsakid'],
    subtypes=['Basic'],
    collector_number=28,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=951,
    abilities=[
        Attack(
            title='Increasing Spice',
            game_text='Search your deck for a Basic Fire Energy card and attach it to this Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Playful Kick',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
