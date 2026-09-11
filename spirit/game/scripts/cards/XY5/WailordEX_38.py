from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1b582673-dc78-54d3-9895-52cc33aa6788',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.WailordEX.Name',
    display_name='Wailord-EX',
    searchable_by=['Wailord-EX', 'Basic', 'EX', 'WailordEX'],
    subtypes=['Basic', 'EX'],
    collector_number=38,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=321,
    abilities=[
        Ability(
            title='Water Veil',
            game_text='Whenever you attach an Energy card from your hand to this Pokémon, remove all Special Conditions from it.',
            passive=standard_passive('Whenever you attach an Energy card from your hand to this Pokémon, remove all Special Conditions from it.'),
        ),
        Attack(
            title='High Breaching',
            game_text='This Pokémon is now Asleep.',
            cost={PokemonTypes.WATER: 5},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
