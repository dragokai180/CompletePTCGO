from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e196bb68-5191-556f-8128-9152934b85f8',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name',
    display_name='Latias',
    searchable_by=['Latias', 'Basic', 'Latias'],
    subtypes=['Basic'],
    collector_number=10,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'HGSS10'}},
    weakness_type=PokemonTypes.COLORLESS,
    weakness_amount=2,
    family_id=380,
    abilities=[
        Attack(
            title='Energy Assist',
            game_text='Search your discard pile for a basic Energy card and attach it to 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Infinite Wind',
            game_text='If Latios is on your Bench, remove 2 damage counters from each of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
