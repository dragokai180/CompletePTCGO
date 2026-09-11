from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bd4f7dd0-0771-5a60-86c3-50d87dcf964a',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name',
    display_name='Charizard-EX',
    searchable_by=['Charizard-EX', 'Basic', 'EX', 'CharizardEX'],
    subtypes=['Basic', 'EX'],
    collector_number=17,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=6,
    abilities=[
        Attack(
            title='Mega Ascension',
            game_text='Search your deck for M Charizard-EX, reveal it, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Brave Fire',
            game_text='This Pokémon does 30 damage to itself.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
