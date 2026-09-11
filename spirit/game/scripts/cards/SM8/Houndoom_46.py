from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b04c4336-9374-57f0-94d1-7a14cd706cd3',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name',
    display_name='Houndoom',
    searchable_by=['Houndoom', 'Stage 1', 'Houndoom'],
    subtypes=['Stage 1'],
    collector_number=46,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name',
    family_id=228,
    abilities=[
        Attack(
            title='Nasty Plot',
            game_text='Search your deck for a card and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Attack Operation',
            game_text='If you have more cards in your hand than your opponent, this attack does 80 more damage.',
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
