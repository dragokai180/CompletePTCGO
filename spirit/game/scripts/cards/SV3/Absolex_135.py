from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='595c22ab-5b5d-553b-a65e-d0037c52dcc2',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Absolex.Name',
    display_name='Absol ex',
    searchable_by=['Absol ex', 'Basic', 'ex', 'Absolex'],
    subtypes=['Basic', 'ex'],
    collector_number=135,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=359,
    abilities=[
        Attack(
            title='Future Sight',
            game_text="Look at the top 3 cards of either player's deck and put them back in any order.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Cursed Slug',
            game_text='If your opponent has 3 or fewer cards in their hand, this attack does 120 more damage.',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
