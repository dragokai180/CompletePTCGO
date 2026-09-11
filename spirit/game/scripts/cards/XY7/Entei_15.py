from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='620728d0-9fb3-556b-839d-56f0bd46065f',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name',
    display_name='Entei',
    searchable_by=['Entei', 'Basic', 'Entei'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=244,
    abilities=[
        Attack(
            title='Flame Screen',
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Heat Tackle',
            game_text='Flip a coin. If tails, this Pokémon does 30 damage to itself.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('This Pokémon may have up to 2 Pokémon Tool cards attached to it.'),
)
