from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='52691a37-db33-51c3-b12b-d8b6ee26a122',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Solgaleo.Name',
    display_name='Solgaleo',
    searchable_by=['Solgaleo', 'Stage 2', 'Solgaleo'],
    subtypes=['Stage 2'],
    collector_number=105,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name',
    family_id=789,
    abilities=[
        Ability(
            title='Sunrise',
            game_text='Once during your turn, if this Pokémon is on your Bench, you may use this Ability. Search your deck for up to 2 Basic Metal Energy cards and attach them to this Pokémon. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Sunsteel Strike',
            game_text='Discard all Energy from this Pokémon.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=220,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
