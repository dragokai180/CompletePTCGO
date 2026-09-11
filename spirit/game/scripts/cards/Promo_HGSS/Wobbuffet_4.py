from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6264ff49-dd7a-5586-be31-a3cbd371954c',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name',
    display_name='Wobbuffet',
    searchable_by=['Wobbuffet', 'Basic', 'Wobbuffet'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    attributes={200790: {'type': 'string', 'value': 'HGSS04'}},
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=202,
    abilities=[
        Ability(
            title='Tenacious Bind',
            game_text="As long as Wobbuffet is your Active Pokémon, your opponent's Active Pokémon's Retreat Cost is ColorlessColorless more.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("As long as Wobbuffet is your Active Pokémon, your opponent's Active Pokémon's Retreat Cost is ColorlessColorless more."),
        ),
        Attack(
            title='Trip Over',
            game_text='Flip a coin. If heads, this attack does 20 damage plus 30 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
