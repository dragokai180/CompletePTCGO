from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2b5ce4a5-9dac-54ac-b79f-a0d99e7277fe',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name',
    display_name='Sableye',
    searchable_by=['Sableye', 'Basic', 'Sableye'],
    subtypes=['Basic'],
    collector_number=96,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=302,
    abilities=[
        Attack(
            title='Quick Hunt',
            game_text='If you go first, you can use this attack on your first turn. Search your deck for a card and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Cursed Drop',
            game_text="Put 3 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
