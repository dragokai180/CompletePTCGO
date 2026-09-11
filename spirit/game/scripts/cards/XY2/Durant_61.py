from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a475706b-1d67-5710-b70b-a206a523e941',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name',
    display_name='Durant',
    searchable_by=['Durant', 'Basic', 'Durant'],
    subtypes=['Basic'],
    collector_number=61,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=632,
    abilities=[
        Attack(
            title='Chip Off',
            game_text="Discard cards from your opponent's hand at random until he or she has 4 cards in his or her hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='X-Scissor',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
