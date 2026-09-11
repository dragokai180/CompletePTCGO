from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3aa98978-4152-56d8-b85d-367fadb47e08',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name',
    display_name='Charizard-EX',
    searchable_by=['Charizard-EX', 'Basic', 'EX', 'CharizardEX'],
    subtypes=['Basic', 'EX'],
    collector_number=11,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=6,
    abilities=[
        Attack(
            title='Stoke',
            game_text='Flip a coin. If heads, search your deck for up to 3 basic Energy cards and attach them to this Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fire Blast',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
