from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='317702bd-eeea-53a2-800b-9567413fe302',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name',
    display_name='Shuckle',
    searchable_by=['Shuckle', 'Basic', 'Shuckle'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=213,
    abilities=[
        Attack(
            title='Hide a Berry',
            game_text='Draw 2 cards. Then, put a card from your hand on the bottom of your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Wrap',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
